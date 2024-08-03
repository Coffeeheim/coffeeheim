PUID := $(shell id -u)
PGID := $(shell id -g)
CLIENT_ID := $(shell uname -n)

export CLIENT_ID
export PUID
export PGID

requirements:
	poetry export -f requirements.txt --output lambda-function/requirements.txt

up:
	CLIENT_ID=${CLIENT_ID} PUID=${PUID} PGID=${PGID} && \
	docker compose up -d --build

down:
	docker compose down