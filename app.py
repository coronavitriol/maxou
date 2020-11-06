# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:52:48 2020

@author: minimilien
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for,make_response
import webbrowser
from config import Projet,Version
from datetime import datetime
import psutil


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
    a = request.args.get('a', 0, type=str)
    analyser = SentimentIntensityAnalyzer()
    var=analyser.polarity_scores(a)
    print("Negative score :",var['neg'])
    print("Positive score :",var['pos'])
    print("Neutral score :",var['neu'])
    vals={var['neg']:'Negative',var['pos']:"Positive",var['neu']:"Neutral"}
    cols={var['neg']:'#BF4C50',var['pos']:"#39c02f",var['neu']:"#000"}
    return jsonify(result=vals[max(var['neg'],var['pos'],var['neu'])],
                   color=cols[max(var['neg'],var['pos'],var['neu'])],
                   )

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