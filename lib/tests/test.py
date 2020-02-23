






# import_list = ["seleniu"]
# import_names = ["ms"]


# def import_install(package, handle):
# 	try:
# 		exec("%s = __import__('%s')" % (handle, package), globals(), globals())
# 	except ImportError:
# 		pip.main(['install', package])
# 		exec("%s = __import__('%s')" % (handle, package), globals(), globals())


# if len(import_list) != len(import_names):
# 	raise Exception("import_list & import_names list lengths mismatch")
# else:
# 	for i in range(0, len(import_list)):
# 		import_install(import_list[i], import_names[i])


# browser = ms.StatefulBrowser()
# browser.open("https://www.kijiji.ca/t-login.html")
# browser.select_form("form[id='login-form']")
# browser["emailOrNickname"] = "illuminamine@gmail.com"
# browser["password"] = "C'est martine"
# browser.submit_selected()