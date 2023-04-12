import requests
import time
import json
import os

# B站API接口
API_URL = 'https://api.bilibili.com/x/series/archives'

# up主的mid
MID = '699438'
SERIES = '210751'

# 上次最新视频的bvid
last_bvid = ''

program_name = 'BBDown.exe'
program_args_addon = '--use-aria2c'


while True:
    # 请求B站API获取up主的最新视频信息
    response = requests.get(API_URL, params={'mid': MID,'series_id': SERIES})
    data = json.loads(response.text)
    # print(json.dumps(data))

    latest_bvid = data['data']['archives'][0]['bvid']
    # print(latest_bvid)

    # 如果最新视频的bvid不等于上次最新视频的bvid，说明up主上传了新视频，进行下载
    if latest_bvid != last_bvid:
        # 下载代码
        program_args = 'https://www.bilibili.com/video/' + latest_bvid
        command_line = f'{program_name} {program_args} {program_args_addon}'
        os.system(command_line)

        print('下载新视频')
        last_bvid = latest_bvid
    else:
        print('没新的')

    # 每隔60秒请求一次
    time.sleep(60)
