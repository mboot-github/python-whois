

all: reformat test build testwhl

reformat:
	./reformat-code.sh

test:
	./test2.py -d google.com

build:
	python -m build
	tar tvf dist/*.tar.gz

testwhl:
	./testwhl.sh 2>2 | tee 1
