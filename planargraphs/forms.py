from django import forms

from .models import Space
from .models import Planargraph

class SpaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Space
        fields = '__all__'
        

class PlanargraphForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    class Meta:
        model = Planargraph
        fields = '__all__'

class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎?')