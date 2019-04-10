from django.db import models
from core.settings import STATIC_URL
class Users(models.Model):
    email = models.EmailField('信箱', primary_key=True) 
    password = models.CharField('密碼', max_length=20) 
    username = models.CharField('使用者名稱', max_length=20)
    def __str__(self):
        return self.username


class Planargraph(models.Model):
    planargraphId = models.AutoField('平面圖id', primary_key=True)
    name = models.CharField('名稱', max_length=20) 
    users = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='使用者')
    def __str__(self):
        return self.name

class Space(models.Model):
    IMAGE_CHOICES =(
        ('square.png','正方形'),
        ('rectangle.png','長方形'),
        ('rectangle-2.png','L形'),
        ('triangle.png','三角形'),)
    spaceId = models.AutoField('空間id', primary_key=True)
    name = models.CharField('名稱', max_length=20) 
    image = models.CharField('圖片',max_length=200, choices=IMAGE_CHOICES)

    planargraph = models.ForeignKey(Planargraph, on_delete=models.CASCADE, verbose_name='平面圖')
    def __str__(self):
        return self.name

    def get_image_url(self):
        return '{}planargraphs/{}'.format(STATIC_URL, self.image)
