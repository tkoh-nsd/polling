from datetime import datetime
import pytz

def get_time_now():
    return datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")