from tkinter import *
from simpleeval import simple_eval
import random
t=Tk()
t.title("🧒Smart Kids Learning Games(AI)")
t.geometry("600x500")
t.resizable(False, False) 
t.configure(bg="lightblue")
expression=""
questions={}
currentquiz=""
score=0
def mathquiz():
    global expression,currentquiz
    entry.config(fg="black")
    entry.delete(0,END)
    expression=""
    operand={'+','-','*'}
    expression+=str(random.randint(1,10))
    expression+=random.choice(list(operand))
    expression+=str(random.randint(1,10))
    temp=""
    for i in expression:
        temp+="  "
        temp+=i
    temp+="  =  ?"
    label2.config(text=temp,font=('Times New Roman',20))
    currentquiz="math"
    
def GK():
    global questions,currentquiz,Q
    entry.config(fg="black")
    questions={
    "how many legs does a cat have?":4,
    "who is the bald warrior of india?":"gandhi",
    "what is the color of rose":"red",   
    }
    entry.delete(0,END)
    Q=random.choice(list(questions.keys()))
    label2.config(text=Q,font=('Times New Roman',20))
    currentquiz="GK"
def Spelling():
    global words,currentquiz,w
    entry.config(fg="black")
    words={
        "elppa": "apple",
    "ananab": "banana",
    "egnaro": "orange",
    "gonam": "mango",
    "sepagr": "grapes",
    "retupmoc": "computer",
    "loohcs": "school",
    "koob": "book",
    "rcikcte": "cricket",
    "nohtyp": "python",
    "enohp": "phone",
    "rac": "car",
    "esuoh": "house",
    "riahc": "chair",
    "elbat": "table" 
    }
    entry.delete(0,END)
    w=random.choice(list(words.keys()))
    label2.config(text=w,font=('Times New Roman',20))
    currentquiz="spelling"
def submit1():
    global expression,currentquiz,questions,Q,words,w,score
    entry.config(fg="black")
    s=str(entry.get())
    if(currentquiz=="math"):
        if(s==str(int(simple_eval(expression)))):
            entry.config(fg="black")
            entry.delete(0,END)
            entry.insert(0,"🎊you got it right🎊🥳")
            score += 1
        else:
            entry.config(fg="red")
            entry.delete(0,END)
            entry.insert(0,"👍Nice Try! but its wrong")
        expression=""
        currentquiz=""
    elif(currentquiz=="GK"):
        result=str(questions[Q]).lower()
        if s.lower()==result:
            entry.config(fg="black")
            entry.delete(0,END)
            entry.insert(0,"🎊you got it right🎊🥳")
            score += 1
        else:
            entry.config(fg="red")
            entry.delete(0,END)
            entry.insert(0,"👍Nice Try! but its wrong")
        currentquiz=""
    elif(currentquiz=="spelling"):
        result=str(words[w]).lower()
        if s.lower()==result:
            entry.config(fg="black")
            entry.delete(0,END)
            entry.insert(0,"🎊you got it right🎊🥳")
            score+=1
        else:
            entry.config(fg="red")
            entry.delete(0,END)
            entry.insert(0,"👍Nice Try! but its wrong")
        currentquiz=""
    else:
        entry.delete(0,END)
        entry.insert(0,"⚠️ Please select the quiz first")
    label4.config(text=score,font=('Times New Roman',20))
def reset():
    global score
    score=0
    label4.config(text="0")
    label2.config(text="")
    entry.delete(0,END)
label = Label(t, text="🤖 AI EDUCATION GAMES FOR KIDS",font=("Times New Roman",20),fg="blue",bg="lightblue")
label.place(x=80,y=20)
label2=Label(t,text="",bg="lightblue")
label2.place(x=150,y=90)
entry=Entry(t,width=30,font=("ariel",14),bd=5,fg="black")
entry.place(x=150,y=130)
math=Button(t,text="➕ MATH QUIZ",bg="yellow",width=20,bd=4,command=lambda:mathquiz())
math.place(x=40,y=200)
gk=Button(t,text="🧠 GK QUIZ",bg="lightgreen",width=20,bd=4,command=lambda:GK())
gk.place(x=228,y=200)
spelling=Button(t,text="📚 SPELLING GAME",bg="lightpink",width=20,bd=4,command=lambda:Spelling())
spelling.place(x=415,y=200)
submit=Button(t,text="🎰SUBMIT ANSWER",bg="orange",width=20,bd=4,font=("ariel",12),command=lambda:submit1())
submit.place(x=210,y=260)
label3=Label(t,text="SCORE:",bg="lightblue",font=('Times New Roman',20))
label3.place(x=100,y=300)
label4=Label(t,text="0",bg="lightblue",font=('Times New Roman',20))
label4.place(x=210,y=300)
reset_btn=Button(t,text="🔄Reset",bg="gray",fg="white",bd=4,width=10,command=lambda:reset(),font=('Times New Roman',15))
reset_btn.place(x=230,y=350)
mainloop()
