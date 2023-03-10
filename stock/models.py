from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.urls import reverse



CATEGORY = (('meet','肉'),('vegetable','野菜'),('alcohol','お酒'),('other','その他'))
# Create your models here.
class stock(models.Model):
    
    category = models.CharField('カテゴリー名', max_length=100, choices = CATEGORY)
    item_name = models.CharField('商品名',max_length=100, null=True, blank=True)
    inventory = models.PositiveIntegerField('在庫数', null=True, blank=True)

    #DateField設定
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = '在庫'
        verbose_name_plural = '在庫'





    #return ParentCategory

