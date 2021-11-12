FROM python:2.7-alpine AS base

RUN apk add openssh gcc openssl-dev musl-dev libffi-dev
RUN apk add git

ARG SSH_PRIV_KEY
RUN echo ${SSH_PRIV_KEY}
RUN mkdir -p /root/.ssh
RUN echo "${SSH_PRIV_KEY}" | base64 -d > /root/.ssh/id_rsa
RUN chmod 400 /root/.ssh/id_rsa
RUN ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts

WORKDIR /usr/local/lib/python2.7
RUN pip install -e git+git@github.com:walterbrunetti/docker_in_tha_house.git@master

FROM python:2.7-alpine

COPY --from=base /etc /etc
COPY --from=base /bin /bin
COPY --from=base /sbin /sbin
COPY --from=base /usr /usr
COPY --from=base /lib /lib

COPY . .

WORKDIR /app

COPY . .

CMD tox
