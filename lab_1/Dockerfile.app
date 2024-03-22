ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

ADD ./wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

WORKDIR /app
COPY ./app /app

RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 cache purge

CMD ["/usr/local/bin/wait-for-it.sh", "db:5432", "--", "python", "app.py"]