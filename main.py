#test for tkinter
from tkinter import messagebox
import  tkinter as tk
from PIL import Image,ImageTk
# set a window
root = tk.Tk()
root.title('山东人测试器')
root.geometry('1000x1000')#这里要用字母x不能用*

label1 = tk.Label(root,text='山东人到底是不是好人?',
                  font=('微软雅黑',30),
                  fg='red')
label1.pack()

#set a frame
button_frame= tk.Frame(root)
button_frame.pack(pady=10)

'''set button
btw you can change the answer'''
def message1():
    messagebox.showinfo('你在搞笑么？','只有我女神xx是')

def message2():
    messagebox.showinfo('这不是废话么','答对咯')

button1= tk.Button(button_frame,
                   text='是',
                   font=('微软雅黑',5),
                   command=message1)
button1.pack(side='left',padx=5)

button2 = tk.Button(button_frame,
                    text='不是',
                    font=('微软雅黑',35),
                    command=message2)
button2.pack(side='left',padx=15)

'''add pics
you can also change different pics'''
Img = Image.open('test.jpg')
Img = Img.resize((800,600))
photo = ImageTk.PhotoImage(Img)
label2 = tk.Label(root, image= photo)
label2.pack()
root.mainloop()
