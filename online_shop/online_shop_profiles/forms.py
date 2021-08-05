from django import forms

from core.forms import BootstrapFormMixin
from online_shop.online_shop_profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')


class ProfileDetailsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('is_complete', 'user',)

