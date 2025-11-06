# SPEECH - Présentation Programmation Dynamique

**Rédigé par :** Loua El Jelassi  
**Matière :** Théorie de la décision  
**Année :** 2025/2026

---

## SLIDE 1 : Page de garde

Bonjour à tous,

Aujourd'hui, je vais vous présenter un sujet fondamental en théorie de la décision : la Programmation Dynamique. Cette présentation a été réalisée dans le cadre du cours de Théorie de la décision pour l'année académique 2025/2026.

---

## SLIDE 2 : Plan de la Présentation

Avant de commencer, voici le plan de ma présentation. Nous allons d'abord introduire le concept de Programmation Dynamique, puis explorer son architecture et ses étapes. Nous verrons ensuite les deux approches stratégiques de calcul, suivies de deux exemples concrets : le problème du sac à dos et le problème du plus court chemin. Nous examinerons les applications industrielles et modernes, discuterons des avantages et limites, et terminerons par une conclusion.

---

## SLIDE 3 : Qu'est-ce que la Programmation Dynamique ?

La Programmation Dynamique, ou PD, est une stratégie d'optimisation qui exploite deux propriétés clés : la structure optimale des sous-problèmes et les sous-problèmes chevauchants.

Comme vous pouvez le voir sur ce diagramme, un problème complexe est décomposé en sous-problèmes plus simples, qui sont résolus et mémorisés pour éviter les recalculs. Les solutions des sous-problèmes sont ensuite combinées pour obtenir la solution optimale du problème principal.

Trois caractéristiques fondamentales distinguent la Programmation Dynamique :

Premièrement, la **décomposition structurée**. Elle permet de décomposer un problème global en sous-problèmes, respectant le principe d'optimalité de Bellman.

Deuxièmement, **éviter les recalculs**. Elle utilise la mémorisation pour éviter de résoudre la même sous-tâche plusieurs fois.

Et troisièmement, **l'application polyvalente**. La Programmation Dynamique est très utilisée dans la gestion des ressources, l'économie, l'ingénierie et l'intelligence artificielle.

---

## SLIDE 4 : Origines et Historique

Passons maintenant à l'historique de cette méthode.

La Programmation Dynamique a été introduite dans les années 1950 par le mathématicien américain Richard Bellman. Il est important de noter que le terme « programmation » se réfère ici à la planification et non au codage informatique. L'objectif initial était de résoudre les problèmes d'optimisation séquentielle complexes.

Comme le disait Bellman lui-même : « La programmation dynamique est une méthode pour résoudre des problèmes complexes en les divisant en sous-problèmes plus simples. »

Cette citation résume parfaitement l'essence de la méthode.

---

## SLIDE 5 : Architecture et Étapes de la Méthode

Comment fonctionne la Programmation Dynamique ? Elle suit un processus structuré en cinq étapes :

**Première étape : Identification du Problème**. Il faut reconnaître la structure optimale et identifier les sous-problèmes chevauchants.

**Deuxième étape : Définition de la Relation de Récurrence**. Il s'agit d'établir la formule mathématique qui relie les sous-problèmes entre eux.

**Troisième étape : Initialisation des Cas de Base**. Il faut définir les valeurs de départ pour les plus petits sous-problèmes.

**Quatrième étape : Construction de la Solution**. On remplit le tableau de mémorisation de manière itérative, en résolvant les sous-problèmes du plus petit au plus grand.

**Cinquième étape : Reconstruction de la Solution**. À partir des résultats stockés, on retrouve la séquence optimale qui a mené à la solution.

Au cœur de cette méthode se trouve l'**Équation de Bellman**, également appelée relation de récurrence. Elle lie la valeur actuelle à la valeur future optimale.

La formule générale est : **V(s) = max sur a de [R(s,a) + γV(s')]**

Laissez-moi vous expliquer chaque élément de cette formule :

- **V(s)** représente la valeur optimale de l'état actuel s. C'est ce que nous cherchons à calculer.
- **max sur a** signifie que nous cherchons la meilleure action parmi toutes les actions possibles.
- **R(s,a)** est la récompense immédiate obtenue en étant dans l'état s et en choisissant l'action a.
- **γ** (gamma) est le facteur d'escompte, un nombre entre 0 et 1 qui permet de pondérer les récompenses futures. Plus γ est proche de 1, plus on valorise les récompenses futures. Plus il est proche de 0, plus on se concentre sur les récompenses immédiates.
- **V(s')** représente la valeur optimale de l'état suivant s' que nous atteignons après avoir pris l'action a.

Cette équation exprime donc que la valeur optimale d'un état est égale à la meilleure récompense immédiate plus la valeur optimale future, pondérée par le facteur d'escompte.

---

## SLIDE 6 : Deux Approches Stratégiques de Calcul

La Programmation Dynamique peut être implémentée selon deux méthodes complémentaires.

**La première approche est l'approche ascendante, ou Bottom-Up**. Cette méthode résout d'abord les plus petits sous-problèmes et stocke les résultats dans un tableau, c'est ce qu'on appelle la tabulation. Elle utilise ensuite ces résultats pour résoudre les problèmes de taille supérieure. Cette approche garantit qu'un sous-problème est résolu avant d'être nécessaire.

**La deuxième approche est l'approche descendante, ou Top-Down**. Elle commence par le problème principal en utilisant la récursion. Elle utilise la mémorisation : les résultats des sous-problèmes sont stockés dès qu'ils sont calculés pour la première fois. Cette approche ne résout que les sous-problèmes réellement rencontrés, ce qui peut être plus efficace dans certains cas.

Ces deux approches ont leurs avantages et sont choisies selon le contexte du problème à résoudre.

---

## SLIDE 8 : Le Problème du Sac à Dos (Knapsack)

Maintenant, passons à un exemple concret : le problème du sac à dos, également appelé Knapsack Problem en anglais.

Ce problème d'optimisation classique consiste à choisir des objets ayant un poids et une valeur pour maximiser la valeur totale sans dépasser une capacité maximale.

**L'objectif** est de maximiser la valeur totale des objets sélectionnés sous contrainte de capacité, qu'il s'agisse de poids ou de volume.

**La stratégie de la Programmation Dynamique** construit une table des solutions optimales pour toutes les combinaisons de poids et d'ensembles d'objets intermédiaires.

Regardons maintenant le schéma. À gauche, nous voyons le sac à dos vide avec une capacité de 10 kilogrammes. Au centre, nous avons les quatre objets disponibles : A, B, C et D. Chaque objet a un poids et une valeur. Par exemple, l'objet A pèse 3 kilogrammes et vaut 15 euros. L'objet B pèse 4 kilogrammes et vaut 20 euros. L'objet C pèse 2 kilogrammes et vaut 8 euros. Et l'objet D pèse 5 kilogrammes et vaut 25 euros.

La question est : quels objets devons-nous mettre dans le sac pour obtenir la plus grande valeur totale, sans dépasser les 10 kilogrammes ?

La Programmation Dynamique trouve la meilleure solution : prendre les objets A, C et D. Avec cette combinaison, nous obtenons exactement 10 kilogrammes (3 + 2 + 5) et une valeur totale de 48 euros (15 + 8 + 25). C'est la solution optimale !

---

## SLIDE 9 : Le Problème du Plus Court Chemin

Passons maintenant à un deuxième exemple concret : le problème du plus court chemin.

Ce problème consiste à trouver le chemin le plus court entre deux nœuds dans un graphe pondéré, où chaque arête a un coût ou une distance associée.

**L'objectif** est de minimiser la distance totale ou le coût pour aller d'un point de départ à un point d'arrivée dans un réseau.

**La stratégie de la Programmation Dynamique** utilise l'algorithme de Floyd-Warshall qui calcule les plus courts chemins entre toutes les paires de nœuds en utilisant la programmation dynamique.

Regardons maintenant le schéma. Nous avons un graphe avec quatre nœuds : A, B, C et D. Le nœud A est notre point de départ et le nœud D est notre point d'arrivée. Chaque arête a un poids associé : de A à B, la distance est de 4 ; de A à C, la distance est de 2 ; de B à D, la distance est de 5 ; et de C à D, la distance est de 3.

La question est : quel est le chemin le plus court pour aller de A à D ?

La Programmation Dynamique trouve la meilleure solution : passer par C, c'est-à-dire le chemin A → C → D. Regardez les flèches vertes qui montrent ce chemin optimal. Avec cette combinaison, nous obtenons une distance totale de 5 (2 + 3), ce qui est plus court que le chemin A → B → D qui aurait une distance de 9 (4 + 5).

**La relation de récurrence** utilisée pour résoudre ce problème avec l'algorithme de Floyd-Warshall est :

**dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])**

Laissez-moi vous expliquer cette formule :

- **dist[i][j]** représente la distance la plus courte entre les nœuds i et j.
- **k** est un nœud intermédiaire qui permet de trouver un chemin plus court entre i et j.
- La formule compare la distance directe entre i et j avec la distance en passant par le nœud intermédiaire k, et choisit la plus petite.

Cette formule se construit de manière itérative, en testant tous les nœuds intermédiaires possibles, garantissant ainsi de trouver le chemin le plus court.

**L'efficacité** de cette méthode permet de résoudre le problème pour toutes les paires de nœuds en une seule fois, ce qui est très utile pour les applications de navigation GPS ou de routage réseau.

---

## SLIDE 9b : Démarche - Tester Tous les Chemins

Maintenant, expliquons la démarche en testant tous les chemins possibles.

**Principe**

La Programmation Dynamique teste tous les chemins possibles de A vers D et garde le plus court.

Regardons le schéma. Il montre le graphe complet avec tous les nœuds et leurs connexions.

**Test de tous les chemins :**

**Premier chemin : A → B → D**

On peut aller de A à B avec une distance de 4, puis de B à D avec une distance de 5. Le chemin total A→B→D a une distance de 4 + 5 = 9.

**Deuxième chemin : A → C → D**

On peut aller de A à C avec une distance de 2, puis de C à D avec une distance de 3. Le chemin total A→C→D a une distance de 2 + 3 = 5.

**Conclusion : Le Plus Court Chemin**

Après avoir testé tous les chemins possibles, on constate que le chemin A→C→D avec une distance de 5 est le plus court, comparé au chemin A→B→D qui fait 9.

La Programmation Dynamique a donc trouvé le chemin optimal en testant systématiquement tous les chemins possibles et en gardant le plus court.

---

## SLIDE 10 : Applications Industrielles Réelles

La Programmation Dynamique est utilisée par les plus grandes entreprises technologiques.

Prenons l'exemple de **Google**. Le problème qu'ils rencontraient était les fautes de frappe dans les recherches. La solution ? L'utilisation de la distance de Levenshtein, un algorithme de Programmation Dynamique qui a permis d'améliorer considérablement la précision des résultats de recherche.

Autre exemple, **Netflix**. Leur problème était des recommandations peu précises. Grâce à des algorithmes de programmation dynamique, ils ont pu optimiser leurs suggestions, améliorant ainsi l'expérience utilisateur.

Ces exemples montrent l'impact concret de la Programmation Dynamique dans notre vie quotidienne.

---

## SLIDE 11 : Autres Applications Courantes et Avancées

La Programmation Dynamique est un pilier dans divers domaines de la décision opérationnelle et stratégique.

On la retrouve dans la **gestion industrielle** : planification de production, gestion de stocks, et ordonnancement.

En **finance et économie** : optimisation de portefeuille, modèles de décision stochastiques.

En **intelligence artificielle et machine learning** : contrôle optimal, apprentissage par renforcement.

En **logistique et réseaux** : recherche du chemin le plus court, optimisation de trajectoires.

Et enfin, en **bio-informatique** : alignement de séquences ADN ou protéines, comme avec l'algorithme Smith-Waterman.

Ces applications montrent l'universalité et la puissance de cette méthode.

---

## SLIDE 13 : Avantages et Limites

Comme toute méthode, la Programmation Dynamique présente des avantages et des limites.

**Les avantages** sont nombreux :
- Elle évite les calculs redondants
- La complexité est souvent réduite
- Elle garantit une solution optimale
- Elle est applicable à de nombreux domaines
- Elle sert de base pour d'autres techniques

**Cependant, elle a aussi ses limites** :
- La complexité spatiale peut être élevée
- L'identification des sous-problèmes peut être difficile
- Il y a un overhead pour les problèmes simples
- Elle nécessite une bonne analyse préalable
- Elle peut être contre-intuitive dans certains cas

Il est important de bien comprendre quand utiliser cette méthode et quand préférer une approche alternative.

---

## SLIDE 12 : Comparaison de Performance

Ce graphique compare l'efficacité entre la méthode naïve et la Programmation Dynamique de manière générale, pour n'importe quel problème résolu par ces deux approches.

La courbe rouge montre l'augmentation rapide du temps avec la méthode naïve. Cette méthode calcule les mêmes sous-problèmes plusieurs fois, ce qui conduit à une croissance exponentielle du temps d'exécution. Vous pouvez voir que même pour des valeurs relativement petites de la taille du problème n, le temps d'exécution devient rapidement prohibitif.

En revanche, la courbe verte illustre l'efficacité de la Programmation Dynamique. Cette méthode évite les recalculs en mémorisant les résultats des sous-problèmes déjà résolus, ce qui conduit à une croissance beaucoup plus lente, quasi-linéaire, du temps d'exécution. Cette différence est spectaculaire : pour des problèmes de taille moyenne, on peut obtenir un gain de performance de plusieurs ordres de grandeur.

Cette visualisation montre clairement pourquoi la Programmation Dynamique est si importante pour l'optimisation des algorithmes et pourquoi elle est largement utilisée dans l'industrie.

---

## SLIDE 14 : Conclusion

Pour conclure, retenons quelques points clés :

**Premièrement**, la Programmation Dynamique optimise les solutions complexes en exploitant la structure des problèmes.

**Deuxièmement**, elle évite les recalculs redondants grâce à la mémorisation, ce qui améliore significativement les performances.

**Troisièmement**, elle s'applique dans de nombreux domaines industriels, de la technologie à la finance en passant par la bio-informatique.

**Enfin**, elle garantit des solutions optimales de manière efficace, ce qui en fait un outil indispensable en théorie de la décision.

---

## SLIDE 15 : Références

Pour conclure cette présentation, je voudrais vous présenter les références qui ont été utilisées dans cette présentation.

**Premièrement**, le livre fondateur de Richard Bellman, "Programmation Dynamique", publié en 1957, qui est la référence historique de cette méthode que nous avons mentionnée dans la partie historique.

**Deuxièmement**, l'article de Levenshtein de 1966 sur les codes binaires capables de corriger les suppressions, insertions et inversions, qui est à la base de l'algorithme de distance de Levenshtein que nous avons présenté dans l'exemple d'application de Google.

**Enfin**, l'article de Smith et Waterman de 1981 sur l'identification de sous-séquences moléculaires communes, que nous avons mentionné dans les applications en bio-informatique.

---

## SLIDE 16 : Remerciements

Je vous remercie pour votre attention.

N'hésitez pas si vous avez des questions.

Fin de la présentation.

---

## NOTES POUR LA PRÉSENTATION

**Durée estimée :** 15-20 minutes

**Conseils :**
- Parlez clairement et à un rythme modéré
- Pausez après chaque slide pour laisser le temps à l'audience de comprendre
- Utilisez les diagrammes et graphiques comme support visuel
- Adaptez le ton selon l'audience (plus technique ou plus accessible)
- Préparez des réponses aux questions courantes sur la complexité et les applications

**Points clés à souligner :**
- La différence entre les approches Bottom-Up et Top-Down
- L'importance de l'Équation de Bellman
- Les gains de performance significatifs montrés par le graphique
- Les applications concrètes dans l'industrie

