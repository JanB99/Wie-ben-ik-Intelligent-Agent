# Onderzoeksrapport

### Versiebeheer
| Versie | Datum | Wijziging/toevoeging |
|------|------|---------|
| 0.1 | 17-9 | Opzet eerste structuur
| 1.0 | 27-9 | Uitgewerkt onderzoek en conclusie |

### Inhoud
1. [Aanleiding](#Aanleiding)
2. [Probleemstelling](#Probleemstelling)
3. [Onderzoek](#Onderzoek)
4. [Conclusie](#Conclusie)
5. [Verwijzingen](#Verwijzingen)

<a name="Aanleiding"></a>
## Aanleiding

Vanuit het Data Intelligence Lectoraat is het project opgesteld om meer inzicht te creëren en een speelsere manier voor mensen te maken om de drempel voor zowel de interesses te wekken als raakvlakken met AI te verlagen. Hiermee wordt het beeld van wat een AI is en hoe dit bij kan dragen aan de samenleving opgezet. Vanuit dit standpunt zijn dus enkele opdrachten opgezet.

Een van deze opdrachten bedraagt het maken van een Intelligent Agent (AI) die tegen de speler “Wie ben ik?” kan spelen. Iedereen is namelijk bekend met het spel “Wie ben ik?”. Wanneer deze manier van AI hierbij ingezet en aangetoond worden dat het niet een zogezegde “toverstaf/ -doos” is die de grootste berekeningen maakt. Hiermee wordt dus eigenlijk de simpliciteit of inzetbaarheid van een AI gedemonstreerd.

De AI achter het spel Wie ben ik loopt dan ook in gradaties op tot een bepaald niveau van complexiteit, waarbij in het begin het een simpelere variant nabootst van de meer standaard Nederlandse variant tot aan de complexe Amerikaanse variant (voorbeelden zoals Akinator etc.).


<a name="Probleemstelling"></a>
## Probleemstelling
Welke methodes zijn het best van toepassing bij het hanteren van een decision tree om het “Wie ben ik?” spel te spelen? 

<a name="Onderzoek"></a>
## Onderzoek
Binnen het eerstgevonden onderzoek, _‘Application of KNN and Decision Tree Classification Algorithms in the Prediction of Education Success from the Edu720 Platform.’_ (Omar Dervisevic, 2019), wordt gebruik gemaakt van het KNN (K nearest algoritme) en decision tree algoritme om een classificatie in taken te maken. Hierbij ligt de focus op de gehanteerde algoritmes en de verkregen resultaten middels deze algoritmes om hier kennis en kunde uit op te halen over het hanteren van soort (gelijkmatige) algoritmes.

In dit onderzoek wordt aangekaart dat de meest voorkomende decision trees algoritmes, ID3, C4.5, CART, etc. en wat het KNN-algoritme in houdt, echter wordt dit verder in dit hoofdstuk behandeld. Wat echter meer van belang is dat zij als definitie voor het principe van een decision tree het volgende definiëren, _‘De kern van het principe van dit algoritme is het opsplitsen van data in knooppunten en bladeren (nodes and leaves), indien de data set nog niet geanalyseerd is.’ (Omar Dervisevic, 2019)._ Hierbij lichten ze verder toe dat de splitsing zodanig wordt toegepast totdat elke criteria zijn eigen blad heeft toegewezen en iedere mogelijkheid zo een uitgangspunt heeft. Om de volgorde te bepalen wordt gebruik gemaakt van een onderscheid in de zogenaamde ‘Information Gain’ wat kortgezegd inhoudt wat de waarde is van een stuk informatie. Hiervoor kunnen methodieken zoals de Gini Index en Gain Ratio gehanteerd worden. 

Om een keuze te onderbouwen voor het hanteren van een decision tree noteren zij het volgende hier, ‘_De decision tree heeft voordelen zoals eenvoud en begrijpelijkheid, de mogelijkheid om met numerieke en categorische variabelenwaarden te werken, de mogelijkheid om snel nieuwe primers te classificeren en flexibiliteit.’ (Omar Dervisevic, 2019)_ 

 Als conclusie wordt geconcludeerd dat het van belang is dat de data die gehanteerd wordt in deze algoritmes goed inzichtelijk is doorgenomen. Hierbij ligt namelijk de focus op unbalanced- en balanced data sets. Indien dit namelijk het geval is kan het voor complicaties in de tree veroorzaken. 

 
#### C4.5 algorithm

C4.5 is een methodiek om besslissingsbomen te creëren. Op elk knooppunt van de boom worden de takken op de meest effectieve manier gesplitst in subsets. C4.5 staat ook ontbrekende attribuutwaarden toe die niet meegeteld zullen worden in het berekenen van de winst en entropie.

De C4.5 methodiek kan ook gebruik maken van verschillende kosten voor attributen. Dit is handig te gebruiken indien attributen gecategorieseerd moeten worden in belangrijkheid. Ook wordt de boom na creëren gepruned. Dit houdt in dat de boom nog eens doorlopen wordt om te proberen takken uit de boom te verwijderen die niet van belang zijn en deze te vervangen met een blad.

(C4.5 Algorithm, n.d.) 



#### C5.0 algorithm

dit is een verbeterede versie van het C4.5 algoritme. Nieuw in deze versie van het algoritme is de mogelijkheid om verschillende gewichten toe te kennen aan verschillende foutmarges.

Vergeleken met C4.5 is C5.0:
- Sneller
- Memory efficiënter
- Kleinere beslissingsboom
- Mogelijkheid voor boosting. Boosting verbetert de trees en verhoogd de accuraatheid
- Toekennen gewicht aan verschillende senarios en misclassificaties.
- Winnowing

(C4.5 Algorithm, n.d.)

> **Wat is Winnowing:**
Winnowing is een techniek uit machine learning voor het leren van linear classifiers uit gelabelde voorbeelden. Winnowing werkt vooral heel goed wanneer meerdere dimensies irrelevant zijn.
(Winnow (algorithm), n.d.)


### Alternatieven
#### KNN methode
> # KNN EXAMPLE FOTO HIER

Het **KNN**, K-nearest neighbors algorithm, berust zich op het opstellen van een model aan de hand van data, op basis van het model wordt een verwachting gegeven op basis van de verkregen K waarde oftewel beter gezegd de criteria. Een voorbeeld van een model is hier links te zien (Figuur 1 - KNN example). Enkele voor- en nadelen voor het toepassen van het KNN-algoritme is:

**Pros**
- Het maakt geen aannamen en is daarom handig toe te passen voor non-lineaire data.
- Het is een relatief simpel en makkelijk te begrijpen algoritme.
- Relatieve hoge nauwkeurigheid.
- Veelzijdig, nuttig voor het classificeren en teruglopen van data

**Cons**
- Vereist veel geheugen, aangezien het alle training data dient op te slaan.
- Indien de N (data) aanzienlijk hoog is kan de voorspelling traag zijn.
- Gevoelig voor irrelevante eigenschapen en de magnitude van de data.

Het **Brute Force** algoritme, is net zoals de naam suggereert het door alle data heen gaan en geen techniek te hanteren. Een nadeel hiervan is dat indien de omvang van de data groter wordt het in tijd fors toeneemt om het gewenste resultaat te vinden. Daarnaast is een voordeel dat het voor kleine problemen snel en enigszins stabiel is. Daarnaast is er nog het **Harmony search** algoritme, een gegeven definitie luidt als volgt, ‘_Harmony Search is een meta-heuristisch zoekalgoritme dat het improvisatieproces van musici probeert na te bootsen bij het vinden van een aangename harmonie.’ (Alireza Askarzadeh, 2017)_ HS is makkelijk te implementeren en verandert snel naar de optimale oplossing echter is dit niet een gepaste oplossing voor het probleemstuk dat zich voorstelt in de casus.


#### RANSAC methode

De RANSAC methode wordt gebruikt om “Noise” te voorkomen. Dit betekend dat als foute input gegeven wordt dit helpt om toch tot het juiste antwoord te komen. Dit wordt gedaan door de outliers en inliers te bepalen. De outliers worden dan geprobeerd Dit doet de methode iteratief.

(Random sample consensus, n.d.)  (RANSAC tutorial, n.d.)

<a name="Conclusie"></a>
## Conclusie
Om terug te komen op de probleemstelling, zijn zoals benoemd in het hoofdstuk 3 (Voor)onderzoek, wordt de beslissingsboom ondersteunt doormiddel van een vergelijkingswaarde. Deze wordt uitgewerkt aan de hand van bijv., de Gini Index of Gain Ratio. Dit is ook terug te vinden in enkele toepassingen van een beslissingsboom in andere settings.

Binnen enkele onderzoeken wordt gesproken van een probleemstuk dat zich vaker voortdoet rondom het toepassen van een beslissingsboom. Indien er namelijk sprake is van een ongelijke verdeling in de data kan het voor komen dat er een verschuiving of een dubbele uitkomst ontstaat. Dit probleem is beter bekend als unbalanced en balanced data. Hier zijn enkele methodes voor om het probleemstuk toch te verhelpen. Een methode die benoemd wordt in het onderzoek, Application of KNN and Decision Tree Class (Omar Dervisevic, 2019), is de SMOTE method. Echter aangezien de data in het ‘wie ben ik’ scenario altijd unieke waardes levert, zal het unbalanced dataprobleem zich in theorie niet voordoen.

Hier ligt de nadruk op het in theorie, aangezien het doeleinde van het ‘wie ben ik’ spel niet de standaard Nederlandse variant is, maar meer gedacht kan worden aan het Akinator spel. Akinator is een spel dat ‘wie ben ik’ nabootst, maar waarbij elk persoon gekozen kan worden als het te raden persoon. Aangezien alle personen die bedacht kunnen worden gekozen kunnen worden, is het mogelijk dat zich het unbalanced dataprobleem toch voordoet.
<a name="Verwijzingen"></a>
## Verwijzingen

Alireza Askarzadeh, E. R. (2017). _Harmony Search Algorithm._ Kerman Graduate University.

Anis Cherfi, K. N. (2018). VeryFast C4.5 Decision Tree Algorithm, Applied Artificial Intelligenc. _DOI_, 119-137.

Bronshtein, A. (2017, April 11). _Usejournal_. Opgehaald van Noteworthy: https://blog.usejournal.com/a-quick-introduction-to-k-nearest-neighbors-algorithm-62214cea29c7

_Brute Force Algorithms Explained_. (2020, January 6). Opgehaald van FreeCodeCamp: https://www.freecodecamp.org/news/brute-force-algorithms-explained/#:~:text=Brute%20Force%20Algorithms%20are%20exactly,%2C%20each%20from%200%2D9.

_C4.5 Algorithm_. (sd). Opgehaald van Wikipedia: https://en.wikipedia.org/wiki/C4.5_algorithm

Omar Dervisevic, E. Z. (2019). _Application of KNN and Decision TreeClassification Algorithms in the Prediction ofEducation Success from the Edu720 Platform._ Department for Computer Science and InformaticsZmaja od Bosne bb, Kampus Univerziteta, 71000 Sarajevo: University of Sarajevo.

_Random sample consensus_. (sd). Opgehaald van Wikipedia: https://en.wikipedia.org/wiki/Random_sample_consensus

_RANSAC tutorial_. (sd). Opgehaald van http://helios.mi.parisdescartes.fr/~lomn/Cours/CV/SeqVideo/Material/RANSAC-tutorial.pdf

Sarah Itania, F. L. (2020). _A One-Class Classification Decision TreeBased on Kernel Density Estimation._ University of Mons, Mons Belgium & FNRS, Brussels Belgium: University of Mons & FNRS.

Sihem Oujdi, H. d. (2019). _C4.5 Decision Tree Algorithm for Spatial Data, Alternatives and Performances._ Oran, Algeria & Paris, France: Oran University of Science and Technology & University Sorbonne Paris Nord.

_Winnow (algorithm)_. (sd). Opgehaald van Wikipedia: https://en.wikipedia.org/wiki/Winnow_(algorithm)
