import numpy as np
from black_scholes import black_scholes_call, black_scholes_vega

def implied_volatility(market_price, S, K, T, r, sigma_guess=0.3, max_iter=100, tolerance=1e-5):
    """
    Calcule la volatilité implicite d'une option call européenne en utilisant la méthode de Newton-Raphson
    
    Paramètres:
    market_price (float): Prix du marché de l'option
    S (float): Prix actuel du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps jusqu'à l'échéance (en années)
    r (float): Taux d'intérêt sans risque
    sigma_guess (float): Estimation initiale de la volatilité
    max_iter (int): Nombre maximum d'itérations
    tolerance (float): Tolérance pour la convergence
    
    Retourne:
    tuple: (volatilité implicite, historique des erreurs)
    """
    sigma = sigma_guess
    errors = []
    
    for i in range(max_iter):
        price = black_scholes_call(S, K, T, r, sigma)
        vega = black_scholes_vega(S, K, T, r, sigma)
        
        error = price - market_price
        errors.append(abs(error))
        
        if abs(error) < tolerance:
            return sigma, errors
        
        if vega == 0:
            raise ValueError("La méthode de Newton-Raphson ne converge pas (vega = 0)")
        
        sigma = sigma - error/vega
        
        if sigma <= 0:
            raise ValueError("La méthode de Newton-Raphson ne converge pas (sigma <= 0)")
    
    raise ValueError(f"La méthode de Newton-Raphson n'a pas convergé après {max_iter} itérations") 