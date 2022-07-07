"""
Main Flask App

Author: Dominik Zulovec Sajovic - July 2022
"""


import logging
from flask import Flask

from bmicalculator.api.endpoints.bmi_calcs import bmi_api
from bmicalculator.api.settings import config_by_name


def create_app(config_name: str) -> Flask:
    """
    Creates the flask api.
    """

    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    app.register_blueprint(bmi_api, url_prefix="/bmi")

    # Setup the logger
    app.logger.handlers[0].setFormatter(
        logging.Formatter(
            "%(levelname)s\t"
            "%(asctime)s\t"
            "%(name)s\t"
            "%(process)s\t"
            "%(pathname)s:%(lineno)d\t"
            "%(message)s"
        )
    )

    if app.config["DEBUG"]:
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)

    app.logger.info(f"BMI API started - {config_name}!")
    app.logger.debug("WE ARE IN DEBUG MODE!!!!!")

    return app
