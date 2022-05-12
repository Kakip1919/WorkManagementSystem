from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://crowdworks.jp/public/jobs/group/development")

sleep(20)
