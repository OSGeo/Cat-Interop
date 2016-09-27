# -*- coding: ISO-8859-15 -*-
###################################################################
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
###################################################################

from flask import abort, Flask, redirect, Response

from model import Vocabulary

APP = Flask(__name__)

VOCAB = Vocabulary()


@APP.route('/')
@APP.route('/vocab/')
def index():
    """return json of entire vocabulary"""

    return Response(VOCAB.dumps(), mimetype='application/json')


@APP.route('/vocab/<resource_type>/')
def resolve_resource_type(resource_type):
    """resolve a given vocabulary resource type"""

    if resource_type not in ['service', 'data']:
        abort(404)

    url = 'http://osgeo.org/vocab/%s' % resource_type
    members = VOCAB.filter(url)

    return Response(VOCAB.dumps(data=members), mimetype='application/json')


@APP.route('/vocab/<resource_type>/<provider>/')
def resolve_resource_type_provider(resource_type, provider):
    """resolve a given vocabulary resource type and provider"""

    url = 'http://osgeo.org/vocab/%s/%s' % (resource_type, provider)
    members = VOCAB.filter(url)

    return Response(VOCAB.dumps(data=members), mimetype='application/json')


@APP.route('/vocab/<resource_type>/<provider>/<identifier>/<version>')
def resolve_vocab_member(provider, resource_type, identifier, version):
    """resolve a given vocabulary member"""

    url = 'http://osgeo.org/vocab/%s' % '/'.join([resource_type, provider,
                                                  identifier, version])

    # check if the link_type exists:
    for link in VOCAB.json:
        if link['link_type'] == url:
            return redirect(link['redirect'])

if __name__ == '__main__':  # run locally, for fun
    APP.run(host='0.0.0.0', port=8000, use_reloader=True, debug=True)
