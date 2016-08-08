import os
import urllib
import jinja2
import webapp2
from frontend import MainPage, RegisterPage, PolicyPage, BookPage, BookInfoPage
from backend import BookType, BookTypeAdd, BookTypeEdit, BookDetails, BookDetailsAdd, BookDetailsEdit, ImageHandler

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__) + "/html")),
	extensions=['jinja2.ext.autoescape'])

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/register', RegisterPage),
	('/policy', PolicyPage),
	('/type', BookPage),
	('/bookinfo', BookInfoPage),
	('/booktype', BookType),
	('/booktypeAdd', BookTypeAdd),
	('/booktypeEdit', BookTypeEdit),
	('/bookdetails', BookDetails),
	('/bookdetailsAdd', BookDetailsAdd),
	('/bookdetailsEdit', BookDetailsEdit),
	('/img', ImageHandler),
], debug=True)
