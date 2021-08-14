from online_shop.online_shop_orders.forms import OrderForm


def test_form_when_orderer_first_name_starts_with_lowercase_expect_not_to_create_it(self):
    data = {
        'orderer_first_name': 'gosho',
        'orderer_last_name': 'Georgiev',
        'address_street': 'Vasil Levski 21',
        'address_city': 'Plovdiv',
        'address_country': 'Bulgaroa',
        'postal_code': 2500,
    }

    form = OrderForm(data)
    self.assertFalse(form.is_valid())


def test_form_when_orderer_last_name_starts_with_lowercase_expect_not_to_create_it(self):
    data = {
        'orderer_first_name': 'Gosho',
        'orderer_last_name': 'georgiev',
        'address_street': 'Vasil Levski 21',
        'address_city': 'Plovdiv',
        'address_country': 'Bulgaroa',
        'postal_code': 2500,
    }

    form = OrderForm(data)
    self.assertFalse(form.is_valid())


def test_form_when_orderer_first_last_name_starts_with_uppercase_expect_create_it(self):
    data = {
        'orderer_first_name': 'Gosho',
        'orderer_last_name': 'Georgiev',
        'address_street': 'Vasil Levski 21',
        'address_city': 'Plovdiv',
        'address_country': 'Bulgaroa',
        'postal_code': 2500,
    }

    form = OrderForm(data)
    self.assertTrue(form.is_valid())
