from django.conf import settings
from django import forms
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from base_app.models import MyUser
from lib.tables import MyTable

@view_function
def process_request(request):
	table = MyTable(request)
	qry = MyUser.objects.all()

	for u in MyUser.objects.all()[0:table.rows_per_page]:
		table.append([ u.get_full_name(), u.salary.__str__() ])
	template_vars = {
		'table': table,
		'initial_page': '1'
	}
	return dmp_render_to_response(request, 'tabledemo.html', template_vars)


@view_function
def get_table(request):
	table = MyTable(request)
	qry = MyUser.objects.all()	

	for u in table.paginate(request, qry):
		table.append([ u.get_full_name(), u.salary.__str__()  ])
	template_vars = {
		'table': table
	}
	return dmp_render_to_response(request, 'tabledemo.get_table.html', template_vars)