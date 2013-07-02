

def add_zero(date):
    day = date.split(" ")[0]
    if len(day) == 1:
        return '0' + date
    else:
        return date
