# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:52:48 2020

@author: minimilien
"""

from AI import analyse
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for,make_response
import webbrowser
from config import Projet,Version
from datetime import datetime
import psutil

def my_open(file_adresse): # give the content of a file
    file = open(file_adresse, 'r', encoding='utf-8', errors='replace')
    text = file.read()
    file.close()
    return text

def my_write(file_adresse, text, add = True): # save a content in a file
    file = open(file_adresse, 'a' if add else 'w')
    file.write(text)
    file.close()

filename = 'static/storage.txt'

app = Flask(__name__)




@app.route('/')
def index():
    print(request.remote_addr)
    return render_template('index.html',
                        Projet=Projet,
                        Version=Version
                        )



@app.route('/horloge',methods=['GET', 'POST'])
def horloge():
    time=datetime.now()
    return jsonify(result=time.strftime("%H:%M:%S"))


@app.route('/RAM',methods=['GET', 'POST'])
def RAM():
    memoire_utilisee=dict(psutil.virtual_memory()._asdict())['percent']
    return jsonify(result="{}%".format(memoire_utilisee))

@app.route('/sentiments')
def sentiments():
    phrase = request.args.get('phrase', 0, type=str)
    my_write(filename, phrase + '\n')
    sentiment,color=analyse(phrase)
    return jsonify(result=sentiment,
                   color=color,
                   )


@app.route('/',methods=['GET', 'POST'])
def submit():
    print('X'*1000)
    sentiment,color=analyse('happy')
    return send_file(filename, as_attachment=True)

@app.errorhandler(405)
def method_not_allowed(e):
    print(request)
    print(request.remote_addr)
    print(request.form.to_dict())
    return jsonify(result={'info':"Non tu n'as pas le droit."})


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


@app.errorhandler(400)
def bad_request(e):
    print(request)
    return jsonify(result={'info':'Non.'})


if __name__ == '__main__':
    #webbrowser.open('http://127.0.0.1:5000/', new=2)
    print("Lancement de l'app")
    app.run(host='0.0.0.0',threaded=True)