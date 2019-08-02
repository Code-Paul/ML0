### CodePaul - https://www.codepaul.herokuapp.com

import os

### make sure a python3 environment is installed on your system
print("Automated installation of pipenv and the required packages...\nMay require a few minutes depending upon your system capacity and internet speed.")
### create a pipenv (pipenv creates a virtual environment which isolates the environment from the rest of the system)
os.system("pip install pipenv")
os.environ['PIPENV_VENV_IN_PROJECT'] = '1'
# create a virtual environment
os.system("pipenv --python 3 install -r requirements.txt")
os.system("pipenv shell")
