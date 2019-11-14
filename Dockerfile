FROM ubuntu:18.04

RUN apt update; \
    apt install -y \
        python3 \
        python3-pip \
        python3-venv;

COPY build /tmp/actions-cloudformation

RUN cd /tmp/actions-cloudformation; \
    python3 -m venv ./venv; \
    source ./venv/bin/activate; \
    pip3 install --upgrade pip3; \
    pip3 install -r ./requirements.txt;

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
