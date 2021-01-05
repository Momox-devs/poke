import requests, json

def primeraRespuesta():
    url = "https://pokeapi.co/api/v2/pokemon?limit=2000&offset=0"

    response  = requests.get(url)
    response  = response.json()
    response  = response.get('results', {})
    filtro=[nun for nun in response if 'at' in nun['name'] and nun['name'].count('a')==2]
    print  len(filtro)
    

def segundarepuesta():
    url = "https://pokeapi.co/api/v2/egg-group/ground"
    response  = requests.get(url)
    response  = response.json()
    response  = response.get('pokemon_species', {})
    url2 = "https://pokeapi.co/api/v2/egg-group/fairy"
    response2  = requests.get(url2)
    response2  = response2.json()
    response2  = response2.get('pokemon_species', {})
    response.extend([element for element in response2 if element not in response])
    cantidad =len(response)
    print cantidad
    
    
def tercerarepuesta():
    url='https://pokeapi.co/api/v2/generation/1'
    response  = requests.get(url)
    response  = response.json()
    response  = response.get('pokemon_species', {})
    response2 = requests.get('https://pokeapi.co/api/v2/type/2')
    response2  = response2.json()
    response2  = response2.get('pokemon', {})
    
    peso=[0,0]
    filtro =[valor for valor in response2 
                    for valor2 in response if valor2['name'] == valor['pokemon']['name']]

    for elem in filtro:
        response3  = requests.get(elem['pokemon']['url'])
        response3  = response3.json()
        responsew  = response3.get('weight', {})
        reponseid  = response3.get('id', {})
        if reponseid <= 151:
            if peso[0] <= responsew:
                peso[0] = responsew
            if peso[1] >= responsew or 0 == peso[1]:
                peso[1] = responsew

    print peso
    

primeraRespuesta()
segundarepuesta()
tercerarepuesta()


       

            

        
        
    


 



     

    

    
 
    
   










