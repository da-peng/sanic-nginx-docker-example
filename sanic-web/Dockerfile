FROM python:3


WORKDIR /usr/src/sanic-web
# code-folder
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD bash -c "cd /usr/src/sanic-web && gunicorn server:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker"