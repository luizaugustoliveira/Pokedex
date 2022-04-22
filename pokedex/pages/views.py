from django.http import HttpResponse
from django.shortcuts import render

import json

with open("pokemon.json", encoding = 'utf-8') as meu_json:
    dados = json.load(meu_json)

def pokemon_elementos(lista):
    saida = ""
    for elemento in lista:
        saida += f"{elemento}\n"
    return saida


def pokemon_elementos_sem_linha_vazia_no_final(lista):
    saida = ""
    for i in range(len(lista)):
        if i != len(lista) - 1:
            saida += f"{lista[i]}\n"
        else:
            saida += f"{lista[i]}"
    return saida


def listagem():
    saida = []
    for indice in range(100):
        saida.append({"number": indice + 1, "name": dados['results'][indice]['name'], "img": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{indice + 1}.png"})
    return saida


def agrupamentos():
    normal = []
    fire = []
    water = []
    grass = []
    flying = []
    fighting = []
    poison = []
    electric = []
    ground = []
    rock = []
    psychic = []
    ice = []
    bug = []
    ghost = []
    steel = []
    dragon = []
    dark = []
    fairy = []
    for indice in range(100):
        if dados['results'][indice]['type'] == "normal":
            normal.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "fire":
            fire.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "water":
            water.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "grass":
            grass.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "flying":
            flying.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "fighting":
            fighting.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "poison":
            poison.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "electric":
            electric.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "ground":
            ground.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "rock":
            rock.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "psychic":
            psychic.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "ice":
            ice.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "bug":
            bug.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "ghost":
            ghost.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "steel":
            steel.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "dragon":
            dragon.append(dados['results'][indice]['name'])

        elif dados['results'][indice]['type'] == "dark":
            dark.append(dados['results'][indice]['name'])

        else:
            fairy.append(dados['results'][indice]['name'])

    lista = [normal, fire, water, grass, flying, fighting, poison, electric, ground, rock, psychic, ice, bug, ghost, steel, dragon, dark, fairy]

    acumulador = ""
    for i in range(len(lista)):
        if i == 0:
            acumulador += "Normal:\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 1:
            acumulador += "Fire (fogo):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 2:
            acumulador += "Water (água):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 3:
            acumulador += "Grass (grama):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 4:
            acumulador += "Flying (voador):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 5:
            acumulador += "Fighting (lutador):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 6:
            acumulador += "Poison (veneno):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 7:
            acumulador += "Electric (elétrico):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 8:
            acumulador += "Ground (terra):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 9:
            acumulador += "Rock (pedra):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 10:
            acumulador += "Psychic (psíquico):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 11:
            acumulador += "Ice (gelo):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 12:
            acumulador += "Bug (inseto):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 13:
            acumulador += "Ghost (fantasma):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 14:
            acumulador += "Steel (ferro):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        elif i == 15:
            acumulador += "Dragon (dragão):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"
        
        elif i == 16:
            acumulador += "Dark (sombrio):\n"
            acumulador += f"{pokemon_elementos(lista[i])}\n"

        else:
            acumulador += "Fairy (fada):\n"
            acumulador += f"{pokemon_elementos_sem_linha_vazia_no_final(lista[i])}"

    return acumulador


def homePageView(request):
    context = {'pokemons': listagem()}
    return render(request, 'home.html', context)
