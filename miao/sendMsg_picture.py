import json
import re
from miao.Obtain_picture import Obtain_picture


async def send_picture(ws, group_id, base64_data):
    """发送图片消息"""
    msg = {
        "action": "send_group_msg",
        "params": {
            "group_id": int(group_id),
            "message": {
                "type": "image",
                "data": {
                    "file": base64_data
                }
            }
        },
        "echo": "msg_" + str(group_id)
    }
    await ws.send(json.dumps(msg))


async def send_text(ws, group_id, text):
    """发送文字消息"""
    msg = {
        "action": "send_group_msg",
        "params": {
            "group_id": int(group_id),
            "message": text
        },
        "echo": "msg_" + str(group_id)
    }
    await ws.send(json.dumps(msg))


async def handle_miao_command(ws, group_id, raw_message):
    """
    处理图片命令
    /miao - 随机普通图片
    /miao<tag> - 标签搜索普通图片
    /miao2 - 随机特殊图片
    /miao2<tag> - 标签搜索特殊图片
    """
    msg = raw_message.strip()

    # /miao2<tag>
    match = re.match(r'^/miao2<(.+)>$', msg)
    if match:
        tag = match.group(1).strip()
        print(f"正在获取特殊图片，标签: {tag}")
        picture_b64 = Obtain_picture(tag=tag, filter_level=2)
        if picture_b64:
            await send_picture(ws, group_id, picture_b64)
        else:
            await send_text(ws, group_id, f"❌ 未找到标签「{tag}」相关图片")
        return True

    # /miao2
    if msg == '/miao2':
        print("正在获取随机特殊图片")
        picture_b64 = Obtain_picture(filter_level=2)
        if picture_b64:
            await send_picture(ws, group_id, picture_b64)
        else:
            await send_text(ws, group_id, "❌ 获取图片失败，请稍后再试")
        return True

    # /miao<tag>
    match = re.match(r'^/miao<(.+)>$', msg)
    if match:
        tag = match.group(1).strip()
        print(f"正在获取图片，标签: {tag}")
        picture_b64 = Obtain_picture(tag=tag, filter_level=0)
        if picture_b64:
            await send_picture(ws, group_id, picture_b64)
        else:
            await send_text(ws, group_id, f"❌ 未找到标签「{tag}」相关图片")
        return True

    # /miao
    if msg == '/miao':
        print("正在获取随机图片")
        picture_b64 = Obtain_picture(filter_level=0)
        if picture_b64:
            await send_picture(ws, group_id, picture_b64)
        else:
            await send_text(ws, group_id, "❌ 获取图片失败，请稍后再试")
        return True

    return False
