# Principes

Een belangrijk kenmerk van een inrichtingsprincipe is dat het niet onderhandelbaar is. Dit onderscheidt principes van requirements, die wel
ter discussie kunnen staan en aangepast kunnen worden. Inrichtingsprincipes spelen een cruciale rol, omdat zij de onderliggende
argumentatie is voor beslissingen over de inrichting en werking van de dataspace.

<div class="grid" markdown>
!!! abstract "Scope van dit document"
    Een data gebruiker voert een data analyse uit in een gefedereerde beveiligde verwerkingsomgeving, dat is verbonden aan een netwerk van _data stations_ zijnde de systemen waarom de data houder de data beschikbaar heeft gesteld en klaargezet voor gebruik.<br>Dit document geeft een functionele specificatie en voorbeeld implementaties van een data station, zijnde het deel van de gezondheidsdatainfrastructuur dat binnen het domein (verwantwoordelijkheid) van de data houder is gerealiseerd.

```mermaid
block
    columns 1
    
    dg["Data analyseren"]
    space
    bvo["Secundair gebruik in BVO"]
    space
    dh2["Data klaarzetten voor veilige verwerking"]
    space
    dh1["Data beschikbaar stellen"]
    
    dh1 --> dh2
    dh2 --> bvo
    dg --> bvo

    classDef green fill:#9DB567,stroke:#9DB567
    classDef orange fill:#EDB23C,stroke:#EDB23C
    classDef blue fill:#223D73,stroke:#223D73,color:#ffffff
    classDef pink fill:#CE8BA7,stroke:#CE8BA7

    class dh1,dh2 green
    class bvo blue
    class dg pink
```
</div>
