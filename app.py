from ui import VolatilityUI
from implied_vol import implied_volatility
from plots import plot_convergence
from tkinter import messagebox

def calculate_volatility(params):
    try:
        # Calcul de la volatilité implicite
        sigma, errors = implied_volatility(
            market_price=params['market_price'],
            S=params['S'],
            K=params['K'],
            T=params['T'],
            r=params['r'],
            sigma_guess=params['sigma_guess'],
            max_iter=params['max_iter'],
            tolerance=params['tolerance']
        )
        
        # Affichage du résultat
        messagebox.showinfo("Résultat", f"Volatilité implicite: {sigma:.4%}")
        
        # Affichage du graphique de convergence
        plot_convergence(errors)
        
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def main():
    ui = VolatilityUI(calculate_volatility)
    ui.run()

if __name__ == "__main__":
    main() 