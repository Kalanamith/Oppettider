FROM alpine:3.9
WORKDIR /app
COPY . /app
RUN apk update && apk add build-base python3 python3-dev --no-cache bash &&  \
    pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.python.org --no-cache-dir -e.

EXPOSE 5000

ENTRYPOINT ["sh","./scripts/run.sh"]