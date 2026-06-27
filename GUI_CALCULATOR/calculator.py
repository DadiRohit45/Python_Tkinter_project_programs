from tkinter import *
from simpleeval import simple_eval
t=Tk()
t.title("calculator")
E1=Entry(t,bg="black",fg="white",width=22,font=("Arial",17),bd=12)
E1.grid(row=0,column=0,columnspan=4)
expression=""
result_shown=False    
def calculation():
    global expression,result_shown
    try:
        result=str(simple_eval(expression))
        E1.delete(0,END)
        E1.insert(0,result)
        expression=result
        result_shown=True
    except:
        E1.delete(0,END)
        E1.insert(0,'ERROR')
        expression=""

def click(a):
    global expression,result_shown
    if result_shown==True:
        E1.delete(0,END)
        E1.insert(0,'ans')
        result_shown=False
    expression+=str(a)
    E1.insert(END,a)
    
def clear():
    global expression,result_shown
    expression=""
    E1.delete(0,END)
    result_shown=False
    
def remove():
    global expression
    l=len(E1.get())-1
    E1.delete(l)
    expression=expression[:-1]

b1=Button(t,text='1',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(1),cursor="hand2")
b1.grid(row=4,column=0)
b2=Button(t,text='2',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(2),cursor="hand2")
b2.grid(row=4,column=1)
b3=Button(t,text='3',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(3),cursor="hand2")
b3.grid(row=4,column=2)
b4=Button(t,text='+',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click('+'),cursor="hand2")
b4.grid(row=4,column=3)
b5=Button(t,text='4',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(4),cursor="hand2")
b5.grid(row=3,column=0)
b6=Button(t,text='5',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(5),cursor="hand2")
b6.grid(row=3,column=1)
b7=Button(t,text='6',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(6),cursor="hand2")
b7.grid(row=3,column=2)
b8=Button(t,text='—',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click('-'),cursor="hand2")
b8.grid(row=3,column=3)
b9=Button(t,text='7',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(7),cursor="hand2")
b9.grid(row=2,column=0)
b10=Button(t,text='8',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(8),cursor="hand2")
b10.grid(row=2,column=1)
b11=Button(t,text='9',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(9),cursor="hand2")
b11.grid(row=2,column=2)
b12=Button(t,text='/',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click('/'),cursor="hand2")
b12.grid(row=2,column=3)
b13=Button(t,text='0',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click(0),cursor="hand2")
b13.grid(row=5,column=0)
b14=Button(t,text='x',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click('*'),cursor="hand2")
b14.grid(row=5,column=2)
b15=Button(t,text='=',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:calculation(),cursor="hand2")
b15.grid(row=6,column=1)
b16=Button(t,text='%',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click("%"),cursor="hand2")
b16.grid(row=5,column=3)
b17=Button(t,text='AC',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:clear(),cursor="hand2")
b17.grid(row=6,column=2)
b18=Button(t,text='•',bg="black",fg="white",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click("."),cursor="hand2")
b18.grid(row=5,column=1)
b19=Button(t,text='⌫',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:remove(),cursor="hand2")
b19.grid(row=6,column=3)
b20=Button(t,text='e',bg="black",fg="orange",font=("Arial",10),bd=7,height=5,width=7,activebackground="grey",command=lambda:click("2.718281828"),cursor="hand2")
b20.grid(row=6,column=0)
mainloop()
