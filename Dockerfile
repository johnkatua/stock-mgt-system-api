
FROM python:3.11


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY .  /code/

EXPOSE 8081


CMD ["python", "main.py"]