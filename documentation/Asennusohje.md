# Asennusohje

Sovellus toimii verkossa, joten sitä ei välttämättä tarvitse asentaa erikseen. Voit käyttää sovellusta verkkoselaimen kautta niin tietokoneella kuin mobiililaitteella osoitteesta https://fef-db-application.herokuapp.com/.

Pelkkä sovelluksen sisällön tarkastelu ei vaadi käyttäjätunnusta, mutta muokkaamiseen sellainen on pakollinen. Voit katsoa ohjeet käyttäjätunnuksen luontiin [käyttöohjeesta](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/K%C3%A4ytt%C3%B6ohje.md).

## Sovelluksen asentaminen paikallisesti omalle tietokoneelle

1. 

## Sovelluksen asentaminen Herokuun

Vaatimukset:
* fef-db-sovellus
* Bash-komentotulkki
* Gitin asennus
* Herokun asennus
* Heroku-käyttäjätunnus
* Git-repositorio, jossa säilytät fef-db:tä.

1. Avaa fef-db:n hakemisto komentorivillä.
2. Luo fef-db:lle paikka Herokuun komennolla `Heroku create haluamasiNimi`.
3. Lisää Gitiin tieto Herokusta komennolla `git remote add heroku https://git.heroku.com/valitsemasiNimi.git`.
4. Commitaa muutokset Gitiin.
5. Lähetä fef-db Herokuun `git push heroku master`.
6. Luo fef-db:lle tietokanta Herokuun komennolla `heroku addons:add heroku-postgresql:hobby-dev`.
