FROM python:3.10.1-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update \
  && apt-get -y install netcat gcc \ 
  && apt-get -y install nano \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./services/users/entrypoint.sh /usr/src/app/entrypoint.sh
RUN echo "export PYTHONPATH=/usr/src/app:${PYTHONPATH}" >> /root/.bashrc

COPY ./services/users /usr/src/app
CMD ["./entrypoint.sh"]