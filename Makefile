requirements:
	poetry export -f requirements.txt --output api/requirements.txt

deploy:
	sam build && sam deploy

up:
	docker compose up -d --build

down:
	docker compose down