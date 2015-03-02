from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from lib.customforms import CustomForm
from lib.customforms import SpecialInput

templater = get_renderer('projects')

@view_function
def process_request(request):

    userform = MyForm(request)

    print(request)
    if(request.POST):
        userform = MyForm(request, request.POST)
        if userform.is_valid():
            pass
        else:
            print('the form did not validate')
    else:
        print('request is get')
    template_vars = {
        'now': datetime.now(),
        'form': userform,
    }
    print userform.errors
    return templater.render_to_response(request, 'create.html', template_vars)

class MyForm(CustomForm):

    def init(self):
        self.fields['action'] = forms.CharField(required=True, widget=SpecialInput)
        self.fields['deliverable'] = forms.CharField(required=True, widget=SpecialInput)
        self.fields['name'] = forms.CharField(required=True, widget=SpecialInput)

    def commit(self):
        print('the form did validate!')
        # self.clean_username()
        # raise forms.ValidationError('This value cannot be empty')

    def clean_username(self):
        return self.cleaned_data['username']

class MySecondForm(forms.Form):
    action = forms.CharField(required=True, widget=SpecialInput)
    deliverable = forms.CharField(required=False, widget=SpecialInput)
    name = forms.CharField(required=False, widget=SpecialInput)