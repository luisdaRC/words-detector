FROM python:3.7.9-slim

COPY find_words_trie.py /
COPY trie.py /

RUN apt-get update

RUN apt-get -y install libenchant1c2a
RUN pip install --upgrade pip && \
    pip install boto3 && \
    pip install boto && \
    pip install pyenchant
    pip install nltk

RUN python -c 'import nltk; nltk.download("words")'

CMD ["python","find_words_trie.py"]
