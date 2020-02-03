from django.shortcuts import render
import sqlite3
import pandas as pd
from rest_framework import viewsets 
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import html
from . import columns_dic
dic=columns_dic.dic
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的api路径
    """
    queryset=User.objects.all()  #  .order_by("-date_joined")
    serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的api路径
    """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer

#@login_required( login_url="http://127.0.0.1:8000/admin/login/")
def index(request):
    #if (request.methord == "GET"):
        
    """
    con =sqlite3.connect("db.sqlite3")
    sql = "SELECT * FROM test01_form1_1_1"
    df = pd.read_sql(sql,con)
    x =df.describe()

    col = list(x.columns)
    c=[]
    #n=0
    for i in x.index:
        li =[x[o][i] for o in col]
        li.insert(0,i)
        c.append(li)
        #c.append([i,df[][i],df[i][1],df[i][2]   ,df[i][3],df[i][4] ,df[i][5]  ,df[i][6]  ,df[i][7]])
        #n+=1
    return render(request,"index.html",context={"col":col,"cc":c})
#使用json


def index2(request):
    #if (request.methord == "GET"):
    
    con =sqlite3.connect("db.sqlite3")
    sql = "SELECT * FROM test01_form1_1_1"
    df = pd.read_sql(sql,con)
    x =df.describe()

    col = list(x.columns)
    c=[]
    #n=0
    for i in x.index:
        li =[x[o][i] for o in col]
        li.insert(0,i)
        c.append(li)
        #c.append([i,df[][i],df[i][1],df[i][2]   ,df[i][3],df[i][4] ,df[i][5]  ,df[i][6]  ,df[i][7]])
        #n+=1
    return render(request,"index.html",context={"col":col,"cc":c})
    #使用json
    """
    return render(request,"index2.html",context={"col":"col","cc":"c"})

#@login_required
def  index3(request,slug,text):
    con =sqlite3.connect("db.sqlite3")
    sql = "SELECT * FROM test01_form{}".format(slug)
    df = pd.read_sql(sql,con)
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
        #c.append([i,df[][i],df[i][1],df[i][2]   ,df[i][3],df[i][4] ,df[i][5]  ,df[i][6]  ,df[i][7]])
        #n+=1
    con.close()

    return render(request,"index.html",context={"name":text,"col":col,"cc":c})


def Daochu(request):
    slug="1_1_1"
    con =sqlite3.connect("db.sqlite3")
    sql = "SELECT * FROM test01_form{}".format(slug)
    df = pd.read_sql(sql,con)
    x =df.describe()
    x.to_excel("./temp.xlsx",encoding="utf-8-sig")
    file = open( "./temp.xlsx",'rb')
    response =FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    #file_name下载下来保存的文件名字
    file_name="导出表.xlsx"
    content_dis = 'attachment;filename="'+file_name+'"'
    response['Content-Disposition'] = content_dis
    return response