FROM node:20.8.0-alpine3.17
WORKDIR /backend
COPY . .
RUN npm install -g npm@8.12.1
RUN npm install

CMD ["npm", "run", "start:json"]
