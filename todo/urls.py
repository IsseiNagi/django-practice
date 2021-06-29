from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view()),
    # detailの中からプライマリーキーを指定して絞り込むという指定
    path('detail/<int:pk>/', TodoDetail.as_view()),
]
