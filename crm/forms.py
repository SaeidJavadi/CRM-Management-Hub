from django import forms
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance


class ObjectModelForm60(forms.ModelForm):
    class Meta:
        model = Common60
        fields = '__all__'


class ObjectModelForm61(forms.ModelForm):
    class Meta:
        model = Common61
        fields = '__all__'


class ObjectModelForm70(forms.ModelForm):
    class Meta:
        model = Common70
        fields = '__all__'


class ObjectModelFormCd(forms.ModelForm):
    class Meta:
        model = CommonDead
        fields = '__all__'


class ObjectModelFormJd(forms.ModelForm):
    class Meta:
        model = JudiciaryDead
        fields = '__all__'


class ObjectModelFormDd(forms.ModelForm):
    class Meta:
        model = DoingDead
        fields = '__all__'


class ObjectModelFormPa(forms.ModelForm):
    class Meta:
        model = PublicAssistance
        fields = '__all__'
