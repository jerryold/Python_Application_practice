
import twstock
import requests
import schedule
import time
import pycron
import pytz
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler




def get_two_float(f_str, n):
    a, b, c = f_str.partition('.')
    c = c[:n]
    return ".".join([a, c])

def sendToLine1():
   
    msg1=(f' \n 現在早上9:30,記得吃葉黃素 \n')
    print(msg1)       

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg1}} #
    headers = {'Authorization': 'Bearer ' + 'FGMlOgB1202tVkhjf6Uh7Xb6n3r1N7Yh6SycDH0AVdk'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

def sendToLine2():
   
    msg2=(f' \n 現在早上11:20,記得吃B群 \n')
    print(msg2)       

    url = "https://notify-api.line.me/api/notify"
    payload2={'message':{msg2}} #
    headers = {'Authorization': 'Bearer ' + 'FGMlOgB1202tVkhjf6Uh7Xb6n3r1N7Yh6SycDH0AVdk'}
    response = requests.request("POST", url, headers=headers, data=payload2)
    print(response.text)

def sendToLine3():
   
    msg3=(f' \n 現在下午1:30,記得吃魚油 \n')
    print(msg3)       

    url = "https://notify-api.line.me/api/notify"
    payload3={'message':{msg3}} #
    headers = {'Authorization': 'Bearer ' + 'FGMlOgB1202tVkhjf6Uh7Xb6n3r1N7Yh6SycDH0AVdk'}
    response = requests.request("POST", url, headers=headers, data=payload3)
    print(response.text)

def sendToLine4():
   
    msg4=(f' \n 現在下午17:10,記得吃C \n')
    print(msg4)       

    url = "https://notify-api.line.me/api/notify"
    payload4={'message':{msg4}} #
    headers = {'Authorization': 'Bearer ' + 'FGMlOgB1202tVkhjf6Uh7Xb6n3r1N7Yh6SycDH0AVdk'}
    response = requests.request("POST", url, headers=headers, data=payload4)
    print(response.text)

    

#設定特定時間執行
now1=datetime.now()
timezone=pytz.timezone('Asia/Singapore')
current_time=now1.astimezone(timezone)


week = datetime.today().weekday()
   


# Creating a scheduler object.
scheduler = BlockingScheduler()
scheduler.add_job(sendToLine1, "cron", minute='30',hour='1',day_of_week='mon-fri')
scheduler.add_job(sendToLine2, "cron", minute='20',hour='3',day_of_week='mon-fri')
scheduler.add_job(sendToLine3, "cron", minute='30',hour='5',day_of_week='mon-fri')
scheduler.add_job(sendToLine4, "cron", minute='20',hour='9',day_of_week='mon-fri')
# Starting the scheduler in a separate thread.
scheduler.start()