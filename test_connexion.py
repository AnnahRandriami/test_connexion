from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

try:
   
    driver.get("http://127.0.0.1:5500/index.html")
    
    time.sleep(2)
    
 
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    

    username_field.send_keys("test_user")  #nom utilisateur de test
    password_field.send_keys("test_password")  # mot de passe de test
    
    login_button.click()
    
   
    time.sleep(3)
    

    try:
       
        home_page_element = driver.find_element(By.XPATH, "//h1[contains(text(),'Bienvenue')]")
        print("Test réussi : Connexion réussie")
    except:
        print("Test échoué : Connexion non réussie")
        
finally:

    driver.quit()
