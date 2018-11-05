from django.db import models

# Create your models here.
# fileModel实例对象save()时候存入table name: app名+FilesModel
class Userphoto(models.Model):
    # 给model定义元数据
    # verbose_name表示FilesModel实例对象输出时候的名称(在admin可以看见)
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
    # 根文件为setting中的MEDIA_URL = '/upload_picture/'
    # 上传的子文件夹upload_to='headImg'
    # 文件:file = models.FileField(upload_to='headImg', default='thisisusersfile')
    # 图片:
    photo = models.ImageField(upload_to='usersPhoto', default='thisisusersphoto')
    date = models.DateTimeField(auto_now=True)


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars', default='thisismycar')
    # 文档 https://docs.djangoproject.com/en/2.1/topics/files/#file-storage
    # models.ImageField()对象的属性和方法:
    # >>> car = Car.objects.get(name="57 Chevy")
    # >>> car.photo
    # <ImageFieldFile: chevy.jpg>
    # >>> car.photo.name
    # 'cars/chevy.jpg'
    # >>> car.photo.path
    # '/media/cars/chevy.jpg'
    # >>> car.photo.url
    # 'http://media.example.com/cars/chevy.jpg'