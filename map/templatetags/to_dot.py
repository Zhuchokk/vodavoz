from django import template
register = template.Library()


@register.filter
def to_dot(obj):
    s = str(obj).replace(',', '.')
    return s
