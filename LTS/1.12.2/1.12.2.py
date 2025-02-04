import turtle
import datetime
import time
import requests
import json 
import easygui as gui

def danwei():
    gui.msgbox(msg='功能开发中，即将开放。', title='单位换算', ok_button='确认', image=None, root=None)
    '''
    temp=gui.choicebox(msg='请选择您需要的服务', title='单位换算', choices=['长度单位','数据单位','质量单位','体积（容积）单位'])
    def cd():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['mm','cm','dm','m','km'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='mm':
            print(b,'mm=',b/10,'cm=',b/100,'dm=',b/1000,'m=',b/1000000,'km')
        if a=='cm':
            print(b*10,'mm=',b,'cm=',b/10,'dm=',b/100,'m=',b/100000,'km')
        if a=='dm':
            print(b*100,'mm=',b*10,'cm=',b,'dm=',b/10,'m=',b/10000,'km')
        if a=='m':
            print(b*1000,'mm=',b*100,'cm=',b*10,'dm=',b,'m=',b/1000,'km')
        if a=='km':
            print(b*1000000,'mm=',b*100000,'cm=',b*10000,'dm=',b*1000,'m=',b,'km')
    def sg():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['B','KB','MB','GB','TB'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='B':
            gui.msgbox(msg=b+'B='+b/1204+'KB='+b/1204/1204+'MB='+b/1204/1204/1204+'GB='+b/1204/1204/1204/1204+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='KB':
            gui.msgbox(msg=b*1024+'B='+b+'KB='+b/1204+'MB='+b/1204/1204+'GB='+b/1204/1204/1204+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='MB':
            print(b*1024*1024,'B=',b*1024,'KB=',b,'MB=',b/1204,'GB=',b/1204/1204,'TB')
        if a=='GB':
            print(b*1024*1024*1024,'B=',b*1024*1024,'KB=',b*1024,'MB=',b,'GB=',b/1204,'TB')
        if a=='TB':
            print(b*1024*1024*1024*1024,'B=',b*1024*1024*1024,'KB=',b*1024*1024,'MB=',b*1024,'GB=',b,'TB')
    def zl():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['g','kg','t'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='g':
            gui.msgbox(msg=b+'g='+b/1000+'kg='+b/1000/1000+'t', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='kg':
            gui.msgbox(msg=b*1000+'g='+b+'kg='+b/1000+'t', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='t':
            gui.msgbox(msg=b*1000*1000+'B='+b*1000+'kg='+b+'t', title='单位换算', ok_button=' ', image=None, root=None)
    def tj():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['ml','l'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='g':
            gui.msgbox(msg=b+'ml='+b/1000+'l', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='kg':
            gui.msgbox(msg=b*1000+'ml='+b+'l', title='单位换算', ok_button=' ', image=None, root=None)
    if temp=='长度单位':
        cd()
    elif temp=='数据单位':
        sg()
    elif temp=='质量单位':
        zl()
    elif temp=='体积（容积）单位':
        tj()
    '''

def gongshi():
    print('功能开发中，即将开放。')
def geshui():
    #print('个人所得税计算器')
    #print('正在加载中，请稍等······')
    #money=(int(input('请问您每月收入多少CNY？')))
    money=int(gui.enterbox(msg='请问您每月收入多少CNY？', title='个人所得税计算器', default='', strip=True, image=None, root=None))
    if money<=5000:
        tax=0
    elif money-5000<=1500:
        tax=(money-5000)*0.03-0
    elif money-5000>1500 and money-5000<=4500:
        tax=(money-5000)*0.1-105
    elif money-5000>4500 and money-5000<=9000:
        tax=(money-5000)*0.2-555
    elif money-5000>9000 and money-5000<=35000:
        tax=(money-5000)*0.25-1005
    elif money-5000>35000 and money-5000<=55000:
        tax=(money-5000)*0.3-2755
    elif money-5000>55000 and money-5000<=80000:
        tax=(money-5000)*0.35-5505
    elif money-5000>80000:
        tax=(money-5000)*0.45-13505
    #print("您每月需交",str(tax),"CNY","的个人所得税。")
    gui.msgbox(msg="您每月需交"+str(tax)+"CNY"+"的个人所得税。", title='个人所得税计算器', ok_button='退出', image=None, root=None)
def huobi():
    currency_code=['CNY 人民币','HKD 港币','USD 美元','EUR 欧元','GBP 英镑','JPY 日元','DEM 德国马克','FRF 法国法郎','SGD 新加坡元']
    original=gui.choicebox(msg='请选择您需要换算的原单位', title='货币换算', choices=currency_code)
    target=gui.choicebox(msg='请选择您需要换算的目标单位', title='货币换算', choices=currency_code)
    num=int(gui.enterbox(msg='请输入原数据', title='货币换算', default='', strip=True, image=None, root=None))
    url = "https://v6.exchangerate-api.com/v6/83c890b38cbb97afed2a8db0/latest/"+original[0]+original[1]+original[2]
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    print(a)
    b=a["conversion_rates"]
    c=b[target[0]+target[1]+target[2]]
    gui.msgbox(msg=str(num)+original[0]+original[1]+original[2]+'='+str(num*c)+target[0]+target[1]+target[2], title='货币换算', ok_button='确定', image=None, root=None)
def clock():
    gui.msgbox(msg='如要退出，请重新启动程序！', title='时钟', ok_button='确定', image=None, root=None)
    t=turtle.Turtle()
    t.speed(0)
    def board(r):#绘制表盘
        t.penup()
        t.setheading(270)
        t.fd(r)
        t.setheading(0)
        t.pendown()
        t.circle(r)
        t.penup()
        t.home()
        t.pendown()
        t.dot()
    def num(r):#写数字，打点
        board(r)
        t.setheading(60)
        for i in range(12):
            t.penup()
            t.fd(r)
            t.pendown()
            t.write(i+1)
            t.dot()
            t.penup()
            t.backward(r)
            t.right(30)
            t.hideturtle()
    def hms(r):#画针
        h=turtle.Turtle()
        m=turtle.Turtle()
        s=turtle.Turtle()
        h.speed(-2)
        m.speed(-2)
        s.speed(-2)
        timing=0
        while True:            
            ti=datetime.datetime.now()
            angles=[]
            h.pendown()
            m.pendown()
            s.pendown()
            hmsGUI=[h,m,s]
            h_angle = -ti.hour*30-ti.minute*(30/60)-ti.second*(30/60/60)+90
            m_angle=-ti.minute*6-ti.second*(6/60)+90
            s_angle=-ti.second*6+90
            angles=[h_angle,m_angle,s_angle]
            for i in range(3):
                hmsGUI[i].pensize(7-2*(i+1))
                hmsGUI[i].setheading(angles[i])
                hmsGUI[i].fd(((i+1)*0.3)*r)
            turtle.tracer(1) 
            time.sleep(1)
            turtle.tracer(0)

            h.clear()
            m.clear()
            s.clear()
            h.penup()
            m.penup()
            s.penup()
            h.home()
            m.home()
            s.home()
            timing=timing+1
            if timing>=3600:
                turtle.bye()
    num(200)     
    hms(200)
def weather():
    url='http://api.airvisual.com/v2/countries?key=510b729a-2501-4701-b1de-74d2a4456b67'
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['country'])
    cou=gui.choicebox(msg='请选择您需要查询的国家', title='天气', choices=c)
    
    url='http://api.airvisual.com/v2/states?country='+cou+'&key=510b729a-2501-4701-b1de-74d2a4456b67'
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['state'])
    sta=gui.choicebox(msg='请选择您需要查询的省份（州）', title='天气', choices=c)
    
    url='http://api.airvisual.com/v2/cities?state='+sta+'&country='+cou+'&key=510b729a-2501-4701-b1de-74d2a4456b67'
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['city'])
    cit=gui.choicebox(msg='请选择您需要查询的城市', title='天气', choices=c)
    url = "http://api.airvisual.com/v2/city?city="+cit+"&state="+sta+"&country="+cou+"&key=510b729a-2501-4701-b1de-74d2a4456b67"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=b['current']
    d=c['weather']
    e='当前时间戳：'+str(d['ts'])+'   '+cou+' '+sta+' '+cit+''+'当前气温为：'+str(d['tp'])+'摄氏度 气压为：'+str(d['pr'])+'百帕 风速为'+str(d['ws'])+'m/s 风向为：'+str(d['wd'])+'度'
    gui.msgbox(msg=e, title='天气', ok_button='确定', image=None, root=None)
while True:
    '''
    print('欢迎来到超级百宝箱 1.4.8！')
    print('1·单位换算')
    print('2·个人所得税计算')
    print('3·货币转换')
    print('4·时钟')
    print('5.天气')
    print(exit)
    temp=input('请选择您需要的服务(1/2/3/4/5/exit)。')
    if temp=='1':
        danwei()
    elif temp=='2':
        geshui()
    elif temp=='3':
        huobi()
    elif temp=='4':
        clock()
    elif temp=='5':
        weather()
    elif temp=='exit':
        break
    '''
    temp=gui.choicebox(msg='请选择您需要的服务', title='超级百宝箱 1.8.8', choices=['个人所得税计算','货币转换','时钟','天气','exit'])
    print(temp)
    '''
    if temp=='单位换算':
        danwei()
        '''
    if temp=='个人所得税计算':
        geshui()
    elif temp=='货币转换':
        huobi()
    elif temp=='时钟':
        clock()
    elif temp=='天气':
        weather()
    elif temp=='exit':
        break