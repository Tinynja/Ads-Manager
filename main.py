#Package dependencies checker
from pip._internal.operations import freeze

DEPENDENCIES = ['selenium',]

for inst_pkg in freeze.freeze():
	for dep_pkg in DEPENDENCIES:
		if inst_pkg.find(dep_pkg) != -1:
			DEPENDENCIES.remove(dep_pkg)
			break

assert (len(DEPENDENCIES) == 0), "Missing packages: %s" % " ".join(DEPENDENCIES)

#Main
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class element_is_stale():
	"""An expectation for checking that the html tag of a
	page has become stale.
	returns True if the page is stale, false otherwise."""
	def __init__(self, element):
		self.element = element

	def __call__(self, driver):
		try:
			self.element.tag_name
		except StaleElementReferenceException:
			return True
		else:
			return False


class Kijiji():

	URLs = {"homepage":"http://kijiji.ca",}

	_url_names = ("homepage", "login")


	def __init__(self, headless=False):
		self._logged_in = False

		#Start the browser
		self._chrome_options = webdriver.ChromeOptions()
		if headless:
			self._chrome_options.add_argument('--headless')
			self._chrome_options.add_argument('--disable-gpu')
		self._chrome_options.add_argument('--log-level=3')
		self._driver = webdriver.Chrome(options=self._chrome_options)

		#Set Kijiji language to English
		self.get("homepage")
		language_toggle = self._driver.find_element_by_xpath("//a[@data-qa-id='language-toggle']")
		if (language_toggle.get_attribute("innerHTML") == "en"):
			language_toggle.click()

		#Fetch all useful URLs
		self.URLs_fetch_all()

		#Initialize categoryId
		self.categoryId_fetch_all()


	def login(self, username, password):
		if self._logged_in:
			self.logout()

		if ("login" not in Kijiji.URLs):
			self.URLs_fetch("login")
		self.get("login")

		email_input = self._driver.find_element_by_xpath("//input[@name='emailOrNickname']")
		password_input = self._driver.find_element_by_xpath("//input[@name='password']")

		email_input.send_keys(username)
		password_input.send_keys(password)
		password_input.submit()

		#Check if login attempt was successful (REDO)
		try:
			self.wait_page_unload(email_input)
			self.wait_page_load()
			assert ("login" not in self._driver.current_url)
		except AssertionError:
			#print("Failed login attempt.")
			return 1
		else:
			self._logged_in = True
			self._username = username
			self._password = password


	def logout(self):
		if self._logged_in:
			self.get("homepage")
			if self.wait_element_present(("xpath", "//button[@aria-label='Navigation menu button']")):
				return 1
			dropdown = self._driver.find_element_by_xpath("//button[@aria-label='Navigation menu button']")
			if dropdown.get_attribute("aria-expanded") == "false": dropdown.click()
			dropdown.find_element_by_xpath("//button[text()='Log Out']").click()
			del self._username
			del self._password
		self._logged_in = False


	def categoryId_fetch_all(self):
		pass


	def URLs_fetch_all(self):
		for n in Kijiji._url_names:
			self.URLs_fetch(n)


	def URLs_fetch(self, name):
		assert (name in Kijiji._url_names), "Invalid URL name: %s" % str(name)
		assert (name in ("homepage", "login")), "Fetching '%s' not implemented (yet)" % str(name)

		if (name == "homepage"):

			Kijiji.URLs["homepage"] = "http://kijiji.ca"

		elif (name == "login"):

			if self._logged_in:
				username_old = self._username
				password_old = self._password
				self.logout()
			self.get("homepage")
			login_button = self._driver.find_element_by_xpath("//a[@title='Sign In']")
			Kijiji.URLs["login"] = login_button.get_attribute("href")
			if "username_old"	in locals():
				self.login(username_old, password_old)


	def get(self, name, force=False):
		element_oldpage = self._driver.find_element_by_tag_name("html")
		self._driver.get(Kijiji.URLs[name])
		return self.wait_page_unload(element_oldpage) or self.wait_page_load()


	def wait_page_unload(self, page_element, timeout=5):
		try:
			WebDriverWait(self._driver, timeout).until(
				element_is_stale(page_element)
			)
		except TimeoutException:
			print("TimeoutException")
			return 1
		else:
			return 0


	def wait_page_load(self, timeout=5):
		return self.wait_element_present(("xpath", "//a[@title='Kijiji']"))


	def wait_element_present(self, locator, timeout=5):
		assert (type(locator) is tuple and len(locator) == 2), "Invalid locator: %s" % str(locator)
		try:
			WebDriverWait(self._driver, timeout).until(
				EC.presence_of_element_located(locator)
			)
		except TimeoutException:
			print("TimeoutException")
			return 1
		else:
			return 0


	def __del__(self):
		self._driver.quit()