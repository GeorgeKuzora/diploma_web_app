"""
Test fixtures for companies app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .fixtures import <function_name>
"""
from companies.models import Address, Company


DEFAULT_TEST_COUNTRY: str = "RUS"
DEFAULT_TEST_REGION: str = "moscow"
DEFAULT_TEST_CITY: str = "moscow"
DEFAULT_TEST_STREET: str = "tverskaya"
DEFAULT_TEST_BUILDING: str = "1"
DEFAULT_TEST_ROOM: str = "1"

DEFAULT_TEST_ADDRESS: tuple = (
    DEFAULT_TEST_COUNTRY,
    DEFAULT_TEST_REGION,
    DEFAULT_TEST_CITY,
    DEFAULT_TEST_STREET,
    DEFAULT_TEST_BUILDING,
    DEFAULT_TEST_ROOM,
)


def add_address_object(
    country: str = DEFAULT_TEST_COUNTRY,
    region: str = DEFAULT_TEST_REGION,
    city: str = DEFAULT_TEST_CITY,
    street: str = DEFAULT_TEST_STREET,
    building: str = DEFAULT_TEST_BUILDING,
    room: str = DEFAULT_TEST_ROOM,
) -> None:
    """
    Creates and saves address object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        country: Address country.
            Default value: 'RUS'
        region: Address region.
            Default value: 'moscow'
        city: Address city.
            Default value: 'moscow'
        street: Address street.
            Default value: 'tverskaya'
        building: Address building.
            Default value: '1'
        room: Address room.
            Default value: '1'

    Example:
        # Call this function like this
        add_address_object(<args>)
    """
    address: Address = Address(
        country=country,
        region=region,
        city=city,
        street=street,
        building=building,
        room=room,
    )
    address.save()
