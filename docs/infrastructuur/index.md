# 5. Perspectief: infrastructuur

## Uitdagingen in het ontwerp en implementatie van een decentrale data infrastructuur

**Heterogene data en systemen**

In een decentraal netwerk leeft de data niet op een centrale plek maar over meerdere datastations. Elk datastation heeft een eigen data ecosysteem met een eigen context en extractie methodes vanuit het domein van de datahouder. Daar waar eerste generatie datawarehouses vooral tabulaire data bevatten, hebben datahouders vandaag de dag een heterogene mix van verschillende data types en mate van structuur waarbij er een continue stroom is aan informatie die binnenkomt.

In een decentraal netwerk is het datastation de poort van de data binnen een organisatie naar het federatieve netwerk. Een datastation heeft hierin dus de essentiele rol om de organisatie eigen data te kunnen convergeren naar een standaard voor hergebruik.
Om deze diversiteit tussen organisaties en in de data zelf te kunnen faciliteren, zal een data infrastructuur een balans tussen flexibiliteit en operabiliteit moeten kunnen bieden.

**Late binding voor data kwaliteit**

Om de balans tussen flexibiliteit ten operabiliteit te kunnen waarborgen is het belangrijk om de kwaliteitseisen die gesteld worden aan een dataset te splitten in de minimale technische kwaliteitseisen en de contextuele kwaliteitseisen. Een infrastructuur moet ten slotte de data voldoende kunnen begrijpen om het te kunnen verwerken maar de contextuele kwaliteitseisen van data zijn vaak sterk gebruiksafhankelijk.

Een data infrastructuur binnen een datastation is alleen verantwoordelijk voor de technische "leesbaarheid" van de data zodat het verzamelen van meta data en het beschikbaar stellen van verdere verwerking niet gehinderd wordt. Dit principe van **late binding**, betekent dat we data niet op voorhand weigeren op inhoudelijke gronden, maar op "leesbaarheid" en technische toegankelijkheid. De inhoudelijke kwaliteitseisen kunnen vervolgens via selectie en ETL-processen gaandeweg worden toegepast, waardoor semantische interoperabiliteit behouden blijft zonder vroegtijdige data-exclusie.

**Metadata zonder data-exposure**

Om centraal ten aller tijde een betrouwbare afspiegeling te kunnen geven van de beschikbare data binnen een datastation, is het faciliteren van een betrouwbare meta data catalog van cruciaal belang. Het is daarom essentieel om het monitoren als een integraal en automatisch proces mee te nemen zodat er geen discrepanties kunnen onstaan tussen de data zelf en de beschikbare meta data. Deze meta data kan vervolgens aan centrale processen beschikbaar worden gesteld, zodat gebruikers alle informatie voor gebruik hebben zonder dat de data zelf beschikbaar gesteld hoeft te worden.

Gegeven deze uitdagingen gaan we in dit hoofdstuk in op de belangrijkste principes hoe de infrastructuur van datastations geimplementeerd kan worden met bestaande technieken. Ten eerste wordt aan de hand van de evolutie van data infrastructuren de verschillende opties en concepten toegelicht. Vervolgens wordt de specificatie van de technische infrastructuur van een datastation beschreven in termen van de lakehouse architectuur en de _composable data stack_. 
