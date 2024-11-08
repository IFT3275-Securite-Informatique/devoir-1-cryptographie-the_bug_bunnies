import requests
from collections import Counter
import random as rnd
#import nltk #dictionnaire
#ajouter librairie python requirement.txt : 

def load_text_from_web(url):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.text
  except requests.exceptions.RequestException as e:
    print(f"An error occurred while loading the text: {e}")
    return None
  
def cut_string_into_pairs(text):
    pairs = []
    for i in range(0, len(text) - 1, 2):
      pairs.append(text[i:i + 2])
    if len(text) % 2 != 0:
      pairs.append(text[-1] + '_')  # Add a placeholder if the string has an odd number of characters
    return pairs

url = "https://www.gutenberg.org/ebooks/13846.txt.utf-8"  # Example URL (replace with your desired URL)
corpus = load_text_from_web(url)
url = "https://www.gutenberg.org/ebooks/4650.txt.utf-8"  # Example URL (replace with your desired URL)
corpus = corpus + load_text_from_web(url)

# Liste fixée.
M = corpus
tab = cut_string_into_pairs(M)

#caracteres = list(set(list(M)))         #tableau des chars sans doublons
#nb_caracteres = len(caracteres)
#nb_bicaracteres = 256-nb_caracteres
#bicaracteres = [item for item, _ in Counter(cut_string_into_pairs(M)).most_common(nb_bicaracteres)]
symboles = ['b', 'j', '\r', 'J', '”', ')', 'Â', 'É', 'ê', '5', 't', '9', 
                    'Y', '%', 'N', 'B', 'V', '\ufeff', 'Ê', '?', '’', 'i', ':', 
                    's', 'C', 'â', 'ï', 'W', 'y', 'p', 'D', '—', '«', 'º', 'A', 
                    '3', 'n', '0', 'q', '4', 'e', 'T', 'È', '$', 'U', 'v', '»', 
                    'l', 'P', 'X', 'Z', 'À', 'ç', 'u', '…', 'î', 'L', 'k', 'E', 
                    'R', '2', '_', '8', 'é', 'O', 'Î', '‘', 'a', 'F', 'H', 'c', 
                    '[', '(', "'", 'è', 'I', '/', '!', ' ', '°', 'S', '•', '#', 
                    'x', 'à', 'g', '*', 'Q', 'w', '1', 'û', '7', 'G', 'm', '™', 
                    'K', 'z', '\n', 'o', 'ù', ',', 'r', ']', '.', 'M', 'Ç', '“', 
                    'h', '-', 'f', 'ë', '6', ';', 'd', 'ô', 'e ', 's ', 't ', 'es', 
                    ' d', '\r\n', 'en', 'qu', ' l', 're', ' p', 'de', 'le', 'nt', 
                    'on', ' c', ', ', ' e', 'ou', ' q', ' s', 'n ', 'ue', 'an', 
                    'te', ' a', 'ai', 'se', 'it', 'me', 'is', 'oi', 'r ', 'er', 
                    ' m', 'ce', 'ne', 'et', 'in', 'ns', ' n', 'ur', 'i ', 'a ', 
                    'eu', 'co', 'tr', 'la', 'ar', 'ie', 'ui', 'us', 'ut', 'il', 
                    ' t', 'pa', 'au', 'el', 'ti', 'st', 'un', 'em', 'ra', 'e,', 
                    'so', 'or', 'l ', ' f', 'll', 'nd', ' j', 'si', 'ir', 'e\r', 
                    'ss', 'u ', 'po', 'ro', 'ri', 'pr', 's,', 'ma', ' v', ' i', 
                    'di', ' r', 'vo', 'pe', 'to', 'ch', '. ', 've', 'nc', 'om', 
                    ' o', 'je', 'no', 'rt', 'à ', 'lu', "'e", 'mo', 'ta', 'as', 
                    'at', 'io', 's\r', 'sa', "u'", 'av', 'os', ' à', ' u', "l'", 
                    "'a", 'rs', 'pl', 'é ', '; ', 'ho', 'té', 'ét', 'fa', 'da', 
                    'li', 'su', 't\r', 'ée', 'ré', 'dé', 'ec', 'nn', 'mm', "'i", 
                    'ca', 'uv', '\n\r', 'id', ' b', 'ni', 'bl']

nb_symboles = len(symboles)
print(nb_symboles)

def bitToTab(C):
   return [C[i:i+8] for i in range (0, len(C), 8)]


def decrypt(C):
  #TextsForStats
    url = "https://www.gutenberg.org/ebooks/13846.txt.utf-8"  # Example URL (replace with your desired URL)
    textsForStats = load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/4650.txt.utf-8"  # Example URL (replace with your desired URL)
    textsForStats = textsForStats + load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/69794.txt.utf-8"
    textsForStats = textsForStats + load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/63267.txt.utf-8"
    textsForStats = textsForStats + load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/18092.txt.utf-8"
    textsForStats = textsForStats + load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/18812.txt.utf-8"
    textsForStats = textsForStats + load_text_from_web(url)
    url = "https://www.gutenberg.org/ebooks/13704.txt.utf-8"
    textsForStats = textsForStats + load_text_from_web(url)



    #crée un dictionnaire de symbol + occurences
    symbolDictionnary = createSymbolDictionnary(textsForStats, symboles)
   
    #calculer les stats du chiffrage 
    bitTab = bitToTab(C)
    tupleBits = sorted(bitCharByOccurence(bitTab).items(), key=lambda item: item[1], reverse=True)
    print("student_code stats tupleBits", tupleBits)

    #mapper chaque chiffre avec la lettre
    dictToutSymbol= dict(symbolDictionnary)
    dictToutBits= dict(tupleBits)
    dictChiffreVersLettre = dict(list(zip(dictToutBits, dictToutSymbol)))
    print("student_code dictionnaire", dictChiffreVersLettre)

    #dechiffrer le message chiffré avec les occurences

    M = ""
    for cypher in bitTab:
      char = dictChiffreVersLettre.get(cypher)
      M = M + char

    #print("**************MESSAGE***************:\n", M)
    print("**************MESSAGE DÉCRYPTÉ***************\n", decrypt)

  
    return M


def createSymbolDictionnary(textsForStats, symboles):

   dictSymboles = dict.fromkeys(symboles, 0)    #dictionnaire des symboles avec 0 comme default val

   #compter les lettres totales
   caractereParOccurence = Counter(list(textsForStats))
   #print(caractereParOccurence)

   #mettre chaque lettre dans le dictionnaire
   for letter in caractereParOccurence:
      if(letter in dictSymboles):
         dictSymboles[letter] += caractereParOccurence.get(letter)


   paires = cut_string_into_pairs(textsForStats)

   for paire in paires:
      if(paire in dictSymboles):
         dictSymboles[paire] += 1

         if(paire[0] in dictSymboles):
            dictSymboles[paire[0]] -=1
         if(paire[1] in dictSymboles):   
            dictSymboles[paire[1]] -=1


   sortedDictSymbol = sorted(dictSymboles.items(), key=lambda item: float(item[1]), reverse=True)

   return sortedDictSymbol



#retourne un dictionnaire de symboles (bit) par fréquence en %
def bitCharByFrequency(dictBitCharByOccurence):

    dictBitFrequency = {}
    for bitchar in dictBitCharByOccurence:
        dictBitFrequency[bitchar] = '%.3f'%((dictBitCharByOccurence.get(bitchar)/len(M))*100)    #en %

    sortedDictBitFrequency = sorted(dictBitFrequency.items(), key=lambda item: float(item[1]))

    return sortedDictBitFrequency


#retourne un dictionnaire qui compte chaque occurence d'un certain bit
def bitCharByOccurence(bitTab):
    dictBitChar = {}
    for bitchar in bitTab:
    #mettre dans un dictionnaire qui incrémente à ch fois
    #si clé exite, créer clé
       if(dictBitChar.get(bitchar)==None):
            dictBitChar[bitchar] = 1
       else:
          dictBitChar.update({bitchar : dictBitChar.get(bitchar)+1})

    return dictBitChar

decrypt("c")
