from django.db import models


# Create your models here.
class TodoModel(models.Model):
    # カラムとフィールドデータ型を指定
    title = models.CharField(max_length=100)  # CharFiledはmax_lengthの指定が必須
    memo = models.TextField()  # CharFieldより多い文字数を入力できるフィールド
