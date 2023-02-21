import tkinter
import time 
import webbrowser
from PIL import Image,ImageTk

def Tot(): #读取待整理行数
    global a
    a = len(open("note.txt",encoding='utf-8').readlines())
    
def Del(): #删除功能
    Tot()
    if a ==0:
        Steeldown.title("全部整理完嘞!")
        time.sleep(0.5)
        Steeldown.title("词条整理软件")
    else:
        with open('note.txt','r',encoding='utf-8') as f:
            dline = f.readlines()
            try:
                dline = dline[1:]#只读取第一行之后内容
                f = open('note.txt','w',encoding='utf-8')
                f.writelines(dline)
                f.close()
            except:
                pass
        Steeldown.title("已经删除了！")
        time.sleep(0.5)
        Steeldown.title("词条整理软件")
        global b
        b = b+1
        z=[]
        z.append(str(b))
        z.append("\n")
        with open('logs.txt','r') as f:
            lines = f.readlines()
        with open('logs.txt','w') as f:
            f.writelines(lines[0:1]+z+lines[2:])
        d2b.set("今天整理了{}条！".format(b))
        Tot()
        f1st.set("剩余笔记{}条".format(a))
        Reat()
        t3p.set (reat)

def Open(): #网站打开功能
    Steeldown.title("打开ing！")
    time.sleep(1)
    Reat()
    Web = reat
    webbrowser.open('https://bkrs.info/slovo.php?ch={}'.format(Web),new=0)
    webbrowser.open('https://zh.glosbe.com/ru/zh/{}'.format(Web),new=0)
    Steeldown.title("词条整理软件")
    

def inpu(): #写入并堆栈功能
    zhi = Input.get() #读取输入的数据
    if len(zhi) ==0:
        Steeldown.title("输入了个啥？")
        time.sleep(0.5)
        Steeldown.title("词条整理软件")
    else:
        with open("note.txt","r+",encoding='utf-8') as f:
            old_content = f.read()
            f.seek(0,0)
            f.write(zhi.rstrip('\r\n') + '\n' + old_content)
        Steeldown.title("堆栈完毕！")
        time.sleep(0.5)
        List0 = zhi.split('\n')
        while '' in List0:
            List0.remove('')
        LEN =len(List0) 
        Steeldown.title("键入{}条".format(LEN))
        Input.delete(0,tkinter.END)#清空输入框里的东西
        time.sleep(0.5)
        Steeldown.title("词条整理软件")
        Tot()
        f1st.set("剩余笔记{}条".format(a))
        Reat()
        t3p.set (reat)

def Reat(): #读取第一行
    global reat
    with open("note.txt",'r',encoding='utf-8') as f:
        reat = f.readline()

def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)


# 判断log文件是否存在
try: 
    f =open('logs.txt','r')
    f.close()
except IOError:
    f = open('logs.txt','a+')

try: 
    f =open('note.txt','r')
    f.close()
except IOError:
    f = open('note.txt','a+')
    
#程序开始
Tot()
Reat()
Steeldown = tkinter.Tk()

#读取数据
with open('logs.txt','r') as f:
    Tline = f.readline()
    Tline = Tline.strip('\n')
Noaday = time.strftime('%y-%m-%d')

#是否当天，如果是则令b等于当天变量
if Tline != Noaday: #判断
    with open('logs.txt','r+') as f:
        b = 0
        old_log = f.read()
        f.seek(0,0)
        f.write(Noaday.rstrip('\r\n') +'\n' +str(b)+ '\n' + old_log)
        
else:
    with open('logs.txt','r+') as f:
        next(f)
        b = f.readline()
        b= b.strip('\n')
        b = eval(b)
#每日所清变量的判断
#声明变量
f1st = tkinter.StringVar()
d2b = tkinter.StringVar()
t3p = tkinter.StringVar()

#变量的初始化

f1st.set("剩余笔记{}条".format(a))
if b == 0:
    d2b.set("今天还没有整理哦!")
else:
    d2b.set("今天已经整理了{}条!".format(b))
t3p.set (reat)
#窗口的声明
Steeldown.title("词条整理软件")
Steeldown.geometry("580x150+0+0")
Steeldown.resizable(False,False)

#画布创建
canvas1 = tkinter.Canvas(Steeldown,width=580,height=150)
im_root = get_image("12.png",580,150)
canvas1.create_image(290,75,image=im_root)
canvas1.pack()
    
#三个按钮
bodel = tkinter.Button(Steeldown,
                       text='del',
                       command=Del,
                       width=5,
                       height=2,
                       anchor='center')

bopen = tkinter.Button(Steeldown,
                       text="OPen",
                       command=Open,
                       width=5,
                       height=2,
                       anchor="center")

gett = tkinter.Button(Steeldown,
                      text="get",
                      command=inpu,
                      width=4,
                      height=1,
                      anchor="center")

bopen.pack()
bodel.pack()
bopen.pack()


#主要显示内容
ttext = tkinter.Label(Steeldown,
                      textvariable=t3p,
                      bg='white',
                      font=('Comic Sans MS',20),
                      height = 1,
                      anchor="n")
ttext.pack()

#堆叠数量
ret = tkinter.Label(Steeldown,
                    textvariable=f1st,
                    fg="black",
                    font=('宋体',10),
                    anchor="center")
ret.pack()

#今日数量
daliy = tkinter.Label(Steeldown,
                      textvariable=d2b,
                      fg="black",
                      font=('宋体',10),
                      anchor="center",
                      wraplength=70)
daliy.pack()

#输入
Input = tkinter.Entry(Steeldown)
Input.pack()
#位置
ret.place(x=0,y=0)
daliy.place(x=510,y=0)
Input.place(x=210,y=70)
bopen.place(x=530,y=90)
bodel.place(x=480,y=90)
ttext.place(x=220,y=10)
gett.place(x=260,y=90)

#背景图片

Steeldown.mainloop()



