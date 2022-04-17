'''
Author: tinsir888,dmy
'''
# coding: utf-8
import csv
import os
import numpy as np
import pandas as pd
from IDNumVerification import IDNumVerification

title=['姓名','身份证号','核酸结果']
id_list=[]#存储所有身份证号信息
name_list=[]#存储所有姓名信息
result_list=[]#存储所有核酸检测结果信息

def ResultChecking(result):
    '''
    检测核酸结果输入是否规范
    '''
    if result=="阳性" or result=="阴性":
        return True
    else:
        return False

def InformationAdding(id,name,result):
    '''
    信息录入
    '''
    id=str(id)
    exist=False
    for i in range(len(id_list)):
        if id_list[i]==id:
            exist=True
            break
    if exist==True:
        print("身份证号重复录入，请重新输入!\n")
        return
    id_list.append(id)
    name_list.append(name)
    result_list.append(result)
    print("信息已成功录入!\n")
    #else:
    #   print("身份证号不存在或者违规，请重新输入!\n") 

def InformationDeleting(id):
    '''
    信息删除
    '''
    id=str(id)
    exist=False#检验该身份证信息是否录入
    for i in range(len(id_list)):
        if id_list[i]==id:
            exist=True
            id_list.pop(i)
            name_list.pop(i)
            result_list.pop(i)
            break
    
    if exist==True:
        print("成功删除!\n")
    else:
        print("该身份信息未存储在系统中，请重新输入!\n")

def InformationChanging(id,name,result):
    '''
    信息修改
    '''
    id=str(id)
    exist=False
    for i in range(len(id_list)):
        if id_list[i]==id:
            exist=True
            name_list[i]=name
            result_list[i]=result
            break

    if exist==True:
        print("成功完成修改!\n")
    else:
        print("该身份信息未存储在系统中或身份证号输入错误，请重新输入!\n")

def InformationFinding(id):
    '''
    信息查询
    '''
    id=str(id)
    exist=False
    for i in range(len(id_list)):
        if id_list[i]==id:
            exist=True
            print("查询结果如下:")
            print("身份证号:%s"%id)
            print("姓名:%s"%name_list[i])
            print("核酸检测结果:%s"%result_list[i])
            break
    
    if exist==False:
       print("该身份信息未记录在系统中或身份证号输入错误，请重新输入!\n")

def InformationFindingAll():
    '''
    输出所有信息
    '''
    for i in range(len(id_list)):
        print("第%d位的具体信息如下:"%(i+1))
        print("身份证号:%s"%id_list[i])
        print("姓名:%s"%name_list[i])
        print("核酸检测结果:%s\n"%result_list[i])

if __name__ == "__main__":
    data=[]
    if os.path.exists('data.csv'):
        with open('data.csv',mode='r',encoding='utf-8') as ff:
            #print("文件已经存在")
            data=np.loadtxt(open("data.csv","rb"),encoding='utf-8',dtype=np.str,delimiter=",").tolist()
            if len(np.array(data).shape)==2:#判断维度
                for i in range(1,len(data)):
                    id_list.append(data[i][0])
                    name_list.append(data[i][1])
                    result_list.append(data[i][2])


    else:
        with open('data.csv','a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(title)

    while 1:
        print("请输入是否继续进行操作，是请输入1，否请输入2:",end='')
        op=int(input())
        if op==2:
            break
        elif op==1:
            print("请输入接下来要进行的操作，录入信息请输入1，删除信息请输入2，修改信息请输入3，查找信息请输入4，输出所有已录入信息请输入5:",end='')
            ope2=int(input())
            if ope2==1:#录入信息
                print("请输入身份证号:",end='')
                id=input()
                ids=IDNumVerification(id)
                print("请输入姓名:",end='')
                name=input()
                print("请输入核酸检测结果,输入\"阳性\"或\"阴性\"",end='')
                result=input()
                if ResultChecking(result)==False:
                    print("核酸检测结果输入错误，请重新输入!")
                elif ids.verify()==False:
                    print("身份证输入有误!请重新输入")
                else:
                    InformationAdding(id,name,result)

            elif ope2==2:#删除信息
                print("请输入要删除的身份证号信息:",end='')
                id=input()
                ids=IDNumVerification(id)
                if ids.verify()==False:
                    InformationDeleting(id)
                else:
                    InformationDeleting(id)

            elif ope2==3:#修改信息
                print("请输入要修改的身份证号:",end='')
                id=input()
                ids=IDNumVerification(id)
                print("请输入姓名:",end='')
                name=input()
                print("请输入核酸检测结果,输入\"阳性\"或\"阴性\"",end='')
                result=input()
                if ResultChecking(result)==False:
                    print("核酸检测结果输入错误，请重新输入!")
                elif ids.verify()==False:
                    print("身份证输入有误!请重新输入")
                else:
                    InformationChanging(id,name,result)

            elif ope2==4:#查找信息
                print("请输入要查询的身份证号信息:",end='')
                id=input()
                ids=IDNumVerification(id)
                if ids.verify()==False:
                    InformationFinding(id)
                else:
                    InformationFinding(id)
        
            elif ope2==5:#输出所有信息
                InformationFindingAll()

            else:
                print("输入指令错误，请重新输入!")

        else:
            print("输入指令错误，请重新输入!")
    
    das=pd.read_csv('data.csv',encoding='utf-8')
    das.drop(das.index[0:len(data)-1],inplace=True)
    das.to_csv("data.csv",index=False,encoding='utf-8')
    with open('data.csv','a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in range(len(id_list)):
            writer.writerow([str(id_list[i]),name_list[i],result_list[i]])
    #print(data)
