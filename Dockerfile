# start by pulling the python image
FROM python:3.8

COPY . /wwa

# switch working directory
WORKDIR /wwa

RUN pip3 install --upgrade setuptools pip &&\ pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
