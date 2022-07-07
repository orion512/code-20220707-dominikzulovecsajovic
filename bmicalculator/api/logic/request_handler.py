"""
Module for handling incoming requests

This script handles the incoming requests.

Author: Dominik Zulovec Sajovic - July 2022
"""

from typing import Dict, Tuple
from flask import Request, current_app

from bmicalculator.api.logic.BMIWizard import BMIWizard

# pylint: disable=W0612


def handle_bmi_request(req: Request) -> Tuple[Dict, int]:
    """The main function that handles the entire bmi magic request"""

    current_app.logger.debug("Entering function handle_bmi_request")

    try:
        # 1. Init the wizard
        wiz = BMIWizard(req.json)

        # 2. wizard performs magic
        wiz.perform_magic(
            current_app.config["BMI_BINS"],
            current_app.config["BMI_CATEGORIES"],
            current_app.config["HEALTH_RISKS"],
        )

        # 3. get the results
        res = wiz.get_results()
        ow = wiz.count_overweight()

        return {"results": res, "overweight_count": ow}, 200

    except Exception as err:
        current_app.logger.error(err)
        raise err


if __name__ == "__main__":
    pass
