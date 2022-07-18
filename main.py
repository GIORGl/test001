from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys

title = sys.argv[1]

#creates a repo 

def main():
    url = "https://github.com/login"


    path = "C:/Users/Administrator/Downloads/chromedriver"

    driver = webdriver.Chrome(path)

    driver.get(url)

    email = "kechekhmadzegiorgi@gmail.com"
    password = "kichigamer2020"

    email_input = driver.find_element(By.ID, "login_field")

    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "password")

    password_input.send_keys(password)

    sign_btn = driver.find_element(By.NAME, "commit")

    sign_btn.click()

    driver.get("https://github.com/new")

    repo_name_input = driver.find_element(By.ID,"repository_name")

    repo_name_input.send_keys(title)


   

    

    btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary.btn"))).click()

    driver.close()

main()

