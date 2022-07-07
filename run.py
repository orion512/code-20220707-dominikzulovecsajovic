"""
Flask Script Entry Point
"""

import os
from bmicalculator import create_app


application = create_app(os.getenv("BOILERPLATE_ENV") or "dev")

if __name__ == "__main__":
    application.run()
