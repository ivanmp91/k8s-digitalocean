DOCKER_IMAGE := do-sticky-floating-ip
DOCKER_REGISTRY := ivanmp91

.PHONY: build test push


build:
	docker build --no-cache . -t $(DOCKER_IMAGE)

test:
	docker run -t -i $(DOCKER_IMAGE) /app/sticky-floating-ip.py --help

push:
	docker tag $(DOCKER_IMAGE) $(DOCKER_REGISTRY)/$(DOCKER_IMAGE)
	docker push $(DOCKER_REGISTRY)/$(DOCKER_IMAGE)
