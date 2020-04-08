from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    firstName = browser.find_element_by_name("firstname")
    lastName = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    uploadButton = browser.find_element_by_id("file")
    firstName.send_keys("First")
    lastName.send_keys("Last")
    email.send_keys("email@example.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    uploadButton.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
