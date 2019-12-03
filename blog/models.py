from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField('标题',max_length=30)
    text = models.TextField('正文')
    img = models.ImageField('图片')
    tags = models.CharField('标签',max_length=30)
    updated = models.DateField('更新时间', auto_now_add=True)
    created = models.DateField('发布时间', auto_now=True)
    is_pub = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_detail',args=(self.created.year,self.created.month,self.created.day,self.id))
    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    article = models.ForeignKey(Article,verbose_name='标题',on_delete=models.CASCADE)
    text = models.CharField('评论内容',max_length=400)
    name =  models.CharField('名字',max_length=30)
    email = models.EmailField('邮箱')
    updated = models.DateField('更新时间', auto_now_add=True)
    created = models.DateField('创建时间', auto_now=True)
    is_pub = models.BooleanField(default=False)
    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name