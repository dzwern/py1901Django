from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

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


def delete(request,id):

    BookInfo.objects.get(pk=id).delete()
    # return HttpResponse("删除成功")
    booklist=BookInfo.objects.all()

    return render(request,"booktest/list.html",{"booklist":booklist})


def addhero(request,bookid):

    # return HttpResponse("添加成功")
    # book=BookInfo.objects.get(pk=id)
    # return HttpResponse("详情页")
    return render(request,"booktest/addhero.html",{"bookid":bookid})


def addherohandler(request):

    bookid=request.POST["bookid"]
    hname=request.POST["heroname"]
    hgender=request.POST["sex"]
    hcontent=request.POST["herocontent"]
    # return HttpResponse("添加成功")

    book=BookInfo.objects.get(pk=bookid)

    hero=HeroInfo()
    hero.hname=hname
    hero.hgender=True
    hero.hcontent=hcontent
    hero.hbookid=book


    print(book,hero,'9999')
    hero.save()
    # return HttpResponse("添加成功")
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/',{"book":book})
