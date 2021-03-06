# Python BMI Calculator API #
 
This is the code repository for the:
- backend (api) part of the Python BMI Calculator

When the code is deployed it stands as a REST API with 1 endpoint.
```
http://hostname/bmi/do-bmi-magic
```
The endpoint accepts a POST request and data in the below format:
```
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
```
 
## How do I get it set up? ###

### Dev Env
 
* Setup the python env
```
# activate an already existing virtual environment
source venv/bin/activate

# create a new virtual env
python -m venv venv
```
* install the required packages
```
pip install -r requirements.txt
```
* Run flask app (dev)
```
export FLASK_APP=run
flask run
```

## Build
The project currently has a very simple github build:
- installs dependencies
- lints with flake 8
- runs unittest


## Running Unit Tests ###

```
python -m unittest discover
```
