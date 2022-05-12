# `py_pet_exercise`

The `py_pet_exercise` module implements a simple Python object to represent
a pet.

The requirements for the `Pet` object were as follows:

- Has attributes for pet name, kind (species), owner, and age;
- Provides property accessors for its private instance variables;
- Prevents a pet's species from being changed after instantiation.

## Installing

To install the dependencies for this package:

1. Install [pdm](https://pdm.fming.dev/), the Python Development Manager,
   following the [installation instructions](https://pdm.fming.dev/#recommended-installation-method).
   Make sure to [enable PEP 582](https://pdm.fming.dev/#enable-pep-582-globally) for
   your environment.

2. Run the command `pdm update` in this directory to install the needed project
   dependencies. Needed libraries will be installed in the `__pypackages__`
   subdirectory, which will be created if needed.

3. To run the unit tests, issue the command `pdm run pytest` in this directory.
   The unit tests will be run, and a test coverage summary will be provided.

## Author

The `py_pet_exercise` was created by [Tammy Cravit](https://github.com/tammymakesthings).
