from datetime import datetime

def get_days_from_today(date: str) -> int|None:
    format = "%Y-%m-%d"
    try:
        #convert from string to datetime
        conveted_date = datetime.strptime(date, format)
        today = datetime.today().date()
        days = conveted_date.toordinal() - today.toordinal()
    except ValueError:
        print("get_days_from_today date format error", type(error), error)
    except Exception as error:
        print("get_days_from_today error", type(error), error)
    else:
        return days
