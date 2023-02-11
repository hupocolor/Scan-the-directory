from cgitb import text
from faulthandler import disable
from tkinter import *
from tkinter import BOTTOM, SUNKEN, W, Frame, Label, Toplevel, filedialog
import os
from tkinter import messagebox
# tkinter._test()

writr_str = ''
def out_put_pathlist(deep,inPath,outPath):
    def fun1(deep,Path):
        global writr_str
        PathStr = '-'
        for z in range(0,deep):
            PathStr+='-' #随层数增加用于判断层数
        if deep == 0:
            return 
        # 若判断该目录下的文件为目录且深度足够则进入递归
        for i in os.listdir(Path):
            print(PathStr+i)
            writr_str += (PathStr+i+'\n')
            if(os.path.isdir(Path+'/'+i)):
                fun1(deep-1,Path+'/'+i)
    fun1(deep,inPath)
    with open (outPath,'w+',encoding='utf-8') as f:
        f.write(writr_str)

class mywindow:
    def __init__(self,window):
        self.deep = int(0)
        self.in_path = ''
        self.out_path = ''
        self.type = -1
        window.title("DirTreeTxt --hupo")
        sw = window.winfo_screenwidth() #屏宽
        sh = window.winfo_screenheight() #屏高
        self.x = int((sw-200)/2)
        self.y = int((sh-200)/2)
        window.geometry('{}x{}'.format(int(self.x),int(self.y)))

        frame_masterA = Frame(window)
        frame_masterA.pack(side='top',fill='both', expand=True,padx=20)
        frame_masterB = Frame(window)
        frame_masterB.pack(side='top',fill='both', expand=True,padx=20)
        frame_masterC = Frame(window)
        frame_masterC.pack(side='top',fill='both',expand=True,padx=20)

        frame_masterD = Frame(frame_masterB)
        frame_masterD.pack(side='left',fill='both',expand=True)
        frame_masterE = Frame(frame_masterB)
        frame_masterE.pack(side='left',fill='both',expand=True)
        frame_masterF = Frame(frame_masterB)
        frame_masterF.pack(side='left',fill='both',expand=True)
        
        frame_masterG = Frame(frame_masterA)
        frame_masterG.pack(side='top',fill='both',expand=True)
        frame_masterH = Frame(frame_masterA)
        frame_masterH.pack(side='top',fill='both',expand=True)

        str1 = Label(frame_masterA,text='请在上处指定要扫描的目录和写入文件的目录')
        str1.pack(side='bottom',anchor='n')
        str2 = Label(frame_masterD,text='输出选项')
        str2.pack(side='left',anchor='nw',fill='x')
        str3 = Label(frame_masterE,text='目录深度')
        str3.pack(side='left',anchor='nw',fill='x') 
        self.ent1 = Entry(frame_masterG,state='disable',width=100)
        self.ent1.pack(side='left',fill='x')
        self.ent2 = Entry(frame_masterH,state='disable',width=100)
        self.ent2.pack(side='left',fill='x')
        self.ent3 = Entry(frame_masterE,width=2)
        self.ent3.pack(side='left')
        self.ent3.insert(END,self.deep)

        self.var = IntVar()
        rd1 = Radiobutton(frame_masterD,text="树形视图",variable=self.var,value=0,command=self.Mysel)
        rd1.pack()

        self.intro = Label(frame_masterC,text='   本程序扫描一个指定目录并将目录中的子目录名和文件名以树形视图输出到选择的文本文件中',relief=SUNKEN,anchor=W)
        self.intro.pack(expand=True)
        self.btn3 = Button(frame_masterF,text='输出',width=5,height=1,command=self.out) #输出按钮
        self.btn3.pack(side='top',expand=True)
        self.btn1 = Button(frame_masterF,text='退出',width=5,height=1,command=window.quit) #退出按钮
        self.btn1.pack(side='top',expand=True)
        self.btn2 = Button(frame_masterG,text='浏览',command=self.inpath) #浏览按钮
        self.btn2.pack(side='right',padx=20,pady=40,anchor='ne')
        self.btn4 = Button(frame_masterH,text='目录',command=self.outpath) #选择输出目录按钮
        self.btn4.pack(side='right',padx=20,pady=40,anchor='se')
        self.btn5 = Button(frame_masterE,text='+',command=self.updeep,width=5,height=1) #深度增加按钮
        self.btn5.pack(side='right')
        self.btn6 = Button(frame_masterE,text='-',command=self.downdeep,width=5,height=1) #深度降低按钮
        self.btn6.pack(side='right')

    def inpath(self):
        self.in_path = filedialog.askdirectory() #选择进行搜索的目录
        self.ent1.config(state='normal')
        self.ent1.delete(0,END)
        self.ent1.insert(END,self.in_path)
        self.ent1.config(state='disable')
        # print(winpath)

    def outpath(self):
        self.out_path = filedialog.askdirectory() #选择存放的目录
        self.ent2.config(state='normal')
        self.ent2.delete(0,END)
        self.ent2.insert(END,self.out_path)
        self.ent2.config(state='disable')

    def updeep(self):
        self.deep += 1
        # print('当前深度为{}'.format(self.deep))
        self.ent3.delete(0,END)
        self.ent3.insert(END,self.deep)

    def downdeep(self):
        if(self.deep > 0):
            self.deep -= 1
            # print('当前深度为{}'.format(self.deep))
            self.ent3.delete(0,END)
            self.ent3.insert(END,self.deep)

    def out(self):
        out_put_pathlist(self.deep,self.in_path,self.out_path+'/输出结果.txt')
        messagebox.showinfo('消息提醒','输出成功!')
    
    def Mysel(self):
        if self.var.get() == 1:
            self.type = 1
        elif self.var.get() == 0:
            self.type = 0
    

window = Tk()
myw = mywindow(window)
window.mainloop()