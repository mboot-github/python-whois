

all: reformat version build testwhl test_upload_pypi

reformat:
	./reformat-code.sh

test:
	./test2.py -t 2>2 | tee 1

build:
	rm -rf dist
	python -m build
	tar tvf dist/whois-$$( cat ./work/version ).tar.gz

testwhl:
	./testwhl.sh 2>2 | tee 1

version:
	mkdir -p work
	grep VERSION ./whois/version.py | awk '{ gsub(/"/, ""); print $$NF }' >./work/version
	cat ./work/version

test_upload_pypi:
	ls -l ./dist/*$$( cat ./work/version )*
	twine upload -r testpypi dist/whois-$$( cat ./work/version ).tar.gz dist/whois-$$( cat ./work/version )-py3-*.whl

upload_pypi:
	ls -l ./dist/*$$( cat ./work/version )*
	twine upload -r pypi dist/whois-$$( cat ./work/version ).tar.gz dist/whois-$$( cat ./work/version )-py3-*.whl
