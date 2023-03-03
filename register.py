from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from getpass import getpass
import time

def register_with_selenium(name_surname, phone_number_or_email, password):
  driver = webdriver.Chrome()
  driver.get("https://www.amazon.com.tr/")
  account_button = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
  account_button.click()
  create_account_button = driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]')
  create_account_button.click()
  name_surname_input = driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]')
  name_surname_input.send_keys(name_surname)
  phone_number_or_email_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
  phone_number_or_email_input.send_keys(phone_number_or_email)
  password_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
  password_input.send_keys(password)
  password_again = driver.find_element(By.XPATH, '//*[@id="ap_password_check"]')
  password_again.send_keys(password)
  continue_button = driver.find_element(By.XPATH, '//*[@id="auth-continue"]/span')
  continue_button.click()
  time.sleep(60)
  driver.close()

def create_account():
  print("To create an Amazon.com.tr account I need some informations")
  name_surname = input("> Name & Surname : ")
  phone_number_or_email = input("> Phone Number or Email : ")
  password = getpass("> Password(min 6 chars) : ")
  password_again = getpass("> Re-enter password : ")
  if name_surname == "" or phone_number_or_email == "" or password == "" or password_again == "":
    print("[!] You have to fill every fields to create account")
    create_account()
  elif password != password_again:
    print("[!] Passwords should be same")
    create_account()
  elif len(password) < 6:
    print("[!] Passwords must be at least 6 characters.")
    create_account()
  else:
    register_with_selenium(name_surname, phone_number_or_email, password)
    print("Your account created.")