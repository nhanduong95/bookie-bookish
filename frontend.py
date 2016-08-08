import os
import urllib
import jinja2
import webapp2
import logging
from model import Type,Product
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__) + "/html/frontend")),
	extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

	def get(self):
		
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Click here to log out'
			if users.is_current_user_admin():
				self.redirect('/booktype')
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Click here to log in'

		all_book_types = Type.query().order(Type.code).fetch()
		template_values = {
			'all_book_types': all_book_types,
			'url': url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('/homepage.html')
		self.response.write(template.render(template_values))

class RegisterPage(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Click here to log out'
			if users.is_current_user_admin():
				self.redirect('/booktype')
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Click here to log in'

		all_book_types = Type.query().order(Type.code).fetch()
		template_values = {
			'all_book_types': all_book_types,
			'url': url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('/register.html')
		self.response.write(template.render(template_values))

class PolicyPage(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Click here to log out'
			if users.is_current_user_admin():
				self.redirect('/booktype')
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Click here to log in'

		all_book_types = Type.query().order(Type.code).fetch()
		template_values = {
			'all_book_types': all_book_types,
			'url': url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('/policy.html')
		self.response.write(template.render(template_values))

class BookPage(webapp2.RequestHandler):

	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Click here to log out'
			if users.is_current_user_admin():
				self.redirect('/booktype')
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Click here to log in'

		all_book_types = Type.query().order(Type.code).fetch()
		all_book_details = Product.query().order(Product.bookId).fetch()

		type_code = self.request.get('code')
		if type_code is None:
			logging.info('No code supplied')
			self.redirect('/')
		else:
			logging.info('Book type code %s', type_code)

		book_type = Type.query(Type.code == type_code).get()
		if book_type is None:
			logging.info('Cannot find type with code %s', type_code)
			self.redirect('/')

		template_values = {
			'all_book_types': all_book_types, 
			'book_type': book_type,
			'all_book_details': all_book_details,
			'url': url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('/product.html')
		self.response.write(template.render(template_values))

class BookInfoPage(webapp2.RequestHandler):

	def get(self):
		
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Click here to log out'
			if users.is_current_user_admin():
				self.redirect('/booktype')
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Click here to log in'

		all_book_types = Type.query().order(Type.code).fetch()

		book_code = self.request.get('code')
		if book_code is None:
			logging.info('No code supplied')
			self.redirect('/')
		else:
			logging.info('Book type code %s', book_code)

		book_details = Product.query(Product.bookId == book_code).get()
		if book_details is None:
			logging.info('Cannot find type with code %s', book_code)
			self.redirect('/')

		template_values = {
			'all_book_types': all_book_types, 
			'book_details': book_details,
			'url': url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('/productdetails.html')
		self.response.write(template.render(template_values))

