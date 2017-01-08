init:
	pip install -r requirements.txt

test:
	py.test tests

docker:
	sudo docker build -t areth/crosssense-lserver .