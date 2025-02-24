from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)

# Odwoływanie się do indexu listy
@register.filter
def index(sequence, i):
    try:
        return sequence[i]
    except (IndexError, TypeError):
        return None