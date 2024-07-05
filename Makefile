deploy:
	poetry export -f requirements.txt --output api/requirements.txt && \
	sam build && \
	sam deploy

up:
	docker compose up -d --build

down:
	docker compose down