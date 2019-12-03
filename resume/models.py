from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField('姓名',max_length=20)
    birth = models.DateField('生日')
    degree = models.CharField('学位',max_length=10)
    sites = models.CharField('网站',max_length=20)
    email = models.EmailField('邮件')
    phone = models.CharField('电话',max_length=20)
    img = models.ImageField('头像',null=True,upload_to='user/info/%Y/%m/%d')
    img_head = models.ImageField('照片',null=True)
    class Meta:
        verbose_name = '基本信息'
        verbose_name_plural = verbose_name

class Program(models.Model):
    language = models.CharField('语言',max_length=20)
    def __str__(self):
        return self.language

class Skill(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,verbose_name='语言',on_delete=models.CASCADE)
    level = models.CharField('掌握程度',max_length=10)
    updated = models.DateField('更新时间',auto_now_add=True)
    created = models.DateField('创建时间',auto_now=True)
    class Meta:
        verbose_name = '技能'
        verbose_name_plural = verbose_name

class WorkExperience(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    company = models.CharField('公司名称',max_length=30)
    started = models.DateField('入职时间',null=False)
    ended = models.DateField('离职时间',null=True,blank=True)
    title = models.CharField('岗位职称',max_length=20)
    description = models.CharField('岗位描述',max_length=30)
    updated = models.DateField('更新时间', auto_now_add=True)
    created = models.DateField('创建时间', auto_now=True)
    class Meta:
        verbose_name = '工作经验'
        verbose_name_plural = verbose_name

class EducationExperience(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    college = models.CharField('学校名称',max_length=20)
    started = models.DateField('入学时间',null=False)
    ended = models.DateField('毕业时间',null=True,blank=True)
    major = models.CharField('专业',max_length=20)
    madescriptionjor = models.CharField('专业描述',max_length=20)
    updated = models.DateField('更新时间', auto_now_add=True)
    created = models.DateField('创建时间', auto_now=True)
    class Meta:
        verbose_name = '教育经验'
        verbose_name_plural = verbose_name

class Project(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    name = models.CharField('项目名称',max_length=20)
    img = models.ImageField('项目图片',null=True,upload_to='user/info/%Y/%m/%d')
    cleent = models.CharField('客户',max_length=50,null=True)
    tags = models.ManyToManyField(Program,verbose_name='标签')
    updated = models.DateField('更新时间', auto_now_add=True)
    created = models.DateField('创建时间', auto_now=True)
    class Meta:
        verbose_name = '项目经验'
        verbose_name_plural = verbose_name
    def get_absolute_url(self):
        return reverse('project_detail',args=(self.created.year,self.created.month,self.created.day,self.id))


# class Contact(models.Model):
#     user = models.ForeignKey(UserInfo,verbose_name='用户',on_delete=models.CASCADE,related_name='contact_user')
#     phone = models.ForeignKey(UserInfo,verbose_name='电话',on_delete=models.CASCADE,related_name='contact_phone')
#     email = models.ForeignKey(UserInfo,verbose_name='邮箱',on_delete=models.CASCADE,related_name='contact_email')
#     site = models.CharField('地址',max_length=50)

