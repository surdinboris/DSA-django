from django import forms
from .models import Attach, Standalone, Source

def lastid(model):
    try:
        lid=model.objects.last().id

    except AttributeError:
        lid=0
    return lid
class Form_create(forms.Form):
    new_id = forms.ChoiceField(label="ID", help_text="New ID")
    #serial = forms.CharField(label="Serial", widget=forms.Textarea(attrs={'rows': 1, 'cols': 10, }))
    #machine_type = forms.CharField(label="machine_type", widget=forms.Textarea(attrs={'rows': 1, 'cols': 10, }))
    #source = forms.ModelChoiceField(label="source",queryset=Source.objects.all())
    attachs=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(Form_create, self).__init__(*args, **kwargs)
        self.fields['new_id'].choices = [[ch, ch] for ch in Standalone.objects.all().values_list('id', flat=True)]
        self.fields['new_id'].choices.append([lastid(Standalone) + 1, lastid(Standalone) + 1])
        self.fields['new_id'].initial = [lastid(Standalone) + 1, lastid(Standalone) + 1]
        print(self.fields)