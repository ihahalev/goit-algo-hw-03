from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    format = "%Y.%m.%d"
    # today = datetime.today().date()
    today = datetime.strptime("2024.01.22", format).date()
    next_week = today + timedelta(days=6)
    greatings = []
    for user in users:
        birth_date = datetime.strptime(user['birthday'], format).date()
        birthday_this_year = datetime(year=today.year, month=birth_date.month, day=birth_date.day).date()
        if (birthday_this_year < today or birthday_this_year > next_week):
            continue
        birthday_this_year_weekday = birthday_this_year.weekday()
        if (birthday_this_year_weekday == 5):
            #if its saturday, move greatings to monday
            greatings_day = (birthday_this_year + timedelta(days=2)).strftime(format)
            greatings.append({"name": user['name'], "congratulation_date": greatings_day})
        elif (birthday_this_year_weekday == 6):
            #if its sunday, move greatings to monday
            greatings_day = (birthday_this_year + timedelta(days=1)).strftime(format)
            greatings.append({"name": user['name'], "congratulation_date": greatings_day})
        else:
            greatings_day = birthday_this_year.strftime(format)
            greatings.append({"name": user['name'], "congratulation_date": greatings_day})
    return greatings
