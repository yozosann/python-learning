from fabric.api import run, env

import os
 
env.hosts = ['ubuntu@ec2-13-59-147-100.us-east-2.compute.amazonaws.com']
env.key_filename = os.path.abspath('../../ytj8929309.pem')
 
def hello():
    run('ls -a')