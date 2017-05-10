.PHONY: test clean run

test:
	python src/test.py	

clean:
	find . -name '*.pyc' -exec rm --force {} +

run:
	python src/app.py
