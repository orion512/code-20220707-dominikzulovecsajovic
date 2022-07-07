"""
Testing bmi calcs endpoint

Author: Dominik Zulovec Sajovic, July 2022
"""

import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from bmicalculator.api.logic.BMIWizard import BMIWizard
from random import randint

# pylint: disable=C0301


class TestBMIWizard(unittest.TestCase):
    """ Holds tests for the BMI Calcs endpoints """

    def test_calculate_bmi_correct_bmi(self):
        """
        ...
        """

        data = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
        ]

        wiz = BMIWizard(data)

        wiz._calculate_bmi()

        self.assertListEqual(
            list(wiz.df_data['bmi']),
            [32.83061454806607, 32.79194475521777, 23.76543209876543, 
            22.49963710262738, 31.11111111111111, 29.402273297715947]
            )


    def test_calculate_bmi_df_created(self):
        """
        ...
        """

        data = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
        ]

        wiz = BMIWizard(data)

        assert_frame_equal(wiz.df_data, pd.DataFrame(data))
