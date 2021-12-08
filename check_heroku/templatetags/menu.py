from django import template
from check_heroku.models import Category


register = template.Library()

@register.inclusion_tag('check_heroku/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories':categories, 'menu_class': menu_class}
