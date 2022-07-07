"""
Module BMI operations

Author: Dominik Zulovec Sajovic - July 2022
"""

import pandas as pd

from typing import List, Dict, Union, Optional
from dataclasses import dataclass, field


@dataclass
class BMIWizard:
    """
    BMI Wizard class to perform BMI magic.
    """

    req_data: List[Dict[str, Union[str, float]]]
    df_data: Optional[pd.DataFrame] = field(init=False)

    def __post_init__(self):
        """After initialisation we create a data frame for vectorisation"""
        self.df_data = pd.DataFrame(self.req_data)

    def perform_magic(
        self, bins: List[float], bmi_labels: List[str], hr_labels: List[str]
    ) -> None:
        """
        This function calculates the bmi and assigns all the related
        labels based on the api.
        """
        self._calculate_bmi()
        self._assign_labels("bmi_category", bins, bmi_labels)
        self._assign_labels("health_risk", bins, hr_labels)

    def count_overweight(self) -> None:
        """
        This function counts the number of overweight people in the data.
        """
        return self.df_data[self.df_data.bmi_category == "Overweight"].shape[0]

    def get_num_by_category(self, cat: str) -> int:
        """..."""

        if "bmi_category" not in self.df_data.columns:
            raise ValueError(
                "This function can only be called if the bmi_category"
                "field has already been calculated. "
                "Try calling the _assign_bmi_category function first."
            )

        return self.df_data[self.df_data.bmi_category == cat].shape[0]

    def get_results(self, as_df: bool = False) -> Union[pd.DataFrame, Dict]:
        """Retrieves the data"""
        if as_df:
            return self.df_data
        else:
            return self.df_data.to_dict("records")

    def _calculate_bmi(self) -> None:
        """
        BMI(kg/m2) = mass(kg) / height(m)2
        The BMI (Body Mass Index) in (kg/m2) is equal to the weight in
        kilograms (kg) divided by your height in meters squared (m)2.
        For example, if you are 175cm (1.75m) in height and 75kg in weight,
        you can calculate your BMI as follows: 75kg / (1.75m2) = 24.49kg/m2
        """

        bmi = self.df_data.WeightKg / (self.df_data.HeightCm / 100) ** 2
        self.df_data["bmi"] = bmi

    def _assign_labels(
        self, col: str, bins: List[float], labels: List[str]
    ) -> None:
        """Assigns a label to a new column based on the bmi"""

        if "bmi" not in self.df_data.columns:
            raise ValueError(
                "This function can only be called if the bmi field has "
                "already been calculated. "
                "Try calling the _calculate_bmi function first."
            )

        self.df_data[col] = pd.cut(
            x=self.df_data["bmi"], bins=bins, labels=labels
        )


if __name__ == "__main__":
    pass
