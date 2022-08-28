from django import template
register = template.Library()


@register.filter
def to_unicode(obj):
    s = obj.encode('unicode_escape')
    ans = str(s)[2:-1].replace('\\\\', '\\')
    return ans