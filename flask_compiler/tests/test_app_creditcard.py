import os
import flask_compiler
import unittest
import tempfile

class AppFlaskCompilerTestCase(unittest.TestCase):

  def setUp(self):
    flask_compiler.app.testing = True
    self.app = flask_compiler.app.test_client()

  # Valid credit card without hyphen
  def test_valid_cc_without_hyphen(self):
    rv = self.app.post('/validate', data=dict(creditcard='4123456789123456'))
    assert b'4123456789123456' in rv.data 
    assert b'true' in rv.data