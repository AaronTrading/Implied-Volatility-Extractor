# Calculateur de Volatilité Implicite

Ce projet permet de calculer la volatilité implicite d'une option européenne de type "call" en utilisant la méthode de Newton-Raphson.

## Description

La volatilité implicite est la valeur de la volatilité qui, lorsqu'elle est utilisée dans le modèle de Black-Scholes, donne un prix théorique égal au prix de marché observé. C'est une mesure importante pour les traders et les analystes financiers.

## Screens

![Screen1](https://media.discordapp.net/attachments/1280431720679870475/1377972635807387800/Screenshot_4.png?ex=683ae885&is=68399705&hm=c5037d483c00f1007aeed8dc1ca220b0eb3902e7b5c1d44c8b672f9089b8045e&=&format=webp&quality=lossless&width=433&height=370)
![Screen2](https://media.discordapp.net/attachments/1280431720679870475/1377972635522302062/Screenshot_1.png?ex=683ae885&is=68399705&hm=8a233eafd2c0627aba2d9a0d85e2f934d76e605b03070dd145278d62afebda31&=&format=webp&quality=lossless&width=1248&height=784)

## Formule de Black-Scholes

Pour une option call européenne, le prix selon le modèle de Black-Scholes est donné par :

C = S _ N(d1) - K _ e^(-rT) \* N(d2)

où :

- C est le prix de l'option call
- S est le prix actuel du sous-jacent
- K est le prix d'exercice (strike)
- T est le temps jusqu'à l'échéance (en années)
- r est le taux d'intérêt sans risque
- σ est la volatilité
- N() est la fonction de répartition de la loi normale standard
- d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
- d2 = d1 - σ√T

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Lancez le programme avec :

```bash
python app.py
```

Une interface graphique s'ouvrira vous permettant de saisir :

- Le prix du marché de l'option
- Le prix du sous-jacent
- Le prix d'exercice (strike)
- Le taux sans risque
- Le temps jusqu'à l'échéance
- La volatilité initiale (estimation)
- Le nombre maximum d'itérations
- La tolérance pour la convergence

Après avoir cliqué sur "Calculer", vous obtiendrez :

1. La volatilité implicite calculée
2. Un graphique montrant la convergence de la méthode de Newton-Raphson

## Méthode de Newton-Raphson

La méthode de Newton-Raphson est utilisée pour trouver la racine de l'équation :
f(σ) = C_théorique(σ) - C_marché = 0

À chaque itération, la volatilité est mise à jour selon :
σ_n+1 = σ_n - f(σ_n)/f'(σ_n)

où f'(σ) est la vega de l'option (dérivée du prix par rapport à la volatilité).

## Auteur

Aaron Z.

## Licence

MIT
