# Wie ben ik AI?
![Zuyd Logo](/lfs/ZuydLogo.png)



**Namen**:

Jan Baljan _(1746545)_

Luc van Deenen _(1728458)_

Kevin Paffen _(1753665)_

Jeroen Kornips _(1653342)_

**Opleiding**:

HBO-ICT, IT Development

**Minor**:

Artificial Intelligence (BD02)

**Organisatie**:

Shannen Dolls & Jim Bemelen


# Inhoud
1. ### [Handleiding](#Kop1)

2. ### [Plan van Aanpak](#Kop2)

3. ### [Onderzoeksrapport](#Kop3)

4. ### [Ontwerp Document](#Kop4)

5. ### [Resultaten](#Kop5)

6. ### [Verwijzigingen](#Kop6)



<a name="Kop1"></a>
# Handleiding

## frameworks
front-end: Vue
- Vuetify, UI 
- Axios, API calls

backend: Flask
- Flask cors, Cross origin requests

## Startup
Om het programma op te starten zal eerst de back end opgestart moeten worden. daarna zal de Front End opgestart worden.

### Back End
De Back End wordt als volgt Opgestart:

Open de PowerShell in het project en type het volgende in deze volgorde:

	cd server

	Python3.8 –m venv env

	Env/scripts/activate

	Pip install Flask Flask-Cors

	python app.py

### Front End

Nu de Back End is opgestart kunnen we de Front End opstarten. Dit doen we door het volgende in een tweede PowerShell in het project in deze volgorde te typen:

	cd client

	npm run serve

<a name="Kop2"></a>
# Plan van Aanpak

>### Versiebeheer
>| Versie | Datum | Wijziging/toevoeging |
>|------|------|---------|
>| 0.1 | 13-9 | Opzet eerste structuur

## Inhoud
1. ### [Inleiding](#PlanVanAanpak/Inleiding)
2. ### [Opdrachtomschrijving](#PlanVanAanpak/Opdrachtomschrijving)
3. ### [Op te leveren producten](#PlanVanAanpak/Producten)
4. ### [Project aanpak en fasering](#PlanVanAanpak/Projectaanpak)

<a name="PlanVanAanpak/Inleiding"></a>
## 1. Inleiding
Het Plan van Aanpak beschrijft hoe de opdracht aangepakt en uitgevoerd gaat worden. Om het project in goede banen te leiden (beheersen & plannen) en het project tot een goed einde te brengen, is dit document opgesteld.

<a name="PlanVanAanpak/Opdrachtomschrijving"></a>
## 2. Opdrachtomschrijving
### Achtergrond - Wie ben ik?
Elke speler krijgt een kaartje op de rug gespeld met daarop de naam van een bekende persoon. Behalve degene die het briefje op zijn rug heeft, kan dus iedereen zien welke persoon daar staat vermeld. Degene die het zelf niet weet, wie hij voorstelt, probeert nu uit te zoeken wie hij is. De spelers zijn nu Intelligent Agents. Hoe spelen zij dit spel? En welke strategie gebruiken ze hierbij?

### Doel en Resultaat
Het doel is om een AI te maken die in staat is om het spel wie ben ik te spelen. We beginnen met de originele versie van het spel. In de loop van het proces gaan we ook mogelijk onderzoeken of de AI ook om kan gaan met veranderende spelregels. Waarbij het resultaat een Intelligent Agent bedraagt die in staat is om het spel Wie ben ik te spelen.

### Probleemanalyse
Om een Intelligent Agent te maken die in staat is om Wie ben ik te spelen komen enkele zaken en vragen te pas die van belang zijn om het succes van dit project te helpen bereiken. Zo dient gedacht te worden over de aanpak van het opstellen van de Intelligent Agent. Hierbij moet ruimte en tijd worden gegeven aan het opzoeken van alternatieven methodieken voor het opstellen van deze Intelligent Agent.

Daarbij is het van belang dat duidelijk wordt aangetoond met behulp van de producten, (die benoemd zijn in het volgende hoofdstuk 4. Op te leveren producten) dit met als doeleinde zodat de weg naar het eindproduct en succes zo duidelijk is als het eindproduct zelf.

<a name="PlanVanAanpak/producten"></a>
## 3. Op te leveren producten
Het product moet gerealiseerd worden in Python en moet ingezet kunnen worden als een demonstrator. Ontwerp het systeem op een modulaire manier, werk met interfaces en kies het juiste abstractieniveau werk met interfaces en kies het juiste abstractieniveau. Werk met .git en documenteer het systeem goed zodat het overdraagbaar is.

### shortlist aan te leveren producten
- Dockerfile
- Overdrachtsdocument in Markdown:
	- Minimale requirements:
	- Ontwerp van software
	- Installatie handleiding met onder andere:
		- Globale stappenplan installatie
		- Gebruikte libraries en frameworks
	- Resultaten
- Source code in GitHub omgeving:
	- Heldere structuur en naamgeving van code en bestanden

### Randvoorwaarden
- Python als backend
- Voorkeur python als tool voor front-end
- Werken met .git versiebeheer
- GitHub repository van Zuyd gebruiken

### Scope
In het kader van de scope van dit
project moet er tenminste voldaan worden aan een user-interface die de menselijke speler in staat stelt om
te interacteren met zowel het spel als de intelligent agent. Daarnaast moet de intelligent agent gerealiseerd
worden op modulaire manier, waarbij de opsplitsing van de modules van belang is.

### Hulpmiddelen van Zuyd
Vanuit Zuyd wordt de Github omgeving gefaciliteerd en ondersteuning aangeboden aan de studenten bij het (aan)maken van de Dockerfiles.

<a name="PlanVanAanpak/Projectaanpak"></a>
## 4. Projectaanpak/fasering
Omdat we vaker contactmomenten met de procesbegeleider hebben, is het voor de kwaliteit van het project van belang om continu feedback te vragen. Vandaar dat er als projectaanpak voor Kanban is gekozen. In tegenstelling tot de watervalmethode kan er door middel van korte sprints zodoende om feedback worden gevraagd wat ten goede komt voor het project.

Binnen het project wordt een aangepaste variant gehanteerd om het project te begeleiden:

- Oriëntatie, Kanban
	- Plan van Aanpak
- Analyse, Kanban
	- Vooronderzoek / Onderzoeksrapport
- Ontwerp, Kanban
	- Ontwerpdocument (bevat de specificaties van het ontwerp en daarbij dus ook gelijk het Srs)
- Realisatie, Agile
	- Proof of Concept / Demo (te vinden in de GitHub omgeving)
- Eind, Kanban
	- Extended Abstract (Markdown)
	- Handleiding
	- Posterpresentatie (Powerpoint)



<a name="Kop3"> </a>
# Onderzoeksrapport

>### Versiebeheer
>| Versie | Datum | Wijziging/toevoeging |
>|------|------|---------|
>| 0.1 | 17-9 | Opzet eerste structuur
>| 1.0 | 27-9 | Uitgewerkt onderzoek en conclusie |

### Inhoud
1. [Aanleiding](#OnderzoeksRapport/Aanleiding)
2. [Probleemstelling](#OnderzoeksRapport/Probleemstelling)
3. [Onderzoek](#OnderzoeksRapport/Onderzoek)
4. [Conclusie](#OnderzoeksRapport/Conclusie)


<a name="OnderzoeksRapport/Aanleiding"></a>
## Aanleiding

Vanuit het Data Intelligence Lectoraat is het project opgesteld om meer inzicht te creëren en een speelsere manier voor mensen te maken om de drempel voor zowel de interesses te wekken als raakvlakken met AI te verlagen. Hiermee wordt het beeld van wat een AI is en hoe dit bij kan dragen aan de samenleving opgezet. Vanuit dit standpunt zijn dus enkele opdrachten opgezet.

Een van deze opdrachten bedraagt het maken van een Intelligent Agent (AI) die tegen de speler “Wie ben ik?” kan spelen. Iedereen is namelijk bekend met het spel “Wie ben ik?”. Wanneer deze manier van AI hierbij ingezet en aangetoond worden dat het niet een zogezegde “toverstaf/ -doos” is die de grootste berekeningen maakt. Hiermee wordt dus eigenlijk de simpliciteit of inzetbaarheid van een AI gedemonstreerd.

De AI achter het spel Wie ben ik loopt dan ook in gradaties op tot een bepaald niveau van complexiteit, waarbij in het begin het een simpelere variant nabootst van de meer standaard Nederlandse variant tot aan de complexe Amerikaanse variant (voorbeelden zoals Akinator etc.).


<a name="OnderzoeksRapport/Probleemstelling"></a>
## Probleemstelling
Welke methodes zijn het best van toepassing bij het hanteren van een decision tree om het “Wie ben ik?” spel te spelen? 

<a name="OnderzoeksRapport/Onderzoek"></a>
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
![KNN picture](/lfs/Onderzoek/Figuur1.png)
*Figuur 1 KNN methode*

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

<a name="OnderzoeksRapport/Conclusie"></a>
## Conclusie
Om terug te komen op de probleemstelling, zijn zoals benoemd in het hoofdstuk 3 (Voor)onderzoek, wordt de beslissingsboom ondersteunt doormiddel van een vergelijkingswaarde. Deze wordt uitgewerkt aan de hand van bijv., de Gini Index of Gain Ratio. Dit is ook terug te vinden in enkele toepassingen van een beslissingsboom in andere settings.

Binnen enkele onderzoeken wordt gesproken van een probleemstuk dat zich vaker voortdoet rondom het toepassen van een beslissingsboom. Indien er namelijk sprake is van een ongelijke verdeling in de data kan het voor komen dat er een verschuiving of een dubbele uitkomst ontstaat. Dit probleem is beter bekend als unbalanced en balanced data. Hier zijn enkele methodes voor om het probleemstuk toch te verhelpen. Een methode die benoemd wordt in het onderzoek, Application of KNN and Decision Tree Class (Omar Dervisevic, 2019), is de SMOTE method. Echter aangezien de data in het ‘wie ben ik’ scenario altijd unieke waardes levert, zal het unbalanced dataprobleem zich in theorie niet voordoen.

Hier ligt de nadruk op het in theorie, aangezien het doeleinde van het ‘wie ben ik’ spel niet de standaard Nederlandse variant is, maar meer gedacht kan worden aan het Akinator spel. Akinator is een spel dat ‘wie ben ik’ nabootst, maar waarbij elk persoon gekozen kan worden als het te raden persoon. Aangezien alle personen die bedacht kunnen worden gekozen kunnen worden, is het mogelijk dat zich het unbalanced dataprobleem toch voordoet.



<a name="Kop4"></a>
# Ontwerpdocument

## Inhoud
1. [Aanpak](#OntwerpDocument/Aanpak) 
2. [Architectuur](#OntwerpDocument/Achitectuur) 
3. [Infrastructuur](#OntwerpDocument/Infrastructuur)
3. [Infrastructuur Back End](#OntwerpDocument/Backend)
3. [Infrastructuur Front End](#OntwerpDocument/Frontend)


<a name="OntwerpDocument/Aanpak"></a>
## 1. Aanpak

Naar aanleiding van de probleemstelling (Baljan, Paffen, van Deenen, & Kornips, 2020) uit de casusbeschrijving moet een set aan karakters geclassificeerd/voorspeld worden op basis van doeltreffende vragen die gesteld worden. Deze vragen moeten, na verloop van tijd en aantal gestelde vragen, de set aan potentiële karakters verkleinen. Hierbij is het essentieel om te weten welke vraag er op welk moment en in welke volgorde gesteld wordt.

## 1.1 Classificatie

In het kader van classificatie zijn er een aantal methodieken beschikbaar die ieder voor- en nadelen met zich meebrengen. In de context van de casus wordt er gaandeweg meer informatie vergaard over een specifiek karakter op basis van de gestelde vragen. Dus hoe meer vragen er gesteld worden, des te meer zekerheid wordt gecreëerd over het te raden karakter.

Ieder classificatie model classificeert een object aan de hand van zogenaamde “features”. Dit zijn kenmerken/eigenschappen die in relatie staan met het te classificeren object. Features kunnen enorm breed worden opgevat, waarbij zowel categorische als numerieke data opgevat kan worden als feature. Dit is in het kader van de casus het geval.

Bovendien kan worden geconcludeerd dat de features die verkregen moeten worden zullen voortkomen uit de antwoorden op de vragen. Hierbij zal na iedere vraag een antwoord verwacht worden die de lijst aan features zal vergroten, waardoor voorspellingen maken gaandeweg nauwkeuriger zullen worden.

## 1.2 Model

Op basis van de kenmerken van het op te lossen probleem en een validerend gesprek met de opdrachtgever is besloten om het Decision Tree algoritme te gebruiken bij toepassing van de oplossing. Uit het bestuderen en observeren van de kenmerkende aspecten van het probleem viel op dat deze op een simplistische manier kunnen worden gemodelleerd in de vorm van een binaire boomstructuur.

De wortel van de boom zal dienen als startpunt, waarbij de punten waar de boom zich vertakt zullen dienen als punten waar vragen zullen worden gesteld. Verder zullen de bladeren van de boom dienen als voorspelling van het karakter. De boom analogie zal in het vervolg ook gehanteerd worden, sinds deze een simpele weergave geeft van de architectuur.

  
<a name="OntwerpDocument/Achitectuur"></a>
# 2. Technische Architectuur

Uit de _Aanpak_ blijkt dat het hanteren van een Decision Tree (Beslissingsboom) voldoende geschikt is om het onderliggend probleem (Baljan, Paffen, van Deenen, & Kornips, 2020) op te lossen. De beslissingsboom is hiertoe in staat mits er wordt voldaan aan bepaalde eisen rondom de data en de omliggende infrastructuur (frameworks, backend, front-end). Deze zullen in dit hoofdstuk worden besproken.

## 2.1 Database

De te voorspellen karakters moeten worden ontleed om passende en authentieke kenmerken/features te onderscheiden. De kenmerken moeten vervolgens in het juiste formaat worden opgesomd in een database. Aangezien slechts één tabel nodig zal zijn om de features en de labels, de namen van de karakters, op te slaan zal er gebruik worden gemaakt van het CSV-bestandsformaat (Comma Separated Values). Hierbij is de achterliggende gedachte dat ieder karakter een rij aan features bevat. De individuele features kunnen zowel numeriek als categorisch zijn.

## 2.2 Beslissingsboom

Om de architectuur zo concreet en gedetailleerd mogelijk te beschrijven is het zeer nuttig om het classificatiemodel van simpel naar complex te ontleden, waarbij ieder deel grondig wordt uitgelegd met passende afbeeldingen en diagrammen (Rokach & Maimon, 2005). Echter is het ook verstandig om eerst een globaal overzicht te geven van de techniek, die in de volgende paragraaf als kern theorie wordt benoemd.

### 2.2.1 Kern theorie

Een beslissingsboom is niets meer dan een structuur van zowel takpunten (nodes) als bladeren (leafs). De boom kan zoals een echte boom getraceerd worden vanaf de wortel tot aan een blad. Dit wordt het doorlopen van de boom genoemd. Normaliter kan een boom op een bepaald punt meerdere vertakkingen hebben. Dit is in de theorie mogelijk, echter wordt er bij beslissingsbomen over het algemeen gewerkt met een binaire boomstructuur. Dit is een structuur die een ingraad van precies 1 heeft en een uitgraad van hoogstens 2. In het kader van de casus wordt een vraag gesteld bij iedere vertakking (node). Dit is een “waar” of “niet waar” vraag, waardoor een binaire boom meer doeltreffend is, omdat er telkens antwoord kan worden gegeven uit twee keuzes (waar, niet waar). Wanneer wordt gesproken over de complexiteit van het zoeken in een binaire zoekboom dan kan deze worden geformuleerd op basis van het beste mogelijke scenario en het slechtst mogelijke scenario, waarbij de complexiteit een O(n) en een O(log n) respectievelijk bedraagt. Hierbij is in het geval van het beste scenario de beslissingsboom volledig gebalanceerd, en in het geval van het slechtste scenario de boom helemaal niet gebalanceerd is (Cormen, Leiserson, Rivest, & Stein, 2009).


![Figuur1](/lfs/Ontwerp/Figuur1.png)
*Figuur 1 Binaire boom*
### 2.2.2 Vraag object

De boom wordt gebouwd aan de hand van mogelijke vragen die gesteld kunnen worden op basis van de dataset. Hierbij worden de features getransformeerd naar vragen. Iedere vraag omvat een waarde, die correspondeert met een bepaalde feature, en een referentie naar de verzamelnaam van de desbetreffende feature.

Door middel van deze constructie kan een vraag worden opgesteld. Bijvoorbeeld: is [verzamelnaam] gelijk aan [feature]? Wanneer de verzamelnaam gelijk is aan “haarkleur” en de bijbehorende feature van deze vraag gelijk is aan “blonde”, dan wordt de vraag: is haarkleur gelijk aan blonde? Wanneer een feature numeriek is van waarde, dan kan de vraag anders worden geformuleerd, namelijk in de vorm van een drempelwaarde. Bijvoorbeeld: is [verzamelnaam] groter dan [feature]? Wanneer “leeftijd” wordt genomen als verzamelnaam en “21” wordt genomen als feature, dan wordt de vraag: is leeftijd groter dan 21?

Op deze manier van vragen formuleren kan er een duidelijke scheiding worden gemaakt binnen de dataset op basis van een vraag.

![Figuur2](/lfs/Ontwerp/Figuur2.png)
*Figuur 2 Question Object Class*


### 2.2.3 Blad object

Aan het uiteinde van iedere tak in de boomstructuur wordt het resultaat gerepresenteerd als een blad object. Hierbij wordt in principe na opdeling van de rijen gekeken of verdere opdeling mogelijk is. Wanneer dit niet het geval is dan blijft er één resultaat over, namelijk de classificatie van een object waarbij het label van dit object zal worden gerepresenteerd.

In het geval dat bepaalde rijen precies dezelfde features hebben, maar geen gelijke labels hebben, dan bestaat het resultaat uit meerdere geclassificeerde objecten. Dit is in de praktijk een ongewenst resultaat, want dan is er geen eenduidige classificatie. Echter is dit wel reden om aan de bel te trekken, want dit resultaat betekent dat er niet voldoende onderscheid is binnen de dataset. Aldus de dataset zal specifieker moeten worden ontleed in de vorm van verschillende features.


![Figuur3](/lfs/Ontwerp/Figuur3.png)
*Figuur 3 Node Object Class*



### 2.2.4 Information Gain

Op basis van het vraag object is het mogelijk om een boomstructuur in elkaar te zetten die de dataset bij ieder takpunt opdeelt in twee groepen. Hiermee kan classificatie worden verricht door de boom vanaf de wortel door te lopen. Echter is dit geen goed classificatie model, sinds er geen slimme vragen worden gesteld. Met “slim” wordt bedoeld dat er van tevoren wordt nagegaan hoeveel informatie deze vertakking oplevert in het kader van het gehele plaatje. Een bepaalde vraag deelt de dataset op in twee delen, waarbij iedere helft een bepaald aantal te classificeren objecten bevat die ieder minstens één feature met elkaar gemeen hebben (Witten, Frank, & Hall, 2011).

**Gini Index**

Om te bepalen wat de mate aan informatie is bij iedere vertakking moet eerst de kwaliteit van een split in de dataset worden gemeten. Een mogelijke en vaak gehanteerde methode is de Gini Index bepalen van een vertakking. Hierbij wordt de mate aan onzuiverheid bepaald van een set aan rijen. Dit geeft een indicatie van de onzekerheid op een bepaald punt aan de hand van een set aan rijen. Wanneer de onzuiverheid gelijk is aan 0, dan is de set optimaal zuiver. Dit betekent bovendien dat er geen twijfels mogelijk zijn over de inhoud van de rijen, sinds er geen variatie is in de rijen. Hierbij is het doel natuurlijk om de Gini score zo dicht mogelijk bij de 0 te krijgen.



	Algorithm gini(rows):

		Counts = countClasses(rows)

		Impurity = 1

		For label in counts:

			Impurity -= (label/size(rows))^2

		Return impurity


Deze pseudocode beschrijft het algoritme om de gini index te berekenen. Hierbij wordt met de parameter _rows,_ de rijen aan data bedoeld die na iedere scheiding verkleind wordt door een bepaalde factor. De maat aan onzuiverheid wordt geretourneerd aan het einde van de functie.

**Information Entropy**

Op basis van de Gini Index kan de onzekerheid van een vertakking worden berekend. Hierbij is de volgende stap om de informatie winst te bepalen, door de proportie van het aantal elementen in beide takken te vermenigvuldigen met de Gini Index van beide takken.


	Algorithm informationGain_Gini (currentGini, true_branch, false_branch):

		P = size(true_branch) / (size(true_branch) + size(false_branch))

		Return currentGini – p * gini(true_branch) - (1 – p) * gini(false_branch)


De parameters van deze functie zijn de huidige gini index waarde voor de desbetreffende dataset en de vertakkingen van de huidige dataset in zowel true als false branches. De variant op de information gain formule wordt geretourneerd aan het einde van de functie.

Uiteraard kan de information entropy functie ook gehanteerd. Deze is een alternatief van de Gini Index, en ziet er als volgt uit in psuedocode. 

	Algorithm informationGain_Entropy(true_branch, false_branch):
		
		p = len(true_branch) / (len(true_branch) + len(false_branch))
		
		if p == 0:
			return - (1-p) * log2(1-p)
		elif (1-p) == 0:
			return - p * log2(p)
		else:
			return - p * log2(p) - (1-p) * log2(1-p)

**Best mogelijke vraag vinden**

Om de best mogelijke vraag te vinden voor een set aan rijen moet de informatie winst worden gemaximaliseerd. Dat wil zeggen dat er voor iedere mogelijke vraag uit de verkregen set aan data, iedere mogelijke vraag moet worden gesteld. Deze vraag resulteert in een specifieke deling van de data in twee branches. Vervolgens wordt de informatie winst bepaald van iedere mogelijke vertakking. De vertakking van de hoogst mogelijke informatie winst op basis van de dataset zal worden gehanteerd als de definitieve deling van de dataset.


	Algorithm findBestQuestion(dataset):

		bestGain = 0

		bestQuestion = null

		For column in columns:

			For unique values in column:

				question = new Question(column, value)

				true_rows, false_rows = partition(dataset, question)

				Gain = informationGain(gini(dataset), true_rows, false_rows)

				If gain > bestGain:

					bestGain = gain

					bestQuestion = question

		return bestGain, bestQuestion



Deze functie vind op basis van een bepaalde dataset de best mogelijke vraag om de dataset zo gebalanceerd mogelijk te scheiden, waarbij de vraag die de hoeveelheid vergaarde informatie genereerd wordt gemaximaliseerd.
### 2.2.5 Model diagram


![Figuur4](/lfs/Ontwerp/Figuur4.png)
*Figuur 4 Model weergave Besslissingsboom*

Door middel van het beschreven algoritme in 2.2.1, 2.2.2, 2.2.3 en 2.2.4 wordt de dataset opgesplitst en verkleind. Wanneer dit proces op een recursieve manier wordt uitgevoerd ontstaat een boomstructuur die bij iedere takpunt een vraagobject bevat en bij ieder blad een bladobject bevat. Wanneer de boom is gebouwd kan deze worden doorlopen van boven naar beneden, waarbij telkens een vraag gesteld wordt over het te classificeren object.

![Figuur5](/lfs/Ontwerp/Figuur5.png)
*Figuur 5 Class Diagram*

In het bovenstaande class diagram is de structuur weergeven van de backend van het “Wie ben ik?" Spel. Deze begint bij een class genaamd Tree die een root bevat van het object type Node. Deze Node bevat op zichzelf weer een question van het type Quesion en een true-, false branch. Deze true- en false branches zijn op zich weer node’s / leafs. De question bevat een column namelijk de index. Daarnaast bevat de leaf class een prediction die aangeeft welke waarde er voorspeld wordt.


### 2.2.6 Voor- en nadelen beslissingsboom

De beslissingsboom brengt een aantal voor- en nadelen met zich mee, die moeten worden afgewogen om deze ontwerpkeuze te doorgronden. Deze zullen in tabel formaat worden opgesomd (Goddard, 2016).


| **Pros** | **Cons** |
|------|------|
|De tijdcomplexiteit is erg snel met een O(d), waarbij d staat voor de diepte van de boom. Dat wil zeggen dat tijdens het doorlopen van de boom ieder element nooit zal worden geraadpleegd, maar slechts een fractie van de elementen die in totaal de diepte van de boom vormen zullen worden doorlopen.| Greedy aanpak, dit wil zeggen dat hoewel er bij ieder takpunt de meest optimale vraag wordt gevonden, deze niet de meest optimale vraag hoeft te zijn wanneer er globaal naar de features wordt gekeken. |
| Wat betreft begrijpbaarheid is een beslissingsboom erg goed te begrijpen door mensen, aangezien de methodiek een juiste en simplistische weerspiegeling biedt van de manier hoe mensen keuzes maken. |Aangezien de boom telkens een lineaire splitsing maakt in de huidige dataset, betekent dit dat er veel splitsingen nodig zijn om een correcte voorspelling te maken over de data.|
|Wanneer de juiste vragen worden gevraagd bij ieder takpunt in de boom, zal de dataset zoveel mogelijk in twee gelijke delen worden gesplitst. Dit draagt bij aan een snellere zoektocht door de boom.| Overfitting, kleine aanpassingen in de data zullen zorgen voor grote variantie in de voorspellingen. Dit is minder relevant in het kader van de casus.|


<a name="OntwerpDocument/Infrastructuur"></a>
# 3. Infrastructuur Architectuur

Naar aanleiding van gesprekken met de opdrachtgevers is besloten om het probleem op te lossen in de vorm van een webapplicatie, waarbij de python omgeving zal dienen als backend. Hierdoor is het benodigd om de infrastructuur architectuur en de bijbehorende API’s te beschrijven. Bovendien is dit in het kader van de demo een belangrijk hulpmiddel zodat geïnteresseerden in de toekomst begrijpen welke ontwerpbeslissingen er zijn gehanteerd.
<a name="OntwerpDocument/Backend"></a>
## 3.1 Backend

Aangezien een van de gestelde randvoorwaarden door de opdrachtgevers was om het probleem op te lossen in python, heeft dit ertoe geleid dat de backend ook in python zal worden geschreven. Hierbij zal de front-end aan de hand van http-requests aanroepen doen om de benodigde data te verkrijgen en te tonen.

Om dit idee te realiseren is gekozen om het lichtgewicht backend framework Flask te gebruiken. Hiermee kan in enkele regels code een micro-server worden opgezet die schaalbaar is bij uitbreiding van complexiteit.

### 3.1.1 Modulariteit

De backend zal worden opgedeeld in meerdere modules naar aanleiding van functionaliteit om een mate aan flexibiliteit te vergroten. Deze vorm van opdeling draagt bij aan de overdraagbaarheid, wanneer het project wordt ingezet als demonstrateur.

De functionaliteit rondom de Flask server zal gescheiden worden van de functionaliteit van de Artificial intelligence. Binnen de AI-functionaliteit zal het Question object ook gescheiden worden, omdat deze niet alleen in de beslissingsboom wordt gebruikt, maar ook tijdens het stellen van een vraag door de gebruiker. De input van de gebruiker wordt namelijk omgezet in de vorm van een vraagobject die de juiste interface bevat om correct te functioneren met de beslissingsboom. Ten slotte worden ook enkele functies apart gezet die dienen als utilisatie functies en over het geheel gebruikt zullen worden.

![Figuur6](/lfs/Ontwerp/Figuur6.png)
*Figuur 6 Opdeling van de functionaliteit in modules*


### 3.1.2 API calls

Tijdens het werken met Flask is gebruik gemaakt van de lokale development server die Flask automatisch opstart: http://127.0.0.1:5000



| **Nr.** | **Naam** | **API-call** | **Beschrijving** |
|-----|-----|-----|-----|
| **1**| /getAllCharacters | GET | De karakterset van alle karakters wordt verkregen in JSON formaat.
| **2** | /character | GET | Zonder parameters retourneert deze call het huidige karakter van de speler. Wanneer de parameter “num” wordt meegegeven in de header met een bepaalde waarde, dan wordt het karakter dat correspondeert met die waarde gezet als het spelerskarakter. Deze call kiest ook een willekeurig karakter voor de AI en initialiseert de beslissingsboom.(vb: http://127.0.0.1:5000/character?num=3). |
| **3** | /labels | GET | Retourneert iedere label/header aan de hand van de dataset. | 
|**4**|/values?label={LABEL}|GET|Retourneert iedere unieke value aan de hand van een label. Hierbij is de parameter, “label”, die overeen moet komen met een label uit de set van labels/headers.|
|**5**|/question?label={LABEL}&value={VALUE}|POST|Aan de hand van parameters “label” en “value”, wordt een vraag geformuleerd waarbij het resultaat een scheiding is van de spelersdataset. Hierbij wordt de gefilterde dataset geretourneerd.|
|**6**|/aiquestion?answer={ANSWER}|GET|Retourneert de huidige vraag in de beslissingsboom. De parameter “answer” kan worden meegegeven om de volgende vraag te verkrijgen. Hierbij is de waarde van “answer” of 0 (false) of 1 (true).|
|**7**|/tree|GET|Retourneert de gehele beslissingsboom mits deze al is geinitialiseerd.|
|**8**|/images?id={ID}|GET|Retourneert een PNG-afbeelding van een karakter uit de dataset middels een bepaalde id meegegeven in de parameter “id”.|
|**9**|/reset|GET|Iedere gebruikte variabele wordt op null gezet en de dataset wordt opnieuw geladen. Retourneert succes bericht wanneer de reset is geslaagd.|
|**10**|/simulate?games={GAMES} &strat1={STRATEGY1} &strat2={STRATEGY2}|GET|Simuleert aan de hand van een variabel aantal "games" de hoeveelheid spellen waarbij 2 instanties van de intelligent agent worden gemaakt. Ook kan er worden meegegeven wat de te hanteren strategie is van zowel AI 1 als AI 2, middels "strategy1" en "strategy2" respectievelijk. Retourneert statistieken van de gespeelde games.|


<a name="OntwerpDocument/FrontEnd"></a>
## 3.2 Front-end

Om de ontwikkelde API’s te gebruiken, zullen de frameworks en technieken gekozen moeten worden om de front-end te realiseren.

### 3.2.1 Vue

Binnen de casus groep is gekozen voor vue vanwege het gebruiksgemak van de vuetify library (Vuetifyjs, sd). Deze library biedt een efficiënte mogelijkheid om een mooie vormgeving te bieden aan de visualisatie van het “Wie ben ik?” spel. Daarnaast is de casus groep al bekend met het vue framework waardoor de tijd niet verloren gaat aan het eigen maken van een nieuw framework, met als eindresultaat dat de focus volledig op het tot stand brengen van het wie ben ik spel staat.

### 3.2.2 Componenten

In het onderstaand component diagram is weergeven hoe de structuur van het “Wie ben ik?” spel weergeven. Hierin is een splitsing gemaakt tussen frontend en backend. In de backend worden de acties verwerkt en data geretourneerd. Deze staat in koppeling met de frontend met behulp van drie interfaces. Deze uiten zich in de vorm van API’s in de code. In het frontend gedeelte zijn deze drie componenten aanwezig. Het Character toont en haalt alle characters op in de frontend met behulp van het IProcesCharacter interface, het question component haalt en verwerkt de vragen met behulp van IProcesQuestion en het laatste component, de DecisionTree, is met behulp van het IProcesDecisionTree interface opgesteld om de decision tree te achter halen en te verkrijgen.

![Figuur7](/lfs/Ontwerp/Figuur7.png)
*Figuur 7 Component Diagram*

<a name="Kop5"></a>
# Resultaten

Aan de hand van de onderliggende architectuur is het mogelijk gemaakt dat er een tweetal instanties van
de intelligent agent zijn gegenereerd die beide in staat zijn om op adequate wijze het "Wie ben ik?" spel te
spelen. Figuur 3.4 toont de configureerbaarheid van de agents, waarbij agent 1 gebruik maakt van de gini
index, terwijl agent 2 gebruik maakt van de information entropy. Het resultaat voor 100 games geeft een win
ratio van 0.890 voor agent 2. Deze manier van grote aantallen games simuleren draagt bij aan de testbaarheid
van de intelligente systemen. Hierdoor kunnen aannames worden getrokken en theorieën worden bewezen.
In het kader van figuur 3.4 is te zien dat agent 2 vele malen beter presteert dan agent 1.

![](/lfs/Resultaat/simulate.png)
*Figuur 1 Simulatie 2 AI's*

<a name="Kop6"></a>
# Verwijzingen

### Onderzoeksrapport
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

### Ontwerp document:
Baljan, J., Paffen, K., van Deenen, L., & Kornips, J. (2020). _Plan van Aanpak._

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). _Introduction to Algorithms (3rd ed.)._ MIT Press and McGraw-Hill.

Goddard, N. (2016). _Pros and cons of decision trees_. Opgehaald van https://media.ed.ac.uk/media/Pros+and+cons+of+decision+trees/1_p4gyge5m

Rokach, L., & Maimon, O. (2005). _Top-down induction of decision trees classifiers - a survey._

_Vuetifyjs_. (sd). Opgehaald van Vuetifyjs: https://vuetifyjs.com/en/

Witten, I. H., Frank, E., & Hall, M. A. (2011). _Data mining : practical machine learning tools and techniques_. Opgehaald van https://archive.org/details/dataminingpracti00witt_966/page/n135/mode/2up
