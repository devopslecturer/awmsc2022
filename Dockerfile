FROM python:3

COPY . /wwa

WORKDIR /wwa

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./app.py