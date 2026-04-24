## Table des matières

1. [Introduction à l'informatique quantique](#1-introduction-à-linformatique-quantique)
2. [Le qubit](#2-le-qubit)
   - [Bit vs qubit](#21-bit-vs-qubit)
   - [La superposition](#22-la-superposition)
   - [La mesure et l'effondrement](#23-la-mesure-et-leffondrement)
   - [La sphère de Bloch](#24-la-sphère-de-bloch)
3. [Notations](#3-notations)
   - [Notation bra-ket (Dirac)](#31-notation-bra-ket-dirac)
   - [Représentation vectorielle et matricielle](#32-représentation-vectorielle-et-matricielle)
   - [Systèmes multi-qubits](#33-systèmes-multi-qubits)
4. [Portes quantiques](#4-portes-quantiques)
   - [Propriétés générales](#41-propriétés-générales)
   - [Portes de Pauli (X, Y, Z)](#42-portes-de-pauli-x-y-z)
   - [Porte Hadamard (H)](#43-porte-hadamard-h)
   - [Portes de phase (S, T)](#44-portes-de-phase-s-t)
   - [Porte CNOT](#45-porte-cnot)
   - [Porte Toffoli (CCX)](#46-porte-toffoli-ccx)
   - [Porte Multi-Controlled X (MCX)](#47-porte-multi-controlled-x-mcx)
5. [L'intrication quantique](#5-lintrication-quantique)
6. [Algorithmes quantiques](#6-algorithmes-quantiques)
   - [Deutsch-Jozsa](#61-deutsch-jozsa)
   - [Algorithme de Grover](#62-algorithme-de-grover)
7. [Exercices — référence code](#7-exercices--référence-code)
   - [Ex00 — Superposition](#ex00--superposition)
   - [Ex01 — Intrication](#ex01--intrication)
   - [Ex02 — Bruit quantique (IBM)](#ex02--bruit-quantique-ibm)
   - [Ex03 — Deutsch-Jozsa](#ex03--deutsch-jozsa)
   - [Ex04 — Algorithme de Grover](#ex04--algorithme-de-grover)
8. [Glossaire](#8-glossaire)
9. [Références](#9-références)

---

## 1. Introduction à l'informatique quantique

L'informatique classique repose sur des **bits** : des interrupteurs qui valent soit 0, soit 1. Toute l'information numérique — images, vidéos, programmes — est encodée dans des séquences de ces deux états.

L'informatique quantique utilise une autre unité d'information : le **qubit**. Un qubit peut lui aussi valoir 0 ou 1, mais avant d'être mesuré, il peut exister dans une **combinaison des deux** — c'est la *superposition*. De plus, deux qubits peuvent être **intriqués**, c'est-à-dire corrélés d'une manière qu'aucune physique classique ne peut reproduire.

Ce ne sont pas de simples curiosités. Ces propriétés permettent à certains algorithmes quantiques de résoudre des problèmes que les ordinateurs classiques ne peuvent pas traiter en temps raisonnable.

**Quelques exemples concrets :**
- Factorisation de grands nombres : classiquement exponentiel, quantiquement polynomial (algorithme de Shor).
- Recherche dans une base non triée : classiquement O(N), quantiquement O(√N) (algorithme de Grover).
- Simulation de molécules et de matériaux pour la chimie ou la pharmacologie.

> **Important :** les ordinateurs quantiques ne remplacent pas les ordinateurs classiques. Ils sont utiles pour une famille spécifique de problèmes où la structure mathématique permet d'exploiter la superposition et l'intrication.

---

## 2. Le qubit

### 2.1 Bit vs qubit

| Propriété | Bit classique | Qubit |
|---|---|---|
| États possibles | 0 ou 1 | 0, 1, ou superposition |
| Avant mesure | Déterministe | Probabiliste |
| Après mesure | Inchangé | Effondrement irréversible |
| Corrélation | Indépendant | Peut être intriqué |

Un bit classique est comme un interrupteur : il est soit éteint (0), soit allumé (1). Un qubit, avant mesure, est comme une pièce qui tourne en l'air — il n'est ni pile ni face, il est *les deux en même temps*, avec des probabilités associées.

### 2.2 La superposition

La superposition est l'état dans lequel un qubit se trouve **avant** toute mesure. Ce n'est pas de l'ignorance — le qubit n'a vraiment pas encore de valeur définie. C'est un état physique à part entière.

Mathématiquement, un qubit en superposition s'écrit :

```
|ψ⟩ = α|0⟩ + β|1⟩
```

où α et β sont des **amplitudes complexes** vérifiant :

```
|α|² + |β|² = 1
```

La probabilité d'obtenir 0 lors d'une mesure est **|α|²**, et la probabilité d'obtenir 1 est **|β|²**.

L'état de superposition le plus courant (50/50) est :

```
|ψ⟩ = (1/√2)|0⟩ + (1/√2)|1⟩
```

Ce qui donne 50% de chance d'obtenir 0 et 50% d'obtenir 1 — c'est exactement ce que produit la porte Hadamard.

<!-- IMAGE: Représentation graphique d'une superposition — deux colonnes de probabilités égales (|0⟩ et |1⟩ à 50% chacun) -->

### 2.3 La mesure et l'effondrement

La mesure est un **processus actif et irréversible**. Quand on mesure un qubit en superposition, son état s'effondre sur l'une des valeurs classiques (0 ou 1) selon les probabilités dictées par ses amplitudes.

Analogie : imaginez un distributeur automatique dont vous ne savez pas ce qu'il contient. Avant d'appuyer, il pourrait sortir n'importe quel article (superposition). Dès que vous appuyez (mesure), il sort un seul article et ne peut plus jamais sortir les autres. L'acte de choisir a forcé le système à se définir.

**Conséquences pratiques :**
- On ne peut pas "lire" un état quantique directement sans le détruire.
- Pour connaître les probabilités, on doit répéter l'expérience de nombreuses fois.
- Chaque répétition s'appelle un **shot**.

```
500 shots → ~250 fois "0", ~250 fois "1" pour un état (|0⟩+|1⟩)/√2
```

Le nombre de shots détermine la précision statistique. 1000 shots donnent une meilleure image des probabilités que 10 shots.

### 2.4 La sphère de Bloch

Tout état pur d'un qubit peut être visualisé comme un **point sur une sphère unitaire** — la sphère de Bloch.

```
|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩
```

- Le **pôle nord** représente |0⟩
- Le **pôle sud** représente |1⟩
- L'**équateur** représente toutes les superpositions 50/50
- La **longitude** (angle φ) encode la phase complexe

Les portes quantiques sont des **rotations** de ce vecteur sur la sphère :
- Pauli X : rotation de 180° autour de l'axe X
- Pauli Y : rotation de 180° autour de l'axe Y
- Pauli Z : rotation de 180° autour de l'axe Z
- Hadamard : rotation de 180° autour de l'axe X+Z (diagonale)

<!-- IMAGE: Sphère de Bloch avec pôles |0⟩ et |1⟩, axes X Y Z, et un vecteur d'état en position quelconque -->

---

## 3. Notations

### 3.1 Notation bra-ket (Dirac)

La notation bra-ket est le langage standard de la mécanique quantique. Elle permet d'écrire des états et des produits scalaires de manière compacte.

**Ket** `|ψ⟩` — représente un état quantique (vecteur colonne) :
```
|0⟩ = [1]    |1⟩ = [0]
      [0]          [1]
```

**Bra** `⟨ψ|` — représente le conjugué transposé du ket (vecteur ligne) :
```
⟨0| = [1, 0]    ⟨1| = [0, 1]
```

**Produit scalaire** `⟨φ|ψ⟩` — amplitude de probabilité de trouver |ψ⟩ dans l'état |φ⟩ :
```
⟨0|0⟩ = 1    ⟨1|1⟩ = 1    ⟨0|1⟩ = 0    ⟨1|0⟩ = 0
```

Les états |0⟩ et |1⟩ sont **orthonormaux** : ils sont perpendiculaires et de norme 1.

**États courants en notation bra-ket :**

| Notation | Description | Vecteur |
|---|---|---|
| `\|0⟩` | État de base "zéro" | [1, 0]ᵀ |
| `\|1⟩` | État de base "un" | [0, 1]ᵀ |
| `\|+⟩` | Superposition (+) = H\|0⟩ | [1/√2, 1/√2]ᵀ |
| `\|-⟩` | Superposition (-) = H\|1⟩ | [1/√2, -1/√2]ᵀ |

### 3.2 Représentation vectorielle et matricielle

Un qubit est un **vecteur dans un espace de Hilbert** de dimension 2. Une porte quantique à 1 qubit est une **matrice unitaire 2×2** (telle que U†U = I).

L'application d'une porte U à un état |ψ⟩ est une **multiplication matricielle** :

```
|ψ'⟩ = U|ψ⟩
```

Exemple avec la porte X appliquée à |0⟩ :
```
X|0⟩ = [0 1] × [1] = [0] = |1⟩  ✓
       [1 0]   [0]   [1]
```

La condition d'**unitarité** (U†U = I) garantit deux choses fondamentales :
1. La norme est préservée (les probabilités somment toujours à 1).
2. L'opération est **réversible** — on peut toujours reconstruire l'entrée depuis la sortie.

### 3.3 Systèmes multi-qubits

Pour décrire un système de n qubits, on utilise le **produit tensoriel** ⊗.

L'espace d'état de 2 qubits est de dimension 4 :

```
Base : |00⟩, |01⟩, |10⟩, |11⟩

|00⟩ = |0⟩ ⊗ |0⟩ = [1, 0, 0, 0]ᵀ
|01⟩ = |0⟩ ⊗ |1⟩ = [0, 1, 0, 0]ᵀ
|10⟩ = |1⟩ ⊗ |0⟩ = [0, 0, 1, 0]ᵀ
|11⟩ = |1⟩ ⊗ |1⟩ = [0, 0, 0, 1]ᵀ
```

> **Convention Qiskit :** le qubit d'indice le plus bas (qubit 0) correspond au bit le plus à droite dans la notation. Ainsi `|01⟩` signifie qubit 1 = 0, qubit 0 = 1.

Un système de n qubits peut exister en superposition de **2ⁿ états simultanément**. C'est la source de la puissance exponentielle de l'informatique quantique : 50 qubits représentent 2⁵⁰ ≈ 10¹⁵ états en même temps.

---

## 4. Portes quantiques

### 4.1 Propriétés générales

Toutes les portes quantiques respectent deux propriétés essentielles :

1. **Unitarité** : `U†U = I` — la porte est réversible et préserve les probabilités.
2. **Linéarité** : `U(α|0⟩ + β|1⟩) = αU|0⟩ + βU|1⟩`

Contrairement aux portes logiques classiques (NAND, OR...), une porte quantique ne peut **jamais perdre d'information**. Connaître la sortie suffit à retrouver l'entrée.

### 4.2 Portes de Pauli (X, Y, Z)

Les trois portes de Pauli correspondent à des rotations de **180°** autour des trois axes de la sphère de Bloch.

---

#### Porte Pauli-X (NOT quantique)

La porte X est l'équivalent quantique du NOT. Elle échange |0⟩ et |1⟩.

**Matrice :**
```
X = [0  1]
    [1  0]
```

**Action :**
```
X|0⟩ = |1⟩
X|1⟩ = |0⟩
X(α|0⟩ + β|1⟩) = α|1⟩ + β|0⟩
```

**Circuit Qiskit :** `circuit.x(qubit)`

<!-- IMAGE: Symbole de circuit de la porte X (carré avec X) et sphère de Bloch montrant la rotation 180° autour de l'axe X -->

---

#### Porte Pauli-Y

La porte Y combine un flip de bit et un flip de phase, avec un facteur imaginaire.

**Matrice :**
```
Y = [0   -i]
    [i    0]
```

**Action :**
```
Y|0⟩ =  i|1⟩
Y|1⟩ = -i|0⟩
```

**Circuit Qiskit :** `circuit.y(qubit)`

<!-- IMAGE: Symbole de circuit de la porte Y et rotation sur la sphère de Bloch autour de l'axe Y -->

---

#### Porte Pauli-Z (flip de phase)

La porte Z ne change pas les probabilités de mesure (|0⟩ reste |0⟩ et |1⟩ reste |1⟩), mais elle inverse la **phase** de |1⟩. Cela n'est visible que si le qubit est en superposition.

**Matrice :**
```
Z = [1   0]
    [0  -1]
```

**Action :**
```
Z|0⟩ = |0⟩
Z|1⟩ = -|1⟩
Z|+⟩ = |-⟩     (change le signe de la superposition)
Z|-⟩ = |+⟩
```

**Circuit Qiskit :** `circuit.z(qubit)`

> La phase est invisible directement, mais essentielle dans les interférences et tous les algorithmes quantiques.

<!-- IMAGE: Symbole de circuit de la porte Z et rotation 180° autour de l'axe Z sur la sphère de Bloch -->

---

### 4.3 Porte Hadamard (H)

La porte Hadamard est **la plus fondamentale** de l'informatique quantique. Elle crée la superposition à partir d'un état de base.

**Matrice :**
```
H = (1/√2) × [1   1]
              [1  -1]
```

**Action :**
```
H|0⟩ = (1/√2)(|0⟩ + |1⟩) = |+⟩    → superposition +
H|1⟩ = (1/√2)(|0⟩ - |1⟩) = |-⟩    → superposition -
```

**Propriété clé :** `H × H = I` (son propre inverse)

```
H|+⟩ = |0⟩    → retour à un état classique par interférence constructive
H|-⟩ = |1⟩
```

C'est cette propriété qui est au cœur de Deutsch-Jozsa : appliquer H deux fois "annule" la superposition, sauf si l'oracle a modifié la phase entre les deux.

**Circuit Qiskit :** `circuit.h(qubit)`

<!-- IMAGE: Symbole de circuit de la porte H, représentation géométrique sur la sphère de Bloch (rotation autour de l'axe X+Z), et schéma montrant H|0⟩ → |+⟩ → mesure 50/50 -->

---

### 4.4 Portes de phase (S, T)

Les portes de phase ajoutent une rotation partielle autour de l'axe Z sans modifier les probabilités de mesure.

---

#### Porte S (√Z)

**Matrice :**
```
S = [1   0]
    [0   i]
```

Rotation de **90°** (π/2) autour de l'axe Z. `S² = Z`.

**Circuit Qiskit :** `circuit.s(qubit)`

---

#### Porte T (⁴√Z)

**Matrice :**
```
T = [1         0      ]
    [0   e^(iπ/4)     ]
```

Rotation de **45°** (π/4) autour de l'axe Z. `T² = S`, `T⁴ = Z`.

**Circuit Qiskit :** `circuit.t(qubit)`

> Les portes S et T sont importantes en cryptographie quantique et dans l'algorithme de Shor. Elles permettent aussi de construire l'universalité quantique avec H et CNOT.

<!-- IMAGE: Tableau comparatif des portes Z, S, T avec les angles de rotation et les matrices -->

---

### 4.5 Porte CNOT

La porte CNOT (Controlled-NOT) agit sur **deux qubits** :
- Le **qubit de contrôle** : si il vaut |1⟩, l'opération est appliquée.
- Le **qubit cible** : reçoit un NOT si le contrôle est |1⟩.

**Matrice (base |00⟩, |01⟩, |10⟩, |11⟩) :**
```
CNOT = [1  0  0  0]
       [0  1  0  0]
       [0  0  0  1]
       [0  0  1  0]
```

**Action :**
```
CNOT|00⟩ = |00⟩    (contrôle=0 → rien)
CNOT|01⟩ = |01⟩    (contrôle=0 → rien)
CNOT|10⟩ = |11⟩    (contrôle=1 → flip cible)
CNOT|11⟩ = |10⟩    (contrôle=1 → flip cible)
```

**Circuit Qiskit :** `circuit.cx(control, target)`

**Création d'intrication :**
```
H|0⟩ ⊗ |0⟩ = |+⟩ ⊗ |0⟩ = (1/√2)(|00⟩ + |10⟩)
CNOT → (1/√2)(|00⟩ + |11⟩)   ← état de Bell intriqué
```

C'est exactement le circuit de l'exercice 01. Après le CNOT, les deux qubits sont intriqués : on ne peut plus les décrire indépendamment.

<!-- IMAGE: Symbole de circuit CNOT (point sur le contrôle, cercle avec plus sur la cible), puis circuit H + CNOT avec les états intermédiaires annotés -->

---

### 4.6 Porte Toffoli (CCX)

La porte Toffoli est une porte CNOT à **deux qubits de contrôle** : le qubit cible est inversé si et seulement si les deux contrôles sont à |1⟩.

```
Toffoli|110⟩ = |111⟩
Toffoli|111⟩ = |110⟩
Tous les autres états → inchangés
```

**Circuit Qiskit :** `circuit.ccx(control1, control2, target)`

Elle permet d'implémenter la porte NAND quantique et est donc **universelle** pour le calcul quantique réversible.

---

### 4.7 Porte Multi-Controlled X (MCX)

Généralisation du CNOT à **n qubits de contrôle** : le qubit cible est inversé seulement si tous les contrôles sont à |1⟩.

**Circuit Qiskit :** `circuit.mcx(control_list, target)`

Utilisée dans l'oracle de Grover pour identifier un état spécifique parmi 2ⁿ.

<!-- IMAGE: Schéma MCX avec 3 qubits de contrôle et 1 qubit cible, montrant les points de contrôle et le cercle NOT -->

---

## 5. L'intrication quantique

L'intrication est peut-être le phénomène le plus contre-intuitif de la mécanique quantique. Deux qubits sont **intriqués** quand leur état global **ne peut pas** s'écrire comme le produit de deux états individuels.

**État de Bell (état intriqué maximal) :**
```
|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)
```

Cet état est **impossible à factoriser** :
```
(1/√2)(|00⟩ + |11⟩) ≠ (a|0⟩ + b|1⟩) ⊗ (c|0⟩ + d|1⟩)  pour tout a, b, c, d
```

**Ce que ça signifie concrètement :**
- Avant mesure : les deux qubits n'ont pas d'état individuel défini.
- En mesurant le qubit 0 et en obtenant 0 → le qubit 1 sera forcément 0.
- En mesurant le qubit 0 et en obtenant 1 → le qubit 1 sera forcément 1.
- Cette corrélation est instantanée, quelle que soit la distance.

> Ce n'est pas que les qubits "se communiquent" : l'information ne voyage pas. C'est que leur état commun était non-local depuis le début.

**Comment créer l'intrication :**

```
Étape 1 : circuit.h(0)   → qubit 0 en superposition : (|0⟩+|1⟩)/√2
Étape 2 : circuit.cx(0, 1) → CNOT copie l'incertitude vers qubit 1

Résultat : (1/√2)(|00⟩ + |11⟩)
```

**Résultats observés (ex01) :**
- Uniquement `00` et `11`  
- Jamais `01` ni `10`  
- Proportions ~50/50

<!-- IMAGE: Histogramme type ex01 montrant uniquement les barres 00 et 11 à 50% chacune -->

---

## 6. Algorithmes quantiques

### 6.1 Deutsch-Jozsa

#### Contexte et motivation

Le problème de Deutsch-Jozsa est le **premier algorithme prouvant l'avantage quantique**. Il n'a pas d'application pratique directe, mais il illustre parfaitement comment la superposition permet de répondre à une question globale en une seule requête là où un ordinateur classique en nécessite plusieurs.

**Le problème :** On nous donne une boîte noire (oracle) f : {0,1}ⁿ → {0,1}. Cette fonction est garantie d'être soit :
- **Constante** : retourne toujours 0, ou toujours 1.
- **Équilibrée** : retourne 0 exactement pour la moitié des entrées, 1 pour l'autre.

**Question :** La fonction est-elle constante ou équilibrée ?

**Coût classique :** Dans le pire cas, il faut évaluer f sur **2^(n-1) + 1 entrées** (la moitié + 1) pour être certain.

**Coût quantique : une seule évaluation de l'oracle** — quelle que soit la taille de l'entrée.

---

#### Circuit de Deutsch-Jozsa

```
Qubits d'entrée  : q0, q1, q2 (n=3)
Qubit ancilla    : q3

q0 : ─── H ─── [Oracle] ─── H ─── Mesure
q1 : ─── H ─── [Oracle] ─── H ─── Mesure
q2 : ─── H ─── [Oracle] ─── H ─── Mesure
q3 : ─ X ─ H ─ [Oracle] ───────── (non mesuré)
```

<!-- IMAGE: Diagramme complet du circuit Deutsch-Jozsa avec les 4 qubits, l'initialisation X sur l'ancilla, les deux séries de H, et le bloc Oracle -->

**Étapes détaillées :**

**1. Initialisation**
```
|ψ0⟩ = |0⟩|0⟩|0⟩|0⟩

Appliquer X sur ancilla → |0⟩|0⟩|0⟩|1⟩
```

**2. Superposition**
```
Appliquer H sur tous → (1/√8)(|0⟩+|1⟩)(|0⟩+|1⟩)(|0⟩+|1⟩) ⊗ (1/√2)(|0⟩-|1⟩)
```
Les n qubits d'entrée sont maintenant dans une superposition uniforme de toutes les entrées possibles. L'ancilla est dans l'état `(|0⟩-|1⟩)/√2` — c'est l'astuce de l'oracle de phase.

**3. Oracle quantique (boîte noire)**

L'oracle réalise la transformation :
```
|x⟩|y⟩ → |x⟩|y ⊕ f(x)⟩
```

Grâce à l'ancilla dans `(|0⟩-|1⟩)/√2`, cela équivaut à :
```
|x⟩ → (-1)^f(x) |x⟩
```

L'oracle **encode f(x) dans la phase** plutôt que dans un qubit de sortie. Ce tour de passe-passe est appelé le **kick-back de phase**.

- Si f est **constante** : toutes les phases sont +1 (ou toutes -1) → aucune différence relative.
- Si f est **équilibrée** : la moitié des phases sont +1, l'autre moitié -1 → interférence destructive.

**4. Deuxième application de H**
```
Appliquer H sur les n qubits d'entrée seulement
```

L'interférence quantique amplifie l'état |00...0⟩ si la fonction est constante, et l'annule si elle est équilibrée.

**5. Mesure**

| Oracle | Résultat attendu | Interprétation |
|---|---|---|
| Constant | `000` (tous les bits à 0) | Interférence constructive sur |0⟩ |
| Équilibré | Autre que `000` | Interférence destructive sur |0⟩ |

<!-- IMAGE: Comparaison de deux histogrammes côte à côte — oracle constant (seule barre à "000") et oracle équilibré (barres réparties sur d'autres états) -->

---

#### Oracles utilisés dans ex03

**Oracle constant-0 :** Ne fait rien. f(x) = 0 pour tout x.

**Oracle constant-1 :** Applique X sur l'ancilla. f(x) = 1 pour tout x.

**Oracle équilibré :** CNOT depuis chaque qubit d'entrée vers l'ancilla. Cela flip l'ancilla pour exactement la moitié des entrées.
```
f(x) = x₀ XOR x₁ XOR x₂
```

---

### 6.2 Algorithme de Grover

#### Le problème de recherche

On a une liste de **N = 2ⁿ éléments non triés** et on cherche un ou plusieurs éléments satisfaisant une condition donnée (l'oracle).

- **Classique :** O(N) en moyenne — il faut en moyenne vérifier la moitié des éléments.
- **Quantique (Grover) :** O(√N) — une accélération quadratique.

Pour N = 1 000 000 : classique = 500 000 vérifications, Grover = ~785.

---

#### Vue d'ensemble du circuit

```
q0 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Mesure
q1 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Mesure
q2 : ─ H ─ [Oracle] ─ [Diffuser] ─ ... ─ Mesure

      Init   Répéter ~(π/4)√(N/k) fois
```

<!-- IMAGE: Circuit complet de Grover avec les 3 blocs : initialisation H, puis itération Oracle+Diffuser, puis mesure -->

---

#### Les trois parties de l'algorithme

**1. Initialisation : superposition uniforme**

On applique H sur tous les qubits pour créer une superposition égale de tous les 2ⁿ états :

```
|s⟩ = H⊗ⁿ|0...0⟩ = (1/√N) Σ|x⟩   pour x ∈ {0,...,N-1}
```

Chaque état a une amplitude de 1/√N et donc une probabilité de 1/N.

**2. L'Oracle : marquage par la phase**

L'oracle est une boîte noire qui inverse la phase de l'état cible (ou des états cibles) :

```
Oracle|x⟩ = -|x⟩   si x est une solution
Oracle|x⟩ =  |x⟩   sinon
```

Après l'oracle, l'amplitude de l'état cible est la seule à être négative. La distribution des probabilités est inchangée (mesurer maintenant donnerait encore 1/N pour tout état). L'information est dans la phase, pas dans l'amplitude.

<!-- IMAGE: Diagramme en barres montrant les amplitudes après l'oracle — toutes positives sauf la cible qui est négative -->

**3. Le Diffuser : amplification par réflexion**

Le diffuser applique la transformation : **réflexion autour de la moyenne des amplitudes**.

```
D = 2|s⟩⟨s| - I = H⊗ⁿ · (2|0⟩⟨0| - I) · H⊗ⁿ
```

**Intuition géométrique :** Imaginez la moyenne des amplitudes. Après l'oracle, la cible est en dessous de la moyenne (amplitude négative). Le diffuser "reflète" chaque amplitude autour de cette moyenne → la cible se retrouve bien au-dessus.

```
Avant oracle  : toutes les amplitudes à +1/√N
Après oracle  : cible à -1/√N, reste à +1/√N
Après diffuser: cible très haute, reste légèrement plus bas
```

<!-- IMAGE: Trois diagrammes en barres : amplitudes initiales (uniformes), après oracle (cible négative), après diffuser (cible amplifiée) -->

**Implémentation du diffuser :**
```
H sur tous → X sur tous → H sur dernier → MCX → H sur dernier → X sur tous → H sur tous
```

---

#### Nombre d'itérations optimal

Après k itérations Oracle + Diffuser, la probabilité de mesurer l'état cible est :

```
P(k) = sin²((2k+1)θ)    où sin(θ) = √(m/N), m = nombre de cibles
```

Le nombre optimal d'itérations est :

```
k_opt ≈ (π/4) × √(N/m)
```

Pour n=3 qubits, N=8, une cible :
```
k_opt ≈ (π/4) × √8 ≈ 2.2 → 2 itérations
```

<!-- IMAGE: Courbe P(k) en fonction du nombre d'itérations, montrant le premier pic au nombre optimal, puis l'oscillation -->

> Trop peu d'itérations = amplitude insuffisante. Trop d'itérations = l'amplitude "dépasse" et redescend. Le nombre optimal est précis.

---

#### Résultats attendus (ex04)

Pour n=3 qubits, cible "101", 2 itérations :
- L'état `|101⟩` devrait apparaître dans **~97%** des mesures.
- Les autres états ont des probabilités très faibles.

<!-- IMAGE: Histogramme de Grover pour n=3, cible "101" — une barre dominante à ≈97%, les 7 autres presque nulles -->

---

## 7. Exercices — référence code

### Ex00 — Superposition

**Objectif :** Créer l'état `(|0⟩ + |1⟩) / √2` avec un seul qubit.

**Circuit :**
```
q0 : ─ H ─ Mesure
```

**Code clé :**
```python
circuit = QuantumCircuit(1, 1)
circuit.h(0)       # Hadamard → superposition
circuit.measure(0, 0)
```

**Résultat attendu :** Histogramme avec `0` et `1` à ~50% chacun sur 500 shots.

<!-- IMAGE: Circuit ex00 (texte ou mpl) + histogramme résultant avec barres 0 et 1 à 50% -->

---

### Ex01 — Intrication

**Objectif :** Créer l'état de Bell `(|00⟩ + |11⟩) / √2`.

**Circuit :**
```
q0 : ─ H ─●─ Mesure
           │
q1 : ─────X─ Mesure
```

**Code clé :**
```python
circuit = QuantumCircuit(2, 2)
circuit.h(0)        # superposition sur q0
circuit.cx(0, 1)    # CNOT : q0 contrôle, q1 cible
circuit.measure([0, 1], [0, 1])
```

**Résultat attendu :** Uniquement `00` et `11`, jamais `01` ni `10`.

<!-- IMAGE: Circuit ex01 + histogramme montrant uniquement 00 et 11 à ~50% chacun -->

---

### Ex02 — Bruit quantique (IBM)

**Objectif :** Exécuter le même circuit de l'ex01 sur un vrai ordinateur quantique IBM et observer les différences.

**Résultat attendu :** Les états `01` et `10` apparaissent (quelques %) à cause du bruit matériel.

**Pourquoi la différence ?**
- Les qubits physiques sont imparfaits : temps de cohérence limités, erreurs de portes.
- La transpilation adapte le circuit à la topologie du backend (toutes les paires de qubits ne sont pas directement connectées).
- Les erreurs de mesure ajoutent aussi du bruit.

<!-- IMAGE: Comparaison de deux histogrammes — ex01 (simulateur, idéal) vs ex02 (IBM réel, avec bruit visible sur 01 et 10) -->

---

### Ex03 — Deutsch-Jozsa

**Objectif :** Implémenter l'algorithme sur 4 qubits (3 entrée + 1 ancilla) et identifier si l'oracle est constant ou équilibré.

**Code clé :**
```python
def build_dj_circuit(oracle, n):
    circuit = QuantumCircuit(n + 1, n)
    circuit.x(n)           # ancilla → |1⟩
    circuit.h(range(n+1))  # superposition globale
    circuit.compose(oracle, inplace=True)
    circuit.h(range(n))    # interférence
    circuit.measure(range(n), range(n))
    return circuit
```

**Interprétation des résultats :**
```
Mesure = "000" → Oracle CONSTANT
Mesure ≠ "000" → Oracle ÉQUILIBRÉ
```

**Usage :**
```bash
python ex03.py
# Teste automatiquement 3 oracles : Constant-0, Constant-1, Balanced
```

---

### Ex04 — Algorithme de Grover

**Objectif :** Implémenter Grover pour retrouver un ou plusieurs états cibles parmi 2ⁿ.

**Code clé :**
```python
# Changer n et targets pour tester
run_exercise(n=3, targets=["101"], shots=1024)
run_exercise(n=3, targets=["011", "110"], shots=1024)
run_exercise(n=2, targets=["11"], shots=1024)
```

**Le nombre d'itérations est calculé automatiquement :**
```python
iterations = max(1, round((math.pi / 4) * math.sqrt(N / k)))
```

**Complexité :**
```
Classique : O(N)    → N/2 vérifications en moyenne
Grover     : O(√N)  → √N itérations Oracle + Diffuser
```

Pour n=10 qubits (1024 états) : classique = ~512 requêtes, Grover = ~25.

---

## 8. Glossaire

| Terme | Définition |
|---|---|
| **Qubit** | Unité d'information quantique, pouvant être en superposition de |0⟩ et |1⟩ |
| **Superposition** | État dans lequel un qubit est simultanément 0 et 1 avec des amplitudes associées |
| **Mesure** | Opération irréversible qui effondre la superposition sur un état classique |
| **Shot** | Une répétition du circuit. On accumule de nombreux shots pour reconstituer les probabilités |
| **Intrication** | Corrélation non-locale entre deux ou plusieurs qubits : l'état global ne peut pas être factorisé |
| **État de Bell** | État intriqué maximal de deux qubits : `(|00⟩+|11⟩)/√2` |
| **Amplitude** | Nombre complexe associé à chaque état de base. La probabilité est le carré de sa norme |
| **Phase** | Argument complexe d'une amplitude. Invisible à la mesure directe, mais crucial pour l'interférence |
| **Porte unitaire** | Transformation quantique réversible qui préserve la norme de l'état |
| **Oracle** | Boîte noire qui encode une fonction f dans le circuit quantique |
| **Kick-back de phase** | Technique pour encoder f(x) dans la phase via un qubit ancilla en `(|0⟩-|1⟩)/√2` |
| **Diffuser** | Opérateur de Grover qui amplifie les amplitudes des états cibles par réflexion |
| **Coherence** | Capacité d'un qubit à maintenir sa superposition. Se dégrade avec le temps (décoherence) |
| **Bruit quantique** | Erreurs dues aux imperfections matérielles, à la décoherence et aux interactions parasites |
| **Transpilation** | Adaptation d'un circuit idéal à la topologie et aux contraintes réelles d'un backend IBM |
| **Simulateur Aer** | Simulateur classique de circuits quantiques, idéal (sans bruit), fourni par IBM/Qiskit |
| **Sphère de Bloch** | Représentation géométrique de l'état d'un qubit sur une sphère unitaire |
| **Produit tensoriel ⊗** | Opération mathématique pour combiner des espaces d'états de plusieurs qubits |

---

## 9. Références

**Documentation officielle**
- [IBM Quantum — Hello World](https://quantum.cloud.ibm.com/docs/en/guides/hello-world)
- [IBM Quantum Learning — Basics of Quantum Information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction)
- [Qiskit Documentation](https://docs.quantum.ibm.com/)

**Vidéos pédagogiques**
- [Introduction to Quantum Computing (playlist)](https://www.youtube.com/watch?v=9PQIKPHgzo4&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4)
- [Qubits en détail](https://www.youtube.com/watch?v=bLW4wraE77I&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=4)
- [Portes quantiques](https://www.youtube.com/watch?v=0WZmkIyHOks&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=10)
- [Algorithmes quantiques](https://www.youtube.com/watch?v=5_Di12FXRsM&list=PLE3ovFxnzNpY3zGw8sHqRorxecoItAAq4&index=18)

**Livres**
- *L'Univers à portée de main* — Christophe Galfard
- *A Brief History of Time* — Stephen Hawking
- *Quantum Computation and Quantum Information* — Nielsen & Chuang (référence académique complète)