docker_build:
	docker build . -t swsec-fastapi

docker_run:
	docker run --rm -p 9000:9000 --name test_fastapi swsec-fastapi:latest
