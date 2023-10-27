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
from companies.tests.fixtures import add_address_object, DEFAULT_TEST_ADDRESS


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
        self.assertEqual(queried_address[0].country, DEFAULT_TEST_ADDRESS[0])
        self.assertEqual(queried_address[0].region, DEFAULT_TEST_ADDRESS[1])
        self.assertEqual(queried_address[0].city, DEFAULT_TEST_ADDRESS[2])
        self.assertEqual(queried_address[0].street, DEFAULT_TEST_ADDRESS[3])
        self.assertEqual(queried_address[0].building, DEFAULT_TEST_ADDRESS[4])
        self.assertEqual(queried_address[0].room, DEFAULT_TEST_ADDRESS[5])

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
