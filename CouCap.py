from tkinter import *
import random

root = Tk()
root.title("Country & Capitals wheel")
root.geometry("500x500")

enter_name = Entry(root)
enter_name.place(relx = 0.5,rely = 0.2,anchor = CENTER)

friend_list = Label(root)

random_number_label = Label(root)

lucky_friend = Label(root)

list1 = []

def add_friend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"] = "Your Country & Capitals" + str(list1)

def random_number():
    length = len(list1)
    random_number = random.randint(0, length-1)
    random_number_label["text"] = str(random_number)
    generated_random_number = list1[random_number]
    lucky_friend["text"] = "Your Country or Capital Is: " + str(generated_random_number)
    
btn = Button(root, text = "Add To Your Country & Capitals", command = add_friend)
btn.place(relx = 0.5,rely = 0.3,anchor = CENTER)

friend_list.place(relx = 0.5,rely = 0.4,anchor = CENTER)

btn1 = Button(root, text = "What is your Country or Capital?", command = random_number)
btn1.place(relx = 0.5,rely = 0.5,anchor = CENTER)

random_number_label.place(relx = 0.5,rely = 0.6,anchor = CENTER)

lucky_friend.place(relx = 0.5,rely = 0.7,anchor = CENTER)

root.mainloop()