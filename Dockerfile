FROM python:3.11-slim

RUN mkdir /odoo

WORKDIR /odoo

COPY 17.0/requirements.txt /odoo

RUN pip install -r requirements.txt

COPY . /odoo/

EXPOSE 8000 8072

ENTRYPOINT [ "/bin/sh", "-c", "bash startup.sh" ]
