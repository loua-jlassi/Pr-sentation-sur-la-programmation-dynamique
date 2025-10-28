# PROGRAMMATION DYNAMIQUE

## Présentation académique

---

**Université/École**  
**Cours : Algorithmique Avancée**  
**Année académique 2024**

---

# PLAN DE LA PRÉSENTATION

1. **Introduction à la programmation dynamique**
2. **Historique et origines**
3. **Principes et méthodes**
4. **Exemples d'application**
5. **Conclusion**

---

# INTRODUCTION À LA PROGRAMMATION DYNAMIQUE

## Qu'est-ce que la programmation dynamique ?

- **Définition** : Technique d'optimisation qui résout des problèmes complexes en les décomposant en sous-problèmes plus simples
- **Principe clé** : Éviter la résolution répétée des mêmes sous-problèmes
- **Objectif** : Optimiser l'efficacité algorithmique

---

# HISTORIQUE ET ORIGINES

## Les pionniers

### Richard Bellman (1950-1957)
- **Père de la programmation dynamique**
- Développe le concept au RAND Corporation
- Publie "Dynamic Programming" en 1957
- Résout des problèmes d'optimisation militaire

### Origine du nom
- **"Dynamic"** : Référence aux problèmes multi-étapes
- **"Programming"** : Au sens de planification/optimisation
- Terme choisi pour contourner les restrictions militaires

---

# HISTORIQUE ET ORIGINES (suite)

## Évolution historique

### 1950s-1960s
- Applications militaires et économiques
- Optimisation de trajectoires
- Planification de ressources

### 1970s-1980s
- Extension aux problèmes combinatoires
- Algorithmes de graphes
- Intelligence artificielle

### 1990s-Aujourd'hui
- Informatique théorique
- Bio-informatique
- Machine Learning

---

# PRINCIPES ET MÉTHODES

## Les 4 méthodes principales

### 1. **Approche Bottom-Up (Ascendante)**
- Résolution des sous-problèmes du plus petit au plus grand
- Utilisation de tableaux pour stocker les résultats
- Exemple : Suite de Fibonacci

### 2. **Approche Top-Down (Descendante)**
- Résolution récursive avec mémorisation
- Évite la résolution répétée des mêmes sous-problèmes
- Exemple : Problème du sac à dos

---

# PRINCIPES ET MÉTHODES (suite)

### 3. **Méthode des étapes**
- Décomposition du problème en étapes séquentielles
- Optimisation à chaque étape
- Exemple : Algorithme de Floyd-Warshall

### 4. **Méthode de la programmation linéaire dynamique**
- Optimisation de fonctions linéaires
- Contraintes temporelles
- Exemple : Problème de transport

---

# EXEMPLES D'APPLICATION

## Exemple 1 : Suite de Fibonacci

### Problème
Calculer le n-ième terme de la suite de Fibonacci :
- F(0) = 0, F(1) = 1
- F(n) = F(n-1) + F(n-2) pour n > 1

### Solution naïve (récursive)
```python
def fibonacci_naif(n):
    if n <= 1:
        return n
    return fibonacci_naif(n-1) + fibonacci_naif(n-2)
```
**Complexité** : O(2^n) - Très inefficace !

---

# EXEMPLES D'APPLICATION (suite)

## Exemple 1 : Suite de Fibonacci (solution optimisée)

### Solution avec programmation dynamique
```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    # Tableau pour stocker les résultats
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Calcul bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```
**Complexité** : O(n) - Beaucoup plus efficace !

---

# EXEMPLES D'APPLICATION (suite)

## Exemple 2 : Problème du sac à dos

### Énoncé
- Sac à dos de capacité W
- n objets avec poids w[i] et valeur v[i]
- Objectif : Maximiser la valeur totale

### Formulation mathématique
```
Maximiser : Σ(v[i] * x[i])
Sous contraintes : Σ(w[i] * x[i]) ≤ W
                  x[i] ∈ {0,1}
```

---

# EXEMPLES D'APPLICATION (suite)

## Exemple 2 : Solution du sac à dos

### Algorithme de programmation dynamique
```python
def sac_a_dos(W, poids, valeurs, n):
    # Tableau 2D pour stocker les résultats
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if poids[i-1] <= w:
                dp[i][w] = max(valeurs[i-1] + dp[i-1][w-poids[i-1]], 
                              dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]
```

---

# EXEMPLES D'APPLICATION (suite)

## Exemple 3 : Plus longue sous-séquence commune (LCS)

### Problème
Trouver la longueur de la plus longue sous-séquence commune à deux chaînes.

### Exemple
- Chaîne 1 : "ABCDGH"
- Chaîne 2 : "AEDFHR"
- LCS : "ADH" (longueur = 3)

### Formule récursive
```
LCS(i,j) = {
    0,                           si i=0 ou j=0
    1 + LCS(i-1,j-1),           si X[i] = Y[j]
    max(LCS(i-1,j), LCS(i,j-1)), sinon
}
```

---

# EXEMPLES D'APPLICATION (suite)

## Exemple 4 : Distance de Levenshtein

### Problème
Calculer la distance minimale entre deux chaînes de caractères (nombre minimum d'opérations : insertion, suppression, substitution).

### Formule
```
d(i,j) = {
    max(i,j),                    si min(i,j) = 0
    d(i-1,j-1),                  si s1[i] = s2[j]
    1 + min(d(i-1,j), d(i,j-1), d(i-1,j-1)), sinon
}
```

### Application
- Correction orthographique
- Comparaison de séquences ADN
- Détection de plagiat

---

# CONCLUSION

## Avantages de la programmation dynamique

### ✅ **Efficacité**
- Évite les calculs redondants
- Complexité souvent réduite de manière significative

### ✅ **Polyvalence**
- Applicable à de nombreux domaines
- Résout des problèmes complexes de manière élégante

### ✅ **Optimisation**
- Trouve souvent la solution optimale
- Base solide pour d'autres techniques

---

# CONCLUSION (suite)

## Limites et considérations

### ⚠️ **Complexité spatiale**
- Peut nécessiter beaucoup de mémoire
- Tableaux multidimensionnels

### ⚠️ **Identification des sous-problèmes**
- Parfois difficile de reconnaître la structure
- Nécessite une bonne analyse du problème

### ⚠️ **Overhead**
- Pas toujours nécessaire pour des problèmes simples
- Évaluation coût/bénéfice importante

---

# CONCLUSION (suite)

## Domaines d'application modernes

### 🚀 **Informatique**
- Algorithmes de graphes
- Traitement d'images
- Intelligence artificielle

### 🚀 **Sciences**
- Bio-informatique
- Physique computationnelle
- Économie

### 🚀 **Industrie**
- Optimisation de ressources
- Planification de production
- Logistique

---

# MERCI POUR VOTRE ATTENTION

## Questions et discussions

### Contact
**Nom de l'étudiant**  
**Email : etudiant@universite.fr**

### Ressources complémentaires
- "Introduction to Algorithms" - Cormen, Leiserson, Rivest, Stein
- "Dynamic Programming" - Richard Bellman
- Cours en ligne : MIT OpenCourseWare

---

**Fin de la présentation**
