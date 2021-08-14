from django.template import Library

from online_shop.online_shop_profiles.models import Profile
register = Library()


@register.inclusion_tag('tags/has_order_request.html', takes_context=True)
def has_order_request_notification(context):
    has_order_request = True
    if context.request.user.id:
        profile = Profile.objects.get(pk=context.request.user.id)
        has_order_request = profile.has_order_request

    return {
        'has_order_request': has_order_request,
    }
