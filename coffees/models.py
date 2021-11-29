from django.db import models


# Create your models here.

class Roast(models.Choices):
    # enum = value(存入的值), display
    LIGHT = 'Light', '極淺度烘焙'
    CINNAMON = 'Cinnamon', '淺度烘焙'
    MEDIUM = 'Medium', '中度烘焙'
    HIGH = 'High', '中度微深烘焙'
    CITY = 'City', '中深度烘焙'
    FULL_CITY = 'Full-City', '微深度烘焙'
    FRENCH = 'French', '極深烘焙'
    ITALIAN = 'Italian', '極深度烘焙'


class OriginPlace(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)


class Coffee(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    weight = models.PositiveIntegerField('重量')
    taste = models.TextField('味道')
    description = models.TextField('描述')
    roast = models.CharField('烘焙程度', max_length=10, choices=Roast.choices)
    price = models.PositiveIntegerField('價格')
    discount = models.PositiveIntegerField('優惠價格')
    origin_place = models.ForeignKey(
        OriginPlace,
        on_delete=models.PROTECT,
        verbose_name='主要處理法'
    )

