from django.urls import path
from .views import todo

urlpatterns = [
    path('a/', todo)  # adminの文字列がない場合は全て、todo.urlsが呼び出される

]
