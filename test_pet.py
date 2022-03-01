# pylint: disable=missing-module-docstring

"""
Unit tests for the Pet class.
"""

import pytest  # pylint: disable=unused-import
from pet import Pet


def test_can_instantiate_object():
    """
    Make sure that we can create a Pet object.
    """
    the_pet = Pet()

    assert not the_pet is None
    assert isinstance(the_pet, Pet)


def test_has_default_properties():
    """
    Make sure that a newly created pet with no parameters has the right
    default values for its properties.
    """
    the_pet = Pet()

    assert the_pet.name == "Fluffy"
    assert the_pet.age == 1
    assert the_pet.kind == "Alpaca"
    assert the_pet.owner == "Tammy"


def test_constructor_sets_properties():
    # pylint: disable=invalid-name
    """
    Make sure the Pet constructor sets its properties correctly.
    """
    the_pet = Pet(name="George", kind="Goldfish", owner="Paden", age=3)

    assert the_pet.name == "George"
    assert the_pet.age == 3
    assert the_pet.kind == "Goldfish"
    assert the_pet.owner == "Paden"


def test_can_set_properties():
    """
    Make sure we can set the properties of a Pet.
    """
    the_pet = Pet(name="George", kind="Goldfish", owner="Paden", age=3)
    the_pet.name = "Boris"
    the_pet.owner = "Raf"
    the_pet.age = the_pet.age + 1

    assert the_pet.name == "Boris"
    assert the_pet.age == 4
    assert the_pet.kind == "Goldfish"
    assert the_pet.owner == "Raf"


def test_kind_is_readonly():
    """
    Make sure trying to change a pet's species raises an error.
    """
    the_pet = Pet(name="George", kind="Goldfish", owner="Paden", age=3)

    with pytest.raises(AttributeError):
        the_pet.kind = "Octopus"


def test_happy_birthday():
    """
    Make sure we can celebrate a birthday correctly.
    """
    the_pet = Pet(name="George", kind="Goldfish", owner="Paden", age=3)
    birthday_msg = the_pet.happy_birthday()

    assert the_pet.age == 4
    assert birthday_msg == (
        f"Happy birthday to {the_pet.name}, who is now {the_pet.age}!"
    )


def test_str_dunder_method():
    """
    Make sure the `__str__` method returns the right thing.
    """
    the_pet = Pet(name="George", kind="Goldfish", owner="Paden", age=3)

    # pylint: disable=line-too-long
    assert (
        str(the_pet) == "George is a Goldfish, who belongs to Paden and is 3 years old."
    )
