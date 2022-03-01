# SPDX-FileCopyrightText: 2022 Tammy Cravit <tammymakesthings.com>
#
# SPDX-License-Identifier: Unlicense

# pylint: disable=missing-module-docstring


class Pet:
    """Represents a pet."""

    def __init__(
        self,
        name: str = "Fluffy",
        kind: str = "Alpaca",
        owner: str = "Tammy",
        age: int = 1,
    ) -> None:
        """
        Create a new pet.

        :param str name: The name of the pet, defaults to "Fluffy"
        :param str kind: The pet's species, defaults to "Alpaca"
        :param str owner: The pet's owner, defaults to "Tammy"
        :param int age: The pet's age, defaults to 1
        """
        self._name = name
        self._kind = kind
        self._owner = owner
        self._age = age

    @property
    def name(self) -> str:
        """
        Retrieve the name of the pet.

        :return str: The name of the pet.
        """
        return self._name

    @property
    def kind(self) -> str:
        """
        Retrieve the kind (species) of the pet.

        :return str: The species of the pet.
        """
        return self._kind

    @property
    def owner(self) -> str:
        """
        Retrieve the owner of the pet.

        :return str: The owner of the pet.
        """
        return self._owner

    @property
    def age(self) -> int:
        """
        Retrieve the age of the pet.

        :return int: The age of the pet.
        """
        return self._age

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the pet's name.

        :param str new_name: The pet's new name.
        """
        self._name = new_name

    @kind.setter
    def kind(self, __: str) -> None:
        """
        Setter for the pet's species.

        The species is a readonly property, so this will always raise a
        `AttributeError`.

        :param str __: The pet's new species. (A placeholder because this is
        not supported)
        :raises AttributeError: Always raised because species is read-only.
        """
        raise AttributeError("You can't change the kind of an animal!")

    @owner.setter
    def owner(self, new_owner: str) -> None:
        """
        Set the pet's owner.

        :param str new_owner: The pet's new owner.
        """
        self._owner = new_owner

    @age.setter
    def age(self, new_age: int) -> None:
        """
        Set the pet's age.

        :param int new_age: The pet's new age.
        """
        self._age = new_age

    def happy_birthday(self) -> str:
        """
        Celebrate the pet's birthday!

        Increments their age, and returns a happy birthday message.

        :return str: The 'happy birthday' message.
        """
        self._age = self._age + 1
        return f"Happy birthday to {self.name}, who is now {self.age}!"

    def __str__(self) -> str:
        # pylint: disable=line-too-long
        return f"{self.name} is a {self.kind}, who belongs to {self.owner} and is {self.age} years old."
