from django.shortcuts import render
from django.http import HttpResponse

# 引入所需映射类
from .models import Course

def index(request):
    return HttpResponse('Hello Shiyanlou')

# 新建视图函数
def courses(request):
    # 从数据库中获取全部课程数据
    courses = Course.objects.all()
    # 使用两个减号将每门课程的课程名和作者连起来
    # 使用 </br> 标签将各个课程数据连起来生成字符串
    # 其中 </br> 标签在浏览器页面上起到换行的作用
    s = '</br>'.join('{} -- {}'.format(course.name,course.pub_date)
            for course in courses)
    return HttpResponse(s)

def course(request, id):
    course = Course.objects.get(id=id)
    s = 'ID: {}</br>Name: {}</br>发布时间：{}</br>学生人数：{}'.format(
            course.id, course.name, course.pub_date, course.stu_number)
    return HttpResponse(s)