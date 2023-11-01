"""
Test module for companies app models.

Tests should be run from project root.

Examples:
    # For running a test use following command
    python web_app/manage.py test
"""
from django.db.models import QuerySet
from django.test import TestCase

from companies.models import Company, Address
from companies.tests.address_fixtures import add_address_object, DEFAULT_TEST_ADDRESS
from companies.tests.company_fixtures import add_company_object, DEFAULT_TEST_COMPANY


class TestAddress(TestCase):
    """
    Tests for Address model
    """

    def test_create_address_with_all_fields(self) -> None:
        """
        Test if address object is created using Address model

        Creates a new address object, fetches all objects from database.
        Checks if number of objects is exactly 1, checks if object's fields
        have proper values.
        """
        add_address_object()
        queried_address: QuerySet[Address] = Address.objects.all()
        self.assertEqual(len(queried_address), 1)
        self.assertEqual(
            queried_address[0].country, DEFAULT_TEST_ADDRESS["country"]
        )
        self.assertEqual(
            queried_address[0].region, DEFAULT_TEST_ADDRESS["region"]
        )
        self.assertEqual(queried_address[0].city, DEFAULT_TEST_ADDRESS["city"])
        self.assertEqual(
            queried_address[0].street, DEFAULT_TEST_ADDRESS["street"]
        )
        self.assertEqual(
            queried_address[0].building, DEFAULT_TEST_ADDRESS["building"]
        )
        self.assertEqual(queried_address[0].room, DEFAULT_TEST_ADDRESS["room"])

    # def test_create_address_with_wrong_country_choice_exception(self) -> None:
    #     """
    #     Tests if address object can be created with wrong country choice.
    #
    #     Country field choices is limited. Function tests if wrong Country
    #     choice raises an exception.
    #     """
    #     test_address_id = 1
    #     test_address: list = [*DEFAULT_TEST_ADDRESS]
    #     test_address[0] = "USA"
    #     test_address.insert(0, test_address_id)
    #     address = Address(*test_address)
    #     address.save()


class TestCompany(TestCase):
    """
    Tests for Company model.
    """

    def test_create_company_with_all_fields(self) -> None:
        """
        Test if company object is created using Company model

        Creates a new company object, fetches all objects from database.
        Checks if number of objects is exactly 1.
        """
        add_company_object()
        queried_company: QuerySet[Company] = Company.objects.all()
        print(queried_company[0])
        self.assertEqual(len(queried_company), 1)
