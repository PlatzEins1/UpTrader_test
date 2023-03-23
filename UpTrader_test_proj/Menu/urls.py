from django.urls import path
from .views import menu

urlpatterns = [
	path('', menu, name = 'menu'),
]
#base level of menu is available via adding '/main/?menu_point=test1_level1' to the basic dev server address