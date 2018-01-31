#
# execution_control/master_controller/rpyc/Dockerfile
#
FROM python:3.6-alpine3.6
LABEL maintainer="Benjamin Mort <ben.mort@gmail.com>"

# Copy python requirements file
COPY requirements.txt /app/requirements.txt

RUN apk update && \
    pip install --no-cache-dir  -r /app/requirements.txt && \
    find /usr/local/lib/python3.6/ -name 'tests' -exec rm -r '{}' + && \
    rm -r /root/.cache

# RPyC service endpoint
EXPOSE 5000

# Working directory
WORKDIR /app

# Copy code to container working directory
COPY . /app/master_controller

# Container healthcheck command
HEALTHCHECK --interval=10s --timeout=1s --start-period=5s --retries=3 \
    CMD python3 master_controller/check_health_client.py localhost 5000 \
    || exit 1

# Entrypoint (command that is run by default)
ENTRYPOINT ["python3", "master_controller/app.py"]
