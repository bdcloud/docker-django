FROM bdcloud/python2-base

MAINTAINER james tang <jamess@126.com> 


# Local directory with project source
ENV DOCKER_SRC=admincloud
# Directory in container for all project files
ENV DOCKER_HOME=/root
# Directory in container for project source files
ENV DOCKER_PROJECT=/root/project
ENV DOCKER_CONFIG=/root/config

# Create application subdirectories
WORKDIR $DOCKER_HOME
RUN mkdir media static

VOLUME ["$DOCKER_HOME/media/"]

RUN apt-get install -y nginx gcc
RUN apt-get install -y  --no-install-recommends cron
RUN pip install --upgrade pip

# Install required packages and remove the apt packages cache when done.

ADD ./config/nginx.conf /etc/nginx/

WORKDIR $DOCKER_CONFIG
COPY ./config  ./
RUN pip install -r requirements.txt
RUN pip install kafka-python

ENV KAFKA_VERSION 2.11-2.0.0

ADD kafka_$KAFKA_VERSION.tar /opt
RUN mv /opt/kafka_$KAFKA_VERSION /opt/kafka

COPY ./project  /root/project


EXPOSE 8000

RUN chmod u+x start_script

ADD ./kafka_cron.sh /root/cron/
#ADD ./crontabfile /root/

#RUN crontab /root/crontabfile

#RUN cp /root/crontabfile /etc/crontab

#RUN chmod 0644 /etc/cron.d/kafka-cron

ENTRYPOINT ["./start_script"]

