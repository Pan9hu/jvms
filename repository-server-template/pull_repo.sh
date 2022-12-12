#!/usr/bin/env sh
service nginx start && service cron start
cd /var/www/html && git clone https://github.com/jjvmm-org/index.git && rm -rf index.nginx-debian.html && mv index/* .
cat > /etc/nginx/sites-enabled/default << EOF
server{
	server_name _;
	listen 80;
	root /var/www/html;
	index index.html index.htm index.json;
	location / {
		autoindex on;
	}
}
EOF
nginx -s reload
echo '*/5 * * * * root cd /var/www/html && git clone https://github.com/jjvmm-org/index.git && rm -rf index.nginx-debian.html && mv index/* .' >> /etc/crontab
tail -f /dev/null
