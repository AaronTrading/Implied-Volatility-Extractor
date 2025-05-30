import tkinter as tk
from tkinter import ttk, messagebox

class VolatilityUI:
    def __init__(self, callback):
        self.root = tk.Tk()
        self.root.title("Calcul de Volatilité Implicite")
        self.callback = callback
        
        # Création des variables
        self.market_price = tk.StringVar(value="10.0")
        self.stock_price = tk.StringVar(value="100.0")
        self.strike_price = tk.StringVar(value="100.0")
        self.risk_free_rate = tk.StringVar(value="0.05")
        self.time_to_maturity = tk.StringVar(value="1.0")
        self.initial_volatility = tk.StringVar(value="0.3")
        self.max_iterations = tk.StringVar(value="100")
        self.tolerance = tk.StringVar(value="1e-5")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Entrées
        ttk.Label(main_frame, text="Prix du marché de l'option:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.market_price).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Prix du sous-jacent:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.stock_price).grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Prix d'exercice (strike):").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.strike_price).grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Taux sans risque:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.risk_free_rate).grid(row=3, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Temps jusqu'à l'échéance (années):").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.time_to_maturity).grid(row=4, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Volatilité initiale:").grid(row=5, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.initial_volatility).grid(row=5, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Nombre max d'itérations:").grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.max_iterations).grid(row=6, column=1, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Tolérance:").grid(row=7, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.tolerance).grid(row=7, column=1, padx=5, pady=2)
        
        # Bouton de calcul
        ttk.Button(main_frame, text="Calculer", command=self.calculate).grid(row=8, column=0, columnspan=2, pady=10)
        
    def calculate(self):
        try:
            params = {
                'market_price': float(self.market_price.get()),
                'S': float(self.stock_price.get()),
                'K': float(self.strike_price.get()),
                'r': float(self.risk_free_rate.get()),
                'T': float(self.time_to_maturity.get()),
                'sigma_guess': float(self.initial_volatility.get()),
                'max_iter': int(self.max_iterations.get()),
                'tolerance': float(self.tolerance.get())
            }
            self.callback(params)
        except ValueError as e:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
    
    def run(self):
        self.root.mainloop() 