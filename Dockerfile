FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir cryptography pycryptodome pyaes

EXPOSE 8443

CMD ["python3", "mtprotoproxy.py"]
