FROM python:3.6

MAINTAINER michael@buffer.com

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["crawler"]
