FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-uvloop python3-socks python3-cryptography

WORKDIR /app

COPY mtprotoproxy.py config.py /app/

USER nobody

EXPOSE 8443

CMD ["python3", "mtprotoproxy.py"]
