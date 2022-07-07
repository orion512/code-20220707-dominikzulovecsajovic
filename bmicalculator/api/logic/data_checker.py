""" Module for validating the data

This script inspects and validates the data sent to the API.

Author: Dominik Zulovec Sajovic - July 2022
"""

from typing import List
from enum import Enum
from pydantic import BaseModel  # pylint: disable=no-name-in-module

# pylint: disable=E0213,R0201


class Gender(str, Enum):
    """Genders"""

    MALE = "Male"
    FEMALE = "Female"


class Person(BaseModel):
    """Representation of a person"""

    Gender: Gender
    HeightCm: float
    WeightKg: float


class JsonChecker(BaseModel):
    """Json checker for the BMI calculator"""

    __root__: List[Person]
