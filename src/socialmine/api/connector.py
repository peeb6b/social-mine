'''
Created on 03/08/2012

@author: Dor
'''

from socialmine.orm import main
session = None

def connect():
    global session
    session = main.Session()
    
def is_connected():
    global session
    return session is not None