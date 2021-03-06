import os, pandas as pd

def test_string():
    abc = 'Test'
    assert abc == 'Test'

def test_if_data_exits():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') != True

def test_if_model_exits():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') != True
    
def test_accuracy_score():
    df = pd.read_csv('metrics.csv')
    print((df['accuracy']>0.70))
    assert (df['accuracy']>0.70).unique() == True
