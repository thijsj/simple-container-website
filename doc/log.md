# LOG

I try to log all the steps I've done to get to the current state of the project

## Initializing environment

Creating a virtual environment for developing, in the main directory of this project.
$ `python3 -m virtualenv --prompt . venv`

Activate virtualenv
$ `source venv/bin/activate`

According to [Setuptools Documentation](https://setuptools.pypa.io/en/latest/index.html) pyproject.toml is the current way of creating a setup configuration for a python project. See [pyproject.toml](../pyproject.toml)

Installing in venv and keep it editable

$ `python3 -m pip install --editable .`
