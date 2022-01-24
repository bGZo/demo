import logging  # 日志记录工具
import asyncio  # 异步 I/O
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)
# https://docs.python.org/zh-cn/3/library/logging.html#logging.getLevelName
# https://docs.python.org/zh-cn/3/library/logging.html#levels
# CRITICAL ERROR WARNING INFO DEBUG NOTSET

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
### return web.Response(body=b'<h1>Awesome</h1>')


# @asyncio.coroutine
# "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
# def init(loop):
async def init(loop):
    app = web.Application()
    # app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()  # await 协程, 指定任务后启动 From https://docs.python.org/zh-cn/3/library/asyncio-task.html
    srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
    # srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()  # 获取事件循环
loop.run_until_complete(init(loop))  # 运行直到 init(loop) 被完成。
loop.run_forever()  # 运行事件循环直到 stop() 被调用。
