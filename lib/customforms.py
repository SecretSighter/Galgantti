import django.forms
from django.utils.safestring import mark_safe
from django.forms.widgets import Input

class SpecialInput(Input):
    input_type = 'special'

    def __init__(self, attrs=None):
        attrs = {'class' : 'form-control'}
        if attrs is not None:
            self.input_type = attrs.pop('type', self.input_type)
        super(SpecialInput, self).__init__(attrs)

class CustomForm(django.forms.Form):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.form_id = request.generate_webid.yield_next();
        super(CustomForm, self).__init__(*args, **kwargs)
        self.init()

    def init(self):
        pass

    def as_full(self):
        "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
        output = []
        output.append("<form method='post' id=" + self.form_id.__str__() + " class='form-inline'><table>")
        output.append(self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s</th><td><div class="bg-danger">%(errors)s</div>%(field)s%(help_text)s</td></tr>',
            error_row='<tr class="danger"><td colspan="2">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<br /><span class="helptext">%s</span>',
            errors_on_separate_row=False))
        output.append("</table><input type='submit' class='btn btn-default'/></form>")
        return mark_safe('\n'.join(output))

    def __str__(self):
        return self.as_full()