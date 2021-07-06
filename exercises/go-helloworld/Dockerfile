FROM golang:alpine
LABEL maintainer="Fatima-Ezzahra OUHMID"

WORKDIR /go/src/app

ADD . .

RUN go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]

