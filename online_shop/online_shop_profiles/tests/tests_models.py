from django.core.exceptions import ValidationError
from django.test import TestCase

from online_shop.online_shop_auth.models import OnlineShopUser
from online_shop.online_shop_profiles.models import Profile


class ModelTests(TestCase):
    def test_model_profile_first_name_starts_with_lowercase_expect_to_raise(self):
        test_user = OnlineShopUser(email='gosho1@abv.bg', password='qwe123')
        test_user.full_clean()
        test_user.save()

        profile = Profile(
            first_name='gosho',
            last_name='Gerogiev',
            age=32,
            user=test_user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_model_profile_last_name_starts_with_lowercase_expect_to_raise(self):
        test_user = OnlineShopUser(email='gosho2@abv.bg', password='qwe123')
        test_user.full_clean()
        test_user.save()

        profile = Profile(
            first_name='Gosho',
            last_name='georgiev',
            age=32,
            user=test_user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)


