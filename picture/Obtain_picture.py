import requests
import base64
import sys
import os

# 添加父目录到路径以便导入 config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import RANDOM_PICTURE_API_URL

def Obtain_picture():
    # 请求逻辑
    api_url = RANDOM_PICTURE_API_URL
    response = requests.get(api_url)

    b64_data = base64.b64encode(response.content).decode('utf8')
    picture_b64Data= "base64://" + b64_data

    return picture_b64Data

