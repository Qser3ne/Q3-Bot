import json
import re
from task.note_manager import db


async def send_group_msg(ws, group_id, content):
    """
    发送群消息
    """
    msg = {
        "action": "send_group_msg",
        "params": {
            "group_id": group_id,
            "message": content
        },
        "echo": "msg_" + str(group_id)
    }
    await ws.send(json.dumps(msg))


async def handle_task_command(ws, group_id, raw_message):
    """
    处理事务相关命令
    """
    msg = raw_message.strip()

    # /添加主要事务<content><start_time>
    match = re.match(r'^/添加主要事务<(.+)><(.+)>$', msg)
    if match:
        content, start_time = match.groups()
        content = content.strip().replace('\\n', '\n')
        start_time = start_time.strip()
        if not content:
            await send_group_msg(ws, group_id, "❌ 事务内容不能为空")
        else:
            db.add_task('main', content, start_time)
            await send_group_msg(ws, group_id, f"✅ 主要事务添加成功\n📌 {content}\n🕒 {start_time}")
        return True

    # /添加次要事务<content><start_time>
    match = re.match(r'^/添加次要事务<(.+)><(.+)>$', msg)
    if match:
        content, start_time = match.groups()
        content = content.strip().replace('\\n', '\n')
        start_time = start_time.strip()
        if not content:
            await send_group_msg(ws, group_id, "❌ 事务内容不能为空")
        else:
            db.add_task('secondary', content, start_time)
            await send_group_msg(ws, group_id, f"✅ 次要事务添加成功\n📌 {content}\n🕒 {start_time}")
        return True

    # /查询事务
    if msg == '/查询事务':
        result = db.get_tasks()
        await send_group_msg(ws, group_id, result)
        return True

    # /删除主要事务<id>
    match = re.match(r'^/删除主要事务<(\d+)>$', msg)
    if match:
        task_id = int(match.group(1))
        if db.delete_task('main', task_id):
            await send_group_msg(ws, group_id, f"✅ 主要事务 ID:{task_id} 已删除")
        else:
            await send_group_msg(ws, group_id, f"❌ 主要事务 ID:{task_id} 不存在")
        return True

    # /删除次要事务<id>
    match = re.match(r'^/删除次要事务<(\d+)>$', msg)
    if match:
        task_id = int(match.group(1))
        if db.delete_task('secondary', task_id):
            await send_group_msg(ws, group_id, f"✅ 次要事务 ID:{task_id} 已删除")
        else:
            await send_group_msg(ws, group_id, f"❌ 次要事务 ID:{task_id} 不存在")
        return True

    # /add<content><start_time> - 添加个人事务
    match = re.match(r'^/add<(.+)><(.+)>$', msg)
    if match:
        content, start_time = match.groups()
        content = content.strip().replace('\\n', '\n')
        start_time = start_time.strip()
        if not content:
            await send_group_msg(ws, group_id, "❌ 事务内容不能为空")
        else:
            db.add_personal_task(content, start_time)
            await send_group_msg(ws, group_id, f"✅ 个人事务添加成功\n📌 {content}\n🕒 {start_time}")
        return True

    # /query - 查询个人事务
    if msg == '/query':
        result = db.get_personal_tasks()
        await send_group_msg(ws, group_id, result)
        return True

    # /delete<id> - 删除个人事务
    match = re.match(r'^/delete<(\d+)>$', msg)
    if match:
        task_id = int(match.group(1))
        if db.delete_personal_task(task_id):
            await send_group_msg(ws, group_id, f"✅ 个人事务 ID:{task_id} 已删除")
        else:
            await send_group_msg(ws, group_id, f"❌ 个人事务 ID:{task_id} 不存在")
        return True

    return False
