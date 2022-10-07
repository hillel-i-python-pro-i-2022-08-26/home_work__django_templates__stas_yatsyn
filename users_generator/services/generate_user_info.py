from random import randint

from faker import Faker

from users_generator.models import UserInfo

fake = Faker()


def generate_names(amount: int) -> list[str]:
    list_with_names: list[str] = []
    for name in range(amount):
        name = f"{fake.first_name().lower()}_{str(randint(1970, 2022))}"
        if name in list_with_names:
            name = f"{'_'.join(fake.first_name().lower())}_{str(randint(1, 1000))}"
        list_with_names.append(name)
    return list_with_names


def generate_emails(amount: int) -> list[str]:
    email_list: list[str] = []
    for email in range(amount):
        email = fake.free_email()
        if email in email_list:
            email = f"{fake.first_name().lower()}{randint(1, 1000)}@gmail.com"
        email_list.append(email)
    return email_list


def generate_passwords(amount: int) -> list[str]:
    list_with_password: list[str] = []
    for password in range(amount):
        password = fake.password(length=randint(5, 25), special_chars=False)
        if password in list_with_password:
            password = fake.password(length=randint(5, 25), special_chars=False).reverse()
        list_with_password.append(password)
    return list_with_password


def organize_info(amount: int) -> UserInfo:
    names = generate_names(amount=amount)
    emails = generate_emails(amount=amount)
    passwords = generate_passwords(amount=amount)

    for name, email, password in zip(names, emails, passwords):
        yield UserInfo(name=name, email=email, password=password)
