"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mysite import settings
from resume import views as resume_views
from blog import views as blog_views
urlpatterns = [
    # 主页部分
    path('admin/', admin.site.urls),
    path('contact/', resume_views.contact, name="contact"),

    # 博客
    path('',blog_views.index,name='index'),
    # 联系我们页面


    path('blog/',blog_views.blog,name="blog"),
    path('blog/<int:year>/<int:month>/<int:day>/<int:id>/',blog_views.blog_detail,name = "blog_detail"),

    #简历
    path('resume/',resume_views.resume,name="resume"),
    path('project/',resume_views.project,name="project"),

    #项目详情页面
    path('project/<int:year>/<int:month>/<int:day>/<int:id>/',resume_views.project_detail,name="project_detail"),
    # 搜索功能页面
    path('search/',blog_views.search,name='seaarch'),
    
]

# 图片
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # 把静态文件的；链接和服务器上本地静态文件的路径关联起来
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)



