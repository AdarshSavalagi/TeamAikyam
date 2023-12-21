# jobs.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from core.Supportings.fetch_news import get_share

def my_hourly_task():
    # stock price prediction 
    data = get_share()
    min_max={
        'AAPL':[0,10],
        'MSFT':[1,10],
        'GOOGL':[1,10],
        'AMZN':[1,10],
        'TSLA':[1,10],
    }
    for key, values in min_max:
        if data[key]>values[1]:
            # notify that stock has reached hike price go get it
            pass
        elif data[key]<values[0]:
            # notify that stock is below threshold value
            pass
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
