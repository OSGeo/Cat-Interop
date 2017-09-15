# -*- coding: ISO-8859-15 -*-
# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2014 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import os
import shutil
from urllib2 import urlopen

from paver.easy import Bunch, cmdopts, options, path, task


options(
    app=Bunch(
        home=path('app'),
        voc='https://raw.githubusercontent.com/OSGeo/Cat-Interop/%s/LinkPropertyLookupTable.csv',  # noqa
        build=path('app/build'),
        version=open('VERSION.txt').read().strip()
    )
)


@task
def setup():
    """setup install"""

    if not os.path.exists(options.app.build):
        options.app.build.mkdir()
    if not os.path.exists(options.app.build / 'LinkPropertyLookupTable.csv'):
        if options.app.version.endswith('-dev'):  # master
            url = options.app.voc % 'master'
        else:
            url = options.app.voc % options.app.version
        file_ = options.app.build / 'LinkPropertyLookupTable.csv'
        with open(file_, 'w') as fileobj:
            fileobj.write(urlopen(url).read())


@task
def clean():
    """return to pristine state"""

    if os.path.exists(options.app.build):
        shutil.rmtree(options.app.build)


@task
@cmdopts([
    ('venv=', 'v', 'path to virtual environment'),
])
def deploy():
    """deploy install"""

    venv = options.get('venv', None)
    if venv is None:
        raise ValueError('path to virtual environment required')
    venv = os.path.abspath(venv)

    loc = [
        'import sys',
        'sys.path.insert(0, "%s/app")' % venv,
        'activate = "%s/bin/activate_this.py"' % venv,
        'execfile(activate_this, {__file__: activate})',
        'from app import APP as application'
    ]

    with open(options.app.build / 'vocab.wsgi', 'w') as fileobj:
        fileobj.write('\n'.join(loc))

    loc = [
        'WSGIDaemonProcess vocab user=user1 group=group1 threads=5',
        'WSGIScriptAlias /vocab %s' % options.app.home,
        '<Directory %s>' % path(venv),
        ' WSGIProcessGroup vocab',
        ' WSGIApplicationGroup %{GLOBAL}',
        ' Order deny,allow',
        ' Allow from all',
        '</Directory>']

    with open(options.app.build / 'osgeo.vocab.conf', 'w') as fileobj:
        fileobj.write('\n'.join(loc))
