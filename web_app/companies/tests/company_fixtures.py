"""
Test fixtures for companies app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .fixtures import <function_name>
"""
from typing import Union
from companies.models import Address, Company
from companies.tests.address_fixtures import add_address_object

DEFAULT_ADDRESS = add_address_object()
DEFAULT_TEST_COMPANY: dict[str, str | Address | int] = {
    "id": 1,
    "title": "yandex",
    "desc": "Software company",
    "email": "example@example.ru",
    "phone": "+78988908789",
    "address": DEFAULT_ADDRESS,
}


def add_company_object(
        id: str | Address | int = DEFAULT_TEST_COMPANY["id"],
        title: str | Address | int = DEFAULT_TEST_COMPANY["title"],
        desc: str | Address | int = DEFAULT_TEST_COMPANY["desc"],
        email: str | Address | int = DEFAULT_TEST_COMPANY["email"],
        phone: str | Address | int = DEFAULT_TEST_COMPANY["phone"],
        address: str | Address | int = DEFAULT_TEST_COMPANY["address"],
        ) -> Company:
    """
    Creates and saves company object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        id: Company id.
            Default value: 1
        title: Company title.
            Default value: 'yandex'
        desc: Company description.
            Default value: 'Software company.'
        email: Company email.
            Default value: 'example@example.ru'
        phone: Company phone.
            Default value: '+78988908789'
        address: Company address.
            Default value: default address

    Example:
        # Call this function like this
        add_company_object(<args>)
    """
    company: Company = Company(
        id=id,
        title=title,
        description=desc,
        email=email,
        phone=phone,
        # address=address,
    )
    company.save()
    company.address = address
    return Company.objects.get(id=id)
