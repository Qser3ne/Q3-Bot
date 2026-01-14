import requests
import sys
import os

# 添加父目录到路径以便导入 config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CTF_INTERNATIONAL_API_URL

def query_UpcomingEvents_international():
    # 请求逻辑
    url = CTF_INTERNATIONAL_API_URL
    cookies = {
    }
    response = requests.get(url, cookies=cookies)
    data = response.json()

    # 定义信息变量
    Total_competition_information = ''
    Total_competition_information += '---------------------------------\n'

    # 信息处理
    try:
        for i in range(len(data[:4])):
            single_competition = data[i]

        
            Total_competition_information += f"比赛名称：{single_competition['比赛名称']}\n"
            Total_competition_information += f"比赛时间：{single_competition['比赛时间']}\n"
            Total_competition_information += f"比赛形式：{single_competition['比赛形式']}\n"
            Total_competition_information += f"比赛链接：{single_competition['比赛链接']}\n"
            Total_competition_information += f"赛事主办：{single_competition['赛事主办']}\n"
            Total_competition_information += '---------------------------------\n'
    except:
            Total_competition_information += ' 没有查询到相关信息\n'
    
    return Total_competition_information

def query_UpcomingEvents_domestic():
    Total_competition_information = '暂无'

    return Total_competition_information
