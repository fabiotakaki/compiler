import os
from flask import Flask, request, render_template, jsonify
from lexical import Lexical
from syntatic import Syntatic
from file import File

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
  assert request.path == '/validate'
  assert request.method == 'POST'

  cr = Lexical(request.form['code'])
  lexical_result = cr.run()

  s = Syntatic(request.form['code'], cr.getTokens())
  syntatic_result = s.run()

  return jsonify({'code': request.form['code'], 'lexical_table': lexical_result, 'syntatic_result': syntatic_result})

@app.route('/validate_file', methods=['POST'])
def validate_file():
  assert request.path == '/validate_file'
  assert request.method == 'POST'
  file = request.files['file']
  new_file = File(file)
  if(new_file.upload()):
    result = new_file.validate() 
    return result
  else:
    return jsonify({'error': 'File Upload failed.'})