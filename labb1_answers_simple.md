# Laboration 1 – kort muntlig redovisning

## Uppgift 1
### 1a
Det finns 3653 rader i datafilen. Jag jämförde det med antalet kalenderdagar från 2008-01-01 till 2017-12-31, som också är 3653. Jag kontrollerade också att alla datum är unika och att datumlistan exakt matchar alla förväntade datum i perioden. Därför kan jag säga att alla dagar från 2008 till 2017 finns med.

### 1b
Det kallaste dygnsminvärdet är -32,1 °C. Det inträffade den 2010-02-24.

### 1c
Jag ritade den empiriska fördelningsfunktionen som en trappstegsfunktion. Den visar hur stor andel av dygnsmedelvärdena som är mindre än eller lika med ett visst värde.

Vid 10 °C får jag F(10) = 0,676. Det betyder att 67,6 % av dygnsmedelvärdena är högst 10 °C. Sannolikheten att dygnsmedelvärdet är större än 10 °C blir resten:

`P(X > 10) = 1 - F(10) = 1 - 0,676 = 0,324`

Figuren finns i `figures/uppgift1c_ecdf.png`.

## Uppgift 2
### 2a
Jag tog ut alla datum i maj 2012. Dygnsmedelvärdena avrundades till heltal eftersom uppgiften säger att tabellen ska använda avrundade heltalsvärden. Det gör också frekvenstabellen lättare att läsa.

Frekvenstabellen gjordes genom att räkna hur många gånger varje avrundat temperaturvärde förekommer. Till exempel förekommer värdet 8 nio gånger, så 8 är det vanligaste värdet.

### 2b
För maj 2012 fick jag:

| Mått | Värde |
|---|---:|
| Typvärde | 8 |
| Median | 8,0 |
| Medelvärde | 8,484 |
| Range | 14 |
| Varians, population | 10,572 |
| Varians, stickprov | 10,925 |
| Standardavvikelse, population | 3,252 |
| Standardavvikelse, stickprov | 3,305 |

Jag använder populationsvariansen som huvudvärde eftersom jag beskriver alla dagar i maj 2012, inte bara ett stickprov ur maj. Formeln är:

`varians = sum((x_i - medelvärde)^2)/n`

Jag skrev också ut stickprovsvariansen:

`s^2 = sum((x_i - medelvärde)^2)/(n-1)`

Det är bra att kunna nämna eftersom vissa lärare förväntar sig varians med n - 1.

De viktigaste formlerna är:

`medelvärde = sum(x_i)/n`

`standardavvikelse = sqrt(varians)`

`range = max - min`

`median = mittersta värdet efter sortering`

`typvärde = vanligaste värdet`

## Uppgift 3
Jag tog ut månadsnumret ur datumet med heltalsberäkningar. Sedan räknade jag medelvärdet för alla januaridagar, alla februaridagar och så vidare för hela perioden 2008–2017.

Resultatet visar tydligt årstidsmönstret. Juli är varmast med ungefär 16,40 °C i genomsnitt, och januari är kallast med ungefär -6,67 °C.

Stapeldiagrammet finns i `figures/uppgift3_monthly_averages.png`.

## Uppgift 4
Korrelationen mellan dag n och nästa dag är 0,948. Det är nära 1, vilket betyder ett starkt positivt samband. När dagens temperatur är högre brukar alltså morgondagens temperatur också vara högre.

Korrelationen mellan dag n och 10 dagar senare är 0,843. Den är fortfarande positiv och ganska stark, men svagare än 1-dagskorrelationen.

Tolkningen är att temperaturen i morgon oftast ligger nära dagens temperatur, men sambandet blir svagare när tidsavståndet blir större.

## Kort att kunna förklara muntligt
- En empirisk fördelningsfunktion visar andelen observationer som är mindre än eller lika med ett värde.
- `P(X > 10) = 1 - F(10)` eftersom F(10) räknar alla värden som är högst 10 °C.
- En vanlig tabell visar varje dag. En frekvenstabell visar hur många gånger varje värde förekommer.
- Varians och standardavvikelse mäter spridningen runt medelvärdet.
- En korrelationskoefficient nära 1 betyder starkt positivt samband.
