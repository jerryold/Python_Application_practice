
import twstock
import requests
import schedule
import time
import pycron
import pytz
from datetime import datetime, timedelta




def get_two_float(f_str, n):
    a, b, c = f_str.partition('.')
    c = c[:n]
    return ".".join([a, c])

def sendToLine1():
   
    msg1=(f' \n 現在早上9:00,記得吃葉黃素 \n')
    print(msg1)       

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg1}} #
    headers = {'Authorization': 'Bearer ' + 'ACtEtEwl80EBocUV05Bbwm5RAltEDpPOAfbxnQyiSdU'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

def sendToLine2():
   
    msg1=(f' \n 現在早上11:00,記得吃B群 \n')
    print(msg1)       

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg1}} #
    headers = {'Authorization': 'Bearer ' + 'ACtEtEwl80EBocUV05Bbwm5RAltEDpPOAfbxnQyiSdU'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

def sendToLine3():
   
    msg1=(f' \n 現在下午1:00,記得吃魚油 \n')
    print(msg1)       

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg1}} #
    headers = {'Authorization': 'Bearer ' + 'ACtEtEwl80EBocUV05Bbwm5RAltEDpPOAfbxnQyiSdU'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

def sendToLine4():
   
    msg1=(f' \n 現在下午17:00,記得吃C \n')
    print(msg1)       

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg1}} #
    headers = {'Authorization': 'Bearer ' + 'ACtEtEwl80EBocUV05Bbwm5RAltEDpPOAfbxnQyiSdU'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

    

#設定特定時間執行
now1=datetime.now()
timezone=pytz.timezone('Asia/Singapore')
current_time=now1.astimezone(timezone)



def weekday_job1(x):
    week = datetime.today().weekday()
    if week<5 and 1<=current_time.now().hour<=2:
        schedule.every().hour.do(x)
def weekday_job2(x):
    week = datetime.today().weekday()
    if week<5 and 3<=current_time.now().hour<=4:
        schedule.every().hour.do(x)

def weekday_job3(x):
    week = datetime.today().weekday()
    if week<5 and 5<=current_time.now().hour<=6:
        schedule.every().hour.do(x)

def weekday_job4(x):
    week = datetime.today().weekday()
    if week<5 and 9<=current_time.now().hour<=10:
        schedule.every().hour.do(x)


weekday_job1(sendToLine1)
weekday_job2(sendToLine2)
weekday_job3(sendToLine3)
weekday_job4(sendToLine4)

while True:
    schedule.run_pending()
    time.sleep(60)