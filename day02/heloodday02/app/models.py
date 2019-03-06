from django.db import models

# Create your models here.
class Student(models.Model):
    # 假如有设置主键 系统就不会帮你添加
    # 假如没有设置主键,系统默认添加id(主键 自增长)
    s_id=models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_score = models.IntegerField(null=True)
    # sex  = models.CharField(max_length=4,default='男')
    s_weight=models.FloatField(null=True)
    s_delete=models.BooleanField(default=False)
    s_detail=models.TextField(default='')
    s_create=models.DateTimeField(auto_now_add=True)
    s_change=models.DateTimeField(auto_now=True)
    s_height=models.DecimalField(max_digits=6,decimal_places=1)
    s_test=models.IntegerField(null=True)
    s_math=models.IntegerField(default=0)
    s_english=models.IntegerField(default=0)

    class Meta:
        db_table='student'
        ordering=['s_score']
