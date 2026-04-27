#!/bin/bash

JS_IPA="/usr/share/ipa/ui/js"
PY_IPA="/usr/lib/python3.12/site-packages/ipaserver"

cp -r ./js/mailoptions $JS_IPA/plugins/
cp -r ./python/* $PY_IPA/plugins/

cd $PY_IPA/plugins/
python -m compileall mail*
python -O -m compileall mail*