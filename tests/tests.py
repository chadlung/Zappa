import glob
import os
import re
import string
import sys
import unittest

import nose
from nose import case
from nose.pyversion import unbound_method
from nose import util

from zappa.wsgi import create_wsgi_request
from zappa.zappa import Zappa


class TestZappa(unittest.TestCase):
    ##
    # Sanity Tests
    ##

    def test_test(self):
        self.assertTrue(True)
    ##
    # Basic Tests
    ##

    def test_zappa(self):
        self.assertTrue(True)
        z = Zappa()

    def test_create_lambda_package(self):
        self.assertTrue(True)
        z = Zappa()
        path = z.create_lambda_zip()
        self.assertTrue(os.path.isfile(path))
        os.remove(path)
    ##
    # WSGI
    ##

    def test_wsgi_event(self):

        event = {
            "body": {},
            "headers": {
                "Via": "1.1 e604e934e9195aaf3e36195adbcb3e18.cloudfront.net (CloudFront)",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Forwarded-Proto": "https",
                "X-Forwarded-For": "109.81.209.118, 216.137.58.43",
                "CloudFront-Viewer-Country": "CZ",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "X-Forwarded-Proto": "https",
                "X-Amz-Cf-Id": "LZeP_TZxBgkDt56slNUr_H9CHu1Us5cqhmRSswOh1_3dEGpks5uW-g==",
                "CloudFront-Is-Tablet-Viewer": "false",
                "X-Forwarded-Port": "443",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-Desktop-Viewer": "true"
            },
            "params": {
                "a_path": "asdf1",
                "b_path": "asdf2",
            },
            "method": "GET",
            "query": {
                "dead": "beef"
            }
        }
        request = create_wsgi_request(event)

if __name__ == '__main__':
    unittest.main()
