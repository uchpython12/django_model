from django.db import models

# Create your models here.

class YourModel(models.Model):
    # 定义模型的字段
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    # 可选：定义模型方法
    def __str__(self):
        return self.name
