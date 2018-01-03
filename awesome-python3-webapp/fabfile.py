import os, re
from datetime import datetime

from fabric.api import *

env.hosts = ['ubuntu@ec2-13-59-147-100.us-east-2.compute.amazonaws.com']
env.key_filename = os.path.abspath('../../ytj8929309.pem')

db_user = 'www-data'
db_password = 'www-data'

_TAR_FILE = 'dist-awesome.tar.gz'

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE

_REMOTE_BASE_DIR = '/srv/awesome'

def _current_path():
    return os.path.abspath('.')

def _now():
    return datetime.now().strftime('%y-%m-%d_%H.%M.%S')

# 将此刻的数据库从远程备份到本地
def backup():
    '''
    Dump entire database on server and backup to local.
    '''
    df = _now()
    # 创建数据库名称
    f = 'backup-awesome-%s.sql' % df
    with cd('/tmp'):
        # 将数据库备份到名为f的sql中
        run('mysqldump --user=%s --password=%s --skip-opt --add-drop-table --default-character-set=utf8 --quick awesome > %s' % (db_user, db_password, f))
        # 将f打包
        run('tar -czvf %s.tar.gz %s' % (f, f))
        # 将f从远程拉到本地当前文件夹的backup中
        get('%s.tar.gz' % f, '%s/backup/' % _current_path())
        # 删除远程名为f的sql和压缩文件
        run('rm -f %s' % f)
        run('rm -f %s.tar.gz' % f)

# 打包本地文件
def bulid():
    '''
    Build dist package.
    '''
    # 打包文件包括：'transwarp', 'favicon.ico',
    includes = ['static', 'templates', '*.py']
    # 不包括文件：
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    # 删除已有的打包文件
    local('rm -f dist/%s' % _TAR_FILE)
    # 进入www目录
    with lcd(os.path.join(_current_path(), 'www')):
        # 讲命令以字符串的方式存储 打包文件：
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))

# 发布
def deploy():
    # 创建当前时间名的目录
    newdir = 'www-%s' % _now()
    # 删除远程压缩包
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # 将本地压缩包发布到远程
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 进入远程项目目录
    with cd(_REMOTE_BASE_DIR):
        # 创建当前时间的源码目录
        sudo('mkdir %s' % newdir)
    # 进入当前时间源码目录
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        # 解压最新源文件压缩包
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 进入远程项目目录
    with cd(_REMOTE_BASE_DIR):
        # 移除原有的www链接
        sudo('rm -f www')
        # 创建新的www链接 链接到当前目录
        sudo('ln -s %s www' % newdir)
        # 让用户www的属主变为www-data
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s' % newdir)
    # 报错不退出，启动supervisorctl监听项目
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')

RE_FILES = re.compile('\r?\n')

# 回滚到上一个版本
def rollback():
    '''
    rollback to previous version
    '''
    with cd(_REMOTE_BASE_DIR):
        r = run('ls -p -1')
        files = [ s[:1] for s in RE_FILES.split(r) if s.startswith('www-') and s.endswith('/')]
        r = run('ls -l www')
        ss = r.split(' -> ')
        if len(ss) != 2:
            print ('ERROR: \'www\' is not a symbol link.')
            return
        current = ss[1]
        print ('Found current symbol link points to: %s\n' % current)
        try:
            index = files.index(current)
        except ValueError as e:
            print ('ERROR: symbol link is invalid.')
            return
        if len(files) == index + 1:
            print ('ERROR: already the oldest version.')
        old = files[index + 1]
        print ('==================================================')
        for f in files:
            if f == current:
                print ('      Current ---> %s' % current)
            elif f == old:
                print ('  Rollback to ---> %s' % old)
            else:
                print ('                   %s' % f)
            print ('==================================================')
            print ('')
            yn = raw_input ('continue? y/N ')
            if yn != 'y' and yn != 'Y':
                print ('Rollback cancelled.')
                return
            print ('Start rollback...')
            sudo('rm -f www')
            sudo('ln -s %s www' % old)
            sudo('chown www-data:www-data www')
            with settings(warn_only=True):
                sudo('supervisorctl stop awesome')
                sudo('supervisorctl start awesome')
                sudo('/etc/init.d/nginx reload')
            print ('ROLLBACKED OK.')

# 回复db到本地 （将实际数据库运用到本地）
def restore2local():
    '''
    Restore db to local
    '''
    backup_dir = os.path.join(_current_path(), 'backup')
    fs = os.listdir(backup_dir)
    files = [f for f in fs if f.startswith('backup-') and f.endswith('.sql.tar.gz')]
    files.sort(cmp=lambda s1, s2: 1 if s1 < s2 else -1)
    if len(files)==0:
        print('No backup files found.')
        return
    print ('Found %s backup files:' % len(files))
    print ('==================================================')
    n = 0
    for f in files:
        print ('%s: %s' % (n, f))
        n = n + 1
    print ('==================================================')
    print ('')
    try:
        num = int(raw_input ('Restore file: '))
    except ValueError:
        print ('Invalid file number.')
        return
    restore_file = files[num]
    yn = raw_input('Restore file %s: %s? y/N ' % (num, restore_file))
    if yn != 'y' and yn != 'Y':
        print ('Restore cancelled.')
        return
    print ('Start restore to local database...')
    p = raw_input('Input mysql root password: ')
    sqls = [
        'drop database if exists awesome;',
        'create database awesome;',
        'grant select, insert, update, delete on awesome.* to \'%s\'@\'localhost\' identified by \'%s\';' % (db_user, db_password)
    ]
    for sql in sqls:
        local(r'mysql -uroot -p%s -e "%s"' % (p, sql))
    with lcd(backup_dir):
        local('tar zxvf %s' % restore_file)
    local(r'mysql -uroot -p%s awesome < backup/%s' % (p, restore_file[:-7]))
    with lcd(backup_dir):
        local('rm -f %s' % restore_file[:-7])