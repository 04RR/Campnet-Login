from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Lol():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://campnet.bits-goa.ac.in:8090/')
        time.sleep(0)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

#time.sleep(30)

rohit = Lol('F20190967','fd481750')
rohit.login()


