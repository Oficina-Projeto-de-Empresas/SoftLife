FROM python:3.9.7-slim-buster
WORKDIR /app

COPY requirements.txt ./
COPY setup.py entrypoint.sh ./
COPY migrations migrations
COPY SoftLife SoftLife

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8

EXPOSE 5000
CMD ["./entrypoint.sh"]