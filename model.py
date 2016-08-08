from google.appengine.ext import ndb

class Type(ndb.Model):
	name = ndb.StringProperty()
	details = ndb.TextProperty()
	code = ndb.StringProperty(required=True)

class Product(ndb.Model):
	bookId = ndb.StringProperty(required=True)
	category = ndb.KeyProperty(kind='Type')
	title = ndb.StringProperty()
	descrip = ndb.TextProperty()
	price = ndb.StringProperty()
	author = ndb.StringProperty()
	image = ndb.BlobProperty()
