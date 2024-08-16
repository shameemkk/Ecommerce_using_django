from django import template

register=template.Library()

@register.simple_tag(name='total')
def total(cart):
    total=0
    for item in cart.added_item.all():
        total+=item.Product.new_price*item.Quantity
    return total