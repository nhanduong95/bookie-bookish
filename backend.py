import os
import urllib
import jinja2
import webapp2
import logging
from google.appengine.api import images
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import users
from model import Type,Product

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__) + '/html/backend')),
	extensions=['jinja2.ext.autoescape'])

class BookType(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				template = JINJA_ENVIRONMENT.get_template('/booktype.html')
				all_book_types = Type.query().order(Type.code).fetch()
				template_values = {
					'all_book_types': all_book_types,
					'url': url,
					'url_linktext': url_linktext,
				}
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')

		else:
			self.redirect('/')

class BookTypeAdd(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				template_values = {
					'url': url,
					'url_linktext': url_linktext,
				}
				template = JINJA_ENVIRONMENT.get_template('/booktype_add.html')
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')

		else:
			self.redirect('/')

	def post(self):
		book_type = Type()
		if self.request.get('code'):
			book_type.code = self.request.get('code')
		if self.request.get('name'):
			book_type.name = self.request.get('name')
		if self.request.get('editor1'):
			book_type.details = self.request.get('editor1')
		book_type.put()
		logging.info('Add a book type with %s', book_type.name)
		self.redirect('/booktype')

class BookTypeEdit(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				type_code = self.request.get('code')
				if type_code is None:
					logging.info('No code supplied')
					self.redirect('/booktype')
				else:
					logging.info('Book type code %s', type_code)

				book_type = Type.query(Type.code == type_code).get()
				if book_type is None:
					logging.info('Cannot find type with code %s', type_code)
					self.redirect('/booktype')
				template_values = {
					'book_type': book_type,
					'url': url,
					'url_linktext': url_linktext,
					}
				template = JINJA_ENVIRONMENT.get_template('/booktype_edit.html')
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')

		else:
			self.redirect('/')

	def post(self):
		type_code = self.request.get('code')
		if type_code is None:
			logging.info('No code supplied')
			self.redirect('/booktype')
		else:
			logging.info('Book type code %s', type_code)

		book_type = Type.query(Type.code == type_code).get()
		if book_type is None:
			logging.info('Cannot find type with code %s', type_code)
			self.redirect('/booktype')

		book_type.code = self.request.get('code')
		book_type.name = self.request.get('name')
		book_type.details = self.request.get('editor1')
		book_type.put()
		logging.info('Edit a book type with: %s', book_type.key)
		self.redirect('/booktype')

	def delete(self):
		logging.info('In delete')

		type_code = self.request.get('code')
		if type_code is None:
			logging.info('No code supplied')
			self.redirect('/booktype')
		else:
			logging.info('Book type code %s', type_code)

		book_type = Type.query(Type.code == type_code).get()
		if book_type is None:
			logging.info('Cannot find this type with code %s', type_code)
			self.redirect('/booktype')

		book_type.key.delete()
		self.redirect('/booktype')

class BookDetails(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				template = JINJA_ENVIRONMENT.get_template('/bookdetails.html')
				all_book_details = Product.query().order(Product.bookId).fetch()
				template_values = {
					'all_book_details': all_book_details,
					'url': url,
					'url_linktext': url_linktext,
				}
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')
		else:
			self.redirect('/')

class BookDetailsAdd(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				types = Type.query().order(Type.code).fetch()
				if types is None:
					logging.info('None')
					self.redirect('/bookdetails')
				else:
					logging.info('Not none')

				template_values = {
					'types': types,
					'url': url,
					'url_linktext': url_linktext,
				}
				template = JINJA_ENVIRONMENT.get_template('/bookdetails_add.html')
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')
		else:
			self.redirect('/')

	def post(self):
		book_type = self.request.get('type')
		if book_type is None:
			logging.info('None')
			self.redirect('/bookdetails')
		else:
			logging.info('Book type: %s', book_type)

		type_name = Type.query(Type.name == book_type).get()
		if type_name is None:
			logging.info('None')
			self.redirect('/bookdetails')
		else:
			logging.info('Type %s',book_type)

		book_details = Product()

		if self.request.get('img'):
			book_details.image = db.Blob (images.resize(self.request.get('img'), 350, 450))

		book_details.bookId = self.request.get('bookcode')
		book_details.title = self.request.get('title')
		book_details.category = type_name.key
		book_details.author = self.request.get('author')
		book_details.price = self.request.get('price')
		book_details.descrip = self.request.get('editor1')
		book_details.put()

		logging.info('Added book with: %s', book_details.bookId)
		self.redirect('/bookdetails')
		
class BookDetailsEdit(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'LOG OUT'

			if users.is_current_user_admin():
				types = Type.query().fetch()
				if types is None:
					logging.info('None')
					self.redirect('/bookdetails')
				else:
					logging.info('Not none')

				book_code = self.request.get('code')
				if book_code is None:
					logging.info('No code supplied')
					self.redirect('/bookdetails')
				else:
					logging.info('Book code %s', book_code)

				book_details = Product.query(Product.bookId == book_code).get()
				if book_details is None:
					logging.info('Cannot find book with code %s', book_code)

				template_values = {
					'book_details': book_details, 
					'types': types,
					'url': url,
					'url_linktext': url_linktext,
				}
				template = JINJA_ENVIRONMENT.get_template('/bookdetails_edit.html')
				self.response.write(template.render(template_values))
			else:
				self.redirect('/')
		else:
			self.redirect('/')

	def post(self):
		book_type = self.request.get('type')
		if book_type is None:
			logging.info('None')
			self.redirect('/bookdetails')
		else:
			logging.info('Book type:  %s', book_type)

		type_name = Type.query(Type.name == book_type).get()
		if type_name is None:
			logging.info('None')
			self.redirect('/bookdetails')
		else:
			logging.info('type %s',book_type)

		book_code = self.request.get('bookcode')
		if book_code is None:
			logging.info('No id supplied')
			self.redirect('/bookdetails')
		else:
			logging.info('Type id is %s', book_code)
		book_details = Product.query(Product.bookId == book_code).get()
		if book_details is None:
			logging.info('Cannot find type with code %s', book_code)

		picture = self.request.get('img')
		if picture:
			pic = images.resize(picture, 350, 450)
			book_details.image = db.Blob (pic)	
		
		book_details.bookId = self.request.get('bookcode')
		book_details.title = self.request.get('title')
		book_details.category = type_name.key
		book_details.author = self.request.get('author')
		book_details.price = self.request.get('price')
		book_details.descrip = self.request.get('editor1')
		book_details.put()

		logging.info('Edited book with id: %s', book_details.bookId)
		self.redirect('/bookdetails')

	def delete(self):
		logging.info('In delete')

		book_code = self.request.get('code')
		if book_code is None:
			logging.info('No code supplied')
			self.redirect('/bookdetails')
		else:
			logging.info('Book code %s', book_code)

		book_details = Product.query(Product.bookId == book_code).get()
		if book_details is None:
			logging.info('Cannot find book with code %s', book_code)
			self.redirect('/bookdetails')

		book_details.key.delete()
		self.redirect('/bookdetails')

class ImageHandler(webapp2.RequestHandler):
	def get(self):
		img_key = ndb.Key('Product', int(self.request.get('img_id')))
		book_details = Product.query(Product.key == img_key).get()
		if book_details.image:
			self.response.headers['Content_Type'] = 'image/png'
			self.response.out.write(book_details.image)
		else:
			self.response.out.write('No image')
