import os
from werkzeug import secure_filename
from lexical import Lexical
from collections import deque
from flask import jsonify

class File:
  def __init__(self, file):
    self.allowed_extensions = set(['txt'])
    self.upload_folder = 'flask_compiler/uploads/'
    self.file = file

  def allowed_file(self):
    return '.' in self.file.filename and self.file.filename.rsplit('.', 1)[1] in self.allowed_extensions

  def upload(self):
    if self.file and self.allowed_file():
      filename = secure_filename(self.file.filename)
      self.filename = filename
      self.file.save(os.path.join(self.upload_folder, filename))
      return True
    else:
      return False

  def validate(self):
    with open(self.upload_folder+self.filename, "r") as file:
      code = file.read()
      cr = Lexical(code)
      result = cr.run()
      return jsonify({'code': code, 'lexical_table': result[0], 'syntatic_result': result[1]})