#!/bin/sh

HERE=$PWD
BUILD_DIR=$HERE/build
LATEX_TEMPLATE=article

#!TODO: replace http://raw.github.com/SciTools/courses/master/course_content/

pushd $BUILD_DIR
for nb in $HERE/*.ipynb
do
    ipython nbconvert --to=latex --template=$LATEX_TEMPLATE --post=pdf $nb
done
