FROM debian:stable

ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get update
RUN apt-get install -y nginx php php-fpm

# Nginx config
RUN rm /etc/nginx/sites-enabled/default
ADD src/config/opentodo.conf   /etc/nginx/sites-available/opentodo.conf
ADD src/config/fastcgi_params   /etc/nginx/fastcgi_params
RUN mkdir -p /var/www/opentodo/
RUN mkdir /run/php/
RUN chown www-data.www-data /run/php/
#ADD src/opentodo /var/www/opentodo
RUN ln -s /etc/nginx/sites-available/opentodo.conf /etc/nginx/sites-enabled/opentodo.conf

# Clean temp files
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Define default command.
CMD /usr/sbin/nginx && /usr/sbin/php-fpm7.0 -F

# Expose ports.
EXPOSE 80
