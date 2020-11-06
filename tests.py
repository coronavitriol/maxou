# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:47:30 2020

@author: minimilien
"""

import requests
import os


def test1():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://localhost:5000/RAM', json=dictToSend)
    print ('response from server:',res.text)
    print(res)

def test2():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://localhost:5000/sfggd', json=dictToSend)
    print ('response from server:',res.text)
    print(res)


def test3():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://localhost:5000/horloge', json=dictToSend)
    print('response from server:',res.text)
    print(res)

def test4():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://localhost:5000/sentiments', json=dictToSend)
    print('response from server:',res.text)
    print(res)

def test5():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://localhost:5000/presence', json=dictToSend)
    print('response from server:',res.text)
    print(res)

class Test:
    def __init__(self,test):
        self.name=test.__name__
        self.test=test
        self.validation=False
    def execution(self):
        try:
            self.test()
            self.validation=True
            print(self.name+' is completed.')
        except Exception as e:
            print(e)
            self.validation=False
            print(self.name+' has failed.')

def deploiement(*tests):
    print("Begining of the tests...")
    cpt=0
    for test in tests:
        cpt+=1
        print('Test {}/{}'.format(cpt,len(tests)))
        test_=Test(test)
        test_.execution()
        if test_.validation==False:       
            raise "échec"
    print("Let's upload the git...")
    print(os.popen('git commit -m "make it better"').read())
    print(os.popen('git push').read())
    print(os.popen('git push heroku master').read())
    return True

deploiement(test1,test2,test3,test4,test5)