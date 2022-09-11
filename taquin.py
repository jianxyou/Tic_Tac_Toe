# Membre 1     Nom:Jianxin You     matricule:20134401
# Membre 2     Nom:Yiwen Wang      matricule:20210763
# Date: 16/02/2022
# Ce programme est un jeu de taquin, Enjoy!

import tuiles

# Au tout début, clarifier deux points importants dans notres codes.
# 1, pour la coordonée d'un pixel, c'est l'inverse au index d'un élément dans
# le tableau 2D. 
# 2, pour la coordonée d'un tuile dans la grille de tuiles, je le traite comme
# un élément dans un tableau 2D. Par example, pour un grille de tuiles 3 * 3,
# afficherTuile(0,1,5). le chiffre 5 va apparaître dans la première ligne, 
# deuxième colone. Dans mon programme, j'utilise (xPixel,yPixel)
# (xTuile,yTuile) pour les distinguer.


# cette procédure sert à échanger iième élément et jième élément d'un tableau
def swapElements(i,j,tab):
    tmp = tab[j]
    tab[j] = tab[i]
    tab[i] = tmp
    
    
    
# cette fonction sert à vérifier si notre tableau de jeu est soluble ou non
def soluble(tab):
    
    longueur = len(tab)
    largeur = int(math.sqrt(longueur))   # nombre de tuiles par coté
    somme = 0
    
    # on commence à trouver l'index du zéro
    for index in range(longueur):
        
        # trouvons la rangée où se trouve le zéro
        if tab[index] == 0:
            # on ajoute 1 parce que la rangée du haut correspond à r=1
            rangeeZero = (index//largeur) + 1     
        
        else:
            somme += inversions(tab,tab[index])
  
    # si n est pair, on n'ajoute la rangée du zéro
    if longueur % 2 == 0:
        somme += rangeeZero
    
    # si la somme est pair, ce tableau est soluble
    if somme % 2 == 0:
        return True
    return False
    
    
    
# cette fonction sert à trouver
# le nombre d'éléments dans le tableau tab qui suivent la valeur x 
# et qui sont une des valeurs de 1 à x-1.    
def inversions(tab, x):
    
    longueur  = len(tab)
    res = 0                         # le résultat de cette fonction 
    
    # on trouve l'index de x dans le tableau
    for index in range(longueur):   
        if tab[index] == x:
            xIndex = index
            break
            
    # pour les éléments après le x, index commence à xIndex + 1
    for index in range(xIndex+1,longueur):
        if tab[index] >= 1 and tab[index] <= x-1:
            res += 1
            
    return res



# La fonction retourne un tableau de longeur largeur*largeur contenant 
# les entiers de 0 à largeur*largeur-1 qui correspond à une
# configuration de tuile qui est soluble.
def initial(largeur):
    if largeur == 0:
        return []
    
    n = largeur * largeur    # longueur du tableau
    
    # on sort de la boucle jusqu'à on trouve un tableau qui est soluble
    while True:
        jeu = permutationAleatoire(n)   # jeu est représenté par un tableau 1D
        
        # si le jeu est déjà réussi, on le rejette
        if reussi(jeu):
            continue
            
        # on le rejette aussi si ce jeu n'est pas soluable    
        if soluble(jeu):
            return jeu
        

        
# cette fonction retourne un nouveau tableau de longueur n 
# contenant les entiers de 0 à n-1 dans un ordre aléatoire
def permutationAleatoire(n):

    tab = []
    
    # les éléments du tableau sont les entiers de 0 à n-1
    # ce sont exactement les index du tableau de longueur n.
    for i in range(n):
        tab.append(i)
        
    # pour chaque index i de ce tableau
    # choisir aléatoirement un index j
    # Ensuite,échanger les éléments aux index i et j.
    brasser(tab)
            
    return tab
 
    
    
# cette procédure retourne un nombre aleatoire entre debut et fin
# cette procédure est dans la note de cours
def aleatoire(debut,fin):
    return math.floor(random() * (fin - debut)) + debut



# cette procédure sert à brasser le tableau
# cette procédure est aussi dans la note de cours
def brasser(tab):
    # pour chaque index,on choisit aléatoirement un autre index 
    # entre [index + 1, longueur du tableau). et on échange les 
    # éléments dans ces deux index.
    for index in range(len(tab)):
        nouvelIndex = aleatoire(index,len(tab))
        swapElements(index,nouvelIndex,tab)
    

    
# cette fonction sert à vérifier si le jeu est réussi ou non,
# ici, le jeu (ou la grille de tuiles) 
# est représenté par un tableau à 1 dimension.
def reussi(tableau):
    
    # n: longueur du tableau
    n = len(tableau)
    
    element  = 1
    for i in range(n-1):
        # si le jeu est réussi, alors les éléments du tableau est dans l'ordre 
        # croissant, commence par 1, et la dernière élément est 0.
        # par example, si n = 4 alors le tableau réussi est [1,2,3,0]
        # donc, on peut juste vérifier les éléments un par un,
        # et pas besoin de vérifier la dernière.
        if tableau[i] != element:
            return False
        element += 1
    
    return True
    

    
# affiche à la coordonnée (x,y) de la grille de pixels l'image 
# indiquée par le paramètre image qui utilise des couleurs 
# définies par le paramètre colormap.
def afficherImage(x, y, colormap, image):
    
    hauteur = len(image)             # hauteur de l'image
    largeur = len(image[0])          # largeur de l'image
    
    for i in range(hauteur):
        for j in range(largeur):
            # on copie chaque élément dans l'image à notre grille de pixels
            # mais faire attention,pour la coordonée (i,j) dans le tableau,
            # c'est la coordonée (j,i) dans notre grille de pixels
            setPixel(x+j,y+i,tuiles.colormap[image[i][j]])
            
    
    
# cette procédure sert à affiche à l'écran à la coordonnée (x,y)
# de la grille de tuiles l'image de la tuile indiquée par le paramètre tuile
# ici, x,y correspond à l'index d'un élément dans un tableau 2D
def afficherTuile(x, y, tuile):
    
    # on doit savoir la largeur de l'image de la tuile est combien de pixels
    largeurImage = len(tuiles.images[tuile])
    
    # pour positionner à la coordonéé de la pixel qu'on applique la procédure
    # afficherImage, yPixel doit être déduit de x, parce qu'ici, x est xTuile
    # même chose pour xPixel
    yPixel = largeurImage*x
    xPixel = largeurImage*y
    afficherImage(xPixel,yPixel,tuiles.colormap,tuiles.images[tuile])
    
    

# cette procédure sert à dessiner le jeu, i.e la grille de tuiles
# ici, grilleTuile est un tableau 1D
def dessineJeu(grilleTuile):
    
    n = len(grilleTuile)         # longueur du tableau, i.e le jeu 
    
    # pour la largeur d'un tuile, on doit savoir il est représenté 
    # par combien de pixel. En outre, ici ,par défaut, image d'un tuile
    # est sous forme carré.
    longueurImage = len(tuiles.images[0])  
    largeur =int(math.sqrt(n))   # nombre de tuile par coté
    
    setScreenMode(largeur*longueurImage, largeur*longueurImage)
    
    for i in range(largeur):
        for j in range(largeur):
            # on constuit le grille par le procédure afficherTuile,
            # pour l'index d'un élément dans un tableau 2D, pour ce jeu,
            # sa postition  correspondant dans 1D est (i * largeur + j)
            afficherTuile(i,j,grilleTuile[i*largeur+j])

            
            
# Cette procédure attend que le bouton de souris soit relaché, 
# puis attend que le bouton de souris soit appuyé
# et retourne un enregistrement contenant les champs x et y 
# qui indiquent la coordonnée de la tuile sur laquelle le joueur a cliqué.
def attendreClic():
    
    while True:
        
        # on consulte l'état de souris par 0.01 seconde.
        sleep(0.01)
        m = getMouse()
        
        
        # si utilisateur clique, m.button va changer de 0 à 1 
        if m.button == 1:
            # on retourne les coordonnées du Pixel qu'il a cliqué
            xPixel = m.x
            yPixel = m.y
            
            # on sleep 0.1 seconde, pour m.button a du temps réagir
            sleep(0.1)
            break
    
    # on doit savoir la largeur d'un image de la tuile est représenté par 
    # combien de pixels
    largeurImage= len(tuiles.images[0]) 
    
    # la coordonnée de tuile qui est cliqué est déduit par xPixel,yPixel
    # mais ici, puisque la coordonnée d'un pixel est inversé à la coordonnée
    # de l'élément dans un tableau 2D, donc, x est déduit par yPixel
    # y est déduit par xPixel
    corTuile = struct(x = yPixel//largeurImage, y = xPixel//largeurImage)
    
    return corTuile


    
# cette procédure sert à rénover (mettre à jour)
# notre jeu après on clique un tuile
# ici le jeu, ou le grille de tuile est représenté par un tableau 1D
# les paramètres xTuile, yTuile sont la coordonée d'une 
def renoverJeu(xTuile,yTuile,grilleTuile):
    
    longueur = len(grilleTuile)
    largeur = int(math.sqrt(longueur))    # combien de tuiles par coté
    
    # on trouve la coordonné du zéro dans  le grille de tuiles   
    for i in range(longueur):
        if grilleTuile[i] == 0:
            # xZero, yZero sont les index dans le tableau 2D
            # ils sont aussi la cordonnée de la  tuile qu'on a cliqué
            xZero = int(i // largeur)
            yZero = int(i % largeur)
    
    # maintenant, on judge si x,y est 
    # dans le même ligne ou même colone que zéro   
    memeLigne = xZero == xTuile
    memeColone = yZero == yTuile
    
    # l'index de la tuile qui est cliqué dans la grille de tuiles (1D)
    indexTuile = int(xTuile * largeur + yTuile)
    
    # l'index du zéro dans la grille de tuiles (1D)
    indexZero =int( xZero * largeur + yZero)

    if memeLigne:
        renoverUneLigne(indexTuile,indexZero,grilleTuile)
        
    elif memeColone:
        renoverUneColone(indexTuile,indexZero,grilleTuile,largeur)     
    
    return grilleTuile



# cette procédure sert à rénover une ligne après on sait que 
# l'utilisateur a cliqué un tuile qui est dans le même ligne que zéro.
# tab ici est un tableau 1D qui représente la grille de tuiles.
# indexTuile: index de la tuile qu'on a cliqué dans le tab
# indexZero: index du Zero dans le tab
def renoverUneLigne(indexTuile,indexZero,tab):
    # si Tuile est à gauche du zéro
    if indexTuile - indexZero > 0:
        
        # on échange le zéro et l'élément à sa droite
        # avec nombre de (indexTuile-indexZero) fois.
        # par example, si tab = [0,1,2,3], et on clique 3
        # 1e itération, tab = [1,0,2,3]
        # 2e itération, tab = [1,2,0,3]
        # 3e itération, tab = [1,2,3,0]
        
        for i in range(indexZero,indexTuile):
            swapElements(i,i+1,tab)
    else:
        
        # le cas contraire qu'avant.
        for i in range (indexZero,indexTuile,-1):
            swapElements(i,i-1,tab)
            
            

#cette procéduresert à rénover une colonne après on sait que 
# l'utilisateur a cliqué un tuile qui est dans le même colonne que zéro.
# tab ici est un tableau 1D qui représente la grille de tuiles.
# indexTuile: index de la tuile cliqué dans le tab
# indexZero: index du Zero dans le tab
# largeur : largeur de la grille de tuiles.          
def renoverUneColone(indexTuile,indexZero,tab,largeur):
    
    # si le Tuile cliqué est au dessous du zéro
    if indexTuile - indexZero > 0:
        
        # on échange le zéro et l'élément qui est au dessus de lui
        # avec nombre de ((indexTuile-indexZero) % largeur) fois.
        # par example, si tab = [0,1,2,3]
        # et la grille de tuiles est 
        # [0  1]
        # [2  3]
        # si on clique 2, le tab va être [2,1,0,3]
        
        for i in range(indexZero,indexTuile,largeur):
            swapElements(i,i+largeur,tab)
    else:      
        # le cas contraire qu'avant.
        for i in range (indexZero,indexTuile,-largeur):
            swapElements(i,i-largeur,tab)        

            
# procédure princiaple du jeu            
def taquin(largeur):
    
    while True:
        # initialiser un jeu et l'afficher
        grilleTuile = initial(largeur)
        dessineJeu(grilleTuile)
        
        while True:
            # réagit aux clics du joueur et déplace les tuiles en conséquence
            # et après, on dessine le jeu.
            corTuile = attendreClic()
            grilleTuile = renoverJeu(corTuile.x,corTuile.y,grilleTuile)
            dessineJeu(grilleTuile)
            
            # si le jeu est réussi
            if reussi(grilleTuile):
                dessineJeu(grilleTuile)
                # ici ,on sleep 0.1 seconde pour l'affichage soit complet
                sleep(0.1)
                alert("Bravo! vous avez réussi!")
                break


def testTaquin():
    assert permutationAleatoire(0) == []
    assert permutationAleatoire(1) == [0]
    assert permutationAleatoire(2) in [[0,1],[1,0]]
    assert permutationAleatoire(-1) == []
    permutation3Elem = [[0, 1, 2], [0, 2, 1], [1, 0, 2], 
                         [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    assert permutationAleatoire(3) in permutation3Elem
    
    
    assert inversions([0],0) == 0
    assert inversions([0,1],1) == 0
    assert inversions([1,0],1) == 0
    assert inversions([3,2,1,0],3) == 2
    assert inversions([2,3,4,5,9,8,7,6,1,0],2) == 1
    assert inversions([2,3,4,5,9,8,7,6,1,0],1) == 0
    
      
    assert soluble([3,1,0,2]) == True
    assert soluble([3,0,2,1]) == True
    assert soluble([1,2,0,3]) == True
    assert soluble([2,0,3,1]) == False
    assert soluble([0,2,3,1]) == False
    
    
    permutataion4Elem = [[0, 1, 2, 3],
                         [0, 1, 3, 2],
                         [0, 2, 1, 3],
                         [0, 2, 3, 1],
                         [0, 3, 1, 2],
                         [0, 3, 2, 1],
                         [1, 0, 2, 3],
                         [1, 0, 3, 2],
                         [1, 2, 0, 3],
                         [1, 2, 3, 0],
                         [1, 3, 0, 2],
                         [1, 3, 2, 0],
                         [2, 0, 1, 3],
                         [2, 0, 3, 1],
                         [2, 1, 0, 3],
                         [2, 1, 3, 0],
                         [2, 3, 0, 1],
                         [2, 3, 1, 0],
                         [3, 0, 1, 2],
                         [3, 0, 2, 1],
                         [3, 1, 0, 2],
                         [3, 1, 2, 0],
                         [3, 2, 0, 1],
                         [3, 2, 1, 0]]
    
    assert initial(0) == []    
    assert initial(2) in permutataion4Elem
    assert soluble(initial(2)) == True
    
    # pour un tableau de 3*3, on vérifie si chaque élément est dans 0 à 8
    tab = initial(3)
    for elem in tab:
        assert elem in list(range(9))
    assert soluble(initial(3)) == True
    

    setScreenMode(2,2)
    afficherImage(1,0,tuiles.colormap,[[2]])
    assert exportScreen() == '#000#fff\n#000#000'
    
    setScreenMode(2,2)
    afficherImage(1,1,tuiles.colormap,[[3]])
    assert exportScreen() == '#000#000\n#000#888'
    
    setScreenMode(2,2)
    afficherImage(0,0,tuiles.colormap,[[2,3]])
    assert exportScreen() == '#fff#888\n#000#000'
    
    setScreenMode(2,2)
    afficherImage(0,0,tuiles.colormap,[[2,2],[1,3]])
    assert exportScreen() == '#fff#fff\n#ccc#888'
    
    setScreenMode(2,2)
    afficherImage(0,1,tuiles.colormap,[[1,1]])
    assert exportScreen() == '#000#000\n#ccc#ccc'

    setScreenMode(16,16)
    afficherTuile(0,0,1) 
    assert exportScreen() == '\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc\n\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888\n\
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888\
'
    
    setScreenMode(16,16)
    afficherTuile(0,0,2) 
    assert exportScreen() == '\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc\n\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888\n\
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888\
'
    setScreenMode(16,16)
    afficherTuile(0,0,15) 
    assert exportScreen() == '\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc\n\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#080#080#ccc#ccc#080#080#080#080#080#080#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888\n\
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888\
'
    
    setScreenMode(16,16)
    afficherTuile(0,0,8)
    assert exportScreen() == '\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc\n\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888\n\
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888\
'
    
    setScreenMode(16,16)
    afficherTuile(0,0,4)
    assert exportScreen() == '\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc\n\
#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#fff#ccc#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#080#080#080#080#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#080#080#ccc#ccc#ccc#888#888\n\
#fff#fff#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#888#888\n\
#fff#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888\n\
#ccc#888#888#888#888#888#888#888#888#888#888#888#888#888#888#888\
'

testTaquin()

