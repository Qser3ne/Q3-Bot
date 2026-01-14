import json
from competition.Obtain_competition import query_UpcomingEvents_domestic
from competition.Obtain_competition import query_UpcomingEvents_international


async def send_group_msg(ws, group_id, content):
    """发送群消息"""
    msg = {
        "action": "send_group_msg",
        "params": {
            "group_id": group_id,
            "message": content
        },
        "echo": "msg_" + str(group_id)
    }
    await ws.send(json.dumps(msg))


async def handle_competition_command(ws, group_id, raw_message):
    """
    处理比赛查询命令
    :return: True 已处理, False 非比赛命令
    """
    msg = raw_message.strip()

    if msg == '/国际比赛':
        print("查询国际比赛")
        result = query_UpcomingEvents_international()
        print(result)
        await send_group_msg(ws, group_id, result)
        return True

    if msg == '/国内比赛':
        print("查询国内比赛")
        result = query_UpcomingEvents_domestic()
        print(result)
        await send_group_msg(ws, group_id, result)
        return True

    return False
