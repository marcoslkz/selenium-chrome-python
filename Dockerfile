FROM python:alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

COPY requirements.txt .
RUN pip install --upgrade pip && pip install selenium && pip install -r requirements.txt

#COPY app/* /$APP_HOME # volume by compose
#CMD tail -f /dev/null
CMD python3 app/main.py
