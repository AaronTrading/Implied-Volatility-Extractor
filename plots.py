import matplotlib.pyplot as plt

def plot_convergence(errors):
    """
    Affiche le graphique de convergence de la méthode de Newton-Raphson
    
    Paramètres:
    errors (list): Liste des erreurs à chaque itération
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(errors) + 1), errors, 'b-o')
    plt.xlabel('Nombre d\'itérations')
    plt.ylabel('Erreur absolue')
    plt.title('Convergence de la méthode de Newton-Raphson')
    plt.grid(True)
    plt.yscale('log')
    plt.show() 