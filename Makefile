run:
	black .
	docker buildx build --platform linux/arm -t derogativ/powered:1.0 --load .
	docker run derogativ/powered:1.0

push:
	black .
	python -m pytest .	
	docker buildx build --platform linux/arm -t derogativ/powered:1.0 --push .

test:
	python -m pytest .
