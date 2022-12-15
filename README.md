# Basketbola spēles rezultāta prognozēšana: projektējuma dokuments
# Ievads
### Problēmas nostādne
Basketbola spēļu rezultātu prognozēšana
### Darba un novērtēšanas mērķis
Palīdzēt sporta entuziastiem/faniem labāk prognozēt basketbola spēles uzvarētāju
# <div align="center">**Līdzīgo risinājumu pārskats**</div>
**Līdzīgo risinājumu pārskats ir salīdzināts 1.tabulā.**
| Līdzīgais risinājums | Parametri | Dati, kas tiek izmantoti | Kas vajadzīgs, lai apmācītu modeli | Plusi/mīnusi |
|---|---|---|---|---|
| Ar lineāro regresiju [(atsauce)](https://deliverypdf.ssrn.com/delivery.php?ID=081001096020079068080113000073116086033075065035019070107070102030004092065001088118056100018023015058017103112102001004112012021054035061019010000089091080110101036082011088020114103093022100101064094005117017113120127088121101117077023121003000106&EXT=pdf&INDEX=TRUE) | 𝑦 - datu iezīmes 𝛽 - vektors, ko aprēķina no 𝑦 𝑋 - rezultātu matrica | Informācija par spēlētājiem - spēlētāja vārds, PPG, MPG, RBG, APG un spēlētāja numurs. | Saistības starp spēlētāju informāciju - kuram ir lielāks svarīguma koeficents, lai iegūtu prognozi | Plusi: viegli saprotama interpretācija. <br /> Mīnusi: jābūt uzmanīgiem ar datiem, jo, ja ir nepareizi ievadīti, tad regresija var nenostrādāt  |
| K-tuvāko kaimiņu algoritms ([atsauce](https://pdfs.semanticscholar.org/b034/eb84e7e6f4feee7c06cbdc4f94a6ec226d5b.pdf)) | x un y vērtības Eiklīda attālums K skaits | Katra spēlētāja uzbrukumu un aizsardzības statistika, punkti, atlēkušās bumbas, pārķertās bumbas, piespēles, bloki, pārkāpumi | Dati ar kuriem strādāt un attālums ar kuru aprēķināt attālumu starp punktiem | Plus ir tāds, ka nevajag izdarīt papildu pieņēmumus par datiem, nav apmācības perioda taču trūkums ir tāds, ka ir grūti izvēlēties pareizo kaimiņu vērtību, algoritms ir jūtīgs pret trūkstošiem datiem. |
| Elo novērtējuma algoritms([atsuce](https://www.geeksforgeeks.org/elo-rating-algorithm/)) | Reitings | Komandu uzvaru skaits, spēlētāju reitingi, komandu iepriekšējo spēļu elo reitings | Piefiksēt vai komanda uzvar, vai zaudē iepriekšējā spēlē, pēc kā uzvara dod attiecīgo punktu skaitu, zaudējums noņem attiecīgo punktu skaitu. <br /> Punkti veido reitingu un algoritms pēc tā paredz spēles uzvarētāju. | Salīdzinoši vienkāršs algoritms, var pielietot spēļu iznākumu prognozoēšanā, jo tas ir loģiski - komanda, kurai sezonā būs vairāk uzvaras, būs lielāks Elo novērtējums, kas ļaus sporta entuziastiem, faniem paredzēt vieglāk uzvarētāju. <br /> Mīnusi : ne vienmēr favorītu komanda, jeb komanda ar lielāku reitingu uzvarēs. |
| Pārmeklēšanas koks (Decision tree) ([atsauce](https://www.samford.edu/sports-analytics/fans/2022/Using-Decision-Tree-Algorithms-to-Test-the-Accuracy-of-NBA-Playoff-Predictions)) | Masīvi | Komandu un spēlētāju punkti, piespēles, atlēkušās bumbas, pārķertas bumbas, kļūdas, iemesto metienu procents, uzvaru skaits, zaudējumu skaits, uzvaru procents, zaudējumu procents | Indukcija - koka veidošana, visu hiearhisko lēmumu defininēšana, datu apjoma ierbežošana. <br /> Atzarošana - lieko un trūkstošo datu izņemšana, lai veicinātu precīzāku rezultātu izvadi, kā arī koka izmēru/apjomu. | Viegli interpretājami rezultāti un grafiski attēlojami, kā arī tiek parādīi novērtējumi, katram zaram. Liekie dati netiek uzrādīti, kas samazina koka izmēru, tā rezultātā tas ir vieglāk pārskatāms. <br /> Mīnusi : algoritms ir lēnāks, piemēram, par lineāro regresiju, tas pieprasa lielāku atmiņas apojomu. Tā apjoms ir sālīdzinoši jāierobežo, lai tiktu uzzīmēts kvalitātīvs un pārskatāms koks. |

# Tehniskais risinājums
## Prasības
Sistēmas lietotāji:
* Basketbola entuziasti 
* Treneri 

**Prasības ir apkopotas 2.tabulā:**

| Prasības ID | Lietotāja stāsts | Prioritāte | 
|---|---|---|
| P1 | Lietotājs vēlas prognozēt basketbola spēles rezultātu | 1 |
| P2 | Lietotājs vēlas redzēt kādas iepriekš ir bijušas prognozes | 2 |

## Algoritms (blokshēma vai pseidokods)


## Konceptu modelis
Basketbola spēles rezultāta prognozēšanas svarīgākie koncepti ir:
* Komandas statistika
* Prognoze 
* Spēles rezultāts 

Konceptu apraksts ir dots 3.tabulā. Konceptu modelis ir dots 1.attēlā.
### 3.tabula Konceptu modelis
| Konceptu ID | Koncepta nosaukums | Apraksts | 
|---|---|---|
| K1 | Komanda | Visas komandas statistika - spēlētāji, uzvaru/zaudējumu skaits un citi parametri |
| K2 | Spēle | Pēc izspēlētām spēlēm ir iespējams apkopot spēlētāju individuālo statistiku, kā arī komandas kopējo statistiku. Un var strādāt ar tās datiem. |
| K3 | Spēletāju statistika | Visu spēlētāju statistiskos parametrus apkopo priekš komandas statistikas |
| K4 | Komandas statistika | Veidojas no visu komandas spēlētāju individuālās statistikas apkopošanas. Piemēram, ja spēlētājs A spēlē vidēji gūst 8 punktus un spēlētājs B gūst 12 punktus, tad vidēji viņi gūst 10 punktus((8+12)/2) |
| K5 | Statistikas pārskats | Apkopo no komandas statistikas |
| K6 | Prognoze | Pēc statistikas apkopojuma tiek spekulēts labvēlīgais/iespējamais spēles rezultāts |
| K7 | Spēles rezultāts | Prognozētais spēles rezultāts |
| K8 | Lietotājs/komandas fans | Veic prognozi, iespējams, balstoties uz statistikas apkopojumu |
### 1.attēls Konceptu modelis
[![koncepta-modelis.png](https://i.postimg.cc/3N8DT1NQ/koncepta-modelis.png)](https://postimg.cc/G8fpPkvX)

## Tehnoloģijas steks
Tehnoloģijas steks ir redzams 4.tabulā.
| Tehnoloģiju steks | 
| ------ | 
| Satvars: Streamlit | 
| Programmēšanas valoda: Python | 
| Tīmekļa serveris: Apache | 
| OS: Ubuntu | 
| Serveris: Fiziskā iekārta vai VM | 

## Programmatūras apraksts

# Novērtējums
## Novērtēšanas plāns
**Eksperimenta mērķis:**  Noskaidrot uzvarošo basketbola komandu

**Ieejas parametri:** Izvēlēto komandu statistika - punkti, +/- , piespēles, atlēkušās bumbas, pārķertās bumbas

**Novērtēšanas mēri:** Punkti - points (PTS) - 5, Plus/mīnus - (+/-) - 4, Piespēles - assists (AST) - 3, Atlēkušās bumbas - rebounds (REB) - 2, Atņemtās bumbas - steals (ST) - 1


| NR. | PTS | (+/-) | AST | REB | ST |
| ------ | ------ |------ |------ |------ |------ |
| 1 |  | | | | |
| 2 |  | | | | |
## Novērtēšanas rezultāti

# Secinājumi
