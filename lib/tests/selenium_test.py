from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

BROWSER = "phantomjs"

if BROWSER == "chrome":
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--log-level=3")
	driver = webdriver.Chrome(options=chrome_options)
elif BROWSER == "phantomjs":
	driver = webdriver.PhantomJS()

driver.get("http://kijiji.ca")