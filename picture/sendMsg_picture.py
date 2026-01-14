import json
from picture.Obtain_picture import Obtain_picture


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


async def handle_ciallo_command(ws, group_id, raw_message):
    """
    处理图片命令
    """
    if raw_message.strip() != '/ciallo':
        return False

    print("正在获取动漫图片")
    picture_b64 = Obtain_picture()
    print("成功获取动漫图片")
    await send_picture(ws, group_id, picture_b64)
    return True
