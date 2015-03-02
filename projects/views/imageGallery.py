from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from lib.customforms import CustomForm
from lib.customforms import SpecialInput

templater = get_renderer('projects')

@view_function
def process_request(request):

    template_vars = {

    }
    return templater.render_to_response(request, 'imageGallery.html', template_vars)