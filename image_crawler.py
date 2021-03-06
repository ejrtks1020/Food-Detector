from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

food_class = ['pizza', 'hamburger', 'pasta', 'rice', 'sushi',
                'sausage', 'steak']
                
FoodNum = 100

for food in food_class:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") 
    elem = driver.find_element_by_name("q")

    elem.send_keys(food)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        if len(images) > FoodNum:
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector("mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    cnt = 0
    for image in images:
        try:
            image.click()
            time.sleep(3)
            imgUrl = driver.find_elements_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img")[0].get_attribute("src")
            urllib.request.urlretrieve(imgUrl, f"../food/{food}_{cnt}.jpg")
            cnt += 1
        except:
            continue
        if cnt >= FoodNum:
            break
    driver.close()
