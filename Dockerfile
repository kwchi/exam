FROM alpine

RUN apk add --update python3

COPY . /app

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]