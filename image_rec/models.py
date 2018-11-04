from django.db import models

# Create your models here.
# fileModel实例对象save()时候存入table name: app名+FilesModel
class FilesModel(models.Model):
    # 给model定义元数据
    # verbose_name表示FilesModel实例对象输出时候的名称(在admin可以看见)
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
    """ 文件名称"""
    # file = models.FileField(upload_to='demo_files/%Y/%m/%d/')
    file = models.FileField()
    date = models.DateTimeField(auto_now=True)