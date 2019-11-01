TÄMÄN KESKENERÄISEN PROJEKTIN KEHITTÄMINEN ON LOPETETTU.

SOVELLUKSEN HEROKU EI OLE KÄYTÖSSÄ.
KAIKKI HEROKUN DYNOT ON SULJETTU, JOTEN NE PITÄÄ AVATA ENNEN KUIN SOVELLUSTA VOI KÄYTTÄÄ UUDELLEEN.

# Fire Emblem Fates -hahmotietokanta

## Kirjautuminen

Unitit listaava sivu on nähtävissä ilman kirjautumista.

Voit **luoda uudet tunnukset** tai kirjautua sisään näillä:

tetstiAdmin

salasana

## Linkit

[Heroku](https://fef-db-application.herokuapp.com/)

[Tietokantakaaavio](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/Tietokantakaavio%20v1.png) (Laajan suunnitelman tietokantakaavio. Lopullinen työ on todennäköisesti suppeampi.)

[User storyt](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/User%20storyt.md)

[Käyttöohje](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/K%C3%A4ytt%C3%B6ohje.md)

[Asennusohje](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/Asennusohje.md)

**Tietokantasovelluksen tarkoituksena on pitää kirjaa Fire Emblem Fates -pelin hahmoista.**

Tietokantasovelluksen on tarkoitus antaa käyttäjälle mahdollisuuden suunnitella erilaisia strategioita.

Tietokantaan voi lisätä hahmoja, joista käyttäjä voi tehdä omia joukkoja. Hahmot ovat näkyvissä kaikille käyttäjille, mutta joukot ovat yksityisiä. Käyttäjä voi vertailla hahmojen ominaisuuksi ja tällä tavoin valita sopivimmat hahmot.

Kaikista hahmoista tallennetaan niiden alkuperäiset statit (stat = hahmon numeerinen ominaisuus, kuten voima tai nopeus), stattien kasvutodennäköisyydet ja luokka (esimerkiksi jousiampuja tai parantaja).

## Toimintoja
Siirretty [user storyeihin](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/User%20storyt.md)

## Yhteenvetokyselyt

**Hakee annetun teamin unitit**

SELECT * FROM team
JOIN team_unit ON team.id = team_unit.team_id
JOIN unit ON team_unit.team_id = unit.id "
WHERE team.id = :teamid

**Laskee annetun teamin unitien määrän**

SELECT COUNT(team.id) FROM team
JOIN team_unit ON team.id = team_unit.team_id 
JOIN unit ON team_unit.team_id = unit.id 
WHERE team.id = :teamid

**Hakee kaikissa käyttäjän teameissa olevat unitit**

SELECT * FROM team
JOIN team_unit ON team.id = team_unit.team_id
JOIN unit ON team_unit.unit_id = unit.id
WHERE team.account_id = :userid
ORDER BY team.id

**Laskee kaikkien käyttäjän eri teamien unitien määrät**

SELECT COUNT(*) FROM team
JOIN team_unit ON team.id = team_unit.team_id
JOIN unit ON team_unit.unit_id = unit.id
WHERE team.account_id = :userid
GROUP BY team.id

## Ongelmat
* Heroku ei toimi
  * Lokin perusteella ainakin osa ongelmasta näyttäisi aiheutuvan siitä, että joidenkin tietokantasarakkeiden nimissä on isoja kirjaimia, mikä aiheuttaa yhteensopivuusongelmia Postgresin kanssa.
    * Olen tehtnyt vastaavanalaiseen ongelmaan korjauksen aiemmassa vaiheessa projektia, minkä seurauksena kitjoitin SQL-kyselyissä kaikki viittaukset kaikkia isoja kirjaimia sisältäviin tietokantasarakkeisiin muodossa \"sarakeAB\". Tämä ei kuitenkaan näytä auttavan nykyiseen ongelmaan.
  * Kirjautuminen ja käyttjätunnuksen luominen toimivat, mutta Unit- ja Teams-sivujen avaaminen aiheuttaa Internal server errorin.
* Hahmojen lisääminen teameihin ei ole käytössä.
  * ALoitin tämän ominaisuuden tekemisen liian myöhään ja en saanut sitä ajoissa toimimaan.
  * Esimerkkiteamien hahmoja pystyy kuitenkin tarkastelemaan.
