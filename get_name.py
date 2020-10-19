from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def name_song(url):
	options = Options()
	path = "C:\\Drivers\\CD\\chromedriver.exe"
	options.headless = True
	driver = webdriver.Chrome(options=options, executable_path=path)
	wait = WebDriverWait(driver, 10)
	driver.get(url)
	element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
	print(element)
	driver.quit()
	return element


if __name__=="__main__":
	url = "https://youtu.be/5MQCWnlTtso"