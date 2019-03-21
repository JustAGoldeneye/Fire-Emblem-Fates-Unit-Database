# Fire Emblem Fates -hahmotietokanta

[Heroku](https://fef-db-application.herokuapp.com/)
[Tietokantakaaavio]()
[User storyt]()

Laajan suunnitelman tietokantakaavio. Lopullinen työ on todennäköisesti suppeampi.

**Tietokantasovelluksen tarkoituksena on pitää kirjaa Fire Emblem Fates -pelin hahmoista.**

Tietokantasovelluksen on tarkoitus antaa käyttäjälle mahdollisuuden suunnitella erilaisia strategioita ja tutkia ja arvioida tilanteita, joissa hän olisikin peliä pelatessaan käyttänyt jotakin erilaista taistelujoukon rakennetta hänen oikeasti käyttämänsä sijasta.

Järjestelmän ylläpitäjä voi lisätä järjestelmään uusia hahmoja, kykyjä ja aseita, joiden avulla tavallinen käyttäjä voi suunnitella hahmoille varustuksia ja taistelujoukkoja eri kenttien läpäisyä varten. Käyttäjä voi esimerkiksi etsiä taistelujoukosta hahmon, jolla on korkein fyysinen hyökkäysvoima tai kaikki hahmot jotka selviävät hengissä jonkin vihollisen hyökkäyksestä. Kaikkien hahmojen tiedoista on taas mahdollista katsoa, kenen nopeus kasvaa eniten hahmon kehittyessä tasoja.

Kaikista hahmoista tallennetaan niiden alkuperäiset statit (stat = hahmon tai aseen numeerinen ominaisuus, kuten voima tai nopeus), stattien kasvutodennäköisyydet, luokka (esimerkiksi jousiampuja tai parantaja) ja kyvyt. Aseesta tallennetaan sen vahvuus, tarkkuus ja tyyppi (esimerkiksi miekka tai keihäs). Luokasta tallennetaan sille sallitut asetyypit ja kyvyistä niiden kuvaus. Taistelujoukosta tallennetaan tieto suurimmasta sallitusta hahmojen määrästä.

## Toimintoja
Siirretty [user storeihin]()

## Huomioita
Tiedostan, että suunnitelmassani on mahdollisesti paljon työtä. Jos projektin aikana huomaankin, että työn määrä on liian suuri, saatan jättää osan vähemmän oleellisista tauluista pois, kuten aseet tai taistelujoukot. On myös mahdollista, että saatan vaihtaa pelin Fire Emblem Fates:sta Fire Emblem Heroes:iin, joka on pelimekaniikoiltaan hyvin samanlainen, mutta hieman yksinkertaisempi, jos ajaudun vaikeaan tilanteeseen projektin aikana. Hahmoista tallennettavista attribuuteista ei kuitenkaan ole tarkoitus leikata ja mahdollisuus laskea hahmon todennäköiset statit jollakin tasolla olisi myös tarkoitus pitää mukana. Kuitenkin, jos huomaankin projektin etenevän helposti saatan jopa tehdä jotain ylimääräistä, kuten lisätä luokan kenttä, joka korvaisi taistelujoukon attribuutin suurimmasta sallitusta hahmomäärästä ja tästä suurimmasta sallitusta hahmomäärästä tulisikin luvun attribuutti.
