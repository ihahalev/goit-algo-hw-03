import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if (min>0 and max<=1000 and quantity>0):
        ticket_range = range(min, max+1)
        ticket_numbers = random.sample(ticket_range, quantity)
        ticket_numbers.sort()
        return ticket_numbers
    else:
        print("get_numbers_ticket input error", min, max, quantity)
        return []
