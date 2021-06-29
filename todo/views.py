from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel
# Create your views here.


class TodoList(ListView):  # djangoのテンプレート、ListViewを継承する
    template_name = 'list.html'  # templateの指定
    model = TodoModel  # models.pyの中のどのクラスを使うのか


class TodoDetail(DetailView):  # djangoのテンプレート、DetailViewを継承する
    template_name = 'detail.html'
    model = TodoModel
