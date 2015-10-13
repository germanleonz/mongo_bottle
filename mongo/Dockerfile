FROM ubuntu:latest
MAINTAINER German Leon <germanleonz@gmail.com>
# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list
# Update apt-get sources AND install MongoDB
RUN apt-get update -y && apt-get install -y mongodb-org
# Create the MongoDB data directory
RUN mkdir -p /data/db
# Expose port 27017
EXPOSE 27017
# Entrypoint
ENTRYPOINT ["/usr/bin/mongod", "--smallfiles"]
