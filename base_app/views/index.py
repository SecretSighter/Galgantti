from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime

templater = get_renderer('base_app')

@view_function
def process_request(request):
	template_vars = {
		'now': datetime.now(),
	}

	return templater.render_to_response(request, 'index.html', template_vars)