import random
from random_address import real_random_address, random_address
from faker import Faker

fake = Faker(['en_US'])


def generate_random_email():
    domains = ["@gmail.com", "@outlook.com", "@yahoo.com"]
    domain = random.choice(domains)
    email = fake.user_name() + domain
    return email


def generate_us_phone_number():
    phone_number = fake.basic_phone_number()
    return phone_number


def generate_us_city_address(city):
    return random_address.real_random_address_by_state('CA')

def generate_profile():
    return fake.profile()
