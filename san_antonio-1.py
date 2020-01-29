# -*- coding: utf8 -*-

import random
import json

#quotes = [
#    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
#    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
#]

#characters = [
 #   "alvin et les Chipmunks", 
  #  "Babar", 
   # "betty boop", 
    #"calimero", 
    #"casper", 
    #"le chat potté", 
    #"Kirikou"
#]

#read values from JSON file
def read_value_from_json(file, key):
  values = []
  # Open a json file with my objects
  with open(file) as f:
    # Load all the data contained in my file. datat = entries
    data = json.load(f)
    for entry in data:
  	  values.append(entry[key])
    return values


def get_random_item(my_list):
  rand_numb = random.randint(0, len(my_list)-1)
  item = my_list[rand_numb] # get an item from a list. For the moment, just get the first one.
  # TODO: show the quote
  return item

def random_character():
  all_values = read_value_from_json('characters.json', 'character')
  return get_random_item(all_values)

def random_quote():
  all_values = read_value_from_json('quotes.json', 'quote')
  return get_random_item(all_values)  

def capitalize(words):
  for word in words:
  	word.capitalize()

def message(character, quote):
  capitalize(character)
  capitalize(quote)
  return "{} a dit : {}".format(character, quote)

user_answer = input('Tapez entrée pour connaitre une autre cittaion ou B pour quitter le programme.')


while user_answer != "B":
  print(message(random_character(), random_quote()))
  user_answer = input('Tapez entrée pour connaitre une autre cittaion ou B pour quitter le programme.')
  