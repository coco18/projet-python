#!bin/bash
rm -R doc
mkdir doc
for x in $(find * -type d -prune)
do
    pydoc -w $x/*.py
done
mv ./*.html -t ./doc
