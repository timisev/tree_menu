from django import template

from app.models import Item


register = template.Library()


@register.inclusion_tag('app/menu.html')  
def menu():  
    latest_posts = Item.objects.all()
    return {'latest_posts': latest_posts}