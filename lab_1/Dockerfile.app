ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

ADD ./wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

WORKDIR /app
COPY ./app /app

RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 cache purge
 
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

CMD ["/usr/local/bin/wait-for-it.sh", "db:5432", "--", "python", "app.py"]