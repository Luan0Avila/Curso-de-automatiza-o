from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

pesquisa = input("Digite a pesquisa: ")

driver = webdriver.Chrome()
driver.get("https://www.google.com")

campo = driver.find_element(By.NAME,"q")
campo.send_keys(pesquisa)
time.sleep(1)
campo.send_keys(Keys.ENTER)
time.sleep(5)

resultados = driver.find_element(By.ID, "result-stats")
print(resultados.text)