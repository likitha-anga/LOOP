from tkinter import *


main_window=Tk()
main_window.title("CALCULATER")
# melabel=label(me,text="calculater",bg="dark gray",font=("times",30,"bold"))
# melabel.pack(side=TOP)
# me.config(background="dark gray")

#user=int(input("enter the number:"))
#user=int(input("enter the number:"))
#print(user+user)
# creating widgets
def clear():
    display_box.delete(0,END)
    
    
def btn_click(num):
    cur_num=display_box.get()
    clear()
    f_num=cur_num+num
    display_box.insert(0,f_num)
first_num=0
math=''


def calculater(math_type):
    global frist_num,math
    math=math_type
    frist_num=display_box.get()
    
      
def equal():
    result=''
    globel=first_num
    second_num=display_box.get()
    clear()
if math=="add":
    result=int(frist_num)+int(second_num)
elif math=="sub":
    result=int(first_num)-int(second_num)
elif math=="multiply":
    result=int(first_num)*int(second_num)
elif math=="divide":
    result=int(first_num)/int(second_num)
    result=round(round,3)
display_box.insert(0,str(result))

display_box=entry(mw,width=14,font=("arial",28),jusify=right)

btn_0=button(mw,text="0",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("0"))
btn_1=button(mw,text="1",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("1"))
btn_2=button(mw,text="2",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("2"))
btn_3=button(mw,text="3",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("3"))
btn_4=button(mw,text="4",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("4"))
btn_5=button(mw,text="5",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("5"))
btn_6=button(mw,text="6",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("6"))
btn_7=button(mw,text="7",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("7"))
btn_8=button(mw,text="8",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("8"))
btn_9=button(mw,text="9",padx=36,pady=10,font=("arial",14),command=lambda:btn_click("9"))

btn_clear=button(mw,text="clear",padx=74,pady=10,font=("arial",14),command=lambda:btn_click("clear"))
btn_division=button(mw,text="%",padx=36,pady=10,font=("arial",14),command=division)
btn_muliply=button(mw,text="*",padx=36,pady=10,font=("arial",14),command=multiply)
btn_substractin=button(mw,text="-",padx=36,pady=10,font=("arial",14),command=substraction)
btn_addition=button(mw,text="+",padx=36,pady=10,font=("arial",14),command=addition)

btn_clear.grid(row=4,colume=1,columnspan=2,padx=2,pady=2)
btn_equal.grid(row=5,column=2,padx=2,pady=2)
btn_divide.grid(row=5,column=0,padx=2,pady=2)
btn_multiply.grid(row=5,column=1,padx=2,pady=2)
btn_substraction.grid(row=6,column=0,padx=2,pady=2)
btn_addition.grid(row=6,column=1,padx=2,pady=2)

btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)

btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)

btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)

main_window.mainloop()






















    
      