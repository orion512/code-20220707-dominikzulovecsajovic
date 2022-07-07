"""
Testing bmi calcs endpoint

Author: Dominik Zulovec Sajovic, July 2022
"""

import unittest
import pandas as pd
from bmicalculator import create_app
from random import randint

# pylint: disable=C0301


class TestBmiCalcs(unittest.TestCase):
    """Holds tests for the BMI Calcs endpoints"""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app("prod")

    def test_do_bmi_magic_request_empty(self):
        """
        ...
        """

        with self.app.test_client() as c:
            rv = c.post(
                "/bmi/do-bmi-magic", json={}, content_type="application/json"
            )
            # json_data = rv.get_json()

        self.assertEqual(rv.status_code, 400)

    def test_do_bmi_magic_test_example(self):
        """
        ...
        """

        data = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
        ]

        with self.app.test_client() as c:
            rv = c.post(
                "/bmi/do-bmi-magic", json=data, content_type="application/json"
            )

            json_data = rv.get_json()

        df = pd.DataFrame(json_data["results"])

        self.assertEqual(rv.status_code, 200)
        self.assertListEqual(
            list(df["bmi"]),
            [
                32.83061454806607,
                32.79194475521777,
                23.76543209876543,
                22.49963710262738,
                31.11111111111111,
                29.402273297715947,
            ],
        )

    def test_do_bmi_magic_big_data(self):
        """
        This can also test the velocity of the function.
        Example: If the data size is set to 1M.
        """

        data_size = 1000

        data = []
        for _ in range(data_size):
            data.append(
                {
                    "Gender": "Male",
                    "HeightCm": randint(150, 200),
                    "WeightKg": randint(50, 130),
                }
            )

        with self.app.test_client() as c:
            rv = c.post(
                "/bmi/do-bmi-magic", json=data, content_type="application/json"
            )

            json_data = rv.get_json()

        df = pd.DataFrame(json_data["results"])

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(df.shape[0], data_size)
