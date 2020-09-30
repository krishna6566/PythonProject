#First Python Project
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

class twitter_bot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path = r'C:\Users\SWAPNIL\AppData\Local\Programs\Python\Python38-32\chromedriver.exe')        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        
    def like_tweet(self,entry3):
        bot = self.bot
        bot.get("https://twitter.com/search?q="+str(entry3)+"&src=typed_query")
        while True:
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            pyautogui.click(pyautogui.locateCenterOnScreen('https://raw.githubusercontent.com/harshitroy2605/twitter_bot/master/1.PNG'),duration=2)
            time.sleep(3)

def execute():
    log = twitter_bot(str(entry1.get()),str(entry2.get()))
    log.login()
    log.like_tweet(entry3.get())

window = Tk()
window.geometry("700x600")
emails = Label(window,text="Enter your email here",font="times 24 bold")
emails.grid(row=0,column=0)
entry1 = Entry(window)
entry1.grid(row=0,column=6)

password = Label(window,text="Enter your password here",font="times 24 bold")
password.grid(row=2,column=0)
entry2 = Entry(window)
entry2.grid(row=2,column=6)

hashtag = Label(window,text="Enter your hashtag here",font="times 24 bold")
hashtag.grid(row=3,column=0)
entry3 = Entry(window)
entry3.grid(row=3,column=6)

b1 = Button(window,text = " GO ",command=execute,width=12,bg='gray')
b1.grid(row=7,column=4)
window.mainloop()
