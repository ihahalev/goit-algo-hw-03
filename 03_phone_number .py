import re

def phone_number(phone: str) -> str:
    filter_pattern = r"[^\+\d]"
    filtered = re.sub(filter_pattern, "", phone)
    format_pattern = r"(?P<plus>\+?)(?P<code>\d*?)?(?P<phone>\d{10}$)"
    def formate_number(match):
        plus = match.group("plus") if match.group("plus") else "+"
        code = match.group("code") if match.group("code") else "38"
        phone_number = plus+code+match.group("phone")
        return phone_number
    formated = re.sub(format_pattern, formate_number, filtered)
    return formated
