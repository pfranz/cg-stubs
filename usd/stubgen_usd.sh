#!/bin/bash

set -e

# version=5

#setpkg -c python-3 mari-$version

# can't activate
#. .venv-py37-linux/bin/activate


REPO_PATH=$(git rev-parse --show-toplevel)

MYPY_ROOT=$REPO_PATH/../mypy
USD_BUILD_ROOT=~/dev/USD/.build-py-sigs
USD_SOURCE_ROOT=~/dev/USD_private_chadrik
export USD_XML_INDEX="${USD_BUILD_ROOT}/docs/doxy_xml/index.xml"
export PYTHONPATH=$REPO_PATH:$REPO_PATH/usd:$MYPY_ROOT:$USD_BUILD_ROOT/lib/python:$USD_SOURCE_ROOT/docs/python

outdir=$REPO_PATH/usd/stubs/

# USD is a mixture of pure python (e.g. pxr.Sdf.__init__) and extension modules (pxr.Sdf._sdf), and 
# the __init__ modules do runtime injection, so parsing these modules produces bad results..
python3 -c "import stubgen_usd;stubgen_usd.main('$outdir')"

rm $outdir/pxr/*/_[a-z]*.pyi
rm $outdir/pxr/*/__DOC.pyi
# mv .out/* $outdir/