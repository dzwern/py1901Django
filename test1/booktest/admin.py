from django.contrib import admin

from .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ["id","title","pub_date"]
    #过滤字段
    list_filter = ["btitle","bpub_date"]
    #搜索字段
    search_fields=["btitle","bpub_date"]
    #分页
    list_per_page = 2

class HeroInfoAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ["id","name","gender","content"]
    #过滤字段
    list_filter = ["hname","hgender","hcontent"]
    #搜索字段
    search_fields = ["hname","hgender","hcontent"]
    #分页
    list_per_page = 2





admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)