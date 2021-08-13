from django import forms

from core.mixins import BootstrapFormMixin
from online_shop.online_shop_profiles.models import Profile


class ProfileDetailsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('is_complete', 'user',)
