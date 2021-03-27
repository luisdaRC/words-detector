FROM python:3.7

COPY find_words.py /

RUN apt-get update

RUN apt-get -y install libenchant1c2a
RUN pip install --upgrade pip && \
    pip install boto3 && \
    pip install boto && \
    pip install pyenchant

CMD ["python","find_words.py"]
