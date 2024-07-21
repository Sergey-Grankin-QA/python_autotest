import requests

URL='https://api.pokemonbattle.ru/v2'
Token='7a8f6695efee737227dc709b16779ae5' 
Header={'Content-Type' :'application/json', 'trainer_token':Token} 
Body_POST_pokemons={
    "name": "generate",
    "photo_id": -1
    
    }

Body_PUT_pokemons={
    "pokemon_id": "44439",
    "name": "Rename",
    "photo_id": 2

}
Body_poimka_pokemons={
    "pokemon_id": "27870"
}

response_sozdanie=requests.post(url=f'{URL}/pokemons',json=Body_POST_pokemons, headers=Header)
print(response_sozdanie.text)

message=response_sozdanie.json()['message']
print(message)

#response_rename=requests.put(url=f'{URL}/pokemons',json=Body_PUT_pokemons, headers=Header)
#print(response_rename.text)
#responce_lovlya=requests.post(url=f'{URL}/trainers/add_pokeball',json=Body_poimka_pokemons,headers=Header)
#print(responce_lovlya.text)




