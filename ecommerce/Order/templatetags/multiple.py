from django import template

register=template.Library()

@register.simple_tag(name='multiple')
def mul(x,y):
    return x*y