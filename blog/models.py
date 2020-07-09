from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_convertor

#My Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="P")

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class Category(models.Model):
    parent   = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
    title    = models.CharField(max_length=30, verbose_name="عنوان دسته‌بندی")
    slug     = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status   = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICE = (
        ('D','پیش‌نویس'),
        ('P','منتشر‌شده'),
    )
    author      = models.ForeignKey(User , null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name="نویسنده")
    title       = models.CharField(max_length=30,verbose_name="عنوان مقاله")
    slug        = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category    = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    description = models.TextField(verbose_name="محتوای مقاله")
    thumbnail   = models.ImageField(upload_to="images",verbose_name="تصویر مقاله")
    publish     = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "تاریخ انتشار"

    def thumbnail_tag(self):
        return format_html("<img width=100 height=50 style='border-radius: 3px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "تصویر مقاله"
    
    objects = ArticleManager()