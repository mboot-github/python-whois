#! /usr/bin/env bash

ENV="tmp/t1"

mkdir -p tmp
rm -rf tmp/t1
python3 -m venv ${ENV}
source ./${ENV}/bin/activate
pip3 install dist/*.whl

python testwhl.py
