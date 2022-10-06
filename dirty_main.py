from application.salary import *
from datetime import datetime, timedelta

if __name__ == '__main__':
    utc_now = datetime.utcnow()
    tz_modifier = timedelta(hours=3)
    current_local_time = utc_now + tz_modifier

    calculate_salary(current_local_time)
