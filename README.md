# online_shop
Online Shop is Django Framework web project for shopping online.
In this project you can sell and buy items online. It has functionality to register user, upload products for sale, search for products with chosen by yourself criteria, ordering products from other users. You can also delete and edit your uploaded products and check if you have some order requests.
The project has the following apps: auth, profiles, orders and products.
To implement the functionality the following models are used:
- model Profile 
- model OnlineShopUser
- model OnlineShopUserManager
- model Product
- model Order

The project is using PostgreSQL as database.

The project has the following requirements:
- Python 3.8
- Django 3.2.5
- asgiref 3.4.1
- Pillow 8.3.1
- psycopg2 2.9.1
- sqlparse 0.4.1