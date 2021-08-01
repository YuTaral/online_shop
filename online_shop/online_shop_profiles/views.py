from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from online_shop.online_shop_profiles.forms import ProfileForm
from online_shop.online_shop_profiles.models import Profile


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/details.html', context)


from online_shop.online_shop_profiles.signals import user_created, check_is_complete
