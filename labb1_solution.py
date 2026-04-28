import numpy as np
import matplotlib.pyplot as plt


def ar_skottar(ar):
    return (ar % 4 == 0 and ar % 100 != 0) or (ar % 400 == 0)


def datum_som_text(datumtal):
    datumtal = int(datumtal)
    ar = datumtal // 10000
    manad = (datumtal // 100) % 100
    dag = datumtal % 100
    return f"{ar:04d}-{manad:02d}-{dag:02d}"


def alla_datum(start_ar, slut_ar):
    manadslangder = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    datumlista = []

    for ar in range(start_ar, slut_ar + 1):
        for manad in range(1, 13):
            antal_dagar = int(manadslangder[manad - 1])
            if manad == 2 and ar_skottar(ar):
                antal_dagar = 29

            for dag in range(1, antal_dagar + 1):
                datumlista.append(ar * 10000 + manad * 100 + dag)

    return np.array(datumlista)


def avrunda_till_heltal(varden):
    return np.where(varden >= 0, np.floor(varden + 0.5), np.ceil(varden - 0.5)).astype(int)


svl = np.loadtxt("Sundsvall.dat")

datum = svl[:, 0].astype(int)
dygnsmedelvarde = svl[:, 1]
dygnsmaxvarde = svl[:, 2]
dygnsminvarde = svl[:, 3]

ar = datum // 10000
manad = (datum // 100) % 100

print("Laboration 1 - Beskrivande statistik")
print()

print("Uppgift 1a")
antal_rader = len(datum)
forvantade_datum = alla_datum(2008, 2017)
forvantat_antal = len(forvantade_datum)
unika_datum = np.unique(datum)
unika = len(unika_datum) == antal_rader
alla_forvantade_datum_finns = np.array_equal(np.sort(datum), forvantade_datum)

print(f"Antal rader/dagar i filen: {antal_rader}")
print(f"Antal kalenderdagar 2008-01-01 till 2017-12-31: {forvantat_antal}")
print(f"Radantalet stammer: {antal_rader == forvantat_antal}")
print(f"Alla datum ar unika: {unika}")
print(f"Datumserien matchar alla forvantade datum: {alla_forvantade_datum_finns}")
if antal_rader == forvantat_antal and unika and alla_forvantade_datum_finns:
    print("Slutsats: Ja, vi kan dra slutsatsen att alla dagar 2008-2017 finns med.")
else:
    print("Slutsats: Nej, radantal och/eller datumkontroll visar att nagot saknas eller avviker.")
print()

print("Uppgift 1b")
kallaste_min = np.min(dygnsminvarde)
kallaste_datum = datum[dygnsminvarde == kallaste_min]
print(f"Kallaste dygnsminvarde: {kallaste_min:.1f} grader C")
print("Datum:", ", ".join([datum_som_text(d) for d in kallaste_datum]))
print()

print("Uppgift 1c")
sorterade_medel = np.sort(dygnsmedelvarde)
ecdf_y = np.arange(1, antal_rader + 1) / antal_rader
ecdf_x_plot = np.concatenate(([sorterade_medel[0] - 1], sorterade_medel))
ecdf_y_plot = np.concatenate(([0], ecdf_y))

plt.figure(figsize=(8, 5))
plt.step(ecdf_x_plot, ecdf_y_plot, where="post")
plt.xlabel("Dygnsmedelvarde (grader C)")
plt.ylabel("F(x)")
plt.title("Empirisk fordelningsfunktion for dygnsmedelvarden")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("figures/uppgift1c_ecdf.png", dpi=150)
plt.close()

f_10 = np.mean(dygnsmedelvarde <= 10)
p_over_10 = 1 - f_10
print(f"F(10) = andelen dygnsmedelvarden <= 10 grader C: {f_10:.3f}")
print(f"P(X > 10) = 1 - F(10): {p_over_10:.3f}")
print("Figur sparad som figures/uppgift1c_ecdf.png")
print()

print("Uppgift 2a - Maj 2012")
maj_2012 = (ar == 2012) & (manad == 5)
maj_datum = datum[maj_2012]
maj_medel = dygnsmedelvarde[maj_2012]
maj_avrundade = avrunda_till_heltal(maj_medel)

print("Datum        Avrundat dygnsmedelvarde")
for d, varde in zip(maj_datum, maj_avrundade):
    print(f"{datum_som_text(d):<12}{varde:>5d}")
print()

frekvens_varden, frekvenser = np.unique(maj_avrundade, return_counts=True)
print("Frekvenstabell")
print("Varde    Frekvens")
for varde, frekvens in zip(frekvens_varden, frekvenser):
    print(f"{varde:>5d}{frekvens:>11d}")
print()

print("Uppgift 2b")
max_frekvens = np.max(frekvenser)
typvarden = frekvens_varden[frekvenser == max_frekvens]
median = np.median(maj_avrundade)
medelvarde = np.mean(maj_avrundade)
variationsbredd = np.max(maj_avrundade) - np.min(maj_avrundade)
varians_population = np.var(maj_avrundade, ddof=0)
varians_stickprov = np.var(maj_avrundade, ddof=1)
standardavvikelse_population = np.std(maj_avrundade, ddof=0)
standardavvikelse_stickprov = np.std(maj_avrundade, ddof=1)

print("Typvarde:", ", ".join([str(int(varde)) for varde in typvarden]))
print(f"Median: {median:.1f}")
print(f"Medelvarde: {medelvarde:.3f}")
print(f"Range/variationsbredd: {variationsbredd}")
print(f"Varians, population (ddof=0): {varians_population:.3f}")
print(f"Varians, stickprov (ddof=1): {varians_stickprov:.3f}")
print(f"Standardavvikelse, population (ddof=0): {standardavvikelse_population:.3f}")
print(f"Standardavvikelse, stickprov (ddof=1): {standardavvikelse_stickprov:.3f}")
print()

print("Uppgift 3")
manadsnamn = np.array([
    "Januari", "Februari", "Mars", "April", "Maj", "Juni",
    "Juli", "Augusti", "September", "Oktober", "November", "December"
])
manadskort = np.array(["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"])
manadsmedel = np.zeros(12)

for manadsnummer in range(1, 13):
    manadsmedel[manadsnummer - 1] = np.mean(dygnsmedelvarde[manad == manadsnummer])

print("Manad  Namn        Medeltemperatur")
for manadsnummer in range(1, 13):
    print(f"{manadsnummer:>5d}  {manadsnamn[manadsnummer - 1]:<10}{manadsmedel[manadsnummer - 1]:>10.2f}")

plt.figure(figsize=(9, 5))
plt.bar(np.arange(1, 13), manadsmedel, color="#4c78a8")
plt.xticks(np.arange(1, 13), manadskort)
plt.xlabel("Manad")
plt.ylabel("Genomsnittlig dygnsmedeltemperatur (grader C)")
plt.title("Medeltemperatur per manad, Sundsvall 2008-2017")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("figures/uppgift3_monthly_averages.png", dpi=150)
plt.close()
print("Figur sparad som figures/uppgift3_monthly_averages.png")
print()

print("Uppgift 4")
korrelation_1_dag = np.corrcoef(dygnsmedelvarde[:-1], dygnsmedelvarde[1:])[0, 1]
korrelation_10_dagar = np.corrcoef(dygnsmedelvarde[:-10], dygnsmedelvarde[10:])[0, 1]

print(f"Korrelation mellan dag n och dag n+1: {korrelation_1_dag:.3f}")
print(f"Korrelation mellan dag n och dag n+10: {korrelation_10_dagar:.3f}")
print("Tolkning: En korrelation nara 1 betyder stark positiv korrelation.")
print("1-dagskorrelationen ar starkare an 10-dagskorrelationen.")
print("Det stoder tumregeln att morgondagens temperatur ofta ligger nara dagens,")
print("men sambandet blir svagare nar tidsavstandet blir storre.")
