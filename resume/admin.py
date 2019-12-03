from django.contrib import admin

# Register your models here.
from resume.models import UserInfo,Program,Skill,WorkExperience,EducationExperience,Project
from blog.models import Article,Comment
# class ProgramInlineAdmin(admin.TabularInline):
#     model = Program
class SkillInlineAdmin(admin.TabularInline):
    model = Skill
    # filter_horizontal = ['program']

class WorkExperienceInlineAdmin(admin.TabularInline):
    model = WorkExperience

class EducationExperienceInlineAdmin(admin.TabularInline):
    model = EducationExperience

class ProjectInlineAdmin(admin.TabularInline):
    model = Project
    filter_horizontal = ['tags']





class UserInfoAdmin(admin.ModelAdmin):
    inlines = [SkillInlineAdmin,WorkExperienceInlineAdmin,EducationExperienceInlineAdmin,ProjectInlineAdmin]

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Program)