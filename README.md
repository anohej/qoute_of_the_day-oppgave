1. Forside

Prosjekttittel: Sitat-applikasjon med Flask
Navn: Jehona
Klasse: VG2
Dato: 18.12.2025

Kort beskrivelse av prosjektet:
Dette prosjektet er en enkel webapplikasjon laget med Flask og MariaDB. Applikasjonen lar brukere se, redigere og slette sitater som er lagret i en database. Prosjektet handler om å koble frontend og backend mot en database.




2. Systembeskrivelse

Formål med applikasjonen:
Formålet med applikasjonen var å lære hvordan Flask fungerer sammen med en database. Jeg ønsket å vise hvordan data kan hentes fra, oppdateres og slettes i en MariaDB-database via en webside.

Brukerflyt:
Brukeren starter på forsiden og ser en liste med sitater. Der kan brukeren klikke på et sitat for å se detaljer og redigere teksten. Brukeren kan også slette et sitat, som da fjernes fra databasen.

Teknologier brukt:

Python / Flask

MariaDB

HTML / CSS / JavaScript





3. Server-, infrastruktur- og nettverksoppsett
Servermiljø

Applikasjonen kjøres lokalt med Flask sin innebygde server.

Nettverksoppsett

Klient (nettleser) kobler til Flask-applikasjonen

Flask kobler videre til MariaDB-databasen

Eksempel:
Klient → Flask → MariaDB → Flask → Klient

Tjenestekonfigurasjon

Flask kjøres med debug=True

Databaseinformasjon er lagret i en egen konfigurasjon (DB_CONFIG)





4. Prosjektstyring – GitHub Projects (Kanban)

Kolonner brukt:

To Do

In Progress

Done

Refleksjon:
Kanban hjalp meg med å få oversikt over hva som måtte gjøres og hva jeg allerede var ferdig med. Det gjorde prosjektet mer strukturert.




5. Databasebeskrivelse

Databasenavn: Quetes

Tabell: quotes

Tabell	Felt	Datatype	Beskrivelse
quotes	id	INT	Primærnøkkel
quotes	name	VARCHAR	Navn på person
quotes	quote	TEXT	Selve sitatet
quotes	created_at	DATETIME	Når sitatet ble laget

SQL-eksempel:

CREATE TABLE quotes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  quote TEXT,
  created_at DATETIME
);



6. Programstruktur
prosjekt/
 ├── app.py
 ├── templates/
 │    ├── quotes.html
 │    ├── quote.html
 │    └── add_quote.html
 ├── static/
 │    └── css/
 │         └── style.css
 ├── venv/
 └── __pycache__/



Databasestrøm:
HTML → Flask → MariaDB → Flask → HTML





7. Kodeforklaring

/ – Henter alle sitater fra databasen og viser dem på forsiden

/quote/<id> – Viser ett sitat og lar brukeren redigere det

/delete/<id> – Sletter et sitat fra databasen

get_db_connection() – Lager tilkobling til MariaDB

8. Sikkerhet og pålitelighet

Bruk av parameteriserte SQL-spørringer (%s) for å unngå SQL-injection

Enkel validering av input (sjekker at tekst ikke er tom)

Lukker databasekoblinger etter bruk






9. Feilsøking og testing

Typiske feil:

Problemer med database-tilkobling

SQL-feil i spørringer

Hvordan jeg løste dem:

Sjekket IP, brukernavn og passord

Printet feilmeldinger og testet SQL direkte i databasen

Testmetoder:

Manuell testing i nettleser

Testet legge til, redigere og slette sitater






10. Konklusjon og refleksjon

Hva lærte jeg?
Jeg lærte hvordan Flask fungerer sammen med MariaDB, og hvordan ruter og databaser henger sammen.

Hva fungerte bra?
Databasekoblingen og visning av data fungerte bra.

Hva ville jeg gjort annerledes?
Jeg ville lagt mer tid på design og bedre validering.

Hva var utfordrende?
Å feilsøke databasefeil og SQL-spørringer var mest utfordrende.





11. Kildeliste

w3schools

https://flask.palletsprojects.com
