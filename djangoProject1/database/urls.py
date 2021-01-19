from django.urls import path
from views.show_pages import show_list

urls =[
path('/pages', show_list)
]