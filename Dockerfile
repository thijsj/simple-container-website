#

FROM python:3.10-slim
LABEL maintainer="Thijs Janssen (https://github.com/thijsj)"
COPY . /src
WORKDIR /src
RUN python3 -m pip install --editable .
EXPOSE 8080
ENTRYPOINT ["hypercorn", "-b", "0.0.0.0:8080", "thijsj_simple_web:app"]
