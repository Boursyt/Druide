class Pile:
    def __init__(self):
        self.elements = []

    #Méthode pour vérifier si la pile est vide
    #Entrée : Aucune
    #Sortie : Booléen, vrai si la pile est vide et faux sinon
    def est_vide(self):
        return len(self.elements) == 0

    #Méthode pour ajouter un élément à la pile
    #Entrée : element a ajouter 
    #Sortie : Aucune
    def empiler(self, element):
        self.elements.append(element)
        
    #Méthode pour retirer le dernier élément de la pile
    #Entrée : Aucune
    #Sortie : Retourne l'élément retiré
    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        
    #Méthode pour regarder le dernier élément de la pile sans le retirer
    #Entrée : Aucune
    #Sortie : Retourne le dernier élément
    def dernierElement(self):
        if not self.est_vide():
            return self.elements[-1]
        
        

    
    #Fonction pour évaluer l'expression en notation postfix en utilisant une pile
    #Entrée : une chaîne de caractères contenant une expression en notation postfix
    #Sortie : Retourne le résultat de l'expression
def gestionPostfix(expression):
    pile = Pile()
    elements = expression.split()# permet les nombre >= a 10

    for element in elements:
        if element.isdigit():
            pile.empiler(int(element))
        else:
            valeur2 = pile.depiler()
            valeur1 = pile.depiler()
            resultat = effectuerOperation(element, valeur1, valeur2)
            pile.empiler(resultat)
    if len(pile.elements)>1:
        raise ValueError("Expression postfixée non valide")
    return pile.depiler()






    #Fonction pour effectuer une opération arithmétique sur deux opérandes
    #Entrée : un opérateur (caractère) et deux opérandes (entiers)
    #Sortie : Retourne le résultat de l'opération
def effectuerOperation(operateur, valeur1, valeur2):
    if operateur == '*':
        return int(valeur1) * int(valeur2)
    elif operateur == '/':
        try:
            return int(valeur2) / int(valeur1)
        except ZeroDivisionError:
            raise ValueError("Division par zero impossible")
    elif operateur == '+':
        return int(valeur1) + int(valeur2)
    elif operateur == '-':
        return int(valeur1) - int(valeur2)
    else:
        raise ValueError(f"Opérateur {operateur} non valide")
    
    
    #Fonction pour saisires les données de l'utilisateur
    #Entrée : Aucune
    #Sortie : Retourne le résultat du calcule/erreures 
def saisirExpression():
    while True:
        expression = input('Entrez l\'expression en notation postfix (ou "q" pour quitter):')
        if expression.lower() == 'q':
            break
        try:
            resultat = gestionPostfix(expression)
            return resultat
        except ValueError as e:
            print(e)
            print("veuillez réessayer avec une expression valide")
            continue
        except:
            print("Une erreur est survenue lors de l'évaluation de l'expression.")
            print("veuillez réessayer avec une expression valide")
            continue

    
    
res=saisirExpression()
print(res)
