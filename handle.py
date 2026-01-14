import json
from config import WHITELIST_GROUPS

from competition.sendMsg_competition import handle_competition_command
from help.sendMsg_help import handle_help_command
from picture.sendMsg_picture import handle_ciallo_command
from miao.sendMsg_picture import handle_miao_command
from task.sendMsg_task import handle_task_command


# 群消息处理器
async def handler(ws):
    print("napcat 已连接")

    async for msg in ws:
        data = json.loads(msg)
        print("收到事件:", data)

        # 过滤非消息事件
        if data.get('post_type') != 'message':
            continue

        raw_message = data.get("raw_message", "")
        group_id = data.get("group_id")

        # 白名单校验
        if not isinstance(raw_message, str) or group_id not in WHITELIST_GROUPS:
            continue

        # 路由分发 - 匹配到就处理并跳过后续
        if await handle_help_command(ws, group_id, raw_message):
            continue

        if await handle_competition_command(ws, group_id, raw_message):
            continue

        if await handle_ciallo_command(ws, group_id, raw_message):
            continue

        if await handle_miao_command(ws, group_id, raw_message):
            continue

        if await handle_task_command(ws, group_id, raw_message):
            continue
