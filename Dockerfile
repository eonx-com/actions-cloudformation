FROM ubuntu:18.04

RUN apt update; \
    apt install -y \
        python3 \
        python3-pip \
        python3-venv;

COPY build /tmp/actions-cloudformation

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
