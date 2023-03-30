# Pizza bot

Konverzačný bot vytvorený pomocoru RASA 3.1

Bot na objednávanie pizze v slovenčine

## Príprava
```
pip3 install rasa 
```

## Trénovanie bota
Tento krok môže trvať niekoľko desiatok sekúnd
```
rasa train
```

## Začiatok konverzácie
Treba otvoriť dva terminály v jednom spustiť:
```
rasa run actions
```
a v druhom:
```
rasa shell
```
Tento krok bude trvať pár desiatok sekúnd 

# Konverzácia
## Začiatok
Keď bude bot pripravený v terminály bude 
```
Your input -> 
```
Pokial bot nie je prepojeny na webovú aplikáciu nie je možné aby zacačal konverzáciu ako prvý.
Preto treba začať vetou napríklad: Dobrý deň, chcel by som si obejdnať pizzu

## Reštartovanie konverzácie
```
Your input -> /restart
```

## Koniec konverzácie
```
Your input -> /stop
```
