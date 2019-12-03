from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import Context
from django.template.loader import get_template

#主页显示
from django.urls import reverse

from blog.models import Article,Comment
from blog.form  import CommentForm
from resume.models import UserInfo,Skill


def index(request):
    id = UserInfo.objects.get(id=1)
    str = id.img.url
    skill = Skill.objects.filter(user=id)
    Context = {'img_index':str,'img':id,'skill_list':skill}
    return render(request,'index.html',Context)


# 博客列表
def blog(request):
    id = UserInfo.objects.get(id=1)
    str = id.img.url
    article = Article.objects.all()
    paginator  = Paginator(article,2)
    # 从request请求发来的页码
    page = request.GET.get('page')
    # 根据页码数获取分页对象
    contacts   = paginator.get_page(page)
    # 将分页对象防止在上下文中并返回
    Context={'contacts':contacts,'img_index':str}
    return render(request,'blog.html',Context)


#博客详情
def  blog_detail(request,year,month,day,id):
    article = get_object_or_404(Article, pk=id)
    img_id = UserInfo.objects.get(id=1)
    str = img_id.img.url
    comments = Comment.objects.all()


    if request.method == 'GET':

        # 如果请求的方式是get  生产一个空的表单对象，通过上下文直接返回
        form = CommentForm()
        Context={'detail_list':article,'img_index':str,'form':form,'comments':comments}
        return render(request,'blog_datail.html',Context)
    elif request.method == 'POST':
        # 如果是post方式，那么先创建一个表单实例然后绑定数据到该表单，然后通过表单的is_valid()方法对form进行数据有效性性检验，
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(article=article,text=data['comments'],name=data['name'],email=data['email'])
            # 这里再次创建一个空的表单对象是因为，上一条的新增数据语句已经执行成功，再次生成空的对象是为了防止网页上新增成功之后
            # 数据依然残留在表单中的bug，（还有其他方式，这并不是一种最完美的解决方案）
            form = CommentForm()
            Context = {'detail_list': article, 'img_index': str, 'form': form,'comments':comments}
            messages.success(request, '留言成功！')
            return render(request, 'blog_datail.html', Context)
        else:
            # 如果数据的有效性建议并没有通过，同上一样，直接返回
            Context = {'detail_list': article, 'img_index': str, 'form': form,'comments':comments}
            messages.error(request, '留言失败')
            return render(request, 'blog_datail.html', Context)



# 实现文章搜索功能
def search(request):
    id = UserInfo.objects.get(id=1)
    str = id.img.url
    q = request.GET.get('q')
    # 判断用户搜索框是否存在输入，如果用户没有输入则重定向页面到博客
    if not q:
        return HttpResponseRedirect(reverse("blog"))
    # 使用Q对象可以将查询条件组合在一起使用，中间可以使用  |    &  连接
    article = Article.objects.filter(Q(title__icontains=q)|Q(text__icontains=q)|Q(tags__icontains=q))
    paginator = Paginator(article,2)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    Context = {'contacts': page, 'img_index': str}
    return render(request, 'search.html', Context)