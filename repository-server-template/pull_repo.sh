#!/usr/bin/env sh
service nginx start && service cron start
cd /var/www/html && git clone https://github.com/bluemiaomiao/jjvmm-repo.git
echo '*/5 * * * * root cd /var/www/html && git clone https://github.com/bluemiaomiao/jjvmm-repo.git' >> /etc/crontab
tail -f /dev/null