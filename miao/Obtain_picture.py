import requests
import base64
import sys
import os

# 添加父目录到路径以便导入 config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BLOCKED_TAGS, PICTURE_FILTER_LEVEL, PICTURE_API_URL


def Obtain_picture(tag=None, filter_level=None):
    """
    获取图片
    :param tag: 搜索标签，None 则随机
    :param filter_level: 内容过滤级别 (0=普通, 1=包含敏感内容, 2=仅敏感内容)
    """
    if filter_level is None:
        filter_level = PICTURE_FILTER_LEVEL
    api_url = PICTURE_API_URL
    params = {
        "r18": filter_level,
        "size": ["regular"],
        "num": 3
    }
    
    if tag:
        params["tag"] = [tag]

    try:
        resp = requests.post(api_url, json=params, timeout=10).json()

        if not resp.get("data"):
            return None

        # 过滤掉带有屏蔽标签的图片
        for item in resp["data"]:
            # 过滤 AI 生成的图片
            if item.get("aiType") == 2:
                continue
                
            tags = item.get("tags", [])
            if any(blocked in tags for blocked in BLOCKED_TAGS):
                continue
            
            img_url = item["urls"].get("regular")
            if not img_url:
                continue

            # 下载图片并转 base64
            img_resp = requests.get(img_url, timeout=15)
            if img_resp.status_code != 200:
                continue

            b64_data = base64.b64encode(img_resp.content).decode('utf8')
            return "base64://" + b64_data

        return None
        
    except Exception as e:
        print(f"获取图片异常: {e}")
        return None
