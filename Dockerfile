FROM python:3.9

WORKDIR /fastapi-tuto-2

COPY ./requirements.txt /blog/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi-tuto-2/requirements.txt

COPY ./blog /fastapi-tuto-2/blog

RUN ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "80"]