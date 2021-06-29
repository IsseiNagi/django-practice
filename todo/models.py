from django.db import models

# choicesのため。タプルで指定。左がデータベースに保存されるデータの名前。右がブラウザで表示される名前。
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


# Create your models here.
class TodoModel(models.Model):
    # カラムとフィールドデータ型を指定
    title = models.CharField(max_length=100)  # CharFiledはmax_lengthの指定が必須
    memo = models.TextField()  # CharFieldより多い文字数を入力できるフィールド
    priority = models.CharField(  # 優先度のカラムを追加
        max_length=50,
        choices=PRIORITY  # プルダウン選択させるにはchoicesを使う
    )
    duedate = models.DateField()  # 日付を管理するモデル

    # __str__でオブジェクトを文字列として返す設定
    def __str__(self):
        return self.title  # titleプロパティを返す
