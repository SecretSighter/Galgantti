from django.conf import settings
from django import forms
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from base_app.models import File
from django.forms.widgets import Input

@view_function
def process_request(request):

	form = UploaderForm()

	if request.method == 'POST':
		form = UploaderForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['upload_fullName'])
			form = UploaderForm()

	template_vars = {
		'form': form
	}
	return dmp_render_to_response(request, 'fileUpload.html', template_vars)

@view_function
def upload(request):
	# print('>>>>>>>>>>>>>>>', request.GET)
	# print('>>>>>>>>>>>>>>>', request.FILES['uploadfile'])
	# print('>>>>>>>>>>>>>>>', request.POST)

	uploaded_file = request.FILES['uploadfile']

	fileLocation = 'upload';

	fh = open(fileLocation+'/'+uploaded_file.name, "wb+")
	for chunk in uploaded_file.chunks():
		fh.write(chunk)
	fh.close()

	uploadedFile = File(filename=uploaded_file.name, guid = request.generate_webid.attempt_session(), location=fileLocation)

	#print(uploadedFile)

	return HttpResponse(fileLocation+'/'+uploaded_file.name)

######
## This widget invokes the default file upload behavior, this input is meant to disappear on form submission
#####
class AjaxFileInput(Input):
    input_type = 'file'
    needs_multipart_form = True

    def render(self, name, value, attrs=None):
        attrs['class'] = 'btn btn-default'
        return super(AjaxFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        "File widgets take data from FILES, not POST"
        return files.get(name, None)

class UploaderForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	upload_fullName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'disabled': 'true'}))
	upload_file = forms.FileField(required=False,widget=AjaxFileInput())

