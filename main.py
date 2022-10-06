from application import calculate_salary, get_employees
from datetime import datetime, timedelta
from pytz import timezone

if __name__ == '__main__':
    utc_now = datetime.utcnow()
    tz_modifier = timedelta(hours=3)
    current_local_time = utc_now + tz_modifier

    calculate_salary(current_local_time)
    get_employees(current_local_time)

    print('*' * 50)
    tz = timezone('Africa/Johannesburg')
    current_local_time = datetime.now(tz)
    calculate_salary(current_local_time)
