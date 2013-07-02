from django import template
# from sat.truenorth.utils import add_zero

register = template.Library()

def format_date(date):
    return date.strftime("%d %B, %Y")

register.filter("format_date", format_date)    
