# Laboration 1 – Beskrivande statistik

## Uppgift 1
### 1a
Datafilen innehåller 3653 rader/dagar. Antalet kalenderdagar från 2008-01-01 till 2017-12-31 är också 3653.

Alla datum är unika och datumserien matchar alla förväntade datum från 2008-01-01 till 2017-12-31. Därför kan vi dra slutsatsen att alla dagar under perioden 2008–2017 finns med i filen.

### 1b
Det kallaste dygnsminvärdet är -32,1 °C.

Det inträffar på datumet 2010-02-24.

### 1c
Den empiriska fördelningsfunktionen för dygnsmedelvärden har sparats som `figures/uppgift1c_ecdf.png`.

Avläsning och beräkning:

| Storhet | Värde |
|---|---:|
| F(10) = andel dygnsmedelvärden <= 10 °C | 0,676 |
| P(X > 10) = 1 - F(10) | 0,324 |

Tolkningen är att F(10) är andelen dygnsmedelvärden som är högst 10 °C. Sannolikheten för att ett dygnsmedelvärde är större än 10 °C blir därför komplementet, alltså 1 - F(10).

## Uppgift 2
### 2a
Dygnsmedelvärden för maj 2012, avrundade till heltal:

| Datum | Avrundat dygnsmedelvärde |
|---|---:|
| 2012-05-01 | 8 |
| 2012-05-02 | 8 |
| 2012-05-03 | 7 |
| 2012-05-04 | 3 |
| 2012-05-05 | 3 |
| 2012-05-06 | 5 |
| 2012-05-07 | 6 |
| 2012-05-08 | 6 |
| 2012-05-09 | 4 |
| 2012-05-10 | 8 |
| 2012-05-11 | 7 |
| 2012-05-12 | 8 |
| 2012-05-13 | 5 |
| 2012-05-14 | 8 |
| 2012-05-15 | 9 |
| 2012-05-16 | 9 |
| 2012-05-17 | 8 |
| 2012-05-18 | 10 |
| 2012-05-19 | 7 |
| 2012-05-20 | 9 |
| 2012-05-21 | 8 |
| 2012-05-22 | 10 |
| 2012-05-23 | 10 |
| 2012-05-24 | 14 |
| 2012-05-25 | 17 |
| 2012-05-26 | 15 |
| 2012-05-27 | 15 |
| 2012-05-28 | 11 |
| 2012-05-29 | 8 |
| 2012-05-30 | 9 |
| 2012-05-31 | 8 |

Frekvenstabell:

| Värde | Frekvens |
|---:|---:|
| 3 | 2 |
| 4 | 1 |
| 5 | 2 |
| 6 | 2 |
| 7 | 3 |
| 8 | 9 |
| 9 | 4 |
| 10 | 3 |
| 11 | 1 |
| 14 | 1 |
| 15 | 2 |
| 17 | 1 |

### 2b
Statistik för de avrundade dygnsmedelvärdena i maj 2012:

| Mått | Värde |
|---|---:|
| Typvärde | 8 |
| Median | 8,0 |
| Medelvärde | 8,484 |
| Range / variationsbredd | 14 |
| Varians, population (ddof=0) | 10,572 |
| Varians, stickprov (ddof=1) | 10,925 |
| Standardavvikelse, population (ddof=0) | 3,252 |
| Standardavvikelse, stickprov (ddof=1) | 3,305 |

Eftersom vi beskriver alla dagar i maj 2012 kan populationsvariansen användas. Stickprovsvariansen med n - 1 visas också eftersom den ofta används när data ses som ett stickprov och läraren förväntar sig s².

Formler:

`mean = sum(x_i)/n`

`variance population = sum((x_i - mean)^2)/n`

`variance sample = sum((x_i - mean)^2)/(n-1)`

`standard deviation = sqrt(variance)`

`range = max - min`

`median = middle value after sorting`

`mode = most frequent value`

## Uppgift 3
Genomsnittligt dygnsmedelvärde per månad för hela perioden 2008–2017:

| Månad | Namn | Medeltemperatur |
|---:|---|---:|
| 1 | Januari | -6,67 |
| 2 | Februari | -5,60 |
| 3 | Mars | -0,92 |
| 4 | April | 3,42 |
| 5 | Maj | 8,94 |
| 6 | Juni | 13,01 |
| 7 | Juli | 16,40 |
| 8 | Augusti | 14,62 |
| 9 | September | 10,69 |
| 10 | Oktober | 4,47 |
| 11 | November | -0,03 |
| 12 | December | -4,66 |

Stapeldiagrammet har sparats som `figures/uppgift3_monthly_averages.png`.

## Uppgift 4
Korrelation mellan dygnsmedelvärdet dag n och dag n+1: 0,948.

Korrelation mellan dygnsmedelvärdet dag n och dag n+10: 0,843.

En korrelation nära 1 betyder stark positiv korrelation. Här är 1-dagskorrelationen starkare än 10-dagskorrelationen. Det stöder tumregeln att morgondagens temperatur oftast ligger nära dagens temperatur, men att sambandet blir svagare när tidsavståndet blir större.

## Muntlig redovisning – saker att kunna förklara
- En empirisk fördelningsfunktion visar andelen observationer som är mindre än eller lika med ett visst värde.
- P(X > 10) = 1 - F(10) eftersom F(10) räknar andelen som är högst 10 °C och resten ligger över 10 °C.
- En rå tabell visar varje observation, medan en frekvenstabell visar hur många gånger varje värde förekommer.
- Varians och standardavvikelse mäter spridning runt medelvärdet. Standardavvikelsen är i samma enhet som observationerna.
- Korrelationskoefficienten mäter styrka och riktning i ett linjärt samband. Värden nära 1 betyder starkt positivt samband, värden nära -1 betyder starkt negativt samband och värden nära 0 betyder svagt linjärt samband.
