'''
db["player_id"] conserve les identifiants.
db["player_name"] conserve les noms de joueurs.
db["player_data"] (liste de listes) conserve la sauvegarde :
 0 : Nom d'utilisateur
 1 : Lieux
 2 : Pokémon capturés (liste de 898 booléens)
 3 : Expérience de chaque Pokémon (898 nombres)
 4 : Objets tenus (898 nombres)
 5 : Pokédex du joueur (898 booléens)
 6 : Équipe du joueur (6 nombres ou None)
 7 : Nombres d'exemplaire de chaque Pokémon (898 listes) [nombre d'exemplaires, nombre d'exemplaires shinys, pv, attaque, défense, attaque péciale, défense spéciale, vitesse, capacité 1, capacité 2, capacité 3, capacité 4, objet]
 8 : Avancée dans le scénario (nombre)
 9 : Argent
 10 : Sac [Pokéballs, ]
 11 : Time for cooldown
 12 : Caught Pokémon (Number)
 13 : Caught of each species (list)
 14 : Total earned money
 15 : Cooldown
 16 : Caught of each shiny species (list)
 17 : Recoil ball recoil catch left (int)
 18 : Recoil ball upgrades (list) [recoil number, recoil effect, recoil reducer]
 19 : [Partner, Dreamed Pokémon]
 20 : Release lock (list of 50 numbers)
 21 : Special encounter [(Is special encounter, dex number, is shiny])
 22 : Fake razz, Rare razz, Lucky machine encounter left (list)
 23 : Number of use of balls, razz, lucky machine, egg hatched [0-10, 11, 12, 13, 14]
 24 : Total money gained from trivia (int)





option :
  0 : Toggle view name in other languages in dex.

types :
0 : Normal
1 : Combat
2 : Vol
3 : Poison
4 : Sol
5 : Roche
6 : Insecte
7 : Spectre
8 : Acier
9 : Feu
10 : Eau
11 : Plante
12 : Électrik
13 : Psy
14 : Glace
15 : Dragon
16 : Ténèbres
17 : Fée

Language (English, French, German, Chinese, Korean, Japanese romaji, Japanese)

french wiki : https://www.pokepedia.fr/Portail:Accueil
german wiki : https://www.pokewiki.de/Hauptseite
japanese wiki : https://wiki.xn--rckteqa2e.com/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8
https://cassarilla.tumblr.com/post/102878795753/pokemon-in-korean-pokemon-types

Lieux :
0. Bourg Palette (Pallet town)
1. Laboratoire de Chen (Pokémon Laboratory) (kanto)
2. Maison du joueur (Home) (kanto)
3. Route 1 (kanto)


Capacités :
[Nom, Précision, % effets spéciaux, PP, Priorité, Puissance, Type de dégâts]


'''
places = ['Pallet town', 'Pokémon Laboratory', 'Home']
