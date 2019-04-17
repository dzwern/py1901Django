from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import BookInfo,HeroInfo

from django.template import loader

#定义视图函数
def index(request):
    # return HttpResponse("首页")
    #加载模板
    # indextemp=loader.get_template("booktest/index.html")
    # cont={"username":"dzw"}
    # # 渲染模板
    # result=indextemp.render(cont)
    # # 返回模板
    # return HttpResponse(result)

    return render(request,"booktest/index.html",{"username":"dzw"})

def list(request):
    # return HttpResponse("列表页")

    booklist=BookInfo.objects.all()

    return render(request,"booktest/list.html",{"booklist":booklist})
def detail(request,id):

    book=BookInfo.objects.get(pk=id)
    # return HttpResponse("详情页")
    return render(request,"booktest/detail.html",{"book":book})
