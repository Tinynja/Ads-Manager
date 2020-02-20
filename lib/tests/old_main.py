import pip

import_list = ["mechanicalsoup"]
import_names = ["ms"]

def import_install(package, handle):
	try:
		exec("%s = __import__('%s')" % (handle, package), globals(), globals())
	except ImportError:
		pip.main(['install', package])
		exec("%s = __import__('%s')" % (handle, package), globals(), globals())

if len(import_list) != len(import_names):
	raise Exception("import_list & import_names list lengths mismatch")
else:
	for i in range(0, len(import_list)):
		import_install(import_list[i], import_names[i])

    


# Create a new ad
ad={}

ad['name']=input('Friendly name (alphanumeric): ')
ad['title']=input('Title: ')
ad['desc']=input('Description: ')
ad['tags']=[x.strip() for x in input('Tags (comma separated): ').split(',')]

os.mkdir('ads/'+ad['name'])
with open('ads/'+ad['name']+'/'+ad['name']+'.json', 'w') as write_file:
		json.dump(ad, write_file)

# Import an ad
# https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=###

def check_connection()


def 

class Ad:

	def __init__(self, adtype=0, seller=0, title="", urgent=0, description="",
							tags=[], pictures=[], youtube="", website="", location="",
							price="", phone="", promotions=[0, 0, 0, 0, 0])
		# Class attributes
		self.adtype = adtype
		self.seller = seller
		self.title = title
		self.urgent = urgent
		self.description = description
		self.tags = tags
		self.pictures = pictures
		self.youtube = youtube
		self.website = website
		self.location = location
		self.price = price
		self.phone = phone
		self.promotions = promotions

	def delete()
		something...

	def create()
		something...

	def update()
		self.delete()
		self.create()