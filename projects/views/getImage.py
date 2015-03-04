from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse
import base64

templater = get_renderer('projects')

@view_function
def process_request(request):
    image_name = request.GET['src']
    image_file = open("projects/media/"+image_name, "rb")
    response = HttpResponse(image_file.read(), content_type='img/jpeg')
    response['Content-Disposition'] = 'attachment; filename='+image_name
    return response;