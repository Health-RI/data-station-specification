# Datastation

In een dataspace voor secundair gebruik is het datastation, naast de processing hub, een essentieel component. Waar de processing hub het component is voor de data-afnemer, is het datastation dat voor de dataleverancier. Beide componenten zijn daarmee elkaars tegenhanger binnen de dataspace-architectuur: voor iedere rol is één kerncomponent gedefinieerd.

Het datastation is een technisch component dat is opgenomen in een knooppunt van de dataspace. Vanuit het datastation stelt de dataleverancier data beschikbaar voor secundair gebruik, onder vooraf vastgestelde voorwaarden. Het datastation ondersteunt functies zoals het ontsluiten van datasets, het toepassen van toegangs- en gebruiksvoorwaarden, het waarborgen van beveiliging en privacy, en het faciliteren van interoperabiliteit met andere knooppunten binnen de dataspace.

Door deze rolverdeling ontstaat een heldere scheiding van verantwoordelijkheden: de dataleverancier behoudt via het datastation controle over de beschikbaarstelling en het gebruik van data, terwijl de data-afnemer via de processing hub de data kan verwerken en analyseren binnen de afgesproken kaders. Samen vormen het datastation en de processing hub de fundamenten voor een betrouwbare, schaalbare en interoperabele dataspace voor secundair gebruik.

!!! info "Definitie van een datastation"

    Een datastation is een door een dienstverlener beheerde omgeving waarin datasets en gegevensdiensten van een dataleverancier worden ontsloten volgens afgesproken standaarden, met expliciete regels voor toegang, autorisatie, logging en gebruik, zodat gegevens betrouwbaar en interoperabel kunnen worden gebruikt en worden uitgewisseld binnen een dataspace.

Het datastation is als systeem betrokken bij de processen voor het [klaarzetten](../../proces/klaarzetten.md) van data en het [analyseren](../../proces/analyseren.md) van data. Het ondersteunt deze processen met de usecases die in het onderstaande diagram zijn weergegeven.

Door het kleurverschil tussen de actoren en het datastation wordt inzichtelijk gemaakt dat het datastation interacteert met de HDAB en met betrouwbare datahouders. De configuratie, het beheer en het onderhoud van het datastation zelf zijn niet opgenomen in de usecases. Met het usecasediagram moet immers inzichtelijk gemaakt worden welke waarde het datastation heeft voor het realiseren van de dataspace. Configuratie, beheer en onderhoud is waardevol, maar is niet de reden waarom dataspace een datastation nodig heeft.


![](uc-datastation.drawio.svg)

///caption
**Figuur 3.** Usecasediagram van het datastation voor secundair gebruik
///

In de onderstaande paragrafen worden de eisen aan een datastation beschreven.

!!! info "Een dataspace schrijft niet de architectuur van een datastation voor"

    De architectuur van een datastation is de verantwoordelijkheid van de dienstverlener die het datastation aanbiedt. Een dienstverlener moet een datastation autonoom kunnen realiseren en implementeren; iedere deelnemer aan de dataspace opereert immers zelfstandig.

    Om die reden wordt in dit hoofdstuk geen gedetailleerde architectuur uitgewerkt. Vanuit de dataspace is het vooral van belang dat de interoperabiliteit met het datastation is geborgd en dat het vertrouwen en de integriteit van de dataspace als geheel worden gewaarborgd, over alle autonome onderdelen heen. De eisen aan een datastation richten zich daarom alleen op interoperabiliteit en vertrouwen.


## Beheer catalogus van datasets

Iedere dataleverancier is zelf verantwoordelijk voor het catalogiseren en publiceren van haar datasets. Dit betekent dat de dataleverancier een eigen datasetcatalogus samenstelt en beheert. In dit document spreken we niet af welke datasets in de catalogus moeten worden opgenomen, maar alleen welk formaat wordt gebruikt. De catalogus moet worden opgesteld in [HealthDCAT-AP Release 5](https://healthdataeu.pages.code.europa.eu/healthdcat-ap/releases/release-5/).

De catalogus moet toegankelijk zijn via het datastation. In de EHDS is vastgelegd (artikel 77) dat de catalogus die door de Health Data Access Body (HDAB) wordt gepubliceerd openbaar toegankelijk is. In lijn daarmee kan ook de catalogus op het datastation openbaar toegankelijk zijn.

![](datastation-beheren.drawio.svg)

///caption
**Figuur 4.** Componenten voor het beheer van de catalogus van datasets
///

Voor de beheer van de catalogus wordt uitgegaan van een servicemedewerker die de catalogus uploadt naar het datastation. Dit is echter slechts een voorbeeld: de dataleverancier bepaalt zelf hoe dit proces wordt ingericht, handmatig of geautomatiseerd.

Met het vrijgeven wordt bedoeld dat de dataleverancier een versie van de datacatalogus publiceert en daarmee een nieuwe versie beschikbaar stelt. Dit vrijgeven kan periodiek plaatsvinden, bijvoorbeeld meerdere keren per jaar. Het aanmelden van de catalogus hoeft daarentegen slechts eenmalig te gebeuren.
Na aanmelding is de catalogus van de dataleverancier geregistreerd in het register van de HDAB ten behoeve van de Nationale catalogus van datasets.

## Haal periodiek catalogus van datasets op

De Health Data Access Body (HDAB) is met het component voor de Nationale Catalogus volledig autonoom in het bepalen van de frequentie waarmee de Nationale Catalogus wordt bijgewerkt. Dit betekent dat de HDAB kan plannen wanneer de catalogus van een dataleverancier wordt opgehaald, in plaats van dat dit ad hoc door alle leveranciers tegelijk gebeurt.

![](datastation-ophalen.drawio.svg)

///caption
**Figuur 5.** Componenten voor het ophalen van de catalogus van datasets
///

Door deze autonomie ontstaat een efficiënte en gecontroleerde updateprocedure, waardoor piekbelasting of “filevorming” wordt voorkomen wanneer meerdere dataleveranciers tegelijk hun catalogus willen bijwerken. Bovendien draagt deze regeling bij aan de betrouwbaarheid en stabiliteit van de Nationale Catalogus, omdat updates gespreid en voorspelbaar plaatsvinden. Dit biedt zowel de HDAB als de dataleveranciers meer controle over het proces en helpt bij het waarborgen van consistente en actuele informatie in de dataspace.

## Maak data beschikbaar voor secundair gebruik

Vanuit de HDAB wordt een verzoek gedaan om een dataset beschikbaar te stellen voor secundair gebruik. Dit verzoek kan gebaseerd zijn op een door de HDAB verleende datavergunning of op een goedgekeurd dataverzoek.

Het uitgangspunt is dat een dataleverancier een data heeft verkregen en deze georganiseerd heeft in een aantal datasets om deze vervolgens via een catalogus te publiceren. In het onderstaande figuur zijn deze randvoorwaardelijke stappen weergegeven. In de datasets die worden aangeboden voor secundair gebruik mogen geen personen zijn verwerkt die via een opt-out hebben aangegeven geen deel te willen uitmaken van het secundair gebruik (artikel 71 EHDS).

![](datastation-organiseren.drawio.svg)

///caption
**Figuur 6.** Overzicht van het organiseren en klaarzetten van de data voor federatieve analyse
///

Het beschikbaar stellen kan inhouden dat:

1. Toegang tot een dataset uit de catalogus wordt verleend.
2. Data moet worden geprepareerd en vervolgens beschikbaar worden gesteld in het datastation (federatief).
3. Data moet worden geprepareerd en vervolgens centraal beschikbaar worden gesteld (data pooling).

Ad 1: Vaak gaat secundair gebruik over het onderzoek doen op basis van gezondheidsgegevens van personen. Maar niet altijd. Het is daarom mogelijk dat het beschikbaar stellen van data betekent dat er toegang kan worden verleend aan een dataset, bijvoorbeeld voor het beschikbaar stellen van data voor een dataverzoek. Het verlenen van toegang betekent dat er toegangsregels worden opgesteld voor het algoritme of het verzoek van de datagebruiker. Alleen wanneer aan deze toegangsregels is voldaan, verkrijgt het algoritme toegang tot de dataset. Voorbeelden van toegangsregels zijn onder andere dat het algoritme zich moet kunnen authenticeren en moet kunnen aantonen te beschikken over een geldige vergunning of goedkeuring van het dataverzoek.

Ad 2: Om te voldoen aan een vergunning of een dataverzoek kan het noodzakelijk zijn om de data te prepareren. Onder prepareren wordt verstaan dat een extract van een dataset wordt gemaakt, bijvoorbeeld om uitsluitend een bepaald cohort te omvatten, of dat data wordt gepseudonimiseerd volgens een door de datagebruiker vastgesteld en door de HDAB goedgekeurd algoritme.

In een federatieve opzet wordt de geprepareerde data beschikbaar gesteld in het lokale datastation, zodat algoritmes toegang hebben tot de datasets zonder dat de data centraal wordt samengebracht.

Ad 3: Wanneer datasets centraal beschikbaar worden gesteld, worden de geprepareerde datasets veilig getransporteerd naar een centrale processing hub. In deze hub kunnen datasets worden samengebracht, geintegreerd en geanalyseerd, zodat onderzoekers en algoritmes toegang hebben tot de gecombineerde gegevenssets binnen de geldende randvoorwaarden van de vergunning. Het transport naar de centrale hub vindt plaats via beveiligde verbindingen, waarbij integriteit en vertrouwelijkheid van de data te allen tijde moeten worden gewaarborgd.

In het onderstaande figuur zijn scenario 2 en 3 weergegeven.

![](datastation-klaarzetten.drawio.svg)

///caption
**Figuur 7.** Proces voor het beschikbaar stellen van data voor secundair gebruik, met alternatieve scenario's voor het uitvoeren van data pooling (centraal) en federatie
///

Met het beschikbaar stellen van de datasets is het datastation gereed voor de ontvangst van een algoritme of een dataverzoek.

## Verwerk algoritme en geef resultaat terug

Een datastation kan onder andere worden gebruikt voor het uitvoeren van een federatieve analyse of voor federatief leren, of kort gezegd voor het uitvoeren van een algortime. De datagebruiker geeft via de processing hub een opdracht om een algoritme uit te voeren op een aantal datastations. In het onderstaande diagram zijn de stappen weergegeven die op het datastation worden uitgevoerd nadat de opdracht door het datastation is ontvangen.

!!! info "Definitie van een algoritme"

    Een algoritme is een set van regels en instructies die een computer uitvoert. Algoritmes helpen bijvoorbeeld om problemen te analyseren maar ook om beslissingen te nemen. (bron: [Digitale Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/algoritmes/))

![](datastation-analyseren.drawio.svg)

///caption
**Figuur 8.** Proces voor het federatief uitvoeren van een algoritme
///

**Ontvangen en uitvoeren van een algoritme op het datastation**

Na ontvangst van een opdracht via de processing hub start het datastation het proces voor het uitvoeren van een algoritme. Als eerste stap worden de authenticiteit en geldigheid van de identiteit van de data-afnemer, de identiteit van de datagebruiker en de vergunning geverifieerd op basis van aangeleverde credentials met een hoog betrouwbaarheidsniveau, conform de eIDAS-verordening. Alleen wanneer deze verificatie succesvol is afgerond, wordt de opdracht verder in behandeling genomen.

Vervolgens haalt het datastation het algoritme, dat onderdeel is van de vergunning, op uit het algoritmeregister. In de huidige implementatie zijn algoritmen beschikbaar in de vorm van Docker-images. Na het ophalen wordt de integriteit van het algoritme gecontroleerd, bijvoorbeeld door middel van checksums of digitale handtekeningen, om vast te stellen dat het algoritme niet is gewijzigd en afkomstig is uit een betrouwbare bron.

Na een succesvolle integriteitscontrole wordt het algoritme opgenomen in de container management-omgeving van het datastation. Hierbij wordt het algoritme geconfigureerd conform de opdracht, waaronder het instellen van benodigde parameters, toegangsrechten tot data en eventuele runtime-beperkingen. Vervolgens wordt het algoritme gestart en uitgevoerd binnen een geïsoleerde containeromgeving, zodat de uitvoering veilig en gecontroleerd plaatsvindt.

**Communiceren van de resultaten**

Zodra het algoritme gereed is met de uitvoering, notificeert het datastation de processing hub. Vanaf dat moment kan het algoritme de resultaten communiceren met de processing hub, conform de afgesproken interfaces en protocollen.

Het is mogelijk dat het algoritme na de initiële uitvoering voor een afgesproken periode actief blijft binnen het datastation. Gedurende deze periode kan het algoritme periodiek opnieuw worden gestart om herhaalde analyses uit te voeren of om federatief te leren op basis van nieuw beschikbare data. Na afloop van deze periode wordt het algoritme beëindigd en uit de container management-omgeving verwijderd, tenzij anders overeengekomen.

![](datastation-leveren.drawio.svg)

///caption
**Figuur 9.** Overzicht van het uitvoeren van een federatieve analyse en het leveren van de resultaten
///

In bovenstaand overzicht is weergegeven hoe resultaten worden geleverd op basis van een federatieve analyse of federatief leren. Het geheel van processing hub en datastation functioneert als geheel als een beveiligde verwerkingsomgeving, compliant aan de eisen van de EHDS en TEHDAS2. De verantwoordelijke partijen moeten garanderen dat alle verwerking van data veilig, gecontroleerd en conform de regelgeving plaatsvindt.

Onder andere moeten de volgende aspecten worden gewaarborgd:

- **Governance**: duidelijke verantwoordelijkheden en afspraken tussen de processing hub en het datastation, inclusief procedures voor goedkeuring van algoritmen en dataverzoeken. 
- **Toegangsbeheer**: strikte controle op wie toegang heeft tot datasets, inclusief authenticatie op hoog betrouwbaarheidsniveau en verificatie van geldige vergunningen. Alleen geautoriseerde en gevalideerde queries en algoritmen mogen de datasets benaderen.
- **Monitoring en logging**: alle toegang tot datasets en alle uitgevoerde activiteiten binnen de verwerkingsomgeving worden gelogd en gemonitord, zodat elke actie traceerbaar is en afwijkingen kunnen worden gedetecteerd.
- **Data-isolatie en resultatenbeheer**: de verwerking vindt plaats in geïsoleerde containeromgevingen, waardoor datasets en algoritmen gescheiden blijven van andere processen. 
- **Integriteit en beveiliging van algoritmen**: alle algoritmen die worden uitgevoerd zijn gecontroleerd op integriteit en authenticiteit, bijvoorbeeld door middel van digitale handtekeningen of checksums.

Ten aanzien van de resultaten moet besloten worden of deze de beveiligde omgeving van de processing hub mogen verlaten. Hiervoor zal een vrijgaveproces gedefinieerd moeten worden waarin strikte regels voor export en overdracht gelden.

## Geef antwoord op dataverzoek

Wanneer een dataverzoek wordt ontvangen via de processing hub, start het datastation het verwerkingsproces. Als eerste stap worden de authenticiteit en geldigheid van de identiteit van de data-afnemer, de identiteit van de datagebruiker en het akkoord op het dataverzoek geverifieerd op basis van aangeleverde credentials met een hoog betrouwbaarheidsniveau, conform de eIDAS-verordening. Alleen na een succesvolle verificatie wordt het dataverzoek verder verwerkt.

Vervolgens haalt het datastation het bijbehorende algoritme op uit het algoritmeregister. In deze context bevat het register een verzameling herbruikbare queries die zijn goedgekeurd voor gebruik binnen de dataspace. Na het ophalen wordt de integriteit van het algoritme gecontroleerd, bijvoorbeeld door middel van digitale handtekeningen of checksums, om te waarborgen dat het algoritme authentiek en onveranderd is.

Het algoritme wordt vervolgens opgestart en uitgevoerd op het datastation. Gedurende de uitvoering wordt het algoritme geïsoleerd verwerkt, zodat gegevensbeveiliging en privacy gewaarborgd blijven. Na afronding van de uitvoering worden de resultaten teruggekoppeld aan de processing hub, conform de afgesproken protocollen en interfaces.

![](datastation-dataverzoek.drawio.svg)

///caption
**Figuur 10.** Proces voor het federatief uitvoeren van een dataverzoek
///

Het algoritme kan gedurende de looptijd en de geldigheidsduur van het dataverzoek opnieuw worden aangeroepen. Dit maakt het mogelijk om periodiek analyses uit te voeren of herhaalde resultaten te genereren zonder dat een nieuw dataverzoek noodzakelijk is. Zodra de geldigheidsduur van het dataverzoek is verstreken, wordt verdere uitvoering van het algoritme gestopt, tenzij expliciet verlengd.