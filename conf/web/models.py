from django.db import models

# Create your models here.



class categoty(models.Model):
    ads_cat = models.CharField(max_length=48, verbose_name="دسته بندی")
    ads_slug = models.SlugField(verbose_name="لینک")






class ads(models.Model):
    title = models.CharField(max_length=48, verbose_name='عنوان')
    ads_categoty = models.ManyToManyField(categoty, verbose_name='دسته بندی')
    body = models.TextField(verbose_name='توضیحات')
    price = models.BigIntegerField(verbose_name='قیمت')
    img = models.ImageField(upload_to='media/img')
