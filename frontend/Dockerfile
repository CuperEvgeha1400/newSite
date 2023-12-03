FROM node:18.16-alpine as builder

WORKDIR /usr/src/app

COPY ./package.json .
COPY ./package-lock.json .

COPY . .

RUN npm install -g npm@8.12.1

RUN export NODE_OPTIONS=--max-old-space-size=9000

RUN npm install

RUN npm run build:prod

