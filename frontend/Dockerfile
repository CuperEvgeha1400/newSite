FROM node:18.16-alpine as builder

WORKDIR /frontend

COPY . .

RUN npm install -g npm@8.12.1

RUN export NODE_OPTIONS=--max-old-space-size=900

RUN export BUILD_PATH='/frontend/dist'

RUN npm install

RUN npm run build:prod

