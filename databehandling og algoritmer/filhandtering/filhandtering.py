# Lese "vanlige" tekstfiler

# åpne og lese fil i python

fil = open("tullefil.txt", encoding="utf-8") # åpner fila tullefil.txt meed utf8-enkoding(lar oss bruke æ ø å)
print(fil.read()) # leser innholder i fila
fil.close() # lukker fila -> frigjør minne

# Alternatovt

with open("tullefil.txt", encoding="utf-8") as fil:
    data = fil.read()

linjer = data.split("\n") # spliter innholdet på newline (\n), linjer er nå en liste der hver liste er et element

# lese json-filer
import json # importerer json.biblioteket

fil = open("sanger.json", encoding= "utf-8") # åpner fila sanger.json
sanger = json.load(fil) # leser innholdet og tolker det i json-format ( sanger er her en liste med ordbøker)
fil.close()

print(sanger[0])

with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)

# Eksempeloppgave 
# Hvor mamge sanger av artisten taylor swift er det på topplista
    
# sett antall til 0
antall = 0

for sang in sanger:
    if sang["artist"] == "The Weeknd":
        antall += 1
print(antall)
# for hver sang in sanger
#    hvis sang sin artist er lik taylor swift
#        øk antall med 1
# print antall
print(len(sanger))

# tankegang: hvilken artist har flest sanger på top 50

#lag en tom ordbok
artister = {}

for sang in sanger:
    if sang["artist"] in artister:
        artister[sang["artist"]] += 1
    else:
        artister[sang["artist"]] = 1

print(artister)
    
høyeste_artist = ""
høyeste_antall = -1


for artist in artister:
    antall_sanger = artister[artist]
    if antall_sanger > høyeste_antall:
        høyeste_artist = artist
        høyeste_antall = antall_sanger

print(høyeste_artist, høyeste_antall)
    