from django import template
from django.template.defaultfilters import stringfilter
from ..models import menu_point
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name):

    query_text = f'''
    WITH RECURSIVE initial_menu (
       id,
       url,
       name,
       parent_id
   )
   AS (
       SELECT id,
              url,
              name,
              parent_id
         FROM Menu_menu_point
        WHERE name = "{name}"
       UNION
       SELECT mp.id,
              mp.url,
              mp.name,
              mp.parent_id
         FROM Menu_menu_point mp
              JOIN
              initial_menu ON mp.id = initial_menu.parent_id
   )
   SELECT *
FROM Menu_menu_point
WHERE parent_id IN (
    SELECT id
    FROM initial_menu
    ORDER BY parent_id
) OR id IN (
    SELECT id
    FROM initial_menu
    ORDER BY parent_id
    LIMIT 1
)
ORDER BY parent_id;
'''
    menu_points = menu_point.objects.raw(query_text)
    tree = queryset_to_tree(menu_points)
    html = render_tree(tree, context['base_url'])

    return mark_safe(html)

def queryset_to_tree(queryset, parent_id=None):
    tree = []
    for row in queryset:
        if row.parent_id == parent_id:
            children = queryset_to_tree(queryset, row.id)
            if children:
                row.children = children
            tree.append(row)
    return tree

def render_tree(tree, base_url):
    html = '<ul>'
    for item in tree:
        html += f'<li><a href="{base_url}?menu_point={item.name}">{item.name}</a>'
        if 'children' in dir(item):
            html += render_tree(item.children, base_url)
        html += '</li>'
    html += '</ul>'
    return html