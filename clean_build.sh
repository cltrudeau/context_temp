#!/bin/bash

version=`grep "__version__ = " context_temp.py | cut -d "'" -f 2`

git tag "$version"

if [ "$?" != "0" ] ; then
    exit $?
fi

rm -rf build
rm -rf dist
python setup.py sdist
python setup.py bdist_wheel

echo "------------------------"
echo
echo "now do:"
echo "   twine upload dist/*"
echo
