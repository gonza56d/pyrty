FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
	# psycopg2 dependencies
	&& apk add --virtual build-deps gcc python3-dev musl-dev \
	&& apk add postgresql-dev \
	# Pillow dependencies
	&& apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
	# Translation dependencies
	&& apk add gettext \
	# CFFI dependencies
	&& apk add libffi-dev py-cffi \
	&& apk add --no-cache openssl-dev libffi-dev \
	&& apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/