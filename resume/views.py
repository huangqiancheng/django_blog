from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.template.loader import get_template

from resume.models import UserInfo,WorkExperience,EducationExperience,Project,Skill

# 获取数据库中的图片（如果需要在页面上展示需要获取图片路径而非图片）
# def index(request):
#     id  = UserInfo.objects.get(id=3)
#     str = "<img src='{0}'>".format(id.img.url)
#     return HttpResponse(str)

def resume(request):
    id = UserInfo.objects.get(id=1)
    str = id.img.url
    # 根据id为1的这个对象去查工作经验表，教育经验表，技能表，返回user_id为1的所有的工作经验、教育经验、技能的数据
    work = WorkExperience.objects.filter(user=id)
    Education = EducationExperience.objects.filter(user=id)
    skill = Skill.objects.filter(user=id)
    # 通过上写文返回之前查到的对象，此处传入 str 是因为每个页面都继承了侧边栏，侧边栏需要一个头像，所以每个页面都需要一个参数对应
    # html页面中的对象，所以每次都需要传入，也可直接传入id对象，然后直接在html页面通过点，点出属性，可以有一样的效果
    Context = {'resume_user':id,'WorkExperience_list':work,'EducationExperience_list':Education,'img_index':str,'img':id,'skill_LIst':skill}
    return render(request,"resume.html",Context)


# 项目页面
def project(request):
    id = UserInfo.objects.get(id=1)
    str = id.img.url
    pro = Project.objects.all()
    Context = {'img_index':str,'project_list':pro}
    return render(request,"portfolio.html",Context)

# 项目详情页面
# 这里传入年月日时因为path路由所对应的路径，（request请求必填）
def  project_detail(request,year,month,day,id):
    img_id = UserInfo.objects.get(id=1)
    str = img_id.img.url
    # 通过页面上的id去查找Project表锁对应的数据，查不到返回404
    article = get_object_or_404(Project,pk=id)
    # 通过上下文返回
    Context={'detail_list':article,'img_index':str}
    return render(request,'project_detail.html',Context)

# 联系我们页面
def contact(request):
    id = UserInfo.objects.get(id=1)
    Context={'context_list':id,'img_index':id.img.url}
    return render(request,'contact.html',Context)