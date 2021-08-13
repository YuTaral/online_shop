from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from online_shop.online_shop_profiles.forms import ProfileDetailsForm
from online_shop.online_shop_profiles.models import Profile


@login_required
def profile_details(request, ):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileDetailsForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile_details.html', context)


from online_shop.online_shop_profiles.templatetags import profile_complete_notification
