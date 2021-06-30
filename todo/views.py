# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.


class TodoList(ListView):  # djangoのテンプレート、ListViewを継承する
    template_name = 'list.html'  # templateの指定
    model = TodoModel  # models.pyの中のどのクラスを使うのか


class TodoDetail(DetailView):  # djangoのテンプレート、DetailViewを継承する
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')  # テーブルのどのフィールドと紐づけるか指定
    success_url = reverse_lazy('list')  # データの作成が完了した時に遷移するURLを指定
    # ＊ メモ　クラスの中で指定するときはreverse_laxy、関数の場合はreverse
    # reverseとは？：urlを逆回りにする　
    # reverseの動き：viewをまずみて、viewに指定されたURLをたどる urls.pyでname指定された情報を辿ってURLを引く。


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')  # データの作成が完了した時に遷移するURLを指定


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')  # データの作成が完了した時に遷移するURLを指定
