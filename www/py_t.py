#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio


async def test():

    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

    #u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    u = Blog(user_id='test_id', user_name='test_user_name', user_image='test_img', name='test_name', summary='test_summary', content='test_content')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()