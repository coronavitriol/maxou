# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:58:36 2020

@author: minimilien
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from joblib import dump, load

def analyse(phrase):
    analyser = load('analyser.joblib')
    var=analyser.polarity_scores(phrase)
    print("Negative score :",var['neg'])
    print("Positive score :",var['pos'])
    print("Neutral score :",var['neu'])
    vals={var['neg']:'Negative',var['pos']:"Positive",var['neu']:"Neutral"}
    cols={var['neg']:'#BF4C50',var['pos']:"#39c02f",var['neu']:"#000"}
    sentiment=vals[max(var['neg'],var['pos'],var['neu'])],
    color=cols[max(var['neg'],var['pos'],var['neu'])]
    return sentiment,color

def create_model():
    analyser = SentimentIntensityAnalyzer()
    dump(analyser, 'analyser.joblib')