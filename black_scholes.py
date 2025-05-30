import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Calcule le prix d'une option call européenne selon le modèle Black-Scholes
    
    Paramètres:
    S (float): Prix actuel du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps jusqu'à l'échéance (en années)
    r (float): Taux d'intérêt sans risque
    sigma (float): Volatilité
    
    Retourne:
    float: Prix de l'option call
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_vega(S, K, T, r, sigma):
    """
    Calcule la vega (dérivée par rapport à la volatilité) d'une option call
    
    Paramètres:
    S (float): Prix actuel du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps jusqu'à l'échéance (en années)
    r (float): Taux d'intérêt sans risque
    sigma (float): Volatilité
    
    Retourne:
    float: Vega de l'option call
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)
    return vega 