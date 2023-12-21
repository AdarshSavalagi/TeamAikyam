# jobs.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import firebase_admin
from firebase_admin import credentials, messaging
from core.Supportings.fetch_news import get_share

def my_hourly_task():
    # stock price prediction 
    data = get_share()
    min_max={
        'AAPL':[124.17,199.11],
        'MSFT':[219.35,384.30],
        'GOOGL':[85.57,142.38],
        'AMZN':[81.43,150.57],
        'TSLA':[231.90,246.66],
    }
    for key, values in min_max:
        if data[key]>values[1]:
            try:
                cred = credentials.Certificate(
                        "gdschackathon-de879-firebase-adminsdk-75ijc-7133a91a32.json")
                firebase_admin.initialize_app(cred)
            except:
                pass
            notification = messaging.Notification(
                title=f'High Price Alert',
                body=f'{key} Price is below your threshold',
            )
            message = messaging.Message(
                notification=notification,
                topic='stocks'
            )
            messaging.send(message)
        elif data[key]<values[0]:
            try:
                cred = credentials.Certificate(
                        "gdschackathon-de879-firebase-adminsdk-75ijc-7133a91a32.json")
                firebase_admin.initialize_app(cred)
            except:
                pass
            notification = messaging.Notification(
                title=f'Low Price Alert',
                body=f'{key} Price is exceeded your limit',
            )
            message = messaging.Message(
                notification=notification,
                topic='stocks'
            )
            messaging.send(message)
    print("Running task every 2 hours")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        my_hourly_task,
        trigger=IntervalTrigger(hours=1),
        id='my_hourly_task',
        name='Run my task every 2 hours',
        replace_existing=True,
    )
    scheduler.start()