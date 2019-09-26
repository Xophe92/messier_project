#source : https://www.cosmodixi.fr/ebook/catalogue-messier.pdf
import re
import pandas as pd
import config

content = """
7 décembre 2018
Malgré le soin apporté à la réalisation de ce document, une erreur est
toujours possible. Afin d’en améliorer le contenu, vous pouvez faire part de
vos remarques à cette adresse : info@cosmodixi.fr.
Les coordonnées équatoriales (époque 2000) et les magnitudes (V) sont
extraites de la base de données HyperLeda (http://leda.univ-lyon1.fr)
et du CDS Portal (http://cdsportal.u-strasbg.fr/).
Document compilé par LATEX.
https://www.cosmodixi.fr
Le catalogue Messier
Les 110 objets répertoriés par Charles Messier
Charles Messier (1730-1817)
Révisé le 7 décembre 2018
I
Sommaire :
Le catalogue de Charles Messier VIII
Messier 1 (Nébuleuse du Crabe) 1
Messier 2 (Amas globulaire) 3
Messier 3 (Amas globulaire) 5
Messier 4 (Amas globulaire) 7
Messier 5 (Amas globulaire) 9
Messier 6 (Amas du Papillon) 11
Messier 7 (Amas ouvert) 13
Messier 8 (Nébuleuse de la Lagune) 15
Messier 9 (Amas globulaire) 17
Messier 10 (Amas globulaire) 19
Messier 11 (Amas du Canard sauvage) 21
Messier 12 (Amas globulaire) 23
Messier 13 (Amas d’Hercule) 25
Messier 14 (Amas globulaire) 27
II
Messier 15 (Amas globulaire) 29
Messier 16 (Amas ouvert) 31
Messier 17 (Nébuleuse Oméga) 33
Messier 18 (Amas ouvert) 35
Messier 19 (Amas globulaire) 37
Messier 20 (Nébuleuse Trifide) 39
Messier 21 (Amas ouvert) 41
Messier 22 (Amas globulaire) 43
Messier 23 (Amas ouvert) 45
Messier 24 (Petit nuage du Sagittaire) 47
Messier 25 (Amas ouvert) 49
Messier 26 (Amas ouvert) 51
Messier 27 (Nébuleuse Dumbbell) 53
Messier 28 (Amas globulaire) 55
Messier 29 (Amas ouvert) 57
Messier 30 (Amas globulaire) 59
Messier 31 (Galaxie d’Andromède) 61
Messier 32 (Galaxie elliptique) 63
Messier 33 (Galaxie du Triangle) 65
Messier 34 (Amas ouvert) 67
Messier 35 (Amas ouvert) 69
III
Messier 36 (Amas ouvert) 71
Messier 37 (Amas ouvert) 73
Messier 38 (Amas ouvert) 75
Messier 39 (Amas ouvert) 77
Messier 40 (Étoile double Winnecke 4) 79
Messier 41 (Amas ouvert) 81
Messier 42 (Grande nébuleuse d’Orion) 83
Messier 43 (Nébuleuse à émission) 85
Messier 44 (Amas de la Crèche) 87
Messier 45 (Amas des Pléiades) 89
Ajouts seconde compilation 93
Messier 46 (Amas ouvert) 93
Messier 47 (Amas ouvert) 95
Messier 48 (Amas ouvert) 97
Messier 49 (Galaxie elliptique) 99
Messier 50 (Amas ouvert) 101
Messier 51 (Galaxie du Tourbillon) 103
Messier 52 (Amas ouvert) 105
Messier 53 (Amas globulaire) 107
Messier 54 (Amas globulaire) 109
IV
Messier 55 (Amas globulaire) 111
Messier 56 (Amas globulaire) 113
Messier 57 (Nébuleuse annulaire) 115
Messier 58 (Galaxie spirale barrée) 117
Messier 59 (Galaxie elliptique) 119
Messier 60 (Galaxie elliptique) 121
Messier 61 (Galaxie spirale barrée) 123
Messier 62 (Amas globulaire) 125
Messier 63 (Galaxie Tournesol) 127
Messier 64 (L’Œil noir) 129
Messier 65 (Galaxie spirale barrée) 131
Messier 66 (Galaxie spirale barrée) 133
Messier 67 (Amas ouvert) 135
Messier 68 (Amas globulaire) 137
Messier 69 (Amas globulaire) 139
Messier 70 (Amas globulaire) 141
Messier 71 (Amas globulaire) 143
Messier 72 (Amas globulaire) 145
Messier 73 (Astérisme) 147
Messier 74 (Galaxie spirale) 149
Messier 75 (Amas globulaire) 151
V
Messier 76 (Petite Dumbbell) 153
Messier 77 (Galaxie spirale) 155
Messier 78 (Nébuleuse à émission) 157
Messier 79 (Amas globulaire) 159
Messier 80 (Amas globulaire) 161
Messier 81 (Galaxie de Bode) 163
Messier 82 (Galaxie du Cigare) 165
Messier 83 (Galaxie spirale) 167
Messier 84 (Galaxie lenticulaire) 169
Messier 85 (Galaxie lenticulaire) 171
Messier 86 (Galaxie elliptique) 173
Messier 87 (Galaxie elliptique) 175
Messier 88 (Galaxie spirale) 177
Messier 89 (Galaxie elliptique) 179
Messier 90 (Galaxie spirale barrée) 181
Messier 91 (Galaxie spirale barrée) 183
Messier 92 (Amas globulaire) 185
Messier 93 (Amas ouvert) 187
Messier 94 (Galaxie spirale) 189
Messier 95 (Galaxie spirale barrée) 191
Messier 96 (Galaxie spirale barrée) 193
VI
Messier 97 (Nébuleuse du Hibou) 195
Messier 98 (Galaxie spirale barrée) 197
Messier 99 (La Toupie) 199
Messier 100 (Galaxie spirale barrée) 201
Messier 101 (Galaxie Pinwheel) 203
Messier 102 (Galaxie lenticulaire) 205
Messier 103 (Amas ouvert) 207
Ajouts ultérieurs 211
Messier 104 (Galaxie du Sombréro) 211
Messier 105 (Galaxie elliptique) 213
Messier 106 (Galaxie spirale barrée) 215
Messier 107 (Amas globulaire) 217
Messier 108 (Galaxie spirale barrée) 219
Messier 109 (Galaxie spirale barrée) 221
Messier 110 (Galaxie elliptique) 223
Sources des images 226
VII
Le catalogue de Charles Messier
L’inventaire dressé par l’astronome Charles Messier (1730 -
1817), aujourd’hui officiellement arrêté à 110 entrées, est toujours
l’un des catalogues d’objets célestes le plus utilisé par les amateurs
d’astronomie.
Le premier « Catalogue Messier » fut rendu public en 1771 et
publié dans les Mémoires de l’Académie Royale des sciences. Il ne
contenait alors que les positions de 45 objets accompagnés d’un
court descriptif. Les années suivantes de nouvelles découvertes
l’incitèrent à publier un catalogue de 58 objets qui vinrent s’ajouter
à la précédente liste.
C’est son ami et collègue Pierre Méchain (1744 - 1804), astronome à l’observatoire de Paris, qui l’aida pour cette compilation
dont il a plus que largement contribué à l’enrichissement. Affecté à
l’observatoire de la Marine à Versailles, Méchain fut également un
rigoureux observateur : il découvrit pas moins de 12 comètes entre
1781 et 1802. Ses multiples pérégrinations célestes l’amenèrent à
trouver de nombreuses nébuleuses faibles, surtout dans la région
située entre la Chevelure de Bérénice et la Vierge. Il ne dressa
pas de liste de ces découvertes mais en informa Messier.
Rédigée dès 1781, puis publiée dans la Connaissance des Temps
de 1784 sous le titre : Catalogue des Nébuleuses et des amas
d’étoiles observées à Paris, par M. Messier, à l’Observatoire de la
Marine, hôtel de Clugni, rue des Mathurins., cette liste constitue
le véritable Catalogue de Messier qui s’arrête donc au n° 103. On
retrouve ainsi plus d’une vingtaine d’objets dont il faut attribuer
la première observation à Méchain.
VIII
Sept autres objets furent incorporés plus récemment au catalogue original de Messier.
M 104 fut rajouté, en 1921, par Camille Flammarion (1842 -
1925) suite à la découverte d’une note relative à son observation.
Les trois objets suivants : M 105, M 106 et M 107, furent
rapportés par l’astronome américano-canadienne Helen Battles
Sawyer Hogg (1905 - 1993).
Owen Gingerich (1930 -), chercheur et historien des sciences,
rallongea la liste avec les objets M 108 et M 109.
Kenneth Glyn Jones (1915 - 1995) compléta l’inventaire en
1968, avec M 110, en démontrant l’observation de cet objet par
messier en 1773 et figurant sur son dessin de M 31 publié en 1807.
Les quatre « erreurs » de Messier
Découverte et identifiée par Johannes Hewel – ou Johan Hœvelke, dit Hévélius (1611 - 1687), M 40 avait déjà été classé comme
nébuleuse. À l’époque on qualifiait de « nébuleuse » tout objet
d’aspect flou que l’on découvrait parmi les étoiles. En fait, il s’agit
d’une étoile double : Winnecke 4, près de δ UMa.
M 73 s’est avéré n’être qu’un simple groupe de 4 étoiles,
formant un Y.
Pour M 91, aucun objet particulier n’a été retrouvé aux environs de la zone mentionnée dans ses notes. Il est possible qu’il
s’agisse d’une méprise et que l’objet concerné soit NGC 4548.
Enfin, les relevés laissés par Messier sur M 102 partagent les
avis des spécialistes en deux thèses.
IX
Classification des amas globulaires selon H. Shapley et H. B. Sawyer
La classification des amas globulaires utilise un chiffre romain indiquant la
concentration des étoiles : I (pour les amas les plus compacts) à XII (pour les
amas les plus dispersés).
Classification des amas ouverts selon R. J. Trumpler
Concentration : I = densité centrale très marquée
II = concentration modérée
III = l’amas se détache sans concentration centrale
IV = concentration centrale peu marquée
Distribution : 1 = étoiles de magnitudes apparentes similaires
2 = distribution régulière des différents éclats
3 = quelques étoiles brillantes dominent
Richesse : p = pauvre, moins de 50 étoiles
m = moyenne, entre 50 et 100 étoiles
r = riche, plus de 100 étoiles
(n) = l’amas est associé à une nébuleuse
Classification des galaxies par de Vaucouleurs (simplifiée)
Classe Subdivisions
Elliptiques E 0 à 7
Lenticulaires SO 1 à 3
1 = aspect plus proche des elliptiques
3 = aspect plus proche des spirales
Spirales
Intermédiaires
Spirales barrées
SA
SAB
SB
a, ab, b, bc, c, cd, d, (r)
a = bras fermés autour d’un bulbe moyen
c = bras très ouverts autour d’un bulbe réduit
(r) = présence d’une structure en anneau
Irrégulières I
NB : pec (peculiar) désigne des galaxies d’un type bien identifié mais possédant
une « anomalie » qui les rend uniques.
X
Messier 1 Rémanant de supernova
Découverte : John Bevis (1731)
Ascension Droite : 05h 34m 31,92s Déclinaison : +22° 00’ 52,3"
Magnitude : 8,40 ± 0,10 Distance : 6 000 a.l.
Classe : - - Dimension : 6’ × 4’
Constellation : Taureau Visibilité : Hiver
Autres appellations : Nébuleuse du Crabe, 3C144, 4C+21.19,
IRAS05315+2158, NGC7089, PGC2817554, PGC2819678
1
Le premier élément du catalogue Messier est l’un des plus rares, il s’agit d’un
résidu de supernova. Déjà repéré en 1731 par l’astronome amateur anglais
John Bevis, cet objet sera (re)découvert par Charles Messier le 12 septembre
1758 alors qu’il recherchait une comète dans cette région. Il le décrivit comme
« une lumière blanchâtre ayant la forme d’une flamme de bougie ».
William Parsons, à l’aide de son réflecteur de 90 cm, sera le premier à y
distinguer des filaments qui, par similitude avec les pinces et les pattes d’un
crabe, lui valurent son nom commun : la nébuleuse du Crabe.
Jocelyn Bell Burnell découvrit en 1967 une étonnante précision dans le signal
émit par le centre de cette nébuleuse. Elle venait d’y découvrir le premier
« pulsar » : une étoile à neutron en rotation extrêmement rapide émettant un
faisceau en émission X et radio qui balaie la Terre à chaque tour.
Aisément repérable par cheminement depuis l’étoile ζ, Messier 1 demande
cependant de bonnes conditions d’observation pour parvenir à y discerner
quelques détails ; pour distinguer les filaments, une ouverture de 400 mm
s’avère nécessaire.
2
Messier 2 Amas globulaire
Découverte : Giovanni Domenico Maraldi (1746)
Ascension Droite : 21h 33m 29,35s Déclinaison : −00° 49’ 23,3"
Magnitude : 6,60 ± 0,10 Distance : 36 800 a.l.
Classe : II Dimension : Ø 12,9’
Constellation : Verseau Visibilité : Automne
Autres appellations : NGC7089, PGC2802702
3
Cet objet fut remarqué par le franco-italien Jean Dominique Maraldi le
7 septembre 1746 alors qu’il cherchait une comète découverte peu avant par
l’astronome suisse Jean Philippe Loys de Chéseaux dans cette portion de ciel.
Charles Messier ne l’observera que le 11 septembre 1760 et la décrira comme
une nébuleuse ronde et sans étoiles.
Ce n’est que 23 années plus tard que William Herschel parviendra à en
distinguer la véritable nature : un amas de quelques centaines de milliers
d’étoiles dont l’âge est estimé à environ 13 milliards d’années.
Inaccessible à l’œil nu, Messier 2 est discernable à l’aide d’une petite lunette
(voire des jumelles), mais un instrument d’au moins 200 à 250 mm d’ouverture
est nécessaire pour parvenir à le résoudre en étoiles.
4
Messier 3 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 13h 42m 11,21s Déclinaison : +28° 22’ 32,1"
Magnitude : 6,30 ± 0,10 Distance : 34 000 a.l.
Classe : VI Dimension : Ø 16,2’
Constellation : Chiens de chasse Visibilité : Printemps
Autres appellations : NGC5272, PGC2802651
5
Observé par Charles Messier le 3 mai 1764, l’amas ne sera résolu en étoiles
que vers 1784 par William Herschel. Très concentré en son centre, la moitié
de sa masse est contenue dans un volume sphérique de 22 années de lumière
de diamètre, pour un diamètre réel estimé à 760 années de lumière.
L’amas contient un grand nombre d’étoiles variables, également un nombre
important d’étoiles bleues qui semblent donc bien plus jeunes que la majorité de
celles composant l’amas. L’explication qui prévaut serait que les couches les plus
superficielles de ces étoiles seraient arrachées par interaction gravitationnelle
lors de passages répétés dans les régions centrales les plus denses.
Repérable aux jumelles, l’amas globulaire est à rechercher à mi-chemin entre
l’étoile α de la constellation et Arcturus. Messier 3 reste difficile à résoudre en
sa partie centrale, il faut des ouvertures supérieures à 100 mm pour commencer
à distinguer individuellement ses étoiles les plus externes.
6
Messier 4 Amas globulaire
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 16h 23m 35,46s Déclinaison : −26° 31’ 31,3"
Magnitude : 5,40 ± 0,10 Distance : 6 500 a.l.
Classe : IX Dimension : Ø 26,3’
Constellation : Scorpion Visibilité : Été
Autres appellations : NGC6121, PGC2802659
7
C’est un amas globulaire relativement peu dense avec une « barre centrale » formée par un ensemble d’étoiles plus lumineuses. Cette structure fut remarquée
pour la première fois par William Herschel en 1783.
En 1987, le premier pulsar observé dans un amas globulaire y fut découvert. Il
s’agit d’une étoile à neutrons en rotation très rapide : 100 tours à la seconde.
Messier 4 est facilement repérable à 1,2° à l’ouest de la brillante Antares. Il
faut cependant une ouverture d’au moins 100 mm pour résoudre l’amas et
observer la « barre centrale ». Un autre amas globulaire, NGC 6144, est visible
à seulement 30’ au nord-ouest d’Antares. À noter que cette zone est parsemée
de nébulosités et de nuages de poussières obscurcissant les amas.
8
Messier 5 Amas globulaire
Découverte : Gottfried Kirch (1702)
Ascension Droite : 15h 18m 33,77s Déclinaison : +02° 04’ 58,1"
Magnitude : 5,70 ± 0,10 Distance : 25 000 a.l.
Classe : V Dimension : Ø 17,4’
Constellation : Serpent Visibilité : Été
Autres appellations : NGC5904, PGC2802656
9
La première observation de cet objet date du 5 mai 1702, elle est à mettre au
compte de Gottfried Kirch à l’observatoire de Berlin. Charles Messier ne le
découvrira que 62 ans plus tard (le 23 mai 1764) sans pouvoir le résoudre en
étoiles.
Il serait l’un des plus vieux amas globulaires connus, également l’un des plus
grands puisque son diamètre réel est estimé à 165 années de lumière.
Objet à la limite de la perception à l’œil nu, dans un ciel exempt de pollution
lumineuse, Messier 5 demande une ouverture minimale de 100 mm pour
résoudre ses étoiles les plus lumineuses. L’amas est à repérer juste au nordouest de l’étoile 5 Serpentis.
10
Messier 6 Amas ouvert
Découverte : Giovanni Battista Hodierna (vers 1654)
Ascension Droite : 17h 40m 19,99s Déclinaison : −32° 14’ 60,0"
Magnitude : 4,20 ± 0,10 Distance : 1 500 a.l.
Classe : III 3 r Dimension : Ø 33’
Constellation : Scorpion Visibilité : Été
Autres appellations : Amas du Papillon, NGC6405
11
La découverte de cet amas ouvert reviendrait à Jean Philippe Loys de Chéseaux
en 1746, il est possible qu’il ait été devancé par Giovanni Battista Hodierna
qui l’aurait observé vers 1654.
Son nom commun, l’amas du Papillon, lui a été attribué par l’astronome
américain Sherburne Wesley Burnham pour qui il suggérait l’image d’un
« papillon aux ailes déployées ».
L’étoile la plus lumineuse de l’amas est la variable semi-régulière BM Scorpi,
une supergéante dont la magnitude apparente oscille entre 6,8 et 8,7 sur une
période d’environ 850 jours.
Messier 6 est vu proche de l’axe du centre galactique dont il n’est séparé que
d’un peu plus de 2°. Aux jumelles, la teinte orangée de l’étoile supergéante
contraste avec la couleur bleutée des principales composantes de l’amas.
12
Messier 7 Amas ouvert
Découverte : Ptolémée (vers 130)
Ascension Droite : 17h 53m 50,54s Déclinaison : −34° 47’ 35,0"
Magnitude : 3,30 ± 0,10 Distance : 820 a.l.
Classe : I 3 r Dimension : Ø 80’
Constellation : Scorpion Visibilité : Été
Autre appellation : NGC6475
13
Cet amas ouvert était déjà connu de Ptolémée qui le note dans son catalogue
comme « un amas nébuleux à la queue du Scorpion ». Cet objet est ainsi
parfois retrouvé sous l’appellation Amas de Ptolémée.
Giovanni Battista Hodierna l’aurait également repéré en même temps que son
homologue précédent depuis la Sicile vers 1654. Charles Messier portera son
intérêt sur ces deux objets le 23 mai 1764.
S’étalant sur un peu plus d’un degré, l’amas est composé d’une centaine
d’étoiles, sa dimension réelle est de 20 année de lumière. Son âge est estimé à
220 millions d’années.
Messier 7 est aisément repérable à l’œil nu sur un ciel bien noir, une simple
paire de jumelles permet de le résoudre.
14
Messier 8 Nébuleuse à émission
Découverte : Guillaume Le Gentil de La Galaisière (1747)
Ascension Droite : 18h 03m 42,01s Déclinaison : −24° 22’ 48,0"
Magnitude : 6 Distance : 5 200 a.l.
Classe : - - Dimension : 90’ × 40’
Constellation : Sagittaire Visibilité : Été
Autres appellations : Nébuleuse de la Lagune, NGC6523
15
La découverte de la nébuleuse de la Lagune revient à Guillaume Le Gentil de
La Galaisière qui l’observa pour la première fois en 1747. L’amas ouvert qui
lui est associé – NGC 6530, classé II 2 m (n) – et procure l’énergie nécessaire
à sa luminescence fut déjà observé par John Flamsteed en 1680. C’est l’amas
que intégra dans son catalogue le 23 mai 1764, mais l’objet considéré de nos
jours comme étant Messier 8 est bien la nébuleuse.
Quelques « globules de Bok » (condensations sombres évoluant vers le stade
de protoétoiles) y ont été repérés. M 8 est également une source d’émission
radio.
À la limite de la perception à l’œil nu sur un ciel exempt de pollution lumineuse,
la nébuleuse est à rechercher à 6° au nord de l’étoile γ qui forme le « bec
verseur » de la théière. Il faut un télescope de 100 mm pour parvenir à distinguer
le « canal » sombre qui semble diviser la nébuleuse en deux et lui donne son
nom commun.
16
Messier 9 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 17h 19m 11,76s Déclinaison : −18° 30’ 58,7"
Magnitude : 7,80 ± 0,10 Distance : 25 000 a.l.
Classe : VIII Dimension : Ø 9,3’
Constellation : Ophiuchus Visibilité : Été
Autre appellation : NGC6333
17
Cet amas globulaire est une découverte originale de Charles Messier, le 28 mai
1764, alors qu’il s’adonnait encore à la recherche de comètes.
Orbitant proche du centre galactique, dont il n’est distant que de 6 000 années
de lumière, la lumisosité de l’amas est sensiblement atténuée en direction de
l’ouest par un nuage de poussières interstellaire : Barnard 64 (LDN 173).
Messier 9 demande une ouverture d’au moins 200 mm pour être partiellement
résolu. À 80’, en direction du nord-est, on retrouve un autre amas globulaire :
NGC 6356. Un second (NGC 6342) est visible à une distance égale au sud -
sud-est.
18
Messier 10 Amas globulaire
Découverte : Charles Messier (29 mai 1764)
Ascension Droite : 16h 57m 08,95s Déclinaison : −04° 05’ 57,8"
Magnitude : 6,60 ± 0,10 Distance : 6 200 a.l.
Classe : VIII Dimension : Ø 15,1’
Constellation : Ophiuchus Visibilité : Été
Autres appellations : NGC6254, PGC2802664
19
Une nouvelle découverte originale de Charles Messier, le lendemain de celle de
M 9 : 29 mai 1764, qu’il décrira comme une « Nébuleuse, ronde et sans étoiles,
près de l’étoile 30 Oph. »
Cet amas globulaire est l’un des plus proches du Système solaire, et malgré
un diamètre réel relativement modeste pour ce type d’objet : 60 années de
lumière, il présente un diamètre apparent d’une demi Lune.
Facilement repérable aux jumelles, Messier 10 demande une ouverture d’au
moins 200 mm pour se révéler dans toute sa splendeur.
20
Messier 11 Amas ouvert
Découverte : Gottfried Kirch (1681)
Ascension Droite : 18h 51m 05,01s Déclinaison : −06° 16’ 12,1"
Magnitude : 5,80 ± 0,10 Distance : 5 600 a.l.
Classe : I 2 r Dimension : Ø 13’
Constellation : Écu de Sobieski Visibilité : Été
Autres appellations : Amas du Canard sauvage, NGC6705
21
Amas ouvert découvert par l’allemand Gottfried Kirch en 1681. Il semble que
ce soit un pasteur anglican, William Derham, qui soit le premier à le résoudre
en étoiles (avant 1733). Charles Messier l’intégrera à son catalogue le 30 mai
1764. Une description, plutôt fantaisiste, due à l’amiral William Smyth lui
donna son nom commun : l’amas du Canard sauvage, également nommé amas
du Vol de canards.
Composé d’environ 3 000 étoiles, l’amas est âgé de 250 millions d’années.
Très riche en étoiles et très compact, Messier 11 ressemble fortement à un
amas globulaire lorsqu’on l’observe avec un petit instrument.
Une étoile de magnitude 8 est visible près du centre, elle se superpose à l’amas
auquel elle n’appartient pas.
22
Messier 12 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 16h 47m 14,50s Déclinaison : −01° 56’ 52,1"
Magnitude : 6,10 ± 0,10 Distance : 19 500 a.l.
Classe : IX Dimension : Ø 14,5’
Constellation : Ophiuchus Visibilité : Été
Autres appellations : NGC6218, PGC2802662
23
Amas globulaire découvert par Charles Messier le 30 mai 1764 (durant la
même nuit d’observation que M 11, les deux objets étant vus proches sur la
voûte céleste). Il le décrira également comme une « Nébuleuse ronde et de
faible luminosité, ne contenant aucune étoile... ». William Herschel sera le
premier à résoudre l’amas en 1783.
La dimension réelle de M 12 est de 75 années de lumière.
Messier 12 est assez facile à retrouver en partant de Yed Prior (δ Oph) : 8°
vers l’est et 2° au nord ; 2° vers l’ouest et 2° au nord, si l’on part de son voisin
Messier 10.
24
Messier 13 Amas globulaire
Découverte : Edmund Halley (1714)
Ascension Droite : 16h 41m 41,49s Déclinaison : +36° 27’ 36,8"
Magnitude : 5,80 ± 0,10 Distance : 25 000 a.l.
Classe : V Dimension : Ø 16,6’
Constellation : Hercule Visibilité : Été
Autres appellations : Amas d’Hercule, 2MASXJ16414163+3627407, NGC6205
25
M 13 fut observé par Charles Messier le 1er juin 1764, 50 ans après sa découverte
par Edmund Halley.
C’est dans sa direction que fut émis, le 16 novembre 1974, à l’aide du radiotélescope d’Arecibo, un message codé à l’intention d’une éventuelle civilisation.
M 13 possède une population d’environ 250 000 étoiles dont l’âge avoisine les
14 milliards d’années. D’un diamètre réel estimé à 140 années de lumière, sa
densité centrale est 500 fois supérieure à notre environnement stellaire.
Facilement repérable au tiers supérieur d’une ligne reliant les étoiles η et ζ, la
position de Messier 13 est discernable à l’œil nu sur un ciel pur.
26
Messier 14 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 17h 37m 36,15s Déclinaison : −03° 14’ 45,4"
Magnitude : 7,60 ± 0,10 Distance : 33 000 a.l.
Classe : VIII Dimension : Ø 11,7’
Constellation : Ophiuchus Visibilité : Été
Autre appellation : NGC6402
27
Charles Messier découvre l’amas le 1er juin 1764, il l’observera à nouveau 5 ans
plus tard lors du passage d’une comète dans cette région du ciel, sans toutefois
parvenir à le résoudre en étoiles.
La dimension réelle de l’amas est de l’ordre de 110 année de lumière et sa
luminosité globale équivaut à 440 000 soleils.
Lors d’un classement d’archives en 1964, l’astronome Amelia Fay Wehlau
retrouva sur 8 plaques photographiques de M 14, prises entre le 21 et le 28
juin 1938, la trace d’une supernova qui atteignit la magnitude 9,2.
Situé dans une région dépourvue d’étoiles lumineuses, le repérage de Messier 14
est assez difficile. Sa vision l’est tout autant, il faut une ouverture d’au moins
200 mm pour commencer à le résoudre en périphérie.
28
Messier 15 Amas globulaire
Découverte : Giovanni Domenico Maraldi (1746)
Ascension Droite : 21h 29m 58,35s Déclinaison : +12° 10’ 00,5"
Magnitude : 6,30 ± 0,10 Distance : 34 000 a.l.
Classe : IV Dimension : Ø 12,3’
Constellation : Pégase Visibilité : Automne
Autres appellations : NGC7078, PGC2802701
29
M 15 fut découvert, en même temps que M 2, par le franco-italien Giovanni
Domenico Maraldi le 7 septembre 1746. Il ne sera (re)découvert par Charles
Messier que le 3 juin 1764.
Il est l’un des 200 amas globulaires connus qui gravitent autour de notre
galaxie. Son diamètre réel est de 130 années de lumière.
Une nébuleuse planétaire, Pease 1 de magnitude 13,8, y a été découverte en
1928, par l’astronome américain Francis Gladheim Pease, sur des plaques
photographiques de l’observatoire du Mont Wilson prises l’année précédente.
Pas moins de 9 pulsars y sont également répertoriés.
Aisément repérable aux jumelles sous la forme d’une « étoile » » diffuse,
Messier 15 peut facilement se retrouver en prolongeant l’axe des étoiles
θ (Biham) et  (Enif) de la moitié de leur distance vers le nord-ouest. Le
cœur de l’amas, très dense, reste impossible à résoudre avec un instrument
d’amateur.
30
Messier 16 Amas ouvert
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 18h 18m 48,05s Déclinaison : −13° 48’ 25,0"
Magnitude : 6,00 ± 0,10 Distance : 6 500 a.l.
Classe : II 3 m (n) Dimension : Ø 7’
Constellation : Serpent Visibilité : Été
Autre appellation : NGC6611
31
L’amas ouvert (NGC 6611) fut découvert par Jean Philippe Loys de Chéseaux
en 1746, la nébuleuse à émission (IC 4703, nébuleuse de l’Aigle) qui lui est
associée sera discernée pour la première fois le 3 juin 1764 par Charles Messier.
Il s’agit d’une zone de forte concentration de gaz et de poussières interstellaires
où se produit une intense formation d’étoiles qui a donné naissance à l’amas
ouvert M 16. La nébuleuse est rendue visible par réémission du rayonnement
de ces jeunes étoiles, massives et très chaudes. La partie centrale : « l’aigle
aux ailes déployées » (également appelée les Piliers de la Création), est une
zone qui absorbe le rayonnement émis par le gaz ionisé par l’amas stellaire vu
au nord et nord-est.
L’amas Messier 16 se repère à un peu moins de 2,5° à l’ouest de l’étoile γ Scuti.
L’observation aux jumelles permet déjà de distinguer une vingtaine d’étoiles ;
pour espérer voir les « piliers », il faut une ouverture d’au moins 300 mm et
s’équiper d’un filtre OIII.
32
Messier 17 Amas ouvert
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 18h 20m 47,06s Déclinaison : −16° 10’ 18,0"
Magnitude : env. 6 Distance : 6 800 a.l.
Classe : II 3 m (n) Dimension : 20’ × 15’
Constellation : Sagittaire Visibilité : Été
Autres appellations : Nébuleuse du Cygne, Nébuleuse Oméga, Nébuleuse du
Fer à cheval, Nébuleuse du Homard, NGC6618
33
Lorsque Charles Messier l’observa le 3 juin 1764 cette « trainée de lumière
sans étoiles », suivant sa propre description, il ne se doutait pas qu’il avait été
encore devancé par le suisse Jean Philippe Loys de Chéseaux en 1746.
D’une masse estimée à 800 soleils, la plus grande extension de ce vaste complexe
gazeux semble s’étendre jusqu’à 40 années de lumière. Il pourrait être associé
au même nuage interstellaire formant M 16, les deux objets étant vus dans un
même axe de direction et situés à des distances proches. Sa vague forme en fer
à cheval lui a valu le nom de Horseshoe Nebula ou « nébuleuse Oméga » (Ω).
L’exubérant Camille Flammarion y discerna plutôt la silhouette d’un cygne
ou d’un « nuage de fumée balayé par le vent ».
À la limite de la perception à l’œil nu, Messier 17 est repérable aux jumelles à
un peu plus de 2° au sud-ouest de l’étoile γ Scuti.
34
Messier 18 Amas ouvert
Découverte : Charles Messier (1764)
Ascension Droite : 18h 19m 58,10s Déclinaison : −17° 06’ 06,1"
Magnitude : 6,90 ± 0,10 Distance : 4 100 a.l.
Classe : II 3 p (n) Dimension : Ø 10’
Constellation : Sagittaire Visibilité : Été
Autres appellations : 2MASSJ18195810-1706062, NGC6613
35
Amas ouvert, assez pauvre en étoiles et peu dense, répertorié par Charles
Messier le 3 juin 1764.
L’amas est relativement jeune : une trentaine de millions d’années. Sa magnitude absolue est de −5, pour une luminosité globale estimée à 8 300 soleils, il
est contenu dans un volume d’environ 17 années de lumière.
Situé à mi-chemin de Messier 17 et Messier 24, une dizaine d’étoiles formant
Messier 18 sont observables aux jumelles.
36
Messier 19 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 17h 02m 37,73s Déclinaison : −26° 16’ 04,8"
Magnitude : 6,80 ± 0,10 Distance : 28 000 a.l.
Classe : VIII Dimension : Ø 13,5’
Constellation : Ophiuchus Visibilité : Été
Autre appellation : NGC6273
37
Amas globulaire découvert par Charles Messier le 5 juin 1764.
Sa luminosité globale est équivalente à 400 000 soleils, sa magnitude absolue
est de −9,2.
38
Messier 20 Nébuleuse à émission
Découverte : Guillaume Le Gentil de La Galaisière (1747)
Ascension Droite : 18h 02m 31,45s Déclinaison : −22° 59’ 58,0"
Magnitude : 9 Distance : 6 700 a.l.
Classe : - - Dimension : 20’ × 20’
Constellation : Sagittaire Visibilité : Été
Autres appellations : Nébuleuse Trifide, NGC6514
39
La première description écrite de cette nébuleuse est celle de Charles Messier
en 1764, mais il est plus que probable que Guillaume Le Gentil de La Galaisière
l’observa dès 1747. C’est sir John Herschel qui emploiera le terme de « trifide »
pour désigner l’aspect que prend la nébuleuse dans un grand télescope : trois
sillons obscurs, concentrations de poussière et de gaz froids se projetant du
centre vers le bord, semblent la découper en trois parties pratiquement égales.
Les meilleures photographies ont depuis montrées qu’il y en avait quatre.
La Trifide est une nébuleuse à émission (ou réflexion) dont le gaz, essentiellement composé d’hydrogène, est ionisé (généralement visible en rouge sur les
photographies ; ces régions sont dites HII) par le rayonnement ultraviolet des
étoiles qu’elle contient.
Une autre nébuleuse, autour de l’étoile HD 164 514 située juste au nord, émet
principalement dans le bleu.
40
Messier 21 Amas ouvert
Découverte : Charles Messier (1764)
Ascension Droite : 18h 04m 13,25s Déclinaison : −22° 29’ 25,2"
Magnitude : 5,90 ± 0,10 Distance : 4 000 a.l.
Classe : I 3 r Dimension : Ø 13’
Constellation : Sagittaire Visibilité : Été
Autres appellations : 2MASSJ18041328-2229251, NGC6531
41
Amas ouvert découvert par Charles Messier le 5 juin 1764, lors d’une observation de la nébuleuse Trifide.
D’une dimension réelle de 20 années de lumière, sa magnitude absolue est de
−5,9, soit l’équivalent de la lumière émise par 20 000 soleils.
42
Messier 22 Amas globulaire
Découverte : Johann Abraham Ihle (1665)
Ascension Droite : 18h 36m 24,19s Déclinaison : −23° 54’ 12,1"
Magnitude : 5,20 ± 0,10 Distance : 10 000 a.l.
Classe : VII Dimension : Ø 24’
Constellation : Sagittaire Visibilité : Été
Autres appellations : NGC6656, PGC2802689
43
La découverte de M 22 est souvent attribuée à l’astronome polonais Johannes
Hewel (Hévélius) qui l’aurait observé vers 1660, mais Charles Messier lui-même
en attribue la paternité à l’allemand Johann Abraham Ihle en 1665.
Il fait partie des amas globulaires les plus faciles à observer, juste derrière
Oméga du Centaure et 47 Toucan (visibles que depuis l’hémisphère Sud) et
devançant notre « amas d’Hercule » (M 13).
L’amas Messier 22 est à retrouver à un peu plus de 2° au nord-est de l’étoile λ
– celle qui forme la pointe du « couvercle de la théière » – soit environ le tiers
de la distance en direction de l’étoile ξ (xi).
44
Messier 23 Amas ouvert
Découverte : Charles Messier (1764)
Ascension Droite : 17h 57m 04,35s Déclinaison : −18° 59’ 03,5"
Magnitude : 5,50 ± 0,10 Distance : 2 100 a.l.
Classe : II 2 r Dimension : Ø 27’
Constellation : Sagittaire Visibilité : Été
Autre appellation : NGC6494
45
Une découverte de Charles Messier le 20 juin 1764.
Avec une magnitude absolue de −4,7, la luminosité globale de l’amas vaut
6 300 soleils ; son âge est estimé à 300 millions d’années.
46
Messier 24 Nuage stellaire
Découverte : Charles Messier (1764)
Ascension Droite : 18h 18m 24,02s Déclinaison : −18° 24’ 24,0"
Magnitude : 11,10 ± 0,10 Distance : 12 000 a.l.
Classe : - - Dimension : 95’ × 35’
Constellation : Sagittaire Visibilité : Été
Autres appellations : Petit nuage du Sagittaire, (NGC6603)
47
M 24 n’est pas un objet physique réel, il n’est qu’une portion plus lumineuse
de la Voie lactée.
La volonté d’octroyer un nom à chaque première observation conduit à lui
allouer celui de Charles Messier. Il aurait déterminé la position de cette
« nébuleuse », facilement discernable à l’œil nu, le 20 juin 1764. Sur son carnet
de notes il lui donna un diamètre de 1° 30’.
Cette mesure ne fut pas prise en considération par les observateurs suivants qui
se méprirent tous sur la nature de l’observation de Messier. Sir John Herschel,
William Parsons, Camille Flammarion et bien d’autres, tous confondirent M 24
avec l’amas ouvert NGC 6603 qui se trouve en sa partie Nord.
Deux petites nébuleuses en absorption (le plan équatorial de notre galaxie
est truffé d’objets de cette nature) viennent se superposer à l’ensemble. Elles
portent les numéros 92 et 93 dans le catalogue de Barnard.
48
Messier 25 Amas ouvert
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 18h 31m 48,00s Déclinaison : −19° 06’ 48,0"
Magnitude : 4,60 ± 0,10 Distance : 2 000 a.l.
Classe : I 3 m Dimension : Ø 32’
Constellation : Sagittaire Visibilité : Été
Autre appellation : IC4725
49
Amas ouvert découvert, en même temps que M 16 et M 17, par le suisse Jean
Philippe Loys de Chéseaux en 1746. Il sera retrouvé par Charles Messier en
1764.
Curieusement cet objet, pourtant discernable à l’œil nu, sera négligé par les
observateurs suivants. Il faudra attendre que Julius Johann Friedrich Schmidt
(re)découvre l’amas en 1866 pour qu’il soit intégré dans l’Index Catalogue en...
1908 ; il y figure sous la référence IC 4725.
Fait rarissime pour ce type d’objet, il contient une céphéide : U Sgr qui varie
de la magnitude 6,3 à 7,1 en 6,7 jours.
50
Messier 26 Amas ouvert
Découverte : Charles Messier (1764)
Ascension Droite : 18h 45m 18,01s Déclinaison : −09° 22’ 50,1"
Magnitude : 8,00 ± 0,10 Distance : 5 000 a.l.
Classe : I 2 m Dimension : Ø 14’
Constellation : Écu de Sobieski Visibilité : Été
Autre appellation : NGC6694
51
La découverte de M 26 est souvent attribuée à Guillaume Le Gentil de La
Galaisière vers 1750, mais aucune certitude n’existe à ce sujet. Charles Messier
l’observera en 1764.
L’amas est repérable à environ 1° à l’est - sud-est de l’étoile δ de la constellation.
52
Messier 27 Nébuleuse planétaire
Découverte : Charles Messier (1764)
Ascension Droite : 19h 59m 36,32s Déclinaison : +22° 43’ 17,4"
Magnitude : 7,40 ± 0,10 Distance : 1 200 a.l.
Classe : - - Dimension : Ø 348"
Constellation : Petit Renard Visibilité : Été
Autres appellations : Nébuleuse du Diabolo, Nébuleuse Dumbbell, Nébuleuse
de l’Haltère, 2MASXJ19593637+2243157, NGC6853
53
Déjà repérable aux jumelles, la nébuleuse planétaire Dumbbell (le « Battant
de cloche », également connue sous les noms de nébuleuse du Diabolo ou de
l’Haltère) a été découverte par Charles Messier le 12 juillet 1764.
La naine blanche centrale qui lui a donné naissance, il y a environ 4 000 ans, a
une température superficielle de 85 000 kelvins. L’expansion de la nébuleuse
continue encore de nos jours à une vitesse de 27 km.s-1
.
54
Messier 28 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 18h 24m 32,92s Déclinaison : −24° 52’ 11,6"
Magnitude : 6,90 ± 0,10 Distance : 19 000 a.l.
Classe : IV Dimension : Ø 11,2’
Constellation : Sagittaire Visibilité : Été
Autres appellations : NGC6626, PGC2802687
55
Amas globulaire découvert par Charles Messier le 26 juillet 1764. Repérable
dans des jumelles 10×50, il faut une ouverture minimum de 100 mm pour
commencer à le résoudre.
Un pulsar, une étoile à neutron tournant sur elle-même 327 fois par seconde,
y fut découvert en 1987.
56
Messier 29 Amas ouvert
Découverte : Charles Messier (1764)
Ascension Droite : 20h 23m 57,86s Déclinaison : +38° 30’ 28,9"
Magnitude : 6,60 ± 0,10 Distance : 6 000 a.l.
Classe : I 2 m (n) Dimension : Ø 6’
Constellation : Cygne Visibilité : Été
Autre appellation : NGC6913
57
Charles Messier découvrit cet amas ouvert le 29 juillet 1764, lors de l’une
de ses multiples pérégrinations qui l’amenaient parfois à la découverte de
nouvelles comètes. Il le décrira comme un amas de 7 ou 8 petites étoiles.
Âgé de seulement 10 millions d’années, M 29 peut être considéré comme
un amas ouvert très jeune. D’un diamètre réel de 11 années de lumière, ses
5 composantes principales sont des étoiles géantes de classe B0 ; la magnitude
absolue de l’amas est de −8,2, soit une luminosité globale équivalente à 160 000
soleils.
58
Messier 30 Amas globulaire
Découverte : Charles Messier (1764)
Ascension Droite : 21h 40m 22,00s Déclinaison : −23° 10’ 44,9"
Magnitude : 6,90 ± 0,10 Distance : 26 000 a.l.
Classe : V Dimension : Ø 11’
Constellation : Capricorne Visibilité : Été
Autres appellations : NGC7099, PGC2802703
59
Amas globulaire découvert le 3 août 1764 par Charles Messier qui le répertoria
comme une simple nébulosité sans étoiles. Repérable aux jumelles 10×50,
il faut cependant une ouverture d’au-moins 100 mm pour commencer à le
résoudre.
Plusieurs variables de type RR Lyræ y ont été découvertes. Les analyses
spectrales ont démontré une faible teneur en éléments lourds, signe d’un
âge très avancé analogue à celui de la Galaxie. L’amas se rapproche de notre
Système solaire à 175 km.s-1. Il est à rechercher à un peu plus de 3° de l’étoile ζ
en direction de l’étoile 41 suivant la description de Charles Messier.
60
Messier 31 Galaxie spirale
Découverte : Abdul Rahman al Suphi (964)
Ascension Droite : 00h 42m 44,33s Déclinaison : +41° 16’ 08,1"
Magnitude : 6.75 ± 3.55 Distance : 2,2 × 106 a.l.
Classe : SAb Dimension : 185,0’ × 75,0’
Constellation : Andromède Visibilité : Automne
Autres appellations : Galaxie d’Andromède, 2MASXJ00424433+4116074,
CGCG535-017, GIN801, LGG011:[G93]001, MCG+07-02-016, NGC0224,
PGC002557, UGC00454, UZC004000+41000
61
Repérable à l’œil nu, la « nébuleuse » d’Andromède est certainement connue
depuis l’Antiquité bien que sa première évocation reste à ce jour celle de
l’astronome perse Abdul Rahman al Suphi (904 - 986) qui la répertoria dans
son Livre des étoiles fixes en 964 sous l’appellation de « Petit nuage ».
C’est William Cranch Bond, en 1847, qui parvient le premier à discerner à
l’aide d’un télescope de 38 cm de diamètre les « canaux de Bond ». De nature
encore inconnue, ces structures se révéleront être des zones obscurcies par
des poussières, caractéristiques fondamentales des galaxies spirales. Le doute
sur la non-appartenance de M 31 à notre système galactique ne sera levé par
Edwin Hubble qu’en 1925. Par l’analyse de quelques céphéides, il estima alors
sa distance à 750 000 années de lumière. Depuis, une meilleure calibration de
ces étoiles pulsantes a permis de tripler cette distance.
La galaxie d’Andromède possède deux galaxies satellites visibles à l’aide d’un
petit télescope. Elles sont également répertoriées dans le catalogue Messier :
M 32 et M 110. Elle se rapproche de notre Voie lactée à une vitesse de
299 km.s-1. Une supernova y fut découverte le 17 août 1885, elle atteignit la
magnitude 5,8.
62
Messier 32 Galaxie elliptique
Découverte : Guillaume Le Gentil de La Galaisière (1749)
Ascension Droite : 00h 42m 41,79s Déclinaison : +40° 51’ 54,4"
Magnitude : 8,13 ± 0,12 Distance : 2,2 × 106 a.l.
Classe : E2 Dimension : 11,0’ × 7,3’
Constellation : Andromède Visibilité : Automne
Autres appellations : 2MASXJ00424182+4051546, ARK012, ARP168,
CGCG535-016, IRAS00399+4035, LGG011:[G93]008, MCG+07-02-015,
NGC0221, PGC002555, UGC00452, UZC003954+40360
63
Cette galaxie satellite de M 31 est également découverte par Guillaume
Le Gentil de La Galaisière en même temps que M 110, le 20 octobre 1749.
De notre position, elle semble posée sur les bras spiraux de Messier 31. Les
mesures spectroscopiques ne montrant aucune absorption de sa lumière, il est
légitime de penser qu’elle se situe plus proche de notre direction.
Cette galaxie naine elliptique, composée de vieilles étoiles, se rapproche de la
Voie lactée à raison de 205 km.s-1. Contrairement à Messier 110, aucun amas
globulaire n’y a été identifié ; en revanche, quelques nébuleuses planétaires ont
été repérées.
Visible à 22’ au sud du centre de Messier 31, Messier 32 est identifiable sous
la forme d’une tache légèrement ovoïde au travers d’un modeste instrument.
64
Messier 33 Galaxie spirale
Découverte : Charles Messier (1764)
Ascension Droite : 01h 33m 50,91s Déclinaison : +30° 39’ 35,5"
Magnitude : 5,79 ± 0,09 Distance : 2,7 × 106 a.l.
Classe : SAcd Dimension : 67’ × 41’
Constellation : Triangle Visibilité : Automne
Autres appellations : Galaxie du Triangle, 2MASXJ01335090+3039357,
AGC001117, CGCG502-110, HIJASSJ0133+30, LGG011:[G93]002,
MCG+05-04-069, NGC0598, PGC005818, UGC01117, UZC013100+30240
65
Galaxie spirale vue de face et très étendue : le grand axe vaut deux diamètres
lunaires. Malgré ce que sa magnitude laisse espérer, elle est assez difficile à
observer car peu contrastée en raison de cette généreuse dispersion. Répertoriée
par Charles Messier le 25 août 1764, il faudra attendre 1850 pour que la
structure spirale de la « Galaxie du Triangle » soit mise en évidence par
William Parsons à l’aide de son célèbre Leviathan de 183 cm de diamètre.
Elle fait partie d’un groupe d’une trentaine de galaxies constituant le « Groupe
local ». La galaxie d’Andromède (M 31), le Petit nuage de Magellan dans la
constellation du Toucan, le Grand nuage de Magellan dans la Dorade et notre
Voie lactée en font également partie.
C’est une galaxie jeune essentiellement composée d’étoiles bleues, elle s’éloigne
de nous à la vitesse de 180 km.s-1. Sa distance reste mal évaluée, les valeurs
oscillent entre 2,4 et 3 millions d’années de lumière. Des résidus de supernovæ
y ont été retrouvés.
66
Messier 34 Amas ouvert
Découverte : Giovanni Battista Hodierna (1654)
Ascension Droite : 02h 42m 05,00s Déclinaison : +42° 45’ 41,8"
Magnitude : 5,20 ± 0,10 Distance : 1 500 a.l.
Classe : II 3 m Dimension : Ø 35’
Constellation : Persée Visibilité : Automne
Autre appellation : NGC1039
67
Giovanni Battista Hodierna est probablement le premier à observer cet amas
ouvert en 1654. Il sera (re)découvert par Charles Messier le 25 août 1764.
Dans un ciel bien noir, il peut être repéré à l’œil nu. Composé d’environ 2 500
étoiles, son âge est estimé à 180 millions d’années.
68
Messier 35 Amas ouvert
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 06h 08m 57,95s Déclinaison : +24° 21’ 14,0"
Magnitude : 5,10 ± 0,10 Distance : 2 800 a.l.
Classe : III 2 m Dimension : Ø 28’
Constellation : Gémeaux Visibilité : Hiver
Autre appellation : NGC2168
69
Amas ouvert découvert indépendamment par le français Jean Philippe Loys
de Chéseaux en 1746 et l’anglais John Bevis vers 1750, il sera intégré dans
son catalogue par Charles Messier le 30 août 1764.
Le repérage de M 35 ne pose pas de problème, il est aisément repérable à un
peu plus de 2° au nord-ouest de l’étoile η. Son âge est estimé à 100 000 000 ans.
Un autre amas, plus petit car situé cinq fois plus loin, est vu vers le sud-ouest :
il est répertorié sous l’appellation NGC 2158.
70
Messier 36 Amas ouvert
Découverte : Guillaume Le Gentil de La Galaisière (1749)
Ascension Droite : 05h 36m 17,70s Déclinaison : +34° 08’ 27,0"
Magnitude : 6,00 ± 0,10 Distance : 4 100 a.l.
Classe : II 3 m Dimension : Ø 12’
Constellation : Cocher Visibilité : Hiver
Autre appellation : NGC1960
71
Objet découvert par Guillaume Le Gentil de La Galaisière en 1749, il sera
observé par Charles Messier le 2 septembre 1764.
L’âge de l’amas est estimé à 25 000 000 ans.
72
Messier 37 Amas ouvert
Découverte : Giovanni Battista Hodierna (1654)
Ascension Droite : 05h 52m 18,30s Déclinaison : +32° 33’ 11,0"
Magnitude : 5,60 ± 0,10 Distance : 4 400 a.l.
Classe : II 1 r Dimension : Ø 22’
Constellation : Cocher Visibilité : Hiver
Autre appellation : NGC2099
73
Observé par Giovanni Battista Hodierna vers 1654 et retrouvé par Charles
Messier 110 ans plus tard.
Il est plus ancien que le précédent : 300 000 000 ans.
74
Messier 38 Amas ouvert
Découverte : Guillaume Le Gentil de La Galaisière (1749)
Ascension Droite : 05h 28m 40,01s Déclinaison : +35° 50’ 54,0"
Magnitude : 6,40 ± 0,10 Distance : 4 300 a.l.
Classe : III 2 m Dimension : Ø 21’
Constellation : Cocher Visibilité : Hiver
Autre appellation : NGC1912
75
Découvert, en même temps que son homologue M 36, par Guillaume Le Gentil
de La Galaisière en 1749, il sera également observé par Charles Messier en
1764.
L’âge de l’amas est de 220 000 000 ans.
76
Messier 39 Amas ouvert
Découverte : Aristote (vers −350)
Ascension Droite : 21h 31m 45,16s Déclinaison : +48° 25’ 57,3"
Magnitude : 4,60 ± 0,10 Distance : 830 a.l.
Classe : III 2 m Dimension : Ø 31’
Constellation : Cygne Visibilité : Été
Autre appellation : NGC7092
77
Charles Messier, notre infatigable observateur remarqua cet amas ouvert en
1764, alors qu’il s’appliquait toujours à son activité favorite : la recherche de
comètes. Mais il ne possède pas la primeur de son observation, Guillaume
Le Gentil de La Galaisière l’avait déjà scruté en 1750 et Aristote (384 - 322
av. J.-C.) vers −350.
D’un diamètre réel estimé à 7,5 années de lumière, l’amas est pauvre en
étoiles et assez dispersé. D’une luminosité globale équivalente à 830 soleils, sa
magnitude absolue est de −2,5.
78
Messier 40 Étoile double
Découverte : Johan Hœvelke (16 ? ?)
Ascension Droite : 12h 22m 12,53s Déclinaison : +58° 04’ 58,6"
Magnitude : 9,0 et 9,3 Distance : 510 a.l.
Classe : - - Séparation : 50"
Constellation : Grande Ourse Visibilité : Circumpolaire
Autre appellation : Winnecke 4
79
Suivant le rapport de la découverte d’une nébuleuse rapportée auparavant par
Johannes Hewel (Hévélius), Charles Messier en explorant la zone mentionnée
ne retrouva qu’un couple d’étoiles séparées de 50” (Winnecke 4). Pour éviter
toute confusion ultérieure, il l’intégra cependant à son catalogue le 24 octobre
1764.
À noter que la galaxie NGC 4290 est visible à environ 2’ de la position de
Winnecke 4.
80
Messier 41 Amas ouvert
Découverte : Giovanni Battista Hodierna (avant 1654)
Ascension Droite : 06h 46m 00,02s Déclinaison : −20° 45’ 19,5"
Magnitude : 4,50 ± 0,10 Distance : 2 350 a.l.
Classe : II 3 m Dimension : Ø 38’
Constellation : Grand Chien Visibilité : Hiver
Autre appellation : NGC2287
81
Charles Messier répertoria M 41 dans son catalogue le 16 janvier 1765. Il
fut déjà observé en 1702 par John Flamsteed, puis en 1749 par Guillaume
Le Gentil de La Galaisière. Depuis 1984, date de la découverte de manuscrits
originaux ayant appartenu à Giovanni Battista Hodierna, on sait que ce dernier
les avait tous devancés avant 1654.
L’âge de l’amas est estimé à 200 000 000 ans.
Bien que restant assez bas sur l’horizon, même lors de son passage au méridien,
M 41 est l’un des objets les plus faciles à repérer, il se situe à 4° au sud de
Sirius, la plus brillante étoile de tout le ciel.
Au centre de l’amas, une étoile de magnitude 7 montre une coloration orangée,
elle est surnommée l’« étoile d’Espin ». Thomas Henry Espinell Compton
Espin, un pasteur et astronome amateur anglais, spécialiste des étoiles doubles,
s’est également illustré dans le recensement des étoiles carbonées. Celle qui
porte son nom est 400 fois plus lumineuse que notre Soleil.
L’étoile la plus brillante de l’amas, vue vers le sud-est est quant à elle située à
une distance de 1 100 années de lumière et n’appartient donc pas à M 41.
82
Messier 42 Nébuleuse à émission
Découverte : Nicolas Claude Fabri de Peyresc (1611)
Ascension Droite : 05h 35m 17,19s Déclinaison : −05° 23’ 26,9"
Magnitude : - - Distance : 1 350 a.l.
Classe : - - Dimension : 65’ × 60’
Constellation : Orion Visibilité : Hiver
Autres appellations : Grande nébuleuse d’Orion, 3C145, 4C-05.21,
MRC0532-054, NGC1976
83
Nébuleuse à émission facilement repérable avec une simple paire de jumelles,
M 42 fut découverte par le français Nicolas Claude Fabri de Peyresc en 1611.
Elle sera retrouvée indépendamment sept ans plus tard par le mathématicien
et astronome suisse Jean Baptiste Cysat et le célèbre Christiaan Huygens en
tracera un sommaire dessin en 1656.
Charles Messier en fera le premier portrait détaillé, publié en 1771, qui sera
malheureusement bien mal rendu par une technique d’imprimerie encore
balbutiante.
La première photographie de celle qui allait très vite devenir une véritable
icône de l’astronomie est faite par Henry Draper le 30 septembre 1880. Un
exploit technique pour l’époque, réalisé avec une lunette de 280 mm et un
temps de pose de 51 minutes.
Il s’agit d’une immense pouponnière d’étoiles qui contient suffisamment de
matière pour fabriquer 10 000 soleils. Des photographies prisent à quelques années d’intervalle ont permis de mettre en évidence d’infimes changements dans
quelques concentrations gazeuses en effondrement gravitationnel (proplyds).
84
Messier 43 Nébuleuse à émission
Découverte : Jean-Jacques d’Ortous de Mairan (1731)
Ascension Droite : 05h 35m 31,31s Déclinaison : −05° 16’ 03,0"
Magnitude : - - Distance : 1 600 a.l.
Classe : - - Dimension : 20’ × 15’
Constellation : Orion Visibilité : Hiver
Autre appellation : NGC1982
85
Contrairement à la description faite par Charles Messier, qui l’intégra dans son
catalogue le 4 mars 1769 et la perçue comme une faible nébuleuse indépendante
de M 42, il s’agit bien d’une extension de la Grande nébuleuse d’Orion.
Elle fut auparavant repérée par Jean-Jacques d’Ortous de Mairan, comme en
témoigne un de ses dessins datant de 1731 et publié deux ans plus tard.
86
Messier 44 Amas ouvert
Découverte : Aratos de Soles (vers −260)
Ascension Droite : 08h 40m 09,71s Déclinaison : +19° 40’ 20,1"
Magnitude : 3,10 ± 0,10 Distance : 525 a.l.
Classe : II 2 m Dimension : Ø 95’
Constellation : Cancer Visibilité : Hiver
Autres appellations : Amas de la Crèche, Amas de la Ruche, NGC2632,
Præsepe
87
Également connu sous les noms de amas de la Crèche ou de la Ruche, cet objet
est discernable à l’œil nu et devient évident avec une simple paire de jumelle.
Centré à l’ouest des étoiles γ et δ, ce « petit brouillard » comme le décrivait le
poète grec Aratos de Soles (315 - 245 av. J.-C.) au IIIe
siècle avant notre ère,
est connu depuis l’Antiquité sous le nom de Præsepe (la Mangeoire, en latin).
Les Arabes l’appelèrent également Al Ma’laf qui désigne le sac de fourrage
que l’on accrochait autour du cou de ces animaux.
Charles Messier le répertoria dans son catalogue en 1769. On estime au moins
à 350 le nombre d’étoiles qui le compose. Il a une similitude de mouvement
avec son homologue du Taureau : les Hyades (Melotte 25), dont il est séparé
par 450 années de lumière.
88
Messier 45 Amas ouvert
Découverte : - - (−2357)
Ascension Droite : 03h 46m 60,00s Déclinaison : +24° 07’ 00,12"
Magnitude : 1,2 Distance : 440 a.l.
Classe : I 3 r (n) Dimension : Ø 110’
Constellation : Taureau Visibilité : Hiver
Autres appellations : Melotte 22, Pléiades, les Sept Sœurs
89
Amas ouvert connu depuis la plus haute Antiquité, il faudra attendre les grecs
pour affubler ses sept étoiles visibles à l’œil nu des noms des sept sœurs des
Pléiades. Les estimations modernes ont portées cette valeur à 2 000 étoiles.
L’amas est très jeune, seulement 78 millions d’années, et semble encore baigner
dans la nébulosité qui lui a donné naissance. Cependant, des études récentes
semblent démontrer que l’ensemble de l’amas et la nébuleuse n’ont pas la
même vitesse apparente. Leur rencontre serait donc fortuite.
Les Pléiades se présentent avec un diamètre pratiquement équivalent à quatre
fois celui de la Lune. La densité de l’amas est donc faible et il devrait se
disperser dans les 250 millions d’années.
90
91
Ajouts seconde compilation :
objets 46 à 103
92
Messier 46 Amas ouvert
Découverte : Charles Messier (1771)
Ascension Droite : 07h 41m 46,81s Déclinaison : −14° 48’ 35,9"
Magnitude : 6,10 ± 0,10 Distance : 5 400 a.l.
Classe : II 2 r Dimension : Ø 27’
Constellation : Poupe Visibilité : Hiver
Autre appellation : NGC2437
93
Découvert par Charles Messier le 19 février 1771, cet amas ouvert débute la
deuxième partie de son catalogue.
William Herschel fut le premier à remarquer la présence d’une nébuleuse
planétaire (NGC 2438) se superposant à l’amas par effet de perspective, cette
dernière se positionnant à 2 900 années de lumière de la Terre.
Pour une luminosité globale équivalente à 9 000 soleils, la taille réelle de l’amas
est de 40 années de lumière. Il est âgé de 300 millions d’années.
94
Messier 47 Amas ouvert
Découverte : Giovanni Battista Hodierna (1654)
Ascension Droite : 07h 36m 35,01s Déclinaison : −14° 28’ 51,9"
Magnitude : 4,40 ± 0,10 Distance : 1 600 a.l.
Classe : I 2 m Dimension : Ø 29’
Constellation : Poupe Visibilité : Hiver
Autre appellation : NGC2422
95
La découverte de cet amas ouvert est certainement à mettre à l’actif de
Giovanni Battista Hodierna en 1654.
Sur la zone correspondant aux coordonnées notées par Charles Messier en
1771 il n’existe aucun objet répondant à sa description : « Amas proche du
précédent, contenant des étoiles peu lumineuses. »
Il s’agit selon toute apparence d’une erreur de notation faite par l’astronome,
l’amas réellement observé étant vraisemblablement NGC 2422 qui se trouve
juste à l’est de M 46. Le diamètre réel de l’amas est de l’ordre de 1 700 années
de lumière, son âge est estimé entre 25 et 30 millions d’années.
96
Messier 48 Amas ouvert
Découverte : Charles Messier (1771)
Ascension Droite : 08h 13m 43,11s Déclinaison : −05° 45’ 01,9"
Magnitude : 5,80 ± 0,10 Distance : 1 500 a.l.
Classe : I 3 r Dimension : Ø 54’
Constellation : Hydre Visibilité : Printemps
Autre appellation : NGC2548
97
Charles Messier a parfois commis quelques erreurs sur les coordonnées de
certains objets qu’il observait. M 48 ne déroge pas à cette règle – voir également
M 91 et M 102. L’objet qu’il a découvert le 19 février 1771 et correspondant à
sa description est bien retrouvé, par Carolyn Herschel en 1783, à l’ascension
droite qu’il a noté, mais avec un écart de 5° en déclinaison.
Constitué d’environ 80 étoiles, sa luminosité globale est équivalente à une
centaine de soleils, pour un diamètre réel de 24 années de lumière.
98
Messier 49 Galaxie elliptique
Découverte : Charles Messier (1771)
Ascension Droite : 12h 29m 46,70s Déclinaison : +07° 59’ 59,2"
Magnitude : 8,28 ± 0,23 Distance : 56 × 106 a.l.
Classe : E2 Dimension : 8,1’ × 7,1’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12294679+0800014, ACSVCS001, ARP134,
CGCG042-134, EVCC0755, GIN781, LGG292:[G93]015, MCG+01-32-083,
NGC4472, PGC041220, SDSSJ122946.76+080001.7, UGC07629,
UZC122712+08160, VCC1226
99
Galaxie elliptique découverte par Charles Messier le 19 février 1771, alors qu’il
recherchait une comète dans les parages.
Elle fut indépendamment observée quelques jours plus tard par l’italien
Barnaba Oriani, depuis la ville de Milan (il en dirigera l’observatoire entre
1802 et 1832) où la pollution lumineuse n’était pas encore d’actualité ! Il n’avait
alors que 19 ans et était à la recherche de la même comète. Repérable aux
jumelles 10×50, c’est l’élément le plus « lumineux » de l’amas de la Vierge.
Une supernova de magnitude 13,0 y a été observée en juin 1969.
100
Messier 50 Amas ouvert
Découverte : Charles Messier (1771)
Ascension Droite : 07h 02m 42,16s Déclinaison : −08° 23’ 12,9"
Magnitude : 5,90 ± 0,10 Distance : 2 900 a.l.
Classe : II 3 m Dimension : Ø 16’
Constellation : Licorne Visibilité : Hiver
Autre appellation : NGC2323
101
Amas ouvert repéré par Jean-Dominique Cassini en 1711, le premier d’une
lignée d’astronomes et également le premier directeur de l’observatoire de
Paris créé par Louis XIV. Charles Messier l’explorera le 5 avril 1772.
Avec un diamètre réel de 14 années de lumière, la luminosité globale de l’amas
équivaut à 6 400 soleils, son âge est estimé à 78 000 000 ans.
102
Messier 51 Galaxie spirale barrée
Découverte : Charles Messier (1773)
Ascension Droite : 13h 29m 52,71s Déclinaison : +47° 11’ 42,7"
Magnitude : 10,72 ± 2,58 Distance : 27 × 106 a.l.
Classe : SABb pec Dimension : 6,4’ × 4,6’
Constellation : Chiens de chasse Visibilité : Printemps
Autres appellations : Galaxie du Tourbillon, Whirlpool,
2MASXJ13295269+4711429, ARP085, CGCG246-008, IRAS13277+4727,
KPG379A, LGG347:[G93]004, MCG+08-25-012, NGC5194, PGC047404,
UGC08493, UZC132748+47270, VV001, VV403
103
Cette galaxie fut repérée par Charles Messier le 13 octobre 1773. Pierre
Méchain qui observera sa nature « double » en 1781.
Au début de l’année 1845, William Parsons parvint à deviner sa structure en
spirale. En 1860, le révérend anglais Thomas William Webb fut le premier à
distinguer le « pont » de matière semblant relier les deux galaxies.
Suivant les études les plus récentes, la plus petite (NGC 5195) est située bien
en arrière de M 51 et le bras qui semble les raccorder n’est qu’un simple effet
de projection bien que sa formation résulte des forces de marées engendrées
lors d’un passage rapproché du couple.
Bien qu’appartenant à la constellation des Chiens de chasse, le repérage de
M 51 est plus facile à partir des étoiles ζ et η qui forment l’extrémité de la
queue de la Grande Ourse. La galaxie forme un triangle rectangle avec ces
deux étoiles, Mizar et Alkaïd, et il est possible de la retrouver en se déplaçant
de la moitié de leur distance en direction du sud-ouest. Messier 51 est déjà
repérable aux jumelles 10×50 sur un fond de ciel bien noir, mais il faut une
ouverture d’au-moins 200 mm pour commencer à apprécier sa structure en
spirale.
104
Messier 52 Amas ouvert
Découverte : Charles Messier (1774)
Ascension Droite : 23h 24m 49,21s Déclinaison : +61° 35’ 59,8"
Magnitude : 6,90 ± 0,10 Distance : 4 900 a.l.
Classe : I 2 r Dimension : Ø 12’
Constellation : Cassiopée Visibilité : Circumpolaire
Autre appellation : NGC7654
105
Le 7 septembre 1774, alors qu’il suivait le passage d’une comète dans ces
parages, Charles Messier observa « un amas de très petites étoiles » qu’il
répertoria sous le numéro 52.
L’amas est compact et se superpose sur la Voie lactée dont il se distingue
difficilement. Pour cette même raison, sa distance reste très mal évaluée en
raison d’une forte extinction interstellaire ; les différentes mesures donnent des
valeurs comprises entre 3 000 et 7 000 années de lumière. Avec un âge estimé à
10 000 000 ans, c’est l’un des plus jeunes amas ouverts essentiellement composé
de géantes bleues.
Le pointage de M 52 peut se réaliser en prolongeant d’un peu plus d’une fois
la distance séparant les étoiles α (Schedar) et β (Caph) de la constellation.
L’amas se situe à 40’ au sud de l’étoile 4 Cas (magnitude 5). Une étoile plus
proche de nous, de teinte jaune-orangée et de magnitude 8,3, est visible sur le
flanc ouest de l’amas.
106
Messier 53 Amas globulaire
Découverte : Johann Bode (1775)
Ascension Droite : 13h 12m 55,28s Déclinaison : +18° 10’ 08,9"
Magnitude : 7,70 ± 0,10 Distance : 58 000 a.l.
Classe : V Dimension : Ø 12,6’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : NGC5024, PGC2802648
107
Cet amas globulaire est découvert par l’astronome allemand Johann Bode le
3 février 1775, il fut redécouvert de façon totalement indépendante par Charles
Messier le 26 février 1777.
Si Messier 53 est repérable aux jumelles 10×50 sous la forme d’un petite tache
ronde diffuse, il faudra une ouverture d’au moins 250 mm pour commencer
à le résoudre en périphérie. L’amas se rapproche de nous à la vitesse de
112 km.s-1, sa luminosité globale est équivalente à 330 000 fois celle du Soleil.
Une cinquantaine d’étoiles variables de type RR Lyræ y ont été observées.
À 1° vers le sud-ouest, et avec une ouverture d’au moins 200 mm, il est
possible de repérer un autre amas globulaire : NGC 5053. Découvert par
William Herschel en 1754, il est bien moins riche que la grande majorité des
amas globulaires (environ 3 000 étoiles), au point d’avoir été classé au début
comme un riche amas ouvert composé d’étoiles faibles. Il se situe à 54 000
années de lumière, mais sa luminosité globale n’excède pas 21 000 soleils.
Objet plus « lumineux » que les galaxies environnantes, le repérage de M 53
est également facilité par sa proximité avec l’étoile α de la constellation : il se
situe à un peu moins de 1° au nord-est.
108
Messier 54 Amas globulaire
Découverte : Charles Messier (1778)
Ascension Droite : 18h 55m 03,30s Déclinaison : −30° 28’ 42,4"
Magnitude : 7,70 ± 0,10 Distance : 87 400 a.l.
Classe : III Dimension : Ø 9,1’
Constellation : Sagittaire Visibilité : Été
Autres appellations : NGC6715, PGC2802337
109
Amas globulaire observé par Charles Messier le 24 juillet 1778, sans toutefois
parvenir à le résoudre.
Cet amas appartient à la galaxie naine du Sagittaire (découverte en 1994,
elle est désignée sous l’appellation SagDEG, pour Sagittarius Dwarf Elliptical
Galaxy), une galaxie satellite de notre Voie lactée qui est en train de la
« phagocyter ».
110
Messier 55 Amas globulaire
Découverte : Nicolas de Lacaille (1751)
Ascension Droite : 19h 39m 59,37s Déclinaison : −30° 57’ 43,4"
Magnitude : 6,30 ± 0,10 Distance : 17 000 a.l.
Classe : XI Dimension : Ø 19,0’
Constellation : Sagittaire Visibilité : Été
Autres appellations : 2MASSJ19395930-3057423, NGC6809, PGC2802695
111
Découvert par l’abbé Nicolas de Lacaille en 1751, il ne sera redécouvert par
Charles Messier que le 24 juillet 1778.
Visible bas sur l’horizon depuis une latitude moyenne de 45° Nord, M 55 n’est
cependant pas à négliger et reste l’un des amas globulaires les plus faciles à
résoudre en étoiles. Pour avoir une chance de l’observer, il faut privilégier son
passage au méridien, la culmination la plus favorable se situant entre mi-août
et mi-septembre. Situé dans une zone dépourvue d’étoile repère nettement
visible, le repérage de l’amas est assez délicat et une carte précise de la zone
sera une aide nécessaire.
112
Messier 56 Amas globulaire
Découverte : Charles Messier (1779)
Ascension Droite : 19h 16m 35,52s Déclinaison : +30° 11’ 04,6"
Magnitude : 8,40 ± 0,10 Distance : 32 900 a.l.
Classe : X Dimension : Ø 7,1’
Constellation : Lyre Visibilité : Été
Autres appellations : NGC6779, PGC2802694
113
Amas globulaire découvert par Charles Messier le 19 janvier 1779 alors qu’il
recherchait une comète découverte par Johann Bode le 6 du même mois.
114
Messier 57 Nébuleuse planétaire
Découverte : Antoine Augustin Darquier de Pellepoix (1779)
Ascension Droite : 18h 53m 35,01s Déclinaison : +33° 01’ 44,9"
Magnitude : 8,80 ± 0,10 Distance : 2 300 a.l.
Classe : - - Dimension : Ø 71"
Constellation : Lyre Visibilité : Été
Autres appellations : Nébuleuse annulaire, Anneau de la Lyre, NGC6720
115
Découverte par le toulousain Antoine Augustin Darquier de Pellepoix en 1779,
la nébuleuse annulaire de la Lyre est l’exemple le plus connu de nébuleuse
planétaire.
Il s’agit d’une étoile très évoluée et très chaude (100 000 kelvins), entourée
d’une enveloppe gazeuse en expansion qu’elle a elle-même éjectée il y a entre
6 000 et 10 000 ans. Désignant pendant un temps le siège supposé de formation planétaire, l’impropre terme « nébuleuse planétaire » repris par William
Herschel pour désigner ce type d’objet était né.
116
Messier 58 Galaxie spirale barrée
Découverte : Charles Messier (1779)
Ascension Droite : 12h 37m 43,54s Déclinaison : +11° 49’ 05,5"
Magnitude : 10,30 ± 0,99 Distance : 65 × 106 a.l.
Classe : SABb Dimension : 5,5’ × 4,6’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12374359+1149051, AGC007796,
CGCG070-197, EVCC0965, IRAS12351+1205, IRAS12352+1205,
LGG289:[G93]047, MCG+02-32-160, NGC4579, PGC042168,
SDSSJ123743.52+114905.4, UGC07796, UZC123512+12050, VCC1727,
[RG2008]J189.43137+11.81818, [TH2002]007
117
Galaxie spirale barrée découverte par Charles Messier le 15 avril 1779.
Elle fut le siège de supernovæ observées les 16 janvier 1988 et 28 juin 1989.
Elles atteignirent respectivement les magnitudes 13,5 et 12,2.
118
Messier 59 Galaxie elliptique
Découverte : Gottfried Kœhler (1779)
Ascension Droite : 12h 42m 02,25s Déclinaison : +11° 38’ 50,4"
Magnitude : 9,56 ± 0,11 Distance : 65 × 106 a.l.
Classe : E5 Dimension : 4,6’ × 3,6’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12420232+1138489, ACSVCS009,
CGCG070-223, EVCC2207, MCG+02-32-183, NGC4621, PGC042628,
SDSSJ124202.25+113848.8, UGC07858, UZC123930+11550, VCC1903,
[RG2008]J190.50940+11.64691, [TH2002]008
119
Galaxie elliptique découverte par Johann Gottfried Kœhler, depuis la ville de
Dresde, alors qu’il observait une comète le 11 avril 1779.
Une supernova y a été observée le 19 mai 1939, elle se porta à la magnitude
11,9 au maximum.
120
Messier 60 Galaxie elliptique
Découverte : Gottfried Kœhler (1779)
Ascension Droite : 12h 43m 39,97s Déclinaison : +11° 33’ 10,0"
Magnitude : 8,79 ± 0,16 Distance : 65 × 106 a.l.
Classe : E2 Dimension : 7,1’ × 6,1’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12434000+1133093, ACSVCS003, ARP116,
CGCG071-016, EVCC1101, KPG353B, LGG292:[G93]026, MCG+02-33-002,
NGC4649, NIBLES1717, PGC042831, SDSSJ124339.97+113309.7, UGC07898,
UZC124106+11500, VCC1978, VV206
121
Cette autre galaxie elliptique fut découverte en même temps que M 59 par
Johann Gottfried Kœhler alors qu’il observait une comète le 11 avril 1779.
Cette comète de 1779 occulta même M 60 dont l’éclat ne fut plus perceptible
pendant deux nuits consécutives.
Elle fut également observée le lendemain par Barnaba Oriani – sans qu’il ne
repère M 59 – et quatre jours plus tard, le 15 avril 1779, par Charles Messier,
qui la décrivit comme « un peu plus apparente que les deux précédentes ».
Une autre galaxie, NGC 4647, est vue angulairement proche.
122
Messier 61 Galaxie spirale barrée
Découverte : Barnaba Oriani (1779)
Ascension Droite : 12h 21m 54,83s Déclinaison : +04° 28’ 25,8"
Magnitude : 10,25 ± 1,21 Distance : 65 × 106 a.l.
Classe : SABbc Dimension : 6,0’ × 5,9’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12215494+0428249, AGC007420, CGCG042-045,
EVCC0429, HIPASSJ1221+04, IRAS12193+0444, IRAS12194+0444,
LGG287:[G93]002, MCG+01-32-022, MRC1219+047, NGC4303, PGC040001,
SDSSJ122154.92+042825.6, UGC07420, UZC121918+04450, VCC0508
123
Galaxie découverte par Barnaba Oriani (1752 - 1832) le 5 mai 1779 en recherchant une comète sur cette zone. Charles Messier la verra la même nuit
persuadé d’observer la comète de 1779, il lui fallut deux autres observations
avant de se rendre compte que l’objet repéré ne se déplaçait pas.
Des supernovæ y ont été observées les 9 mai 1926, 3 juin 1961 et en juin 1964.
Aucune ne dépassa la magnitude 13,0.
Un grand nombre de petites galaxies entoure M 61, elles ne se laisseront
admirer que sur des photographies à long temps de pose.
124
Messier 62 Amas globulaire
Découverte : Charles Messier (1771)
Ascension Droite : 17h 01m 12,64s Déclinaison : −30° 06’ 44,0"
Magnitude : 6,40 ± 0,10 Distance : 20 500 a.l.
Classe : IV Dimension : Ø 14,1’
Constellation : Ophiuchus Visibilité : Été
Autres appellations : NGC6266, PGC2802666
125
À nouveau une découverte de Charles Messier datée du 7 juin 1771. Cet amas
globulaire, situé à la limite du Scorpion dans lequel il est parfois classé, serait
l’un des plus proches du centre galactique.
Sa magnitude absolue est de −8,8, ce qui correspond à une luminosité globale
de 276 000 soleils.
126
Messier 63 Galaxie spirale
Découverte : Pierre Méchain (1779)
Ascension Droite : 13h 15m 49,31s Déclinaison : +42° 01’ 45,6"
Magnitude : 8,61 ± 0,04 Distance : 35 × 106 a.l.
Classe : SAbc Dimension : 13,5’ × 8,3’
Constellation : Chiens de chasse Visibilité : Printemps
Autres appellations : Galaxie Tournesol, 2MASXJ13154932+4201454,
CGCG217-023, IRAS13135+4217, LGG347:[G93]002, MCG+07-27-054,
NGC5055, PGC046153, SDSSJ131549.26+420145.8, UGC08334,
UZC131330+42170
127
La première d’une longue série de découvertes à mettre au compte de Pierre
Méchain. Elle sera observée par Charles Messier le 14 juin 1779.
Une supernova qui atteignit la magnitude 11,5, observée le 24 mai 1971 dans
un de ses innombrables bras spiraux, a permis d’en déduire sa distance.
128
Messier 64 Galaxie spirale barrée
Découverte : Edward Pigott (1779)
Ascension Droite : 12h 56m 43,69s Déclinaison : +21° 40’ 55,8"
Magnitude : 9,54 ± 1,63 Distance : 16 × 106 a.l.
Classe : SABa Dimension : 9,2’ × 4,6’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : L’Œil noir, 2MASXJ12564369+2140575,
ADBSJ125711+2135, AGC008062, CGCG130-001, EVCC2248,
HIPASSJ1256+21, IRAS12542+2157, KIG0559, MCG+04-31-001, NGC4826,
PGC044182, UGC08062, UZC125412+21570
129
Galaxie spirale observée indépendamment par l’anglais Edward Pigott le
23 mars 1779 et l’allemand Johann Bode le 4 avril, alors devenu directeur de
l’observatoire de Berlin. Elle fut également retrouvée indépendamment par
Charles Messier l’année suivante, sans qu’il eut vent de son existence.
Déjà repérable aux jumelles 10×50 sous la forme d’une étoile diffuse, il faut
cependant un télescope de 200 mm pour commencer à distinguer la bande
sombre qui borde le noyau et lui vaut son nom commun : l’Œil noir. Cette
structure est composée de poussières qui absorbent le rayonnement des étoiles
situées en arrière-plan.
La distance de M 64 est encore sujette à caution, aucun indicateur de distance
(supernova) ne s’y est manifesté, les différentes sources donnent des valeurs
comprises entre 12 et... 44 millions d’années de lumière.
Le repérage de Messier 64 peut se faire à partir de la discrète étoile α de la
constellation (magnitude 4,3). En se déplaçant vers le nord-ouest d’environ 5°,
il est possible de retrouver l’étoile 35 Com au chercheur, M 64 est situé à 1°
au nord-est.
130
Messier 65 Galaxie spirale barrée
Découverte : Pierre Méchain (1780)
Ascension Droite : 11h 18m 55,92s Déclinaison : +13° 05’ 32,5"
Magnitude : 9,32 ± 0,11 Distance : 31 × 106 a.l.
Classe : SABa Dimension : 8,7’ × 2,2’
Constellation : Lion Visibilité : Printemps
Autres appellations : 2MASXJ11185595+1305319, ADBSJ111852+1305,
AGC006328, ARP317, CGCG067-054, IRAS11163+1322, LGG231:[G93]002,
MCG+02-29-018, NGC3623, PGC034612, SDSSJ111855.91+130532.3,
UGC06328, UZC111618+13220, VV308
131
Galaxie spirale, vue de trois-quarts, découverte par Pierre Méchain le 1er mars
1780.
Son diamètre est de 80 000 années de lumière, la magnitude absolue est de
−20,6, ce qui correspond à une luminosité de 15 milliards de soleils à une
distance de 31 millions d’années de lumière.
M 65 se repère facilement au milieu du segment joignant les étoiles θ et ι. Ces
deux étoiles sont visibles à l’œil nu, elles sont respectivement de magnitude
3,3 et 4,0.
132
Messier 66 Galaxie spirale barrée
Découverte : Pierre Méchain (1780)
Ascension Droite : 11h 20m 15,02s Déclinaison : +12° 59’ 30,0"
Magnitude : 10,31 ± 1,45 Distance : 31 × 106 a.l.
Classe : SABb Dimension : 8,2’ × 3,9’
Constellation : Lion Visibilité : Printemps
Autres appellations : 2MASXJ11201502+1259286, ADBSJ112020+1259,
AGC006346, ARK288, ARP016, ARP317, CGCG067-057, HIPASSJ1120+13A,
IRAS11176+1315, LGG231:[G93]003, MCG+02-29-019, MRC1117+132,
NGC3627, PGC034695, SDSSJ112014.98+125929.4, UGC06346,
UZC111736+13160
133
Galaxie découverte en même temps que M 65 par Pierre Méchain.
Dans la nuit du 1er au 2 novembre 1773, soit 7 ans avant l’observation faite par
Méchain, Charles Messier suivit le passage d’une comète dont la trajectoire
passa exactement entre ce couple de galaxies. M 65 et M 66 sont visibles dans
un même champ – seulement 21’ les sépare sur la voûte céleste – mais, en
raison de l’éclat de la comète, il ne put les distinguer.
M 66 a une magnitude absolue de −21. D’un diamètre réel de 75 000 années
de lumière, elle brille comme 21 milliards de soleils.
Des supernovæ y ont été observées les 19 décembre 1973 et 30 janvier 1989.
134
Messier 67 Amas ouvert
Découverte : Johann Gottfried Köhler (1772)
Ascension Droite : 08h 51m 10,06s Déclinaison : +11° 48’ 21,7"
Magnitude : 6,90 ± 0,10 Distance : 2 600 a.l.
Classe : II 2 m Dimension : Ø 10’
Constellation : Cancer Visibilité : Hiver
Autre appellation : NGC2682
135
Charles Messier observa cet amas ouvert le 6 avril 1780, cet objet avait déjà
été repéré comme « nébuleuse » par Johann Gottfried Köhler en 1772. Il est
l’un des plus vieux amas ouverts de la Galaxie : entre 4 et 5 milliards d’années.
La force gravitationnelle au sein de l’amas est donc élevée pour avoir évité
la totale dispersion de ses membres. Il contient au moins 500 étoiles jusqu’à
la magnitude 16 sur une surface équivalente à un demi diamètre lunaire. Sa
position est atypique car il est relativement éloigné du plan galactique, là où
se situent généralement les amas ouverts.
Un amas de galaxies, situé exactement dans l’alignement de M 67, a été
déniché par le télescope Keck.
Messier 67 est repérable à un peu moins de 2° à l’ouest de l’étoile α de la
constellation également appelée Acubens.
136
Messier 68 Amas globulaire
Découverte : Charles Messier (1780)
Ascension Droite : 12h 39m 28,02s Déclinaison : −26° 44’ 34,1"
Magnitude : 7,30 ± 0,10 Distance : 33 000 a.l.
Classe : X Dimension : Ø 12’
Constellation : Hydre Visibilité : Printemps
Autres appellations : HD110032, NGC4590, PGC2802647
137
Amas globulaire découvert par Charles Messier le 9 avril 1780. Quelques
variables, essentiellement des RR Lyræ y ont été repérées, permettant une
estimation de sa distance avec une relative précision.
Très bas sur l’horizon, vu depuis la France, il faut impérativement surveiller son
passage au méridien (et un ciel limpide) pour avoir une chance de l’observer.
Il se repère en prolongeant de la moitié de leur distance le segment qui relie
les étoiles δ et β de la constellation voisine du Corbeau. L’amas se trouve à
un demi-degré vers le nord-est d’une étoile de magnitude 5,5 (SAO 180965)
visible au chercheur.
138
Messier 69 Amas globulaire
Découverte : Nicolas de Lacaille (1752)
Ascension Droite : 18h 31m 23,18s Déclinaison : −32° 20’ 53,3"
Magnitude : 8,31 Distance : 33 000 a.l.
Classe : V Dimension : Ø 7,1’
Constellation : Sagittaire Visibilité : Été
Autres appellations : NGC6637, PGC2802688
139
Amas globulaire découvert depuis le Cap de Bonne Espérance par Nicolas
de Lacaille en 1752 et observé par Charles Messier le 31 août 1780.
140
Messier 70 Amas globulaire
Découverte : Charles Messier (1780)
Ascension Droite : 18h 43m 12,66s Déclinaison : −32° 17’ 31,2"
Magnitude : 7,80 ± 0,10 Distance : 34 000 a.l.
Classe : V Dimension : Ø 7,8’
Constellation : Sagittaire Visibilité : Été
Autres appellations : NGC6681, PGC2802690
141
Une découverte de Charles Messier le 31 août 1780, alors que l’objet ne
« culmine » qu’à moins de 10 degrés au dessus de l’horizon de Paris. Il parvint
même à y discerner quelques détails.
142
Messier 71 Amas globulaire
Découverte : Jean Philippe Loys de Chéseaux (1746)
Ascension Droite : 19h 53m 46,15s Déclinaison : +18° 46’ 41,8"
Magnitude : 8,40 ± 0,10 Distance : 12 000 a.l.
Classe : - - Dimension : Ø 7,2’
Constellation : Flèche Visibilité : Été
Autres appellations : NGC6838, PGC2802696
143
Charles Messier observa cet amas globulaire le 4 octobre 1780, suite à la
déclaration de découverte faite par Pierre Méchain le 29 août précédent. Il
avait déjà été repéré par Johann Gottfried Köhler cinq ans plus tôt, mais ce
dernier n’avait pas pris la peine de divulguer sa trouvaille. La primeur de la
découverte semble revenir à l’astronome suisse Jean Philippe Loys de Chéseaux
qui l’observa dès 1746.
Il est l’un des amas globulaires les moins denses (état intermédiaire entre amas
ouvert et amas globulaire), à tel point que les astronomes ont longuement
hésité avant de le classer dans cette catégorie.
La luminosité globale vaut 13 200 soleils, et la magnitude absolue est de −5,5.
144
Messier 72 Amas globulaire
Découverte : Pierre Méchain (1780)
Ascension Droite : 20h 53m 27,94s Déclinaison : −12° 32’ 13,4"
Magnitude : 9,20 ± 0,10 Distance : 55 420 a.l.
Classe : IX Dimension : Ø 5,9’
Constellation : Verseau Visibilité : Automne
Autres appellations : NGC6981, PGC2802699
145
Comme beaucoup d’entrées constituant le catalogue Messier, la découverte de
M 72 est associée au nom de Pierre Méchain. Il découvrit ce modeste amas
globulaire le 29 août 1780. Charles Messier l’observera le 4 octobre suivant.
Il s’agit de l’un des amas globulaires les plus dispersés.
146
Messier 73 Astérisme
Découverte : Charles Messier (1780)
Ascension Droite : 20h 58m 55,95s Déclinaison : −12° 38’ 07,7"
Magnitude : 8,90 ± 0,10 Distance : 2 000 a.l.
Classe : - - Dimension : Ø 2,8’
Constellation : Verseau Visibilité : Automne
Autre appellation : NGC6994
147
Astérisme parfois classé comme amas ouvert. L’objet repéré par Charles
Messier la nuit du 4 au 5 octobre 1780, alors qu’il cherchait la position de M 72
qui venait d’être découvert par Pierre Méchain, est l’un des plus atypiques de
son catalogue. Trompé par la piètre qualité de son instrument, Messier crut
voir à cet endroit une nébulosité entourant 3 à 4 étoiles de faible éclat.
Depuis, des optiques plus performantes ont démontré qu’il ne s’agit que d’un
simple alignement fortuit de quatre étoiles en forme de Y. Cette impression
d’objet qui « ressemble à une nébuleuse au premier coup d’œil » est souvent
donnée au travers d’une lunette de 50 mm.
148
Messier 74 Galaxie spirale
Découverte : Pierre Méchain (1780)
Ascension Droite : 01h 36m 41,81s Déclinaison : +15° 47’ 00,3"
Magnitude : 9,31 ± 0,11 Distance : 32 × 106 a.l.
Classe : SAc Dimension : 11,0’ × 11,0’
Constellation : Poissons Visibilité : Automne
Autres appellations : 2MASXJ01364177+1547004, AGC001149, CGCG460-014,
HIPASSJ0136+15, IRAS01340+1531, IRAS01340+1532, LGG029:[G93]005,
MCG+03-05-011, NGC0628, PGC005974, UGC01149, UZC013400+15320
149
Galaxie découverte par Pierre Méchain fin septembre 1780 et scrutée par
Charles Messier le 18 octobre de la même année.
John Herschel la décrira par la suite comme un amas d’étoiles non résolu.
Il faudra la venue d’un pionnier de l’astrophotographie, Isaac Roberts, pour
découvrir le déroulement des bras spiraux après une pose avoisinant les 5 heures.
Offrant un faible contraste, son observation visuelle reste difficile, mais son
repérage est aisé à 1,3° au nord-est de l’étoile η.
150
Messier 75 Amas globulaire
Découverte : Pierre Méchain (1780)
Ascension Droite : 20h 06m 04,79s Déclinaison : −21° 55’ 18,7"
Magnitude : 8,60 ± 0,10 Distance : 67 500 a.l.
Classe : I Dimension : Ø 6’
Constellation : Sagittaire Visibilité : Été
Autres appellations : 2MASXJ20060484-2155201, NGC6864, PGC2802697
151
Amas globulaire découvert par Pierre Méchain le 27 août 1780. Les instruments
de cette époque ne permettaient pas de résoudre cet objet. Charles Messier
nota pourtant, le 18 octobre suivant, à propos de son observation de M 75 :
« composée que de très petites étoiles, contenant de la nébulosité ».
Comme son homologue M 55, M 75 est situé dans une zone manquant de jalon
aisément visible et l’emploi d’une carte détaillée sera encore une fois d’une
aide précieuse.
152
Messier 76 Nébuleuse planétaire
Découverte : Pierre Méchain (1780)
Ascension Droite : 01h 42m 19,69s Déclinaison : +51° 34’ 31,6"
Magnitude : 10,10 ± 0,10 Distance : 4 000 a.l.
Classe : - - Dimension : Ø 65"
Constellation : Persée Visibilité : Automne
Autres appellations : Petite Dumbbell, 3C050, NGC0650, NGC0651,
PGC2817502
153
Troisième des quatre nébuleuses planétaires que contient le catalogue Messier,
elle fut découverte par Pierre Méchain le 5 septembre 1780 et observée par
Charles Messier le 21 octobre suivant.
Une similitude de forme avec la nébuleuse planétaire M 27 (dans la constellation
du Petit Renard) lui vaut son nom usuel de « petite Dumbbell ». C’est l’un
des objets les plus faibles du catalogue Messier, que l’on retrouve parfois sous
l’appellation de « nébuleuse du Papillon ».
Longtemps soupçonnée d’être une nébuleuse double avec les composantes au
contact, elle a officiellement reçu deux numéros différents dans le catalogue
NGC (650 et 651).
154
Messier 77 Galaxie spirale
Découverte : Pierre Méchain (1780)
Ascension Droite : 02h 42m 40,74s Déclinaison : −00° 00’ 48,0"
Magnitude : 9,85 ± 0,96 Distance : 65 × 106 a.l.
Classe : SABab(r) Dimension : 8,2’ × 7,3’
Constellation : Baleine Visibilité : Automne
Autres appellations : 2MASXJ02424077-0000478, 3C071, 4C-00.13,
AGC002188, ARP037, CGCG388-098, HIPASSJ0242+00, IRAS02401-0013,
KUG0240-002, LGG073:[G93]002, MCG+00-07-083, MRC0240-002, NGC1068,
PGC010266, PKS0240-002, UGC02188, UZC024006-00130
155
Galaxie repérée par Pierre Méchain le 29 octobre 1780. La découverte sera
vérifiée par Charles Messier le 17 décembre suivant. Elle est le prototype des
galaxies de type Seyfert, caractérisées par un noyau très actif et lumineux.
Source d’émission radio, elle est également répertoriée sous le matricule 3C 71.
Elle est le principal élément du groupe composé également des NGC 1055,
1073, 1087 et 1090.
156
Messier 78 Nébuleuse à émission
Découverte : Pierre Méchain (1780)
Ascension Droite : 05h 46m 45,41s Déclinaison : +00° 04’ 46,5"
Magnitude : 8.3 Distance : 1 600 a.l.
Classe : - - Dimension : 8’ × 6’
Constellation : Orion Visibilité : Hiver
Autre appellation : NGC2068
157
Cette nouvelle découverte de Pierre Méchain, au début de l’année 1780, est
une petite nébuleuse à émission qui ne sera observée par Charles Messier que
le 17 décembre de la même année.
Le rayonnement à l’origine de cette excitation provient essentiellement de deux
étoiles de magnitudes 10,2 et 10,6 nichées au cœur de la nébuleuse et séparées
de 50”. La plus au nord est une binaire, la séparation du couple est de 2”.
158
Messier 79 Amas globulaire
Découverte : Pierre Méchain (1780)
Ascension Droite : 05h 24m 10,64s Déclinaison : −24° 31’ 27,5"
Magnitude : 7,70 ± 0,10 Distance : 41 000 a.l.
Classe : V Dimension : Ø 8,7’
Constellation : Lièvre Visibilité : Hiver
Autres appellations : NGC1904, PGC2802630
159
Amas globulaire découvert par Pierre Méchain le 26 octobre 1780, il sera
répertorié par Charles Messier le 17 décembre. Il n’est pas impossible qu’il
fut déjà observé par Giovanni Battista Hodierna plus d’un siècle auparavant,
malheureusement ses notes sont trop imprécises pour pouvoir le garantir avec
certitude.
L’amas s’éloigne de nous à 198 km.s-1
.
160
Messier 80 Amas globulaire
Découverte : Pierre Méchain (1780)
Ascension Droite : 16h 17m 02,55s Déclinaison : −22° 58’ 30,0"
Magnitude : 7,30 ± 0,10 Distance : 28 000 a.l.
Classe : II Dimension : Ø 8,9’
Constellation : Scorpion Visibilité : Été
Autres appellations : NGC6093, PGC2802658
161
Découvert par Charles Messier le 4 janvier 1781, cet amas globulaire fut décrit
comme : « une nébuleuse ronde avec un centre plus brillant ressemblant au
noyau d’une comète ».
Bien que les instruments de l’époque ne permettaient pas de résoudre l’amas,
des observateurs anglais et allemand découvrirent une étoile au sein de la
« nébuleuse » le 21 mai 1860. Il s’agissait en fait de la première nova observée
au sein de ce type d’objet, à son maximum elle fut plus brillante que l’ensemble
de l’amas qui contient plus de 100 000 étoiles.
162
Messier 81 Galaxie spirale
Découverte : Johann Bode (1774)
Ascension Droite : 09h 55m 33,15s Déclinaison : +69° 03’ 55,2"
Magnitude : 6,92 ± 0,11 Distance : 10 × 106 a.l.
Classe : SAab Dimension : 24,0’ × 13,0’
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : Galaxie de Bode, 2MASXJ09553318+6903549,
CGCG333-007, HIJASSJ0955+69, IRAS09514+6918, KPG218A,
LGG176:[G93]003, MCG+12-10-010, NGC3031, PGC028630, UGC05318,
UZC095124+69180
163
Située à la périphérie du « groupe local », c’est l’une des galaxies les plus
lumineuses de l’hémisphère Nord. Elle fut découverte par le directeur de
l’observatoire de Berlin, Johann Bode, le 31 décembre 1774. Elle sera retrouvée
de manière indépendante par Pierre Méchain en 1779 avant d’être répertoriée
par Charles Messier le 9 février 1781.
Une supernova de type II (SN1993J : 09h 55m 25s, +69° 01’ 13”) y a été
observée le 28 mars 1993 ; magnitude maximale : 9,91.
Le pointage de M 81 peut se réaliser à partir de l’étoile 24 UMa (magnitude
4,6), la galaxie se repère à 2° au sud-est. En utilisant les cercles gradués d’une
monture équatoriale, il est également possible de partir depuis la position de
l’étoile λ de la constellation voisine du Dragon et de se déplacer de 1 h 36 min
vers l’ouest.
164
Messier 82 Galaxie irrégulière
Découverte : Johann Bode (1774)
Ascension Droite : 09h 55m 52,31s Déclinaison : +69° 40’ 47,4"
Magnitude : 8,30 ± 0,17 Distance : 10 × 106 a.l.
Classe : I Dimension : 12,0’ × 5,6’
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : Galaxie du Cigare, 2MASXJ09555243+6940469,
2MFGC07685, 3C231, 4C+69.12, ARP337, CGCG333-008, HIJASSJ0955+69,
IRAS09517+6954, KPG218B, LGG176:[G93]012, MCG+12-10-011, NGC3034,
PGC028655, UGC05322, UZC095142+69550
165
Vue proche de M 81, cette galaxie fut découverte avec la précédente. Cette
double trouvaille restera quasi inconnue car publiée dans un almanach en
langue allemande et d’un tirage quasi confidentiel.
Le couple M 81 - M 82 sera ainsi (re)découvert par Pierre Méchain en août
1779 et répertorié 2 ans plus tard par Charles Messier.
La radioastronomie à permis de détecter un « pont » de gaz et de poussière
reliant ces deux galaxies né à la suite d’un rapprochement du couple. Ces deux
objets sont les plus gros éléments d’un petit amas de galaxies qui se développe
sur la constellation voisine de la Girafe.
La recherche de M 82 se fait de manière analogue à celle de M 81.
166
Messier 83 Galaxie spirale
Découverte : Nicolas de Lacaille (1752)
Ascension Droite : 13h 37m 00,94s Déclinaison : −29° 51’ 56,1"
Magnitude : 7,16 ± 0,21 Distance : 22 × 106 a.l.
Classe : SABc Dimension : 15,5’ × 13,0’
Constellation : Hydre Visibilité : Printemps
Autres appellations : 2MASXJ13370091-2951567, ESO444-081,
ESOLV4440810, FLASHJ133700.23-295204.5, HIPASSJ1337-29,
IRAS13341-2936, IRAS13342-2933, LGG355:[G93]001, MCG-05-32-050,
MRC1334-296, NGC5236, PGC048082, UGCA366
167
Galaxie découverte par l’abbé Nicolas de Lacaille lors d’une expédition au cap
de Bonne Espérance en 1751-1752. Elle sera répertoriée par Charles Messier
le 17 février 1781.
Les étoiles jeunes (de couleur bleue) se distribuent dans les bras spiraux, les
générations plus anciennes (de coloration rouge) se retrouvent essentiellement
dans le bulbe central.
Une demi-douzaine de supernovæ y ont été observées : les 5 mai 1923 (magnitude 14,0), 13 juillet 1945 (14,2), 15 mars 1950 (14,5), 1957 (15,0), 17 juillet
1968 (11,9) et 3 juillet 1983 (12,5).
Avec un diamètre de 100 000 années de lumière, d’une luminosité globale
équivalente à 36 milliards de soleils, sa magnitude absolue est de −21,6.
L’observation de M 83, toujours vue bas sur l’horizon, nécessite un ciel de
grande transparence. Sa position peut-être retrouvée après un alignement sur
l’étoile HN 69, visible au chercheur, la galaxie se trouve à un peu plus de 3°
vers le sud.
168
Messier 84 Galaxie lenticulaire
Découverte : Charles Messier (1781)
Ascension Droite : 12h 25m 03,71s Déclinaison : +12° 53’ 13,8"
Magnitude : 9,79 ± 1,32 Distance : 65 × 106 a.l.
Classe : E1 Dimension : 5,1’ × 4,1’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12250377+1253130, 3C272.1, 4C+13.47,
ACSVCS006, CGCG070-058, EVCC0539, GIN778, IRAS12224+1309,
LGG292:[G93]005, MCG+02-32-034, MRC1222+131, NGC4374, PGC040455,
SDSSJ122503.74+125312.8, UGC07494, UZC122230+13100
169
Galaxie découverte par Charles Messier le 18 mars 1781 à l’aide d’une lunette
de 80 mm.
C’est également une forte source d’émission radio au sein de laquelle ont été
observées des supernovæ les 23 avril 1957, 13 juin 1980 et 3 décembre 1991.
Elles atteignirent respectivement les magnitudes 12,5, 14,0 et 14,0.
170
Messier 85 Galaxie lenticulaire
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 25m 24,01s Déclinaison : +18° 11’ 24,9"
Magnitude : 9,05 ± 0,22 Distance : 65 × 106 a.l.
Classe : SO- Dimension : 7,5’ × 5,7’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : 2MASXJ12252405+1811278, ACSVCS005,
CGCG099-045, EVCC0554, GIN779, KPG334A, LGG292:[G93]035,
MCG+03-32-029, NGC4382, PGC040515, UGC07508, UZC122254+18280,
VCC0798, [TH2002]004
171
Galaxie découverte par Pierre Méchain le 4 mars 1781 qui, comme à l’accoutumé, informa Charles Messier de sa trouvaille. Ce dernier l’observera à son
tour le 18 du même mois.
Elle fait partie de l’amas de la Vierge et fut le siège d’une supernova découverte
le 20 décembre 1960 à la magnitude 12.
Une autre galaxie, la spirale barrée NGC 4394 (magn. 11,9) peut être observée
proche.
172
Messier 86 Galaxie elliptique
Découverte : Charles Messier (1781)
Ascension Droite : 12h 26m 11,79s Déclinaison : +12° 56’ 45,1"
Magnitude : 8,86 ± 0,28 Distance : 60 × 106 a.l.
Classe : E3 Dimension : 12,0’ × 9,3’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12261181+1256454, ACSVCS004, AGC007532,
ALFALFA1-315, CGCG070-072, EVCC0597, GIN780, MCG+02-32-046,
NGC4406, PGC040653, SDSSJ122611.75+125646.3, UGC07532,
UZC122342+13140, VCC0881, VIRGO:[TT2002]01,
[RG2008]J186.54898+12.94622
173
Galaxie elliptique découverte avec M 84. Ces deux galaxies sont vues proches
du centre de « l’amas Virgo » qui contient plusieurs milliers de membres.
Contrairement à toutes les galaxies de l’amas de la Vierge, qui s’éloignent
de nous avec des vitesses comprises entre 300 et 2 500 km.s-1, M 86 nous
« tombe dessus » à la vitesse de 248 km.s-1. Elle ne devrait ainsi pas faire partie
intégrante de l’amas, mais n’y serait qu’en « transit ». Ayant une orbite très
allongée autour de la partie centrale de l’amas qu’elle traverse à 1 500 km.s-1
,
sa présence actuelle serait ainsi tout à fait fortuite.
174
Messier 87 Galaxie elliptique
Découverte : Charles Messier (1781)
Ascension Droite : 12h 30m 49,54s Déclinaison : +12° 23’ 26,1"
Magnitude : 9,00 ± 0,38 Distance : 65 × 106 a.l.
Classe : E1 Dimension : 7,1’ × 7,1’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12304942+1223279, 3C274, 4C+12.45,
ACSVCS002, ARP152, CGCG070-139, EVCC0786, GIN800,
IRAS12282+1240, LGG289:[G93]012, MCG+02-32-105, MRC1228+126,
NGC4486, PGC041361, SDSSJ123049.41+122328.1, UGC07654, Virgo A
175
Galaxie également découverte par Charles Messier – en même temps que M 87
et M 88 – le 18 mars 1781, pour qui il ne s’agissait que d’une nébuleuse de
plus. Elle marque le centre de l’amas Virgo (Abell 1060).
John Gatenhy Bolton découvrit en 1948, avec une antenne radio encore
peu performante, que M 87 était également une puissante source émettrice
dans ces longueurs d’onde (cataloguée 3C 274). Lorsque la résolution des
radiotélescopes devint aussi performante que celle des télescopes optiques, il
apparut clairement que cette source radio se superposait sur un jet de matière
émanant du noyau de la galaxie (découvert dès 1918 par Heber Doust Curtis).
Depuis, des satellites équipés de détecteurs U.V. et X ont également confirmés
l’émission du jet de M 87 dans ces longueurs d’onde.
Le noyau de cette galaxie pourrait renfermer un « trou noir » très massif et en
rotation rapide. Une partie de la matière située à la frontière de ce trou noir
pourrait être éjectée suivant l’axe de rotation sur une distance de plusieurs
centaines d’années de lumière.
Une supernova y a été observée le 24 février 1919 à la magnitude 12,3.
176
Messier 88 Galaxie spirale
Découverte : Charles Messier (1781)
Ascension Droite : 12h 31m 59,30s Déclinaison : +14° 25’ 12,3"
Magnitude : 10,33 ± 1,53 Distance : 65 × 106 a.l.
Classe : SAb Dimension : 6,1’ × 2,8’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : 2MASXJ12315921+1425134, AGC007675,
ALFALFA1-339, CGCG099-076, EVCC2153, HIPASSJ1231+14,
IRAS12294+1441, LGG285:[G93]017, MCG+03-32-059, NGC4501,
PGC041517, UGC07675, UZC122924+14420, VCC1401
177
Une découverte originale de Charles Messier datée du 18 mars 1781. William
Parsons sera le premier à deviner ses nombreux bras spiraux.
Un couple d’étoiles de notre Galaxie vient se superposer à l’extrémité de deux
d’entre-eux.
Bien que se projetant sur la constellation de la Chevelure de Bérénice, elle
appartient également à l’amas de la Vierge.
178
Messier 89 Galaxie elliptique
Découverte : Charles Messier (1781)
Ascension Droite : 12h 35m 39,86s Déclinaison : +12° 33’ 22,7"
Magnitude : 10,08 ± 0,74 Distance : 65 × 106 a.l.
Classe : E- Dimension : 3,4’ × 3,4’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12353988+1233217, ACSVCS010,
CGCG070-184, EVCC2176, MCG+02-32-149, NGC4552, PGC041968,
SDSSJ123539.80+123322.8, UGC07760, UZC123306+12500, VCC1632,
[RG2008]J188.91587+12.55634, [TH2002]009
179
Encore une galaxie découverte par Charles Messier le 18 mars 1781. Elle était
à la limite de la détection dans son instrument de l’époque : une lunette de
80 mm de diamètre.
180
Messier 90 Galaxie spirale barrée
Découverte : Charles Messier (1781)
Ascension Droite : 12h 36m 49,95s Déclinaison : +13° 09’ 48,4"
Magnitude : 10,67 ± 1,35 Distance : 60 × 106 a.l.
Classe : SABab Dimension : 10,5’ × 4,4’
Constellation : Vierge Visibilité : Printemps
Autres appellations : 2MASXJ12364981+1309463, AGC007786,
ALFALFA1-370, ARP076, CGCG070-192, EVCC2184, IRAS12343+1326,
MCG+02-32-155, NGC4569, PGC042089, UGC07786, UZC123418+13260,
VCC1690, [RG2008]J189.20747+13.16294
181
Elle fait partie du même lot de découvertes faites par Charles Messier dans la
nuit du 18 mars 1781 (avec les objets notés M 84 à M 89).
182
Messier 91 Galaxie spirale barrée
Découverte : Charles Messier (1781)
Ascension Droite : 12h 35m 26,50s Déclinaison : +14° 29’ 46,1"
Magnitude : 10,96 ± 1,43 Distance : 65 × 106 a.l.
Classe : SBb Dimension : 5,0’ × 4,1’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : 2MASXJ12352642+1429467, AGC007753,
ALFALFA1-361, CGCG099-096, EVCC2174, HIPASSJ1235+14,
IRAS12328+1446, IRAS12329+1446, MCG+03-32-075, NGC4548,
PGC041934, PGC3096162, SDSSJ123526.44+142946.7, UGC07753,
UZC123254+14460, VCC1615, [RG2008]J188.86022+14.49634
183
Également observé le 18 mars 1781, le mystérieux objet vu par Charles
Messier en lieu et place de ses coordonnées n’existe tout simplement pas. Trois
hypothèses se sont partagées les faveurs des historiens en sciences :
– c’était une véritable comète et il est normal de ne rien trouver à cet endroit ;
– il y a une erreur dans les coordonnées. Charles Messier a parfois manqué de
précision sur la position de certains objets : voir M 48 et M 102 ;
– soit il s’agit d’une confusion et l’objet observé était NGC 4548.
Par méprise, les coordonnées de cette galaxie spirale barrée ont été calculées
d’après celles de M 89, et non M 58 comme l’a cru Charles Messier. C’est
cette thèse qui a été démontrée par l’astronome amateur William C. Williams
en 1969 et aujourd’hui largement reconnue.
184
Messier 92 Amas globulaire
Découverte : Johann Bode (1777)
Ascension Droite : 17h 17m 07,30s Déclinaison : +43° 08’ 11,5"
Magnitude : 6,50 ± 0,10 Distance : 27 000 a.l.
Classe : IV Dimension : Ø 11,2’
Constellation : Hercule Visibilité : Été
Autres appellations : NGC6341, PGC2802670
185
Amas globulaire découvert par le directeur de l’observatoire de Berlin, Johann
Bode, en décembre 1777. Il sera observé par Charles Messier le 18 mars 1781
qui le décrira comme une nébulosité très lumineuse, avec un centre clair et
brillant, similaire au noyau d’une grosse comète. L’amas ne sera résolu en
étoiles que 20 ans plus tard par William Herschel.
D’un diamètre réel de 80 années de lumière et d’une luminosité globale
équivalente à 150 000 soleils, M 92 se fait plus discret que son homologue
M 13 ; sa magnitude absolue est de −8,1. Plusieurs étoiles variables y ont été
répertoriées, dont une binaire avec les composantes au contact.
Le repérage de Messier 92 est un peu moins évident que celui de Messier 13,
il est possible de le trouver en pointant l’étoile π et de se décaler de 6° en
déclinaison vers le nord.
186
Messier 93 Amas ouvert
Découverte : Charles Messier (1781)
Ascension Droite : 07h 44m 29,62s Déclinaison : −23° 51’ 17,4"
Magnitude : 6,20 ± 0,10 Distance : 3 400 a.l.
Classe : I 3 r Dimension : Ø 10’
Constellation : Poupe Visibilité : Hiver
Autre appellation : NGC2447
187
Amas ouvert découvert par Charles Messier le 20 mars 1781.
Avec un diamètre réel de 20 années de lumière, il brille comme 4 000 soleils.
L’amas est une cible relativement facile, car déjà visible dans la majorité des
chercheurs. M 93 se situe à 1,5° au nord-ouest de l’étoile ξ. En se servant des
graduations d’une monture équatoriale, il est également possible de partir de
l’étoile o2 de la constellation du Grand Chien. Les deux étoiles ayant la même
déclinaison, il suffit de se déplacer de 42’ vers l’est.
188
Messier 94 Galaxie spirale
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 50m 53,11s Déclinaison : +41° 07’ 13,3"
Magnitude : 9,48 ± 1,30 Distance : 21 × 106 a.l.
Classe : SAab(r) Dimension : 13,0’ × 11,0’
Constellation : Chiens de chasse Visibilité : Printemps
Autres appellations : 2MASXJ12505314+4107125, CGCG216-034,
CGCG217-001, IRAS12485+4123, LGG290:[G93]012, MCG+07-26-058,
NGC4736, PGC043495, UGC07996, UZC124830+41230
189
Une nouvelle découverte de Pierre Méchain, le 22 mars 1781. Charles Messier
l’observera deux jours plus tard.
D’abord pris pour un amas globulaire non-résolu, il faudra attendre les photographies prises en 1912 à l’aide du télescope de 1,5 m du Mont Wilson pour
lever définitivement le doute : M 94 est bien une galaxie spirale avec un bulbe
très étalé.
190
Messier 95 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 10h 43m 57,71s Déclinaison : +11° 42’ 13,5"
Magnitude : 9,77 ± 0,08 Distance : 31 × 106 a.l.
Classe : SBb(r) Dimension : 7,8’ × 4,6’
Constellation : Lion Visibilité : Printemps
Autres appellations : 2MASXJ10435773+1142129, AGC005850,
ALFALFA5-309, CGCG066-004, HIPASSJ1044+11, IRAS10413+1158,
LEO_GROUP:[FS90]007, LGG217:[G93]002, MCG+02-28-001, NGC3351,
PGC032007, SDSSJ104357.69+114213.6, UGC05850, UZC104124+11580
191
Galaxie découverte par Pierre Méchain le 20 mars 1781 et retrouvée par
Charles Messier quatre jours plus tard.
D’un diamètre de 70 000 années de lumière, M 95 brille comme 10 milliards
de soleils, ce qui lui vaut une magnitude absolue de −20,2. Une supernova y a
été observée le 17 mars 2012 à la magnitude 13.
192
Messier 96 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 10h 46m 45,70s Déclinaison : +11° 49’ 11,9"
Magnitude : 9,21 ± 0,09 Distance : 31 × 106 a.l.
Classe : SABab(r) Dimension : 6,9’ × 4,6’
Constellation : Lion Visibilité : Printemps
Autres appellations : 2MASXJ10464574+1149117, AGC005882,
ALFALFA5-321, CGCG066-013, HIPASSJ1046+11, IRAS10441+1205,
LEO_GROUP:[FS90]019, LGG217:[G93]003, MCG+02-28-006, NGC3368,
PGC032192, SDSSJ104645.67+114911.8, UGC05882, UZC104406+12050
193
Galaxie découverte dans les mêmes circonstances que M 95, dont elle est vue
proche. Ces deux galaxies sont, avec M 105 vue au N-E, les éléments les plus
abordables de l’amas du Lion.
D’une magnitude absolue de −20,7 pour un diamètre de 62 000 années de
lumière, sa luminosité globale équivaut à 16 milliards de soleils.
194
Messier 97 Nébuleuse planétaire
Découverte : Pierre Méchain (1781)
Ascension Droite : 11h 14m 47,70s Déclinaison : +55° 01’ 08,9"
Magnitude : 9,90 ± 0,10 Distance : 2 600 a.l.
Classe : - - Dimension : Ø 194"
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : Nébuleuse du Hibou, NGC3587,
SDSSJ111447.70+550108.7
195
Objet difficile à observer, cette nébuleuse planétaire fut découverte par Pierre
Méchain le 16 février 1781. Elle sera répertoriée par Charles Messier le 24 mars.
C’est William Parsons qui en fera les premières observations scrupuleuses à
l’aide de son télescope géant et lui donnera son nom commun, la nébuleuse
du Hibou, en remarquant les deux zones sombres qui forment les « yeux » de
l’animal.
Il s’agit d’une étoile en fin de vie qui a éjecté les couches supérieures de son gaz
en une gigantesque sphère de 3 années de lumière de diamètre. Les déductions
les plus récentes tendent à démontrer que M 97 aurait plutôt la forme d’un
cylindre vu de dessus, les deux zones sombres étant des cavités moins denses
inclinées par rapport à l’axe du cylindre.
196
Messier 98 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 13m 48,35s Déclinaison : +14° 54’ 00"
Magnitude : 10,84 ± 1,36 Distance : 65 × 106 a.l.
Classe : SABab Dimension : 5’ × 1’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : 2MASXJ12134829+1454016, 2MFGC09627, AGC007231,
ALFALFA1-177, CGCG098-108, EVCC0188, IRAS12112+1510,
MCG+03-31-079, NGC4192, PGC039028, SDSSJ121348.28+145401.6,
UGC07231, UZC121112+15100, VCC0092
197
Galaxie spirale vue pratiquement par la tranche, elle est découverte par Pierre
Méchain le 15 mars 1781 et observée par Charles Messier le 13 avril suivant.
Elle se rapproche de notre Voie lactée à une vitesse de 243 km.s-1
.
198
Messier 99 Galaxie spirale
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 13m 48,35s Déclinaison : +14° 54’ 00"
Magnitude : 10,84 ± 1,36 Distance : 65 × 106 a.l.
Classe : SAc Dimension : 5’ × 1’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : La Toupie, 2MASXJ12184962+1424593, AGC007345,
ALFALFA1-248, CGCG098-144, CGCG099-011, EVCC0319,
HIPASSJ1218+14, IRAS12162+1441, LGG285:[G93]011, MCG+03-31-099,
MRC1216+146, NGC4254, PGC039578, SDSSJ121849.60+142459.4,
UGC07345
199
Galaxie appartenant à l’amas de la Vierge, découverte avec M 98 par Pierre
Méchain.
Elle possède la plus grande vitesse d’éloignement de « l’amas Virgo » :
2 380 km.s-1 et fut le théâtre de plusieurs supernovæ découvertes les 2 juillet
1967, 14 décembre 1972 et 17 mai 1986. Aucune ne fut plus brillante que la
magnitude 14.
200
Messier 100 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 22m 54,89s Déclinaison : +15° 49’ 20,3"
Magnitude : 9,47 ± 0,11 Distance : 65 × 106 a.l.
Classe : SABbc Dimension : 4’ × 3’
Constellation : Ch. de Bérénice Visibilité : Printemps
Autres appellations : 2MASXJ12225489+1549205, AGC007450,
ALFALFA1-289, CGCG099-030, EVCC0467, HIPASSJ1222+15,
IRAS12203+1606, IRAS12204+1605, KUG1220+160, LGG289:[G93]057,
MCG+03-32-015, NGC4321, NIBLES1641, PGC040153,
SDSSJ122254.91+154920.2, UGC07450
201
Cette galaxie spirale vue de face est également une découverte de Pierre
Méchain datée du 15 mars 1781 comme les deux précédentes du catalogue
Messier. Alors directeur de l’observatoire de Paris, il l’observa avec un télescope
plus puissant que la lunette dont disposait Charles Messier. Ce dernier eut
d’ailleurs quelques difficultés à la retrouver, le 27 mars, pour mesurer sa
position avec précision.
Comme la plupart des galaxies observées sur la constellation de la Chevelure
de Bérénice, elle appartient à l’amas de la Vierge.
Plusieurs supernovæ y ont été observées les 17 mars 1901, 2 mars 1914,
21 février 1960 et 19 avril 1979 avec des magnitudes comprises entre 12,1 et
17,5.
202
Messier 101 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 14h 03m 12,59s Déclinaison : +54° 20’ 56,7"
Magnitude : 7,90 ± 0,09 Distance : 25 × 106 a.l.
Classe : SABcd Dimension : Ø 22’
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : Galaxie Pinwheel, 2MASXJ14031258+5420555, ARP026,
CGCG272-021, IRAS14013+5435, KIG0610, LGG371:[G93]001,
MCG+09-23-028, NGC5457, PGC050063, SDSSJ140312.52+542056.2,
SDSSJ140312.54+542056.1, UGC08981, UZC140130+54350, VV344, VV456
203
D’observation difficile, cette galaxie vue de face fut découverte par Pierre
Méchain début 1781 et observée le 27 mars par Charles Messier avec un
télescope de seulement 84 mm d’ouverture. Il faudra cependant attendre
1845 pour que William Parsons, depuis son château irlandais, parvienne à
reconnaître sa structure en spirale à l’aide de son Leviathan de 183 cm.
L’observation de quelques céphéides ont permis d’en évaluer la distance avec
une relative précision.
Plusieurs supernovæ y ont été détectées : SN1909A de type II, le 26 janvier
1909 (14h 02m 03s, +54° 28’ 05” - magnitude maximale : 12,1) ; SN1951H
de type II, le er septembre 1951 (14h 03m 55s, +54° 21’ 41” - magnitude
maximale : 17,19) ; SN1970G de type II, le 30 juillet 1970 (14h 03m 01s, +54°
14’32” - magnitude maximale : 11,42) et SN2011fe de type Ia, le 24 août 2011
(14h 03m 05s, +54° 16’ 25” - magnitude maximale : 9,48).
204
Messier 102 Galaxie lenticulaire
Découverte : Pierre Méchain (1781)
Ascension Droite : 15h 06m 29,54s Déclinaison : +55° 45’ 47,7"
Magnitude : 11,27 ± 1,70 Distance : 45 × 106 a.l.
Classe : SO- Dimension : 6,6’ × 3,2’
Constellation : Dragon Visibilité : Circumpolaire
Autres appellations : Galaxie du Fuseau, 2MASXJ15062956+5545479,
CGCG274-016, EGISJ150629.4+554547, EONJ226.622+55.763,
IRAS15051+5557, LGG396:[G93]001, MCG+09-25-017, NGC5866,
PGC053933, UGC09723, UZC150506+55570
205
Galaxie classée comme lenticulaire, également appelée galaxie du Fuseau, mais
il se pourrait qu’il s’agisse d’une spirale vue exactement par la tranche.
Charles Messier en observateur attentif, et ce malgré quelques imprécisions sur
certaines positions qui ont pu être corrigées depuis – voir également M 48 et
M 91 – mesurait avec soin les coordonnées de ses observations. M 102 semble
être l’une des exceptions qui confirment cette règle.
Les faveurs des spécialistes se partagent entre deux thèses, à savoir :
– suite à une banale méprise, M 102 ne serait qu’un doublon de M 101, la
« découverte » aurait d’ailleurs été démentie par Pierre Méchain lui-même ;
– soit l’objet existe réellement et serait la galaxie NGC 5866 du Dragon.
Cette dernière hypothèse est étayée par le fait que Charles Messier situe son
observation entre les étoiles ι du Dragon et... o du Bouvier. Vu l’écart entre
ces deux étoiles (environ 40°, o étant encore plus au sud que Arcturus), elles
ne semblent pas être toutes indiquées pour préciser une position. En prenant
θ du Bouvier à la place de o (une erreur typographique entre ces deux signes
serait possible, ils ne diffèrent que d’une barre horizontale), l’objet NGC 5866
devient ainsi un candidat plus que probable.
206
Messier 103 Amas ouvert
Découverte : Pierre Méchain (1781)
Ascension Droite : 01h 33m 23,00s Déclinaison : +60° 38’ 59,8"
Magnitude : 7,40 ± 0,10 Distance : 9 200 a.l.
Classe : III 3 p Dimension : Ø 6,0’
Constellation : Cassiopée Visibilité : Circumpolaire
Autre appellation : NGC0581
207
Officiellement, c’est le dernier objet classé par Charles Messier sur sa liste
(les références suivantes ont été rajoutées ultérieurement suite à des notes
retrouvées et portant sur leurs observations), il fut rajouté à la hâte juste
avant publication, sans même faire mention de ses coordonnées. Sa découverte
revient à Pierre Méchain en 1781.
Pauvre en étoiles et de faible densité, l’amas est dominé par deux géantes
bleues (dont la binaire HD 9311) et une géante rouge. Son statut d’amas ouvert
semble lui être contesté par certains qui n’y voient qu’un simple regroupement
d’étoiles vues en projection.
L’âge est estimé à 40 000 000 ans.
208
209
Ajouts ultérieurs :
objets 104 à 110
210
Messier 104 Galaxie spirale
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 39m 59,46s Déclinaison : −11° 37’ 22,6"
Magnitude : 8,67 ± 0,50 Distance : 30 × 106 a.l.
Classe : SAa Dimension : 7,1’ × 4,4’
Constellation : Vierge Visibilité : Printemps
Autres appellations : Galaxie du Sombréro, 2MASXJ12395949-1137230,
IRAS12373-1120, MCG-02-32-020, NGC4594, PGC042407
211
Cette galaxie fut observée par Pierre Méchain le 11 mai 1781. Sa morphologie
la situe entre les galaxies spirales et les galaxies elliptiques.
Elle ne sera intégrée au catalogue Messier qu’en 1921, après la découverte par
Camille Flammarion d’une annotation de la main de Charles Messier lui-même
sur un exemplaire de Connaissance des Temps paru en 1784.
L’ouvrage avait appartenu au célèbre astronome qui y avait noté la date de la
découverte faite par Méchain et les coordonnées de la « nébuleuse ». Celles-ci
correspondaient à l’objet répertorié dans le catalogue NGC sous le numéro
4594, qui devint ainsi également M 104. La galaxie spirale est quasiment vue
par la tranche, elle doit son nom commun à la bande de poussières qui barre
son bulbe très brillant et fait ainsi penser au célèbre couvre-chef mexicain.
Les possesseurs d’une monture équatoriale pourront la retrouver facilement à
l’aide d’un oculaire à grand champ après avoir pointé l’étoile α (Spica) de la
constellation. Les deux objets ayant quasiment la même déclinaison, il suffit
de se déplacer ensuite de 45’ vers l’ouest.
212
Messier 105 Galaxie elliptique
Découverte : Pierre Méchain (1781)
Ascension Droite : 10h 47m 49,60s Déclinaison : +12° 34’ 54,1"
Magnitude : 9,27 ± 0,17 Distance : 31 × 106 a.l.
Classe : E1 Dimension : 3,9’ × 3,9’
Constellation : Lion Visibilité : Printemps
Autres appellations : 2MASXJ10474959+1234538, CGCG066-018, GIN773,
LEO1:[TT2002]02, LEO_GROUP:[FS90]025, LGG217:[G93]004,
MCG+02-28-011, NGC3379, NIBLES1105, PGC032256,
SDSSJ104749.60+123453.9, UGC05902, UZC104512+12510
213
Galaxie découverte par Pierre Méchain le 24 mars 1781. Il tarda visiblement
pour annoncer sa trouvaille à Charles Messier qui ne put intégrer l’objet à sa
liste, car bien que Connaissance des Temps ne parut qu’en 1784, l’ouvrage
était déjà imprimé.
Helen Sawyer Hogg l’ajouta officiellement à la liste en 1947 après la découverte
d’une lettre de Méchain, adressée à Jean Bernoulli et datée du 6 mai 1783,
attestant la connaissance de cet objet (ainsi que ceux répertoriés M 106 et
M 107).
D’une luminosité globale valant celle de 15 milliards de soleils, cette galaxie
elliptique présente un diamètre réel de 35 000 années de lumière, et sa magnitude absolue est de −20,6.
214
Messier 106 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 12h 18m 57,59s Déclinaison : +47° 18’ 14,2"
Magnitude : 9,29 ± 1,48 Distance : 23 × 106 a.l.
Classe : SABbc Dimension : 20,0’ × 8,4’
Constellation : Chiens de chasse Visibilité : Printemps
Autres appellations : 2MASXJ12185761+4718133, CGCG243-067,
CGCG244-003, LGG290:[G93]004, MCG+08-22-104, NGC4258, PGC039600,
UGC07353, UZC121630+47350, VV448
215
Cette galaxie spirale barrée, source d’émission radio, fut observée par Pierre
Méchain en juillet 1781. Il tarda visiblement pour annoncer sa trouvaille à
Charles Messier qui ne put intégrer l’objet à son catalogue, car bien que
Connaissance des Temps ne parut qu’en 1784, l’ouvrage était déjà imprimé.
Helen Sawyer Hogg l’ajouta officiellement à la liste en 1947 après la découverte
d’une lettre de Méchain, adressée à Johann Bernoulli et datée du 6 mai 1783,
attestant la connaissance de cet objet.
Une supernova y a été observée en août 1981 à la magnitude 16.
Messier 106 est l’une des galaxies les plus « lumineuses » du ciel boréal, son
repérage peut cependant se révéler délicat. Une des possibilités pour y parvenir
est de pointer dans un premier temps l’étoile 3 CVn, la galaxie se trouve à
1,7° au sud. Avec une ouverture d’au-moins 250 mm, il est également possible
d’apercevoir la galaxie NGC 4248 (située aux abords de M 106), de magnitude
12,5, à 12’ au nord-ouest de M 106.
216
Messier 107 Amas globulaire
Découverte : Pierre Méchain (1782)
Ascension Droite : 16h 32m 31,87s Déclinaison : −13° 03’ 12,8"
Magnitude : 7,80 ± 0,10 Distance : 20 000 a.l.
Classe : X Dimension : Ø 13,0’ × 8,4’
Constellation : Ophiuchus Visibilité : Été
Autres appellations : NGC6171, PGC2802660
217
Amas globulaire découvert par Pierre Méchain en avril 1782. Il s’agit vraisemblablement du dernier objet en date repéré par l’astronome. Helen Sawyer
Hogg l’ajouta officiellement au catalogue Messier en 1947 après la découverte
d’une lettre de Méchain, adressée à Johann Bernoulli et datée du 6 mai 1783,
attestant la connaissance de cet objet (ainsi que ceux répertoriés M 105 et
M 106).
L’amas globulaire Messier 107, également répertorié NGC 6171, est situé à
environ 20 000 années de lumière. Son diamètre apparent est d’environ 13’, ce
qui correspond à une dimension réelle de 80 années de lumière à sa distance. Il
est composé d’une population de plusieurs milliers de vieilles étoiles concentrées
dans un volume qui représente seulement vingt fois la distance entre notre
Soleil et son voisin le plus proche : Alpha Centauri.
218
Messier 108 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 11h 11m 30,94s Déclinaison : +55° 40’ 27,6"
Magnitude : 10,06 ± 0,05 Distance : 45 × 106 a.l.
Classe : SBcd Dimension : 8,1’ × 2,1’
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : 2MASXJ11113096+5540268, 2MFGC08733,
CGCG267-048, CGCG268-001, IRAS11085+5556, KIG0469, MCG+09-18-098,
NGC3556, PGC034030, PGC2510596, UGC06225, UZC110830+55560
219
Vraisemblablement découverte en même temps que M 97 et M 109 par Pierre
Méchain, et visiblement dans l’indifférence de ses contemporains ; seul William
Herschel en fera une vague allusion.
Cet objet fut rajouté au catalogue par l’astronome, expert en histoire de
l’astronomie, Owen Gingerich en 1953 après la découverte de l’annotation
manuscrite de ses coordonnées faite par Charles Messier en marge de son
exemplaire personnel de Connaissance des Temps.
Une supernova de type II (SN1969B : 11h 11m 21s, +55° 40’ 12”) y a été
découverte le 6 février 1969 ; magnitude maximale : 14,57.
220
Messier 109 Galaxie spirale barrée
Découverte : Pierre Méchain (1781)
Ascension Droite : 11h 57m 35,99s Déclinaison : +53° 22’ 28,5"
Magnitude : 9,88 ± 0,12 Distance : 55 × 106 a.l.
Classe : SBbc Dimension : 7,6’ × 4,3’
Constellation : Grande Ourse Visibilité : Circumpolaire
Autres appellations : 2MASXJ11573598+5322282, CGCG269-023,
IRAS11549+5339, IRAS11550+5339, LGG258:[G93]006, MCG+09-20-044,
NGC3992, PGC037617, PGC2439331, UGC06937, UZC115500+53390
221
Une trouvaille de Pierre Méchain, la même nuit que M 97 et M 108, également
rajoutée à la liste en 1953 par Owen Gingerich.
Une supernova y fut découverte le 8 mars 1956 à la magnitude 12,3.
222
Messier 110 Galaxie elliptique
Découverte : Guillaume Le Gentil de La Galaisière (1749)
Ascension Droite : 00h 40m 22,10s Déclinaison : +41° 41’ 07,0"
Magnitude : 8,15 ± 0,10 Distance : 2,2 × 106 a.l.
Classe : E5 pec Dimension : 19,5’ × 12,5’
Constellation : Andromède Visibilité : Automne
Autres appellations : 2MASXJ00402207+4141070, CGCG535-014,
IRAS00376+4124, LGG011:[G93]006, MCG+07-02-014, NGC205, PGC002429,
UGC00426, UZC003736+41250
223
L’une des deux galaxies satellites de M 31, découverte par Guillaume Le Gentil
de La Galaisière en même temps que M 32. Elle sera retrouvée par Charles
Messier le 10 août 1773, elle est bien présente sur l’un de ses dessins publié en
1807, mais curieusement il ne l’intégra pas à son catalogue. Elle sera découverte
indépendamment, dix ans plus tard, par Carolyn Herschel.
L’objet fut rajouté à la liste par l’astronome amateur anglais Kenneth Glyn
Jones dans son ouvrage publié en 1968 : Les amas et nébuleuses de Messier.
Est-ce pour cette raison que les « puristes » évitent l’appellation M 110 ?
Elle est généralement classée comme galaxie sphéroïde naine, huit amas globulaires ont été identifiés dans son halo.
En raison de sa dimension apparente, Messier 110 est facilement identifiable à
l’aide d’un petit télescope en observant Messier 31.
224
225
Sources des images
M1 : ESO/Manu Mejias
M2-M6 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M7 : Dieter Willasch (Astro-Cabinet) [Astronomy Picture of the Day]
M8 : ESO/VPHAS+ team
M9-M15 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M16 : ESO
M17 : ESO/INAF-VST/OmegaCAM
M18-M19 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M20 : Martin Pugh [Astronomy Picture of the Day]
M21-M26 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M27 : Gaillard Jérôme (CC BY-SA 3.0 Licence)
M28-M41 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M42 : ESO/G. Beccari
M43 : Gábor Tóth (CC BY-NC-ND Licence)
M44-M56 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M57 : NASA, ESA, and C. Robert O’Dell (Vanderbilt University)
M58-61 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
M62 : Wikipedia Commons/Hewholooks
M63-M110 : Aladin Sky Atlas développé au CDS, Observatoire de Strasbourg
Cartes créées sur le logiciel Cartes du Ciel
➥ www.ap-i.net/skychart/fr/
226

"""

re_result = re.findall(r"Messier ([0-9]+) .*\nDécouverte : (.*)\s+\((.*)\)", content)

data = pd.DataFrame(data=re_result, columns=["M#", "Decouvreur", "Date_decouverte"])
data["M#"] = data["M#"].apply(lambda x: "M"+str(int(x)))

def convert_period_to_numeric(a):

    non_numeric_discover_period = {
        "vers 1654": 1654,
        "vers 130": 130,
        "29 mai 1764": 1764,
        "vers −350": -350,
        "16 ? ?": 1600,
        "avant 1654": 1654,
        "vers −260": -260,
        "−2357": -2357
    }

    try:
        return int(a)
    except:
        return non_numeric_discover_period[a]

data["Date_decouverte"] = data["Date_decouverte"].map(convert_period_to_numeric)

print(data.groupby("Decouvreur")["M#"].count().sort_values(ascending=False))
print(data.groupby("Decouvreur")["Date_decouverte"].max().sort_values(ascending=False))

data.to_pickle(config.DISCOVER_FILE)