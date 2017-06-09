#!bin/bash
rm doc
mkdir doc
for x in $(find * -type d -prune)
do
    pydoc -w $x/*.py
    mv ./*.html -t ./doc
done
