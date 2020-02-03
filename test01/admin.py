from django.contrib import admin
from test01 import models
from django.http import HttpResponse, FileResponse
import sqlite3
import pandas as pd

# Register your models here.
#admin.site.register(models.Eos)
@admin.register(models.Form1_1_1)
class Form1_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]#21
    list_filter = ["id{}".format(i) for i in range(1,21,1) ]#21
    list_editable = ["id{}".format(i) for i in range(1,21,1) ][1:]
    list_per_page = 50
    

@admin.register(models.Form1_1_2)
class FormForm1_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]


@admin.register(models.Form2_1_1)
class Form2_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_1_2)
class Form2_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_1_3)
class Form2_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]


@admin.register(models.Form2_2_1)
class Form2_2_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,14,1) ]


@admin.register(models.Form3_1_1)
class Form3_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]


@admin.register(models.Form3_1_2)
class Form3_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]#33


@admin.register(models.Form3_1_3)
class Form3_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,10,1) ]



@admin.register(models.Form3_2_1)
class Form3_2_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]


@admin.register(models.Form3_2_2)
class Form3_2_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]


@admin.register(models.Form3_2_3)
class Form3_2_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,9,1) ]


@admin.register(models.Form3_3_1)
class Form3_3_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]

@admin.register(models.Form3_3_2)
class Form3_3_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]


@admin.register(models.Form3_3_3)
class Form3_3_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]


@admin.register(models.Form3_3_4)
class Form3_3_4Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,35,1) ]


@admin.register(models.Form3_3_5)
class Form3_3_5Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]


@admin.register(models.Form3_4_1)
class Form3_4_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,15,1) ]


@admin.register(models.Form3_4_2)
class Form3_4_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]



@admin.register(models.Form3_4_3)
class Form3_4_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,13,1) ]


@admin.register(models.Form4_1_1)
class Form4_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,16,1) ]


@admin.register(models.Form5_1_1)
class Form5_1_1Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,17,1) ]

@admin.register(models.Form5_1_2)
class Form5_1_2Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,24,1) ]

@admin.register(models.Form5_1_3)
class Form5_1_3Admin(admin.ModelAdmin):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]

admin.site.site_header = '国家科技支撑计划课题“牛肉安全生产技术集成与示范”（编号）         牦牛肉安全数据库系统'
admin.site.site_title = '牦牛安全数据库系统'
##########################---Xadmin-###################################################

import xadmin
# Register your models here.
from xadmin import views
import pandas as pd
from . import columns_dic
from django.shortcuts import render
dic=columns_dic.dic

def make_published(self, request, queryset): 
    #pd.DataFrame(queryset.values)
    slug=request.path[-6:-1]  #获取当前发出请求的网页地址中的 slug字段，用于根据字典dic查找表头
    df = pd.DataFrame(queryset.values())
    x =df.describe()

    #col.insert(0,'id')
    c=[]
    li=[]
    col=[]
    for o in (x.index):
        li=[round(x[i][o],2) for i in list(x.columns)]
        li.insert(0,o)
        c.append(li)
    col=[dic[slug][int(i[-1:])-1] for i in list(x.columns)[1:] ]
    return render(request,"index.html",context={"name":" ","col":col,"cc":c})

make_published.short_description = "数据统计"



class GlobalSetting(object):

    # 设置后台顶部标题
    site_title ='牦牛肉安全生产数据库'
    # 设置后台底部标题
    site_footer ='国家科技支撑计划课题“牛肉安全生产技术集成与示范”（编号）         牦牛肉安全数据库系统'


xadmin.site.register(views.CommAdminView, GlobalSetting)


#创建注册类

class Form1_1_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]#21
    list_filter = ["id{}".format(i) for i in range(1,21,1) ]#21
    list_editable = ["id{}".format(i) for i in range(1,21,1) ][1:]
    list_per_page = 50
    actions = [make_published]

xadmin.site.register(models.Form1_1_1, Form1_1_1Admin)


class Form1_1_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,21,1) ]
    list_filter = ["id{}".format(i) for i in range(1,21,1) ]
    list_editable = ["id{}".format(i) for i in range(1,21,1) ]
    list_per_page = 50
    actions = [make_published]
    
xadmin.site.register(models.Form1_1_2, Form1_1_2Admin)

class Form2_1_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]
    list_filter = ["id{}".format(i) for i in range(1,48,1) ]
    list_editable = ["id{}".format(i) for i in range(1,48,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form2_1_1, Form2_1_1Admin)

class Form2_1_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]
    list_filter = ["id{}".format(i) for i in range(1,48,1) ]
    list_editable = ["id{}".format(i) for i in range(1,48,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form2_1_2, Form2_1_2Admin)


class Form2_1_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,48,1) ]
    list_filter = ["id{}".format(i) for i in range(1,48,1) ]
    list_editable = ["id{}".format(i) for i in range(1,48,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form2_1_3, Form2_1_3Admin)


class Form2_2_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,14,1) ]
    list_filter = ["id{}".format(i) for i in range(1,14,1) ]
    list_editable = ["id{}".format(i) for i in range(1,14,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form2_2_1, Form2_2_1Admin)

class Form3_1_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]
    list_filter = ["id{}".format(i) for i in range(1,5,1) ]
    list_editable = ["id{}".format(i) for i in range(1,5,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_1_1, Form3_1_1Admin)

class Form3_1_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]#33
    list_filter = ["id{}".format(i) for i in range(1,33,1) ]
    list_editable = ["id{}".format(i) for i in range(1,33,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_1_2, Form3_1_2Admin)


class Form3_1_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,10,1) ]
    list_filter = ["id{}".format(i) for i in range(1,10,1) ]
    list_editable = ["id{}".format(i) for i in range(1,10,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_1_3, Form3_1_3Admin)

class Form3_2_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,5,1) ]
    list_filter = ["id{}".format(i) for i in range(1,5,1) ]
    list_editable = ["id{}".format(i) for i in range(1,5,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_2_1, Form3_2_1Admin)


class Form3_2_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,33,1) ]
    list_filter = ["id{}".format(i) for i in range(1,33,1) ]
    list_editable = ["id{}".format(i) for i in range(1,33,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_2_2, Form3_2_2Admin)


class Form3_2_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,9,1) ]
    list_filter = ["id{}".format(i) for i in range(1,9,1) ]
    list_editable = ["id{}".format(i) for i in range(1,9,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_2_3, Form3_2_3Admin)


class Form3_3_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]
    list_filter = ["id{}".format(i) for i in range(1,7,1) ]
    list_editable = ["id{}".format(i) for i in range(1,7,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_3_1, Form3_3_1Admin)


class Form3_3_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]
    list_filter = ["id{}".format(i) for i in range(1,7,1) ]
    list_editable = ["id{}".format(i) for i in range(1,7,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_3_2, Form3_3_2Admin)


class Form3_3_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]
    list_filter = ["id{}".format(i) for i in range(1,7,1) ]
    list_editable = ["id{}".format(i) for i in range(1,7,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_3_3, Form3_3_3Admin)


class Form3_3_4Admin(object):
    list_display = ["id{}".format(i) for i in range(1,35,1) ]
    list_filter = ["id{}".format(i) for i in range(1,35,1) ]
    list_editable = ["id{}".format(i) for i in range(1,35,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_3_4, Form3_3_4Admin)


class Form3_3_5Admin(object):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]
    list_filter = ["id{}".format(i) for i in range(1,11,1) ]
    list_editable = ["id{}".format(i) for i in range(1,11,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_3_5, Form3_3_5Admin)


class Form3_4_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,15,1) ]
    list_filter = ["id{}".format(i) for i in range(1,15,1) ]
    list_editable = ["id{}".format(i) for i in range(1,15,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_4_1, Form3_4_1Admin)


class Form3_4_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,7,1) ]
    list_filter = ["id{}".format(i) for i in range(1,7,1) ]
    list_editable = ["id{}".format(i) for i in range(1,7,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_4_2, Form3_4_2Admin)



class Form3_4_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,13,1) ]
    list_filter = ["id{}".format(i) for i in range(1,13,1) ]
    list_editable = ["id{}".format(i) for i in range(1,13,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form3_4_3, Form3_4_3Admin)


class Form4_1_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,16,1) ]
    list_filter = ["id{}".format(i) for i in range(1,16,1) ]
    list_editable = ["id{}".format(i) for i in range(1,16,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form4_1_1, Form4_1_1Admin)


class Form5_1_1Admin(object):
    list_display = ["id{}".format(i) for i in range(1,17,1) ]
    list_filter = ["id{}".format(i) for i in range(1,17,1) ]
    list_editable = ["id{}".format(i) for i in range(1,17,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form5_1_1, Form5_1_1Admin)

class Form5_1_2Admin(object):
    list_display = ["id{}".format(i) for i in range(1,24,1) ]
    list_filter = ["id{}".format(i) for i in range(1,24,1) ]
    list_editable = ["id{}".format(i) for i in range(1,24,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form5_1_2, Form5_1_2Admin)

class Form5_1_3Admin(object):
    list_display = ["id{}".format(i) for i in range(1,11,1) ]
    list_filter = ["id{}".format(i) for i in range(1,11,1) ]
    list_editable = ["id{}".format(i) for i in range(1,11,1) ]
    list_per_page = 50
    actions = [make_published]
xadmin.site.register(models.Form5_1_3, Form5_1_3Admin)

#######################################################################################