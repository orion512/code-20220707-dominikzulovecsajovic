"""
Configuration file for the flask REST API
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base Config for API.
    """

    SOME_VARIABLE = os.getenv("ENV_VAR_NAME", "important string")
    DEBUG = 0

    BMI_BINS = [0, 18.4, 24.9, 29.9, 34.9, 39.9, 9999]
    BMI_CATEGORIES = [
        'Underweight',
        'Normal weight',
        'Overweight',
        'Moderately obese',
        'Severely obese',
        'Very severely obese',
    ]

    HEALTH_RISKS = [
        'Malnutrition risk',
        'Low risk',
        'Enhanced risk',
        'Medium risk',
        'High risk',
        'Very high risk',
    ]


class DevelopmentConfig(Config):
    """
    Development Config for API.
    """

    DEBUG = 1


class ProductionConfig(Config):
    """
    Production Config for API.
    """


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)
