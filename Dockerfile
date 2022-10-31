FROM python:3.10
ADD . /deploy
WORKDIR /deploy
RUN pip install -r requirements.txt
CMD python app.py