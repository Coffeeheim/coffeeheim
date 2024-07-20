OS := $(shell uname)
PUID := $(shell id -u $(USER))
PGID := $(shell id -g $(USER))
CLIENT_ID := $(shell uname -n)

ifeq ($(OS), Darwin)
  FLUENTD_ADDRESS := docker.for.mac.localhost:24224
else
  FLUENTD_ADDRESS := localhost:24224
endif

export FLUENTD_ADDRESS
export CLIENT_ID
export PUID
export PGID

requirements:
	poetry export -f requirements.txt --output api/requirements.txt

deploy:
	sam build --use-container && sam deploy

up:
	FLUENTD_ADDRESS=${FLUENTD_ADDRESS} CLIENT_ID=${CLIENT_ID} PUID=${PUID} PGID=${PGID} && \
	docker compose up -d --build

down:
	docker compose down