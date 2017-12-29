import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Ann', email='Ann@example.com', passwd='21111234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()

loop.run_until_complete(test(loop))
loop.close()
