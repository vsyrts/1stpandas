#!/usr/bin/env python3
# import pyhon_dataframe as pdf
from cProfile import label
import tkinter as tk
import tkinter.font as TkFont
import glob
from turtle import title
from click import command, open_file, style

# from numpy import pad

class ChildApp(tk.Frame):
    def __init__(self,child=None):
        tk.Frame.__init__(self,child,width=200,height=200)
        self.grid()

class Application(tk.Frame):
    """
        Приложение для выбора файлов версия 3.1.5
    """
    dapp=object 
    contacts={"telephonenumber":"+7(999)989-11-94","mail":"vasiliy.syrytsev@gazprombank.ru","telegram":"+7(999)989-11-94","whatapp":"+7(999)989-11-94"}
    cursorstyles = ['arrow' ,'man' ,'based_arrow_down' ,'middlebutton' ,'based_arrow_up' ,'mouse' ,'boat' ,'pencil' ,'bogosity' ,'pirate' ,'bottom_left_corner' ,'plus' ,'bottom_right_corner' ,'question_arrow' ,'bottom_side' ,'right_ptr' ,'bottom_tee' ,'right_side' ,'box_spiral' ,'right_tee' ,'center_ptr' ,'rightbutton' ,'circle' ,'rtl_logo' ,'clock' ,'sailboat' ,'coffee_mug' ,'sb_down_arrow' ,'cross' ,'sb_h_double_arrow' ,'cross_reverse' ,'sb_left_arrow' ,'crosshair' ,'sb_right_arrow' ,'diamond_cross' ,'sb_up_arrow' ,'dot' ,'sb_v_double_arrow' ,'dotbox' ,'shuttle' ,'double_arrow' ,'sizing' ,'draft_large' ,'spider' ,'draft_small' ,'spraycan' ,'draped_box' ,'star' ,'exchange' ,'target' ,'fleur' ,'tcross' ,'gobbler' ,'top_left_arrow' ,'gumby' ,'top_left_corner' ,'hand1' ,'top_right_corner' ,'hand2' ,'top_side' ,'heart' ,'top_tee' ,'icon' ,'trek' ,'iron_cross' ,'ul_angle' ,'left_ptr' ,'umbrella' ,'left_side' ,'ur_angle' ,'left_tee' ,'watch' ,'leftbutton' ,'xterm' ,'ll_angle' ,'X_cursor' ,'lr_angle']
    buttonimages = ['error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead','question', 'warning']
    submenu=[]
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def open():
        print("open")
    def show_dialog(self):
        # print("dialog")
        self.child=ChildApp()
        self.child.title="Дочернее окно"
        self.child.mainloop()

    def __scrollHandler(self, *L):
        op, howMany = L[0], L[1]
        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)
    
    def __aboutHandler(self):
        print("Информация о системе:\n{}".format(self.__doc__))
    
    def __aboutContacts(self):
        msgcontacts="Контакты:\n"
        for key,value in self.contacts.items():
            msgcontacts+="{}:{}\n".format(key,value)
        self.message=tk.Message(self,text=msgcontacts)
        self.message.grid()

    def open_file(self):
        print("Здесь надо открыть файл {}".format(self.__doc__))
    def createWidgets(self):
        # 'white', 'black', 'red','green', 'blue', 'cyan', 'yellow', and 'magenta'
        bgc='#ed1c24'
        fgc='#ffffff'
        self.quitButton = tk.Button(self
        # , cnf= "Quit"
        , activebackground= fgc
        # b'\xff\xfc\xfc\xfc'
        , activeforeground= bgc
        , bg=bgc
        , fg=fgc
        ,font=TkFont.Font(
            family="Times New Roman",size=10,weight='bold',slant='italic',underline=1, overstrike=1 )
        # b'\xff\xcc\xcc\xcc'
        # , anchor= tk.
        , text='Quit'
        , command=self.quit
        )
        self.quitButton.grid(
            column=0
            ,columnspan=1
            ,ipadx=10
            # ,ipady=24
            # ,padx=8
            # ,pady=8
            ,row=10
            # ,rowspan=4
            # ,
            # ,sticky=tk.S
            # tk.NE #top right
            # tk.SE bottom right
            # tk.SW bottom left
            # tk.NW top left
            # tk.N top center
            # tk.E right center
            # tk.S bottom center
            # tk.W left center
            )
        self.logo=[]
        for fname in glob.iglob(r"images\buttons\*.gif",recursive=True):
            self.logo.append(tk.PhotoImage(file=fname))
        
        self.mtklabel = tk.Label(self
        , activeforeground= bgc
        , activebackground= fgc
        , bg = bgc
        , fg = fgc
        , font = 1
        # TkFont(family="Monotype Corsiva",size=12,weight='bold',slant='italic',underline=0,overstrike=1)
        , text="New Text For Item"
        , anchor= 'e'
        , cursor=self.cursorstyles[2]
        , compound='top'
        , image= self.logo[-1]
        )
        self.mtklabel.grid(
            sticky=tk.SE
        )
        self.mytkbutton = tk.Button(self
            , activebackground= fgc
            # b'\xff\xfc\xfc\xfc'
            , activeforeground= bgc
            , bg=bgc
            , fg=fgc
            , font=TkFont.Font(family="Times New Roman",size=10,weight='bold',slant='italic',underline=1, overstrike=1 )
            # b'\xff\xcc\xcc\xcc'
            # , anchor= tk.
            # , text='DialogWindow'
            # ,bitmap='error'
            , bitmap='gray75'
            , textvariable='Диалоговое окно'
            , compound='left'
            , image=self.logo[1]
            # ,bitmap='gray50'
            # ,
            , command=self.show_dialog
        )
        self.mytkbutton.grid(
            # column=1
            # ,columnspan=2
            # ,ipadx=2
            # ,ipady=2
            # ,padx=10
            # ,pady=1
            # ,row=1
            # ,rowspan=2
            # ,
            sticky=tk.E
        )
        self.canvas = tk.Canvas()
        arc=self.canvas.create_arc(100,100,250,250
        ,activewidth=2
        # ,activestipple=3
        # ,activeoutlinestipple=4
        ,activeoutline="red"
        ,activefill="cyan"
        ,activedash=(3,1,3,1)
        ,dashoffset=3
        ,fill="yellow"
        ,outline="green"
        # ,style=
        # tk.PIESLICE
        # tk.CHORD
        # tk.ARC
        )

        self.canvas.create_bitmap(350,150
        # ,backgroud="red",activebackgroup="blue",foregroud="green",activeforegroud="yellow"
        )
        # self.canvas.create_image(self.logo[3])
        self.canvas.create_line(
            1,2,3,4,5,6,7,8,9,10
        )
        self.canvas.create_oval(10,20,30,40)
        self.canvas.create_polygon(100,100,150,150,250,250,100,300,fill="yellow",outline="green",activefill="green",activeoutline="yellow")
        self.canvas.create_rectangle(10,10,100,100)
        self.canvas.create_text(50,50,text="None")
        # self.canvas.create_window()
        self.canvas.grid(
            sticky=tk.S
        )
        self.ckbutton=tk.Checkbutton(text='Use\nCB')
        self.ckbutton.grid(
        )

        self.entry = tk.Entry(self, width=10)
        self.entry.grid(row=100, sticky=tk.E+tk.W)
        self.entryScroll = tk.Scrollbar(self, orient=tk.HORIZONTAL,
        command=self.__scrollHandler)
        self.entryScroll.grid(row=105, sticky=tk.E+tk.W)
        self.entry['xscrollcommand'] = self.entryScroll.set
        self.mylabelframe=tk.LabelFrame(
            bg="yellow"
            ,bd=2
            ,fg="red"
            ,height=500
            ,width=450
            ,text="Форма селективного выбора"
            ,labelanchor='sw'
            ,relief=tk.FLAT
        )
        self.mylabelframe.grid()
        self.mentry=tk.Entry(self,width=200)
        self.mentry.grid(sticky=tk.SE+tk.SW)
        self.entryScroll = tk.Scrollbar(self, orient=tk.HORIZONTAL,
        command=self.__scrollHandler)
        self.entryScroll.grid(row=50, sticky=tk.E+tk.W)
        self.mentry['xscrollcommand'] = self.entryScroll.set
        self.yScroll = tk.Scrollbar(self.mylabelframe, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N+tk.S)
        self.xScroll = tk.Scrollbar(self.mylabelframe, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E+tk.W)
        self.mtklistbox = tk.Listbox(self.mylabelframe,cursor=self.cursorstyles[10],activestyle="dotbox",height=20,width=200,xscrollcommand=self.xScroll.set,yscrollcommand=self.yScroll.set)
        self.mtklistbox.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.xScroll['command'] = self.mtklistbox.xview
        self.yScroll['command'] = self.mtklistbox.yview
        top=self.winfo_toplevel()
        self.mainmenu=tk.Menu(
            top
            ,activebackground =fgc ,
            activeforeground= bgc,
            bg= bgc,
            fg= fgc,
            title="Main menu"
        )
        top['menu']=self.mainmenu
        self.submenu.append(tk.Menu(self.mainmenu))
        self.mainmenu.add_cascade(label="Файл",menu=self.submenu[-1])
        self.submenu[-1].add_command(label="Открыть",command=self.open_file)
        self.submenu.append(tk.Menu(self.submenu[-1]))
        self.submenu[-2].add_cascade(label="Вид",menu=self.submenu[-1])
        self.submenu[-1].add_radiobutton(label="Каскадно",state="active")
        self.submenu[-1].add_radiobutton(label="Вертикально")
        self.submenu[-1].add_radiobutton(label="Горизонтально")
        self.submenu[-1].add_separator()
        self.submenu[-1].add_checkbutton(label="Формат 3x7")
        self.submenu[-1].add_separator()
        self.submenu[-1].add_radiobutton(label="Рандомно")
        self.submenu.append(tk.Menu(self.mainmenu))
        self.mainmenu.add_cascade(label='Помощь',menu=self.submenu[-1])
        self.submenu[-1].add_command(label='О программе',command=self.__aboutHandler)
        self.submenu[-1].add_command(label='Контакты',command=self.__aboutContacts)

        self.mb = tk.Menubutton(self, text='condiments',relief=tk.RAISED)
        self.mb.grid()
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu
        self.mayoVar = tk.IntVar()
        self.ketchVar = tk.IntVar()
        self.mb.menu.add_checkbutton(label='mayo',variable=self.mayoVar)
        self.mb.menu.add_checkbutton(label='ketchup',variable=self.ketchVar)

        # self.mainmenu.grid(
        #     # sticky=tk.N+tk.NE+tk.NW
        #     )
        # self.myentry=tk.Entry(self,justify=tk.LEFT,width=150)
        # self.myentry.grid()
        # self.entryScroll = tk.Scrollbar(self, orient=tk.VERTICAL,
        # command=self.__scrollHandler)
        # self.entryScroll.grid(row=1, sticky=tk.E+tk.W)
        # self.myentry['xscrollcommand'] = self.entryScroll.set

        # self.mainmenu.grid()

        # self.mainmenu.add('cascade',cnf='Форма')

        # # self.mainmenu.add_cascade('Файл')
        # # self.mainmenu.add_command('Выход',command=self.close)
        # # self.mainmenu.add_command('Открыть',command=self.open)
        # self.mainmenu.grid(
        #     column=0
        #     ,columnspan=2
        #     ,ipadx=15
        #     ,ipady=15
        #     ,padx=10
        #     ,pady=10
        #     ,row=0
        #     ,rowspan=0
        #     ,sticky=tk.N
        #     # tk.NE+tk.NO
        # )
    def __del__(self):
        print("exit")
        return None 

if __name__=="__main__":
    try:
        app = Application()
        app.master.title('Простое приложение')
        app.mainloop()
    finally:
        if "app" in locals() or "app" in globals():
            del app
