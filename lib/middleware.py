from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

class WebGuidMiddleware:
	def process_request(self, request):
		request.generate_webid = WebIdGenerator()

class WebIdGenerator(object):

	def __init__(self):
		self.i = 0

	def iterate(self):
		while True:
			self.i += 1
			yield self.i

	def yield_next(self):
		return next(self.iterate())

	def attempt_session(self):
		s = SessionStore()
		s.create()
		s.save()
		return s.session_key

# ask the database to start the number, use the postgres database to generate this unique id