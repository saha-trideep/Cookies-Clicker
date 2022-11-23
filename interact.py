from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL", ))

##############################################################

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
time.sleep(15)

language_box = driver.find_element(By.ID, "promptContentChangeLanguage")
select_language = language_box.find_element(By.ID, "langSelect-EN")
select_language.click()

time.sleep(10)

button = driver.find_element(By.CSS_SELECTOR, "#cookieAnchor button")
end_time = round(time.time() + 300, 0)


def click(start):
    try:
        cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
        store_section = driver.find_element(By.ID, "products")
        switch1 = f"product{start}"
        switch2 = f"productPrice{start}"
        my_variable = store_section.find_element(By.ID, switch1)
        try:
            required_cookies = int(my_variable.find_element(By.ID, switch2).text.replace(",", ""))
            if cookies >= required_cookies:
                try:
                    wait = WebDriverWait(driver, 10)
                    element = wait.until(ec.element_to_be_clickable((By.ID, switch1)))
                    element.click()
                except TimeoutError:
                    pass
        except ValueError:
            pass
    except AttributeError:
        pass


def remain_cookies(start):
    try:
        cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
        store_section = driver.find_element(By.ID, "products")
        switch1 = f"product{start}"
        switch2 = f"productPrice{start}"
        my_variable = store_section.find_element(By.ID, switch1)
        required_grandma = int(my_variable.find_element(By.XPATH, '//*[@id="productPrice1"]').text)
        try:
            required_cookies = int(my_variable.find_element(By.ID, switch2).text.replace(",", ""))

            if cookies >= required_cookies + required_grandma:
                return True
        except ValueError:
            pass
    except AttributeError:
        pass


while True:
    start_time = round(time.time(), 0)
    button.click()
    if remain_cookies(start=2):
        click(start=2)
    elif end_time - start_time < 40:
        for i in range(0, 11):
            click(start=1)

    if start_time >= end_time:
        break
print(driver.find_element(By.ID, "cookies").text)











# time.sleep(1)


# store_section = driver.find_element(By.ID, "products")
#
# switch1 = "product0"
#
# my_variable = store_section.find_element(By.ID, switch1)
# required_cookies = int(my_variable.find_element(By.ID, "switch2").text)
# cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])
# print(type(cookies))
# print(type(required_cookies))


####################################################################
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
# driver.maximize_window()
# time.sleep(5)
#
# game = driver.find_element(By.ID, "game")
# money = game.find_element(By.ID, "money")
# save_menu = driver.find_element(By.CSS_SELECTOR, "#saveMenu div")
#
# number_of_cookies = int(save_menu.text.split(":")[1].strip())
#
# store = driver.find_element(By.ID, "store")
#
# segments = store.find_elements(By.CLASS_NAME, "grayed")
# store_dict = {}
# store_list = []
# final_list = []
# button = driver.find_element(By.ID, "cookie")
#
#
# def click_on():
#     for segment in segments:
#         numbers = segment.find_elements(By.CSS_SELECTOR, "b")
#         for number in numbers:
#             try:
#                 store_dict = {
#                     number.text.split("-")[0].strip(): int(number.text.split("-")[1].replace(",", ""))
#                 }
#                 store_list.append(store_dict)
#             except IndexError:
#                 pass
#
#         [final_list.append(pair) for pair in store_list if pair not in final_list]
#         _id = segment.get_attribute('id')
#         store.find_element(By.ID, f"{_id}").click()
#
#
# end_time = datetime.now() + timedelta(seconds=120)
# while True:
#     button.click()
#     start_time = datetime.now()
#     if start_time >= end_time:
#         break
# time.sleep(5)
# click_on()

#
#     for i in range(len(final_list)):
#         pairs = final_list[i]
#         for key in pairs:
#

#
# cookies_second = driver.find_element(By.CSS_SELECTOR, "#saveMenu div")
#
# print(cookies_second.text)

# .split("-")[1].strip().replace(",", "")


# f_name = driver.find_element(By.NAME, "fName")
# f_name.send_keys("trideep")
# l_name = driver.find_element(By.NAME, "lName")
# l_name.send_keys("saha")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("trideepsaha009@gmail.com")
# button = driver.find_element(By.CLASS_NAME, "btn-lg")
# button.click()
