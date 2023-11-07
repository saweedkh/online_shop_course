from django import template

register = template.Library()

@register.filter
def translte_number(number):
    value = str(value)
    english_to_persian_table = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(english_to_persian_table)