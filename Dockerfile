FROM python:3-alpine

# Setup the Python script that will compile the CloudFromation output from Jinja2 templates

COPY build /tmp/actions-cloudformation

RUN cd /tmp/actions-cloudformation; \
    python3 -m venv ./venv; \
    source ./venv/bin/activate; \
    pip3 install --upgrade pip3; \
    pip3 install -r ./requirements.txt;

# Configure Docker entrypoint

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
