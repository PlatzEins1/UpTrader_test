from django.shortcuts import render


def menu(request):

    context = {}
    menu_point = request.GET.get('menu_point','')
    if menu_point:
        context['curent_menu'] = menu_point
    base_url = request.build_absolute_uri().split('?')[0]
    context['base_url'] = base_url
    return render(request, 'Menu.html', context)