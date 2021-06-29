from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls'))  # adminの文字列がない場合は全て、todo.urlsが呼び出される

]
