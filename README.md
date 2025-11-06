## Projektöversikt:
Detta projekt analyserar försäljningsdata från en e-handelsplattform för att identifera trender och toppar i omsättningen över tid. Vi i Studiegrupp 4 använder Python och bibliotek som pandas och matplotlib för att bearbeta data och visualisera resultat.

## Vad som hittils är gjort (Roller och ansvar):
- Kevin skapade projektets mappstruktur utifrån intruktioner och initierade GitHub-ropositories. Delade detta så att alla kunde klona och arbeta vidare i samma klonbas.

- Magdalena har tagit fram analyser för intäkt per kategori och intäkt per stad. Förberett datan för visualisering samt rensade datan genom att kontrollera och ta bort dubbletter.

- Katarina analyserade intäkter per månad och vecka samt skapade stapel- och linjediagram för att visa försäljningstrender över tid. Hon har även börjat skriva sammanfattning i README- sektionen. 

- Katarina har gjort färdigt intäkter per månad/veckor - nyckeltalen inklusive 2-3 rekommendationer samt städat upp allt i rätt mapp (viz, metrics, images)

- Kevin undersökte hur mycket kunder brukar handla för per order, alltså AOV (Average Order Value), och om det varierar mycket mellan ordrar. Han skapade en graf, där man enkelt kan läsa av resultatet. 

- Jan började arbeta med eventuella avvikelser (något oväntat mönster), samtidigt som Magdalena ritade upp grafer och städade upp hennes koder. 

## Rapport (Slutsatser baserat på aktuell data)
### Nyckeltal (från notebooken, efter lätt städning):
- **Produktkategorier som driver nest intäkt:** 1. Elektronik 2. Sport 3. Kläder
- **Städer som står för störst del av intäkten:** 1. Stockholm 2. Göteborg 3. Malmö
- **Månad med högsta intäkter:** Januari med 664 083.32 kr
- **Vecka med högsta intäkter:** v22, i mitten av Juni 
- **Genomsnittlig värde av en order:**
- **Spridning mellan ordrar:**
- **Topp 3 kategorier:** 1. Elektronik 2. Sport 3. Kläder
- **Eventuella avvikelser:**
- Vid analys av omsättning per stad ser man tydligt att Stockholm ligger över 30% över genomsnittet. Göteborg, Malmö och Uppsala ligger inom den vanliga gränsen. Västerås har en negativ/låg avvikelse med mer än 30% mindre än genomsnittet.
- Analysen visar tydligt hur efterfrågan varierar mellan de olika kategorierna. Kategorien "Beauty" minskar krafitgt i februari (-52%) men ökar kraftigt i Mars (+68%). Electronics kategorien visar en stor nedgång i Mars med (-41%) medan Clothing och Sports kategorien ökar kraftigt under våren.
- Analysen visar att några ordrar har ovanligt hög units värde (>7), vilket gör dem tyligt större än genomsnittet. Det finns flera ordar med mycket låg omsättning,ofta under 100 kr jamfört med medianen på cirka 1089 kr. Priserna i sig verkar stabila mellan kategorierna.
- I analysen av "Revenue per månad" hittar man inga konsithgeter dvs inga hopp eller extrem stora skillnader mellan månaderna dock så är revenuen lägst i månaden Mars 


### Figurer
![Intäkt per månad](../data/images/fig_intakt_per_manad.png)
![Intäkt per vecka](../data/images/inakt_per_vecka.png)
![Intäkt per stad](../data/images/inakt_per_stad.png)
![Intäkt per kategori](../data/images/inakt_per_kategori.png)
![Intäkt per stad med avvikelsemarkering](..data/images/fig_city_revenue.png)


## Miljö
- **Python:** 3.13.7
- **Paket:** `Pandas`, `matplotlib`, `Numpy`

## Hur man kör projektet:

```bash
# klona projektet
git clone https://github.com/KevinCJohansson/E-handel-snabbrapport.git

cd E-HANDEL-SNABRAPORT

# Skapa och aktivera virtuell miljö
python -m venv . venv
# Windows PowerShell
.venv\Scripts\Activate

# macOs\ Linux
# source .venv/bin/activate

# instalera beroenden
python -m pip install -r requirement.txt
```