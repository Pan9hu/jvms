FROM ubuntu:latest
COPY pull_repo.sh /pull_repo.sh
WORKDIR /
RUN apt update && apt upgrade -y && apt install nginx cron git -y && chmod a+x /pull_repo.sh
ENTRYPOINT ["/pull_repo.sh"]
CMD ["/bin/sh","-c"]