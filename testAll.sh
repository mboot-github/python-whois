#! /usr/bin/env bash

# test all known tld's and produce output on file 1
# we expect Quota exeptions and a few parsing errors if there is no output
# the errrs are listed at the end of the run so
# you can start from the end of the file to look for unexpected issues

./test2.py -a 2>2 | tee 1
