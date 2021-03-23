FROM python:3.7

ADD test.py .

RUN apt-get update

RUN apt-get -y install libenchant1c2a

RUN python3 -m pip install pyenchant

CMD ["python","./test.py"]
