from tkinter import *
hisoblash_mashinasi=Tk()
hisoblash_mashinasi.title("KALKULYATOR")
hisoblash_mashinasi.geometry("500x450")
hisoblash_mashinasi.resizable(False,False)
hisoblash_mashinasi.configure(bg='yellow')
natija_oynasi=Label(hisoblash_mashinasi,width=400,text='0',font=('Times New Roman',50))
natija_oynasi.pack()

natija=""
def show(qiymat):
    global natija
    natija+=qiymat
    natija_oynasi.configure(text=natija)

def tozala():
    global natija
    natija=""
    natija_oynasi.configure(text=natija)

def one_dalete():
    global natija
    new_natija=natija[:-1]
    natija=new_natija
    natija_oynasi.configure(text=natija)

def hisobla():
    global natija
    hisob_natija=""
    if natija !="":
        try:
            natija_oynasi.configure(text=eval(natija))
            natija=""
        except:
            hisob_natija+="xatolik yuz berdi"
            natija+=""
            natija_oynasi.configure(text=hisob_natija)






Button(hisoblash_mashinasi,text='C',width=6,height=1,font=('Times New Roman',25),fg="red",command=lambda :tozala()).place(x=10,y=90)
Button(hisoblash_mashinasi,text='%',width=6,height=1,font=('Times New Roman',25),command=lambda :show("%")).place(x=130,y=90)
Button(hisoblash_mashinasi,text='//',width=6,height=1,font=('Times New Roman',25),command=lambda :show("//")).place(x=250,y=90)
Button(hisoblash_mashinasi,text='/',width=6,height=1,font=('Times New Roman',25),command=lambda :show("/")).place(x=370,y=90)

Button(hisoblash_mashinasi,text='7',width=6,height=1,font=('Times New Roman',25),command=lambda :show("7")).place(x=10,y=160)
Button(hisoblash_mashinasi,text='8',width=6,height=1,font=('Times New Roman',25),command=lambda :show("8")).place(x=130,y=160)
Button(hisoblash_mashinasi,text='9',width=6,height=1,font=('Times New Roman',25),command=lambda :show("9")).place(x=250,y=160)
Button(hisoblash_mashinasi,text='*',width=6,height=1,font=('Times New Roman',25),command=lambda :show("*")).place(x=370,y=160)


Button(hisoblash_mashinasi,text='4',width=6,height=1,font=('Times New Roman',25),command=lambda :show("4")).place(x=10,y=230)
Button(hisoblash_mashinasi,text='5',width=6,height=1,font=('Times New Roman',25),command=lambda :show("5")).place(x=130,y=230)
Button(hisoblash_mashinasi,text='6',width=6,height=1,font=('Times New Roman',25),command=lambda :show("6")).place(x=250,y=230)
Button(hisoblash_mashinasi,text='-',width=6,height=1,font=('Times New Roman',25),command=lambda :show("-")).place(x=370,y=230)


Button(hisoblash_mashinasi,text='1',width=6,height=1,font=('Times New Roman',25),command=lambda :show("1")).place(x=10,y=300)
Button(hisoblash_mashinasi,text='2',width=6,height=1,font=('Times New Roman',25),command=lambda :show("2")).place(x=130,y=300)
Button(hisoblash_mashinasi,text='3',width=6,height=1,font=('Times New Roman',25),command=lambda :show("3")).place(x=250,y=300)
Button(hisoblash_mashinasi,text='+',width=6,height=3,font=('Times New Roman',25),command=lambda :show("+")).place(x=370,y=300)


Button(hisoblash_mashinasi,text='0',width=6,height=1,font=('Times New Roman',25),command=lambda :show("0")).place(x=10,y=370)
Button(hisoblash_mashinasi,text='=',width=6,height=1,font=('Times New Roman',25),fg='green',command=lambda :hisobla()).place(x=130,y=370)
Button(hisoblash_mashinasi,text='<=',width=6,height=1,font=('Times New Roman',25),command=lambda :one_dalete()).place(x=250,y=370)






hisoblash_mashinasi.mainloop()

