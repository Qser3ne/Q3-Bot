import json


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


async def handle_help_command(ws, group_id, raw_message):
    """
    处理帮助命令
    """
    if raw_message.strip() != '/help':
        return False

    help_msg = (
        "📖 命令帮助\n"
        "\n"
        "【比赛查询】\n"
        "/国际比赛 - 查询国际比赛\n"
        "/国内比赛 - 查询国内比赛\n"
        "\n"
        "【事务管理】\n"
        "/查询事务 - 查询当前事务\n"
        "/添加主要事务<内容><时间>\n"
        "/添加次要事务<内容><时间>\n"
        "/删除主要事务<ID>\n"
        "/删除次要事务<ID>\n"
        "\n"
        "【图片功能】\n"
        "/ciallo - 获取动漫图片\n"
        "/miao - 随机图片\n"
        "/miao<标签> - 标签搜索图片\n"
        "/miao2 - 随机特殊图片\n"
        "/miao2<标签> - 标签搜索特殊图片\n"
    )
    await send_group_msg(ws, group_id, help_msg)
    return True
