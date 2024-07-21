import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
Token='7a8f6695efee737227dc709b16779ae5' 
Header={'Content-Type' :'application/json', 'trainer_token':Token} 
Trainer_id='4440'



def test_status_code():
    response=requests.get(url=f'{URL}/trainers')
    assert response.status_code==200
    
def test_imya():
    response_get=requests.get(url=f'{URL}/trainers',params={'trainer_id':Trainer_id})
    assert response_get.json()["data"][0]["trainer_name"]=='Serennja'
