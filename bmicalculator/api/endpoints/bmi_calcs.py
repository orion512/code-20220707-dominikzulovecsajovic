"""
The Endpoints for BMI calculations

Author: Dominik Zulovec Sajovic - July 2022
"""

from typing import Dict, Tuple
from flask import request, current_app, Blueprint
from flask_pydantic import validate
from bmicalculator.api.logic.request_handler import handle_bmi_request
from bmicalculator.api.logic.data_checker import JsonChecker

bmi_api = Blueprint("api", __name__)


@bmi_api.route("/do-bmi-magic", methods=["POST"])
@validate(body=JsonChecker)
def do_bmi_magic() -> Tuple[Dict[str, str], int]:
    """ Endpoint for doing BMI magic """

    try:
        return handle_bmi_request(request)
    except Exception as err:
        current_app.logger.error(err)
        return {"error": "Internal Server Error!"}, 500
