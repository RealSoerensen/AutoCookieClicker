from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


class CookieBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)

    def start(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        sleep(2)
        CookieBot.cookie_click(self)

    def cookie_click(self):
        while True:
            for product_num in range(17, -1, -1):
                print(product_num)
                if self.driver.find_element(By.ID, "product" + str(product_num)).get_attribute("class") == "product " \
                                                                                                           "unlocked " \
                                                                                                           "enabled":
                    CookieBot.store(self, "product" + str(product_num))
            self.driver.find_element(By.ID, "bigCookie").click()

    def store(self, item):
        self.driver.find_element(By.ID, item).click()


bot = CookieBot()
bot.start()
