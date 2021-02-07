FROM nginx:latest

COPY index.html /usr/share/nginx/html
COPY dist/ /usr/share/nginx/html/dist

RUN chmod +r /usr/share/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;"]