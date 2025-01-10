# Use an official Node.js runtime as a parent image
FROM node:21.1.0

WORKDIR /app

COPY ./translator_client/package*.json ./

RUN npm install

COPY ./translator_client .

# Build the Next.js application in production mode
# RUN npm run build