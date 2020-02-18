from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://kijiji.ca")