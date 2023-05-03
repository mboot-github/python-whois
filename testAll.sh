#! /usr/bin/env bash

# test all known tld's and produce output on file 1
# stderr goes to 2, that should be empty at the end

# in 1 we expect Quota exeptions and a few parsing errors if there is no output
# naturally also the privateRegistry entries will appear
# and if a query takes more then 30 seconds we show a timeout error

# the errors are listed at the end of the run so
# you can start from the end of the file to look for unexpected issues

# all tld's that produce no output (None), we also show the raw try data

./test3.py -V | tee 1
./test3.py -a 2>2 | tee -a 1
