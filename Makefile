run:
	docker-compose up

push:
	black .
	python -m pytest .	
	docker buildx build --platform linux/arm -t derogativ/powered:1.3 --push .

test:
	black .
	mypy .
	python -m pytest .
