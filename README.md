# Fire Emblem Fates -hahmotietokanta

**Huomiot**

Toivoisin, että käyttäisitte arvostelussa tätä versiota, vaikka se on palautettu määräajan jälkeen. Unohdin tallentaa, muutokset README:hen ennen 23.59 commitia, joten siitä vain puuttuu hieman tekstiä. Lisäksi tuohon palautukseen pääsi vahongossa mukaan tekstieditorini väliaikaistiedosto, README.md.kate-swp, joka ei ole tässä versiossa. Mitään muutoksia koodiin tai varsinaiseen dokumentaation ei tässä versiossa ajallaan palautettuun verrattuna ole.

Unit-taulun on tarkoitus olla sama kaikille käyttäjille.

En onnistunut saamaan tietokannan tietojen päivttämistä ja uusien käyttäjätunnusten luomista sovelluksen kautta toimimaan.

## Käyttäjätunnus ja salasana:
Voit kirjautua sisään näillä tunnuksilla.

tetstiAdmin

salasana

## Linkit

[Heroku](https://fef-db-application.herokuapp.com/)

[Tietokantakaaavio](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/Tietokantakaavio%20v1.png) (Laajan suunnitelman tietokantakaavio. Lopullinen työ on todennäköisesti suppeampi.)

[User storyt](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/User%20storyt.md)

**Tietokantasovelluksen tarkoituksena on pitää kirjaa Fire Emblem Fates -pelin hahmoista.**

Tietokantasovelluksen on tarkoitus antaa käyttäjälle mahdollisuuden suunnitella erilaisia strategioita ja tutkia ja arvioida tilanteita, joissa hän olisikin peliä pelatessaan käyttänyt jotakin erilaista taistelujoukon rakennetta hänen oikeasti käyttämänsä sijasta.

Järjestelmän ylläpitäjä voi lisätä järjestelmään uusia hahmoja, kykyjä ja aseita, joiden avulla tavallinen käyttäjä voi suunnitella hahmoille varustuksia ja taistelujoukkoja eri kenttien läpäisyä varten. Käyttäjä voi esimerkiksi etsiä taistelujoukosta hahmon, jolla on korkein fyysinen hyökkäysvoima tai kaikki hahmot jotka selviävät hengissä jonkin vihollisen hyökkäyksestä. Kaikkien hahmojen tiedoista on taas mahdollista katsoa, kenen nopeus kasvaa eniten hahmon kehittyessä tasoja.

Kaikista hahmoista tallennetaan niiden alkuperäiset statit (stat = hahmon tai aseen numeerinen ominaisuus, kuten voima tai nopeus), stattien kasvutodennäköisyydet, luokka (esimerkiksi jousiampuja tai parantaja) ja kyvyt. Aseesta tallennetaan sen vahvuus, tarkkuus ja tyyppi (esimerkiksi miekka tai keihäs). Luokasta tallennetaan sille sallitut asetyypit ja kyvyistä niiden kuvaus. Taistelujoukosta tallennetaan tieto suurimmasta sallitusta hahmojen määrästä.

## Toimintoja
Siirretty [user storyeihin](https://github.com/JustAGoldeneye/Fire-Emblem-Fates-Unit-Database/blob/master/documentation/User%20storyt.md)

## Huomioita
Tiedostan, että suunnitelmassani on mahdollisesti paljon työtä. Jos projektin aikana huomaankin, että työn määrä on liian suuri, saatan jättää osan vähemmän oleellisista tauluista pois, kuten aseet tai taistelujoukot. On myös mahdollista, että saatan vaihtaa pelin Fire Emblem Fates:sta Fire Emblem Heroes:iin, joka on pelimekaniikoiltaan hyvin samanlainen, mutta hieman yksinkertaisempi, jos ajaudun vaikeaan tilanteeseen projektin aikana. Hahmoista tallennettavista attribuuteista ei kuitenkaan ole tarkoitus leikata ja mahdollisuus laskea hahmon todennäköiset statit jollakin tasolla olisi myös tarkoitus pitää mukana. Kuitenkin, jos huomaankin projektin etenevän helposti saatan jopa tehdä jotain ylimääräistä, kuten lisätä luokan kenttä, joka korvaisi taistelujoukon attribuutin suurimmasta sallitusta hahmomäärästä ja tästä suurimmasta sallitusta hahmomäärästä tulisikin luvun attribuutti.
