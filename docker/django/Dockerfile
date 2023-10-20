FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
COPY docker/django/init_app.sh /app/init_app.sh
WORKDIR /app
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm requirements.txt \
    && chmod +x /app/init_app.sh

COPY . /app

ENTRYPOINT ["/bin/bash", "/app/init_app.sh"]
