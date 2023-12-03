FROM node:18.16-alpine as builder

WORKDIR /frontend

COPY . .

RUN npm install -g npm@8.12.1

RUN export NODE_OPTIONS=--max-old-space-size=9000

RUN npm install

RUN npx cross-env NODE_OPTIONS=--max-old-space-size=9000 webpack --env mode=production


FROM nginx:latest as production

COPY --from=builder frontend/dist /data/www/

COPY /nginx/www.solopharma.shop.crt /etc/nginx/www.solopharma.shop.crt

COPY /nginx/www.solopharma.shop.key /etc/nginx/www.solopharma.shop.key

COPY /nginx/devopsbyexample.conf /etc/nginx/conf.d/devopsbyexample.conf


CMD ["nginx", "-g", "daemon off;"]