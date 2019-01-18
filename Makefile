.PHONY: build test push

build:
	docker-compose build

test:
	docker run -t -i ivanmp91/do-sticky-floating-ip /app/sticky-floating-ip.py --help

push:
	docker-compose push
