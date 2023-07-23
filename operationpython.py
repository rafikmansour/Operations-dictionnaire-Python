#Création d'un dictionnaire:

# Méthode 1 : Utilisation des accolades {}
my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Méthode 2 : Utilisation de la fonction dict()
my_dict = dict(nom='Bob', age=25, ville='Paris')

# Méthode 3 : Utilisation de la fonction zip()
keys = ['nom', 'age', 'ville']
values = ['Charlie', 22, 'Londres']
my_dict = dict(zip(keys, values))



#Accès aux valeurs d'un dictionnaire :

my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Accès à une valeur par sa clé
print(my_dict['nom'])  # Sortie: 'Alice'

# Méthode get() pour accéder à une valeur
print(my_dict.get('age'))  # Sortie: 30

# Récupération des clés et des valeurs sous forme de listes
keys = my_dict.keys()
values = my_dict.values()


#Modification et ajout de paires clé-valeur :

my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Modification de la valeur d'une clé existante
my_dict['age'] = 31

# Ajout d'une nouvelle paire clé-valeur
my_dict['profession'] = 'Ingénieur'


#Suppression d'une paire clé-valeur :

my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Suppression d'une clé et de sa valeur
del my_dict['age']

# Suppression d'une clé avec la méthode pop()
my_dict.pop('ville')


#Vérification de l'existence d'une clé :

my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Vérification si une clé existe
if 'age' in my_dict:
    print("La clé 'age' existe dans le dictionnaire.")
else:
    print("La clé 'age' n'existe pas dans le dictionnaire.")


#Parcourir un dictionnaire :

my_dict = {'nom': 'Alice', 'age': 30, 'ville': 'New York'}

# Parcourir les clés et les valeurs
for key, value in my_dict.items():
    print(key, ':', value)

# Parcourir les clés uniquement
for key in my_dict:
    print(key)

# Parcourir les valeurs uniquement
for value in my_dict.values():
    print(value)


