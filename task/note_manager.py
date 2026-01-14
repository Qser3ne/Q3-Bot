import sqlite3
import sys
import os

# 添加父目录到路径以便导入 config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABASE_PATH


class NoteManager:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = DATABASE_PATH
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._init_tables()

    def _init_tables(self):
        """初始化主要事务、次要事务和个人事务三张表"""
        for table in ['main_tasks', 'secondary_tasks', 'personal_tasks']:
            self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
        self.conn.commit()

    def add_task(self, task_type, content, start_time):
        """添加事务"""
        table = 'main_tasks' if task_type == 'main' else 'secondary_tasks'
        self.cursor.execute(
            f"INSERT INTO {table} (content, start_time) VALUES (?, ?)",
            (content, start_time)
        )
        self.conn.commit()
        return True

    def _get_task_list(self, task_type):
        """获取任务列表，按 start_time 排序"""
        table = 'main_tasks' if task_type == 'main' else 'secondary_tasks'
        self.cursor.execute(
            f"SELECT id, content, start_time FROM {table} ORDER BY start_time ASC"
        )
        return self.cursor.fetchall()

    def get_tasks(self):
        """查询所有事务"""
        main_rows = self._get_task_list('main')
        sec_rows = self._get_task_list('secondary')

        msg = "【主要事务】\n"
        if main_rows:
            for idx, row in enumerate(main_rows, 1):
                _, content, start_time = row
                msg += f"{idx}. {content}\n   ⏰ {start_time}\n\n"
        else:
            msg += "暂无 🎉\n\n"

        msg += "【次要事务】\n"
        if sec_rows:
            for idx, row in enumerate(sec_rows, 1):
                _, content, start_time = row
                msg += f"{idx}. {content}\n   ⏰ {start_time}\n\n"
        else:
            msg += "暂无 🎉"

        return msg.strip()

    def delete_task(self, task_type, display_id):
        """
        按显示序号删除事务
        """
        rows = self._get_task_list(task_type)
        
        if display_id < 1 or display_id > len(rows):
            return False

        # 获取对应序号的实际数据库 id
        real_id = rows[display_id - 1][0]
        table = 'main_tasks' if task_type == 'main' else 'secondary_tasks'
        self.cursor.execute(f"DELETE FROM {table} WHERE id = ?", (real_id,))
        self.conn.commit()
        return True

    def add_personal_task(self, content, start_time):
        """添加个人事务"""
        self.cursor.execute(
            "INSERT INTO personal_tasks (content, start_time) VALUES (?, ?)",
            (content, start_time)
        )
        self.conn.commit()
        return True

    def get_personal_tasks(self):
        """查询所有个人事务"""
        self.cursor.execute(
            "SELECT id, content, start_time FROM personal_tasks ORDER BY start_time ASC"
        )
        rows = self.cursor.fetchall()

        msg = "【个人事务】\n"
        if rows:
            for idx, row in enumerate(rows, 1):
                _, content, start_time = row
                msg += f"{idx}. {content}\n   ⏰ {start_time}\n\n"
        else:
            msg += "暂无 🎉"

        return msg.strip()

    def delete_personal_task(self, display_id):
        """按显示序号删除个人事务"""
        self.cursor.execute(
            "SELECT id FROM personal_tasks ORDER BY start_time ASC"
        )
        rows = self.cursor.fetchall()

        if display_id < 1 or display_id > len(rows):
            return False

        real_id = rows[display_id - 1][0]
        self.cursor.execute("DELETE FROM personal_tasks WHERE id = ?", (real_id,))
        self.conn.commit()
        return True

    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()


db = NoteManager()
