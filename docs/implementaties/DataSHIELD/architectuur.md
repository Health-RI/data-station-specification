## Simpele configuratie

Bron: https://molgenis.github.io/molgenis-service-armadillo/

![](https://molgenis.github.io/molgenis-service-armadillo/img/ds-simple-setup.png)

///caption
A user writes analysis commands in R, using client-side DataSHIELD R packages. The commands are sent to the biobank servers. For Armadillo, the communication between the client and the server is handled by the R packages DSI and DSMolgenisArmadillo, whilst the data storage and execution of commands on the server is handled by ArmadilloService. The non-disclosive summary statistics are then returned to the user.
///


## Configuratie met centrale server

![](https://molgenis.github.io/molgenis-service-armadillo/img/ds-complete-setup.png)

///caption
Once logged in to the CAS, users write their code as if they were running RStudio locally. The advantage of this setup is that Biobank servers can be configured so that they are blocked off from the rest of the internet by a firewall and can only be accessed from the CAS. This provices an additional layer of data protection. It also benefits users, as all required DataSHIELD R packages can be pre-installed thus removing the needs for users to set up their R environment.
///