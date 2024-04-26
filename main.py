import requests
import time
import datetime
from colorama import init, Fore, Style


"""
1、通过第三方服务Server酱发送微信消息，可正常使用
2、免费额度，从注册开始只有7天，且一天智能发送五条消息
3、第三方服务Server酱：https://sct.ftqq.com/after
"""

def check_schedule(num):
    try:
        url = 'https://wxmpro.jctopinfo.com/TKService/GetSchedule'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJTWVNUT0tFTiI6IntcIkNvbXBhbnlcIjp7XCJBcHBJZFwiOlwid3hlZTg2ZWUzNTI4ZTk2Y2Y3XCIsXCJDb21wYW55Q29kZVwiOlwiZHF4bXBcIixcIkNvbXBhbnlOYW1lXCI6XCLov5Dlvrflh7rooYxcIixcInN1cGVyUHJpdmlsZWdlZFwiOmZhbHNlLFwiY3VycmVudFN0YXRpb25cIjpcIlpaSlwifSxcIkxvZ2luVXNlclwiOntcIk9wZW5JRFwiOlwib0xpckE2OW5NWm5EUm5DUk9zRDhFR0FjeTh4RVwiLFwid3hVc2VySURcIjoxMzEyNjk3LFwiVXNlcklEXCI6MTMxMjY5NyxcIlVzZXJDb2RlXCI6XCJvSXM4djBiVHdrVm9HY0pLY0c0eGNHNFZoS0JNXCIsXCJVc2VyTmFtZVwiOlwi5b6u5L-h55So5oi3b0lzOHZcIixcImhlYWRJbWdcIjpcIlwiLFwiVGVsXCI6bnVsbCxcIkNhcmRUeXBlXCI6XCJcIixcIklEQ2FyZFwiOm51bGx9LFwiU2Vzc2lvbkxldmVsXCI6MixcIkV4cGlyZWRUaW1lXCI6XCJcXC9EYXRlKDE3MjE2MzU3MzI2MTIpXFwvXCJ9IiwiZXhwIjoxNzIxNjM1NzMyfQ.BBTnWm1tmT6gysoR1vxkqJBQ5z4ynfTi6oO4QpeJLsE',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Referer': 'https://servicewechat.com/wxee86ee3528e96cf7/115/page-frame.html'
        }
        data = 'cp=dqxmp&st=530028027&DepStation=530028027&SchLine=&DstNode=246&NodeType=0&SchDate=2024-05-01'

        response_json = requests.post(url, headers=headers, data=data).json()

        # print(response_json)


        ticket = False

        # 打印所有班次
        for item in response_json['data']:
            if 'SchTime' in item and 'RemainSeatCount' in item:
                sch_time = item['SchTime']
                remain_seat_count = item['RemainSeatCount']
                now = datetime.datetime.now()

                # 检查班次是否为"08:40"
                if sch_time == "08:40":
                    init(autoreset=True)  # 初始化colorama，并设置样式自动重
                    # 使用colorama将"08:40"部分高亮显示
                    print(Fore.GREEN + Style.BRIGHT + f"请求次数：{num} 当前时间：{now} 班次：{sch_time} 剩余座位: {remain_seat_count}")
                    if remain_seat_count > 0:
                        ticket = True
                else:
                    # 普通打印
                    print(f"请求次数：{num} 当前时间：{now} 班次：{sch_time} 剩余座位: {remain_seat_count}")
        print("-----------------------------------------------------------------------------")

        if ticket:
            send_wechat_message(f"08:40的班次还剩{remain_seat_count}个座位！")
            # 发了一次消息后，休眠20分钟，防止重复发消息
            print("发送微信消息成功，休眠20分钟...")
            time.sleep(1200)

        # # 判断是否有票
        # for item in response_json['data']:
        #     if item['SchTime'] == '08:40':
        #         remain_seat_count = item['RemainSeatCount']
        #         # now = datetime.datetime.now()
        #         # print(f"请求次数：{num}      当前时间：{now}      班次：08:40      剩余座位: {remain_seat_count}")
        #         if remain_seat_count > 0:
        #             send_wechat_message(f"08:40的班次还剩{remain_seat_count}个座位！")
        #
        #             # 发了一次消息后，休眠20分钟，防止重复发消息
        #             time.sleep(1200)


    except Exception as e:
        print(f"发生错误：{e}")


def send_wechat_message(message):
    # 使用第三方服务Server酱发送消息
    wechat_url = "https://sctapi.ftqq.com/SCT245991TOWUswgChVagimuz8Y1IuABzE.send"
    requests.post(wechat_url, data={'title': '余票监控通知', 'desp': message})



num = 3020

# 设定脚本运行频率
while True:
        check_schedule(num)
        num += 1
        time.sleep(30)

