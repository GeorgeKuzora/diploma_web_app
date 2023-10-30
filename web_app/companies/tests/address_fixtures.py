"""
Test fixtures for companies app tests.

Provides fixtures for repeated actions.

Examples:
    # import it in a test module
    from .fixtures import <function_name>
"""
from companies.models import Address


DEFAULT_TEST_ADDRESS: dict[str, str | int] = {
    "id": 1,
    "country":  "RUS",
    "region":  "moscow",
    "city":  "moscow",
    "street":  "tverskaya",
    "building":  "1",
    "room":  "1",
}


def add_address_object(
    id: str | int = DEFAULT_TEST_ADDRESS["id"],
    country: str | int = DEFAULT_TEST_ADDRESS["country"],
    region: str | int = DEFAULT_TEST_ADDRESS["region"],
    city: str | int = DEFAULT_TEST_ADDRESS["city"],
    street: str | int = DEFAULT_TEST_ADDRESS["street"],
    building: str | int = DEFAULT_TEST_ADDRESS["building"],
    room: str | int = DEFAULT_TEST_ADDRESS["room"],
) -> Address:
    """
    Creates and saves address object.

    If no arguments provided creates object with defaults arguments.
    Default arguments is always the same.

    Args:
        id: Address id.
            Default value: 1
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
        id=id,
        country=country,
        region=region,
        city=city,
        street=street,
        building=building,
        room=room,
    )
    address.save()
    return Address.objects.get(id=id)
