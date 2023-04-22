FROM python:3.9.16-bullseye

WORKDIR /python-flask

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
