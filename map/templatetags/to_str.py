from django import template
register = template.Library()


@register.filter
def to_str(obj):
    return str(obj)
