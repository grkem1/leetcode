#!/usr/bin/env bash

# take only one accepted solution from each directory

cd "src"
dir="$(pwd)"
for i in $(ls); do
	cd $i
	find . -iname "*.py"  -exec mv {} . \;
	find . -iname "*.c"   -exec mv {} . \;
	find . -iname "*.cpp" -exec mv {} . \;
	find . -iname "*.js"  -exec mv {} . \;
	find . -type d -exec rm -r {} \;
	cd $dir
done
