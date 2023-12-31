# LOG

I try to log all the steps I've done to get to the current state of the project

## Initializing environment

- Creating a virtual environment for developing, in the main directory of this project.
```
python3 -m virtualenv --prompt . venv
```

- Activate virtualenv
```
source venv/bin/activate
```

According to [Setuptools Documentation](https://setuptools.pypa.io/en/latest/index.html) pyproject.toml is the current way of creating a setup configuration for a python project. See [pyproject.toml](../pyproject.toml)

- Installing in venv and keep it editable
```
python3 -m pip install --editable .
```

## Running the application

Assuming the environment in `venv` is active

- Running the application in debug mode:
```
quart --app thijsj_simple_web:app --debug run
```

## Creating Docker image

Create [Dockerfile](../Dockerfile).

- Create a Docker image, using tag "simple-container-website:0.0.1"

```
docker build -t simple-container-website:0.0.1 .
```

- Tagging it with my Docker repository namespace "thijsj"
```
docker tag simple-container-website:0.0.1 thijsj/simple-container-website:0.0.1
```

- Push image to [my repository](https://hub.docker.com/repositories/thijsj)
```
docker push thijsj/simple-container-website:0.0.1
```

## Running

Starting this image on port 5000
```
docker run -d --name SCW -p 5000:8080 thijsj/simple-container-website:0.0.1
```




