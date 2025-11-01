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

Avant de commencer, voici le plan de ma présentation. Nous allons d'abord introduire le concept de Programmation Dynamique, puis explorer son architecture et ses étapes. Nous verrons ensuite les deux approches stratégiques de calcul, suivies d'un exemple concret : le problème du sac à dos. Nous examinerons les applications industrielles et modernes, discuterons des avantages et limites, et terminerons par une conclusion.

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

Au cœur de cette méthode se trouve l'**Équation de Bellman**, également appelée relation de récurrence. Elle lie la valeur actuelle à la valeur future optimale. La formule générale est : V(s) = max sur a de [R(s,a) + γV(s')], où V(s) représente la valeur de l'état s, R(s,a) est la récompense, γ est le facteur d'escompte, et s' est l'état suivant.

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

Comme vous pouvez le voir sur ce schéma, nous avons plusieurs objets avec leurs poids et valeurs. La Programmation Dynamique permet de trouver la combinaison optimale, ici les objets A et C, qui maximise la valeur tout en respectant la contrainte de poids.

**Formulation mathématique** : On cherche à maximiser la somme des valeurs multipliées par les variables de décision, sous la contrainte que la somme des poids ne dépasse pas la capacité W. Chaque objet peut être pris ou non, ce qui se traduit par des variables binaires.

La **relation de récurrence** utilisée est : dp[i][w] = max entre prendre l'objet i ou ne pas le prendre, ce qui donne : max de dp[i-1][w] et dp[i-1][w-wi] + vi, où dp[i][w] représente la valeur maximale avec les i premiers objets et une capacité w.

**L'efficacité** de cette méthode évite de tester les milliers de combinaisons possibles, garantissant la solution optimale de manière polynomiale.

---

## SLIDE 9 : Applications Industrielles Réelles

La Programmation Dynamique est utilisée par les plus grandes entreprises technologiques.

Prenons l'exemple de **Google**. Le problème qu'ils rencontraient était les fautes de frappe dans les recherches. La solution ? L'utilisation de la distance de Levenshtein, un algorithme de Programmation Dynamique qui a permis d'améliorer considérablement la précision des résultats de recherche.

Autre exemple, **Netflix**. Leur problème était des recommandations peu précises. Grâce à des algorithmes de programmation dynamique, ils ont pu optimiser leurs suggestions, améliorant ainsi l'expérience utilisateur.

Ces exemples montrent l'impact concret de la Programmation Dynamique dans notre vie quotidienne.

---

## SLIDE 10 : Autres Applications Courantes et Avancées

La Programmation Dynamique est un pilier dans divers domaines de la décision opérationnelle et stratégique.

On la retrouve dans la **gestion industrielle** : planification de production, gestion de stocks, et ordonnancement.

En **finance et économie** : optimisation de portefeuille, modèles de décision stochastiques.

En **intelligence artificielle et machine learning** : contrôle optimal, apprentissage par renforcement.

En **logistique et réseaux** : recherche du chemin le plus court, optimisation de trajectoires.

Et enfin, en **bio-informatique** : alignement de séquences ADN ou protéines, comme avec l'algorithme Smith-Waterman.

Ces applications montrent l'universalité et la puissance de cette méthode.

---

## SLIDE 11 : Avantages et Limites

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

Ce graphique compare la complexité temporelle entre la méthode naïve et la Programmation Dynamique pour le calcul de la suite de Fibonacci.

La courbe rouge montre l'explosion exponentielle du temps avec la méthode naïve, qui a une complexité de O(2ⁿ). Vous pouvez voir que même pour des valeurs relativement petites de n, le temps d'exécution devient rapidement prohibitif.

En revanche, la courbe verte illustre l'efficacité linéaire de la Programmation Dynamique, qui a une complexité de O(n). Cette différence est spectaculaire : pour n égal à 30, on obtient un gain de performance d'environ un milliard de fois.

Cette visualisation montre clairement pourquoi la Programmation Dynamique est si importante pour l'optimisation des algorithmes.

---

## SLIDE 13 : Conclusion

Pour conclure, retenons quelques points clés :

**Premièrement**, la Programmation Dynamique optimise les solutions complexes en exploitant la structure des problèmes.

**Deuxièmement**, elle évite les recalculs redondants grâce à la mémorisation, ce qui améliore significativement les performances.

**Troisièmement**, elle s'applique dans de nombreux domaines industriels, de la technologie à la finance en passant par la bio-informatique.

**Enfin**, elle garantit des solutions optimales de manière efficace, ce qui en fait un outil indispensable en théorie de la décision.

En ce qui concerne les **perspectives d'avenir**, la Programmation Dynamique continue d'évoluer avec l'intelligence artificielle et le machine learning, ouvrant de nouvelles possibilités d'optimisation. Elle reste un domaine de recherche actif avec de nombreuses applications émergentes.

---

## SLIDE 14 : Remerciements

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

