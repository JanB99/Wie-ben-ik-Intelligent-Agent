# FROM node:15.1.0-alpine3.10 as build
 
# WORKDIR /client
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build
 
# FROM nginx:1.19.4-alpine as production
# COPY --from=build /client/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off"]

# FROM node:12

# # Create app directory
# WORKDIR /usr/src/app

# # Install app dependencies
# # A wildcard is used to ensure both package.json AND package-lock.json are copied
# # where available (npm@5+)
# COPY package*.json ./

# RUN npm install
# # If you are building your code for production
# # RUN npm ci --only=production

# # Bundle app source
# COPY . .

# EXPOSE 8080
# CMD ["npm", "run", "serve"]

FROM node:lts-alpine
# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]