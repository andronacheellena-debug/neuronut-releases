# Analiza videoului model → pași 1–3

**Video:** „Моя ИИ-команда на 1 млн₽" (Михаил Тимочко), episodul-pilot din reality-ul „Закулисье", publicat pe 2026-11-25. Durată: 45:05. Limbă: rusă.
**Rezultat la momentul analizei:** 11.078 vizualizări, 279 like-uri, 68 comentarii (vidIQ).
**De ce e un model bun pentru Nevo:** e un episod-pilot de reality, lansat în campania de Black Friday. Vinde un club (Кэш'ю) fără să-l pitch-uiască în corp, iar produsul rămâne în afara cadrului până în ultimul minut.

---

## 0. Ce am făcut și ce nu (citește întâi)

| Pas din brief | Stare | Detalii |
|---|---|---|
| Descărcare yt-dlp | **PARȚIAL** | Videoul propriu-zis nu se poate descărca. După ce am deschis hosturile YouTube, YouTube cere autentificare („Sign in to confirm you're not a bot") pentru formatele video/audio de la IP-uri cloud. Nu am cookies și nu ocolesc verificarea. Ce am putut lua legal: **storyboard-urile** (cadre reale la ~10 s). |
| Subtitrări / Whisper pe cuvânt | **NU SE POATE** | Fără audio nu rulează Whisper. Subtitrările YouTube cer PO token. Am transcrierea completă de la vidIQ, cu timpi la 15–20 s, nu pe cuvânt. Timpii „ce se spune" sunt deci aproximativi (±10 s). |
| Cadre cheie | **FĂCUT, la rezoluție mică** | 272 de cadre reale, 320×180, câte unul la ~9,9 s, 00:00 → 44:54, în `cadre/` (numite după timp). Plus 31 de foi de contact în `cadre/foi/` (9 cadre pe foaie). Le-am vizionat pe toate. Nu am detectare de scene (ar fi cerut videoul). |
| Strategia din Notion | **FĂCUT** | Centrul proiectului NeuroCreator, „Semnătura Elenei", jurnalul 25 oct – 23 nov. |

**Încredere:**
- **Ce se spune** și **capitolele**: sigure (transcriere vidIQ + descrierea autorului). Timpii: ±10 s.
- **Ce se vede, text pe ecran, tip de cadru, decor**: **verificate pe cadre reale** (eșantion la ~10 s). Ce se întâmplă între două cadre nu se vede.
- **Tranziții și muzică**: **nu pot fi judecate** din imagini statice. Le-am scos din tabel acolo unde nu am dovadă. Marcajele `[музыка]` din transcriere arată doar unde e muzică.
- **Durata medie a cadrului**: **nu o pot măsura** cu eșantion la 10 s. Detalii la 2c.
- **Corectură:** o primă variantă a analizei folosea descrierea vizuală generată de vidIQ. Cadrele reale au arătat că era în parte greșită: nu există „apel Zoom cu expert secret", iar graficele nu sunt înregistrări de ecran, ci animații stilizate. Varianta de mai jos o înlocuiește.

**Ce lipsește:** ritmul exact al tăieturilor, tranzițiile și muzica. Le obțin doar dacă îmi dai tu videoul descărcat în `./model/`.

---

## 2a. Timeline

Timpii vin din transcriere și din cadre (eșantion la ~10 s). „Ce se spune" e rezumat în română.

| Timp | Ce se spune | Ce se vede (cadre) | Tip cadru | Text pe ecran |
|---|---|---|---|---|
| 00:00–00:29 | „Acum o lună mi s-a născut un fiu... spălând pompele de lapte m-am gândit: ce-ar fi dacă ar lucra rețelele neuronale în locul meu?" Apoi: ce creează oamenii cu AI, „vreau la fel". | Close-up cu copilul pe umăr; spălat vase în bucătărie; mâini pe tastatură (macro); apoi el, plan larg în living | **B-roll de viață reală** (3 cadre) + talking head | — |
| 00:29–00:48 | „Am mers la un expert să mă învețe de la zero. În reality arăt ce funcționează." | Talking head, living; apare un card alb în stil de fereastră | Talking head + grafică | Card: „În acest reality: Învăț Claude Code de la zero" (cuvântul „reality" evidențiat galben) |
| 00:48–01:11 | **Provocarea:** echipă de agenți „de un milion", 1.000.000 ₽/lună economie. | Card „Provocare principală: Echipa de agenți AI"; card mare „Cheltuieli pe echipă 1 000 000 ₽" cu cifra pe fundal galben; colaj de miniaturi (montaj, slide-uri, reel-uri, conținut, postări) | **Grafică animată** (3 cadre consecutive) | „1 000 000 ₽" |
| 01:11–01:26 | „Arăt tot drumul ca novice pentru novici, cost = o lună de abonament." | Pe canapea, lista de agenți ca card lângă el | Talking head + card | „ca novice pentru novici", „pentru 1 mil ₽" |
| 01:26–02:09 | **Prima declanșare:** fostul elev Artiom (la 16 ani), un video cu 605.000 vizualizări; postează zilnic. | Pe canapea cu copilul pe genunchi, laptop; bară de căutare suprapusă; apoi **captură de ecran** cu canalul lui pe YouTube și grila de miniaturi | Talking head + **screen capture real** | Căutare: „videoul meu > 605 mii vizualizări" |
| 02:09–02:59 | Vizualizări zilnice; i-a scris „ce e ritmul ăsta maniacal?"; arată lista de skill-uri. | Card cu numele Artiom Voronkov; **mesaj Telegram** în balon galben; **laptopul ținut spre cameră** cu cifra „11585" | Talking head + grafică + prop (laptop) | Balon: „Artiom, ce e asta?" |
| 02:59–03:49 | Un clip al lui: 2 săptămâni, mai multe etape; 2–2,5 clipuri/lună. | Chips galbene („nu AI-gunoi", „montaj bun", „scenariu bun"); **diagramă Gantt animată „Un clip de Misha"**: ZIUA 01 → ZIUA 05 → ZIUA 14, blocuri pe etape (scenariu, filmare, montaj, corecturi) | **Grafică animată** | „ZIUA 01 / 05 / 14", „2,5" |
| 03:49–04:28 | „Artiom: 20 clipuri/lună, de 10 ori mai productiv." | Râde pe canapea; card hartă; **titlu full-screen alb**: „Un băiat cu Claude ne depășește de 10 ori ca dinamică pe YouTube" | Talking head + **cadru de titlu** | „în 10 ori" cu subliniere galbenă |
| 04:28–05:58 | **A doua declanșare:** Nick Saraev, 560.000 abonați. Vizualizări de milioane; YouTube vs Instagram. | Captură cu canalul lui Saraev (miniaturi în engleză); card calendar „Noiembrie"; grafic cu creștere „zeci de mil."; **reel pe telefon** „ASA ARATĂ 150 000 000" | Screen capture + grafică | „zeci de mil.", „150 000 000" |
| 05:58–07:27 | Re-hook „nuanță uitată"; **recapitularea problemei:** „lider de piață, echipă mare, 50.000 ₽/clip, 2–3 clipuri/lună vs ei, zilnic". | Card text: „**Problema:** • blogger experimentat • lider de piață online-education"; **tabel comparativ „Eu / Băieții"**: „până la 50.000 ₽ / 2–3 pe lună" vs „în fiecare zi" (galben); **își acoperă fața cu mâna** | Grafică + talking head | „Problema:", „în fiecare zi" |
| 07:27–08:57 | **A doua declanșare (costuri pe rol):** designer, manageri de direct, monteuri, producător de conținut. | Card „Învață"; **„Raport financiar → Cheltuieli"** care se umple rând cu rând (Designer 250–300 mii, Manageri de direct 200.000 ₽, Monteur YouTube 150–300 mii, Monteur Reels), chip „și dacă Claude?" | **Grafică animată cu rânduri care apar** | Sume pe rol |
| 08:57–10:07 | Producătorul de conținut, coperți, suport; „pot economisi minim 500.000 ₽/lună, poate 1,5 mil." | Reel pe telefon „NETWORKING DE LA DUMNEZEU 18 000"; **fotografie a colegului** cu subtitlul numelui; carduri suport (cărți, plăți); carduri „500 000 ₽" apoi „**1,5 mil ₽**" | Grafică + talking head | „500 000 ₽", „1,5 mil ₽" |
| 10:07–18:30 | **Viziunea:** schema echipei de 22 de agenți (YouTube / Instagram / Telegram / Comune / Director). | **Schimbare de decor:** în picioare lângă **un poster fizic tipărit**, cu agenți ca personaje de desen animat (negru-galben), pe un perete alb. Gesticulează către rânduri. Rar apar carduri: „Ambalator 1 din 3 gata", **mesaj Telegram**, **pagina lui web negru-galben** („5 convingeri cu care îți găsești clienți ușor") la ~16:15 | Plan mediu/larg, prop fizic, close-up când comentează | Poster; „Ambalator" |
| 18:30–20:03 | **Țintele anuale** + „poate e doar o fantezie". | Card **„Eu vreau:"** care se completează pe rând (YouTube 3–4/săpt., Reels 6–10, Insta +300 mii, YouTube +100–200 mii, Telegram 100 mii, club 15–20 mii, „produs nou — secret"), alternat cu el la poster | Grafică + talking head | Lista cu valori pe fundal galben |
| 20:03–20:17 | **Pattern interrupt:** „Fă screenshot la lista de 150 de rețele și șterge-le." | Captură „Top 50 Gen AI web products" | Screen capture | — |
| 20:17–22:34 | **De ce Claude:** onest, scrie ca om, digeră volum, **face.** | **Schimbare de decor:** la masa din bucătărie, luminos. Dock cu iconițe („acum 1,5 ani"); **mock-up ChatGPT:** „Idee: vând un curs de AI tuturor" → „Idee genială! Sunteți cu un pas înainte! Total de acord!"; **mock-up Claude:** „Sincer? **Idee slabă.**"; bare comparative | Talking head + **mock-up de chat animat** | „Sincer? Idee slabă." (galben) |
| 22:34–26:07 | **Diferența:** chat-ul îți dă instrucțiune; Code face treaba. | Mock-up „Claude Code: Iată 101 blogeri — descarcă toate reel-urile" → „aprox. 100 000 de reel-uri" cu un **mozaic de feţe**; chat: „Vreau să fac conținut. Cum?" cu întrebări; laptop negru cu steluța Claude; mock-up chat care răspunde cu o instrucțiune; mock-up Code cu **checklist care se bifează** („Deschid Google Chrome / Pun extensia / Conectez serviciul / Descarc") | Mock-up-uri animate (nu înregistrări reale) | Checklist cu bife galbene |
| 26:07–29:13 | **Voce de pe telefon:** „sunt la plimbare cu copilul". Generare video prin alt serviciu. | **Schimbare de decor:** în aer liber cu **cărucior, pe aleea unui cartier**, vorbind la telefon; card pe telefon: „Descarcă clipul de pe YouTube și taie-l în 10 reel-uri"; „Mac-ul de acasă: Am primit sarcina"; mock-up „Toate AI-urile — 1 abonament" (GPT, Grok, Gemini); grilă „Posturi, Montaj, Scenarii, Site-uri, Coperți, Direct, Carusele, Research, Conspecte, Analitică"; conexiune Claude → Higgsfield; **b-roll** cu un băiat în Moscova (video generat, din povestea lui) | Decor nou în aer liber + grafică | Etichete de skill-uri |
| 29:13–30:42 | **Obiecția „la noi e blocat":** o reframează ca avantaj. | Iconițe Telegram/YouTube/Instagram/WhatsApp cu insignă roșie, „indisponibil"; card „100 de site-uri / 1000 de reel-uri într-o lună" (frilanceri) | Talking head + grafică | „indisponibil" |
| 30:42–34:57 | **Instalare cu invitată.** | **Schimbare de decor:** la masă, **invitata** („Amalia — expert invitat") cu un nou-născut la piept; carduri **VPN / Cont / Metodă de plată / Adresă** (adresa Moscova → Almatî); **screen recording real** cu site-ul Claude și Google, cu **cercul feței lui în colț (PiP)**; căutare „servicii SMS număr străin" (eSIM, Virtual Phone, Temporary SMS); card „Rudă" | Două persoane la masă + mock-up-uri telefon + screen recording cu PiP | „+10 ani", numele invitatei |
| 34:57–39:55 | **Onestitate:** „Clarificarea 1 din 3 / 2 din 3 / 3 din 3". 60% abilitatea ta. Plan B (Codex). | **Schimbare de decor:** **selfie în mers, în aer liber**, altă ținută (cămașă cu model). Carduri cu **chip galben „Clarificare 1 din 3"** și diagrame animate: bare GPT vs Claude de acum 6 luni; benchmark-uri; meniu „Model: Fable 5.2 / Opus / Sonnet / Haiku" + „Efort"; „Totul îl decid mâinile" (camera A = camera B); novice vs profesionist cu „+80%"; bară „**60%** abilitatea ta / 25–30% model / 10% brand" | Talking head în mișcare + grafice animate numerotate | „Clarificare 1 din 3" |
| 38:46–41:46 | Dacă te blochează, munca rămâne în folder. Tabul „Code". Plata. | Foldere „Casa lui Claude"; selfie lângă mașină; la masă; **screen recording real** al aplicației Claude cu PiP; card „Pro: Chat / Proiecte / Claude Code"; selfie cu telefonul (plata prin intermediari) | Mixt | „Pro" |
| 41:46–43:58 | **Prima sarcină cu vocea:** folderul „Casa lui Claude" + 2 subfoldere; Downloads; o prezentare pe Desktop. | Animații: folder galben → „Business / Personal"; bară de înregistrare vocală în aplicația Claude; foldere sortate (Foto, Video, Muncă, Proiecte); comandă pe Desktop | Mock-up + screen recording | „Business / Personal" |
| 43:58–44:21 | **Cliffhanger** spre episodul 2. | Card „**Seria 2: Cine e el?** expert în rețele neuronale" cu un „?" peste fața lui; grilă de iconițe pentru episoadele următoare (Claude Code / Codex / Design) | Grafică animată | „Seria 2", „Cine e el?" |
| 44:21–45:05 | **Oferta.** | Card **negru-galben „Black Friday · Кэш'ю · până pe 29.11 · 2 luni la prețul uneia · 6 000 ₽"**; **ultimul decor:** pe canapea, cu copilul în brațe, „**9 serii**" tăiat, „**Toate seriile în Кэш'ю**" | Card full-screen + talking head | Oferta + „Toate seriile în Кэш'ю" |

---

## 2b. Structura

| Parte | Interval | Durată | % din 45:05 |
|---|---|---|---|
| Hook: viață reală + întrebare deschisă | 00:00–00:29 | 29 s | 1,1% |
| Promisiune + miză (agenți „de un milion") + format | 00:29–01:26 | 57 s | 2,1% |
| Problemă 1: elevul și Saraev depășesc eroul | 01:26–05:58 | 4:32 | 10,1% |
| Problemă 2: recapitulare + costul echipei, în ruble | 05:58–10:07 | 4:09 | 9,2% |
| **Viziunea:** poster cu 22 de agenți + țintele anuale | 10:07–20:03 | 9:56 | 22,1% |
| De ce această unealtă (Claude vs. ChatGPT) | 20:03–22:34 | 2:31 | 5,6% |
| Ce o face diferită: „face, nu doar sfătuiește" | 22:34–29:13 | 6:39 | 14,8% |
| Obiecția „la noi e blocat" | 29:13–30:42 | 1:29 | 3,3% |
| Instalarea (cu invitata) | 30:42–34:57 | 4:15 | 9,4% |
| Blocul de onestitate (3 clarificări, 60/25/10, plan B) | 34:57–39:55 | 4:58 | 11,0% |
| Prima sarcină reală | 39:55–43:58 | 4:03 | 9,0% |
| Cliffhanger + ofertă + CTA | 43:58–45:05 | 1:07 | 2,5% |

(Intervalele vin din capitolele autorului; hook-ul sare de la 16 s din transcriere la 29 s ca să prindă secvența de b-roll.)

- **Eroul:** autorul, ca începător („novice pentru novici"), cu vulnerabilitate (copil nou-născut, mai puțin timp) și statut amenințat. Apare **mereu în decor de viață reală, cu copilul**, deci nu joacă „expertul".
- **Dovezi:** ale cazului (cifrele elevului și ale lui Saraev, propriile costuri). Rezultatele agenților nu sunt arătate în acest episod (doar poster, liste de skill-uri, mock-up-uri).
- **CTA:** un singur moment, la 44:21.

## 2c. Ritmul

- **Ce pot afirma:** în eșantionul de ~10 s, **aproape fiecare cadru e alt plan sau altă grafică**, deci schimbare vizuală cel puțin la 10 s. Din cele 272 de cadre, **aprox. 1 din 3 sunt grafici sau capturi**, restul talking head sau b-roll.
- **Ce NU pot afirma:** durata medie exactă a unui cadru. Eșantionul nu arată tăieturile dintre cadre. vidIQ estima 2,5–4 s în primele 5 minute, dar estimarea lui s-a dovedit nesigură în alte privințe, așa că nu o folosesc.
- **Accelerează** (grafic la fiecare 10 s): 00:48–01:11, 02:59–03:49 (Gantt), 07:27–08:57 (raportul financiar care se umple), 34:57–37:17 (clarificările numerotate).
- **Lasă spațiu:** secvențele la poster (10:07–18:30) și pe canapea, cu 3–5 cadre consecutive doar el, când spune ce simte și ce nu știe.
- **Ritmul prin decor:** **schimbă locul la fiecare 5–10 minute**, ca re-hook vizual (vezi 2h).
- **Tranziții și muzică:** `[de verificat dacă primesc videoul]`.

## 2d. Cum e arătat produsul, pas cu pas

Ordinea: (1) **rezultatul dorit, în cifre** → (2) **dovada că se poate** (elevul, Saraev) → (3) **posterul** cu ce vrea să construiască → (4) **de ce această unealtă** (mock-up chat, „Idee slabă") → (5) **diferența-cheie** („face, nu doar sfătuiește") → (6) **instalare** → (7) **prima sarcină, mică și vizibilă.**

- **Observație nouă din cadre:** produsul **nu e arătat în înregistrări reale** în cea mai mare parte. E **explicat cu animații stilizate** (mock-up de chat, checklist care se bifează, mozaic de 100.000 de reel-uri). Înregistrările reale apar doar la instalare și la prima sarcină, cu cercul feței în colț (PiP).
- **Cât de tehnic:** deloc în vorbire. Analogii („fixik", „aparate foto", „arme nucleare"). Tehnicul apare doar la instalare.
- **Ce rămâne nespus:** rezultatele reale ale agenților, cum se face un skill, cât costă abonamentul, ce nu funcționează încă.
- **Slăbiciune de evitat la Nevo:** viziunea (posterul de 22 de agenți) vine înaintea oricărei dovezi din produs. La Nevo avem demo real, deci îl punem înaintea viziunii.

## 2e. Psihologia

**Tensiune creată:**
1. *Întrebare deschisă* în primele 29 s („ce-ar fi dacă ar lucra rețelele în locul meu?"), răspuns amânat 44 de minute.
2. *Amenințare de statut*: elevul îl depășește de 10 ori; pune mâna la față, deci recunoaște că doare.
3. *Cifre concrete*, în ruble pe rol, care apar rând cu rând pe ecran.

**Re-hook-uri:**
- „O nuanță pe care am uitat s-o spun" (06:20).
- „Să fixăm încă o dată problema" (06:45) cu card **„Problema:"** pe ecran.
- „Nu știu dacă e real, poate e fantezie" (19:34): vulnerabilitate.
- „Fă screenshot și șterge-le" (20:03): pattern interrupt.
- **„Clarificare 1 din 3 / 2 din 3 / 3 din 3"** (34:57–37:17): enumerarea promisă ține spectatorul până la capăt.
- Obiecția anticipată (29:13) și cliffhangerul de episod (43:58).

**Cum construiește încrederea:** recunoaște ce nu știe; spune că ChatGPT poate fi la fel de bun; 60/25/10 (abilitatea ta contează cel mai mult); plan B (Codex) și plan C (munca rămâne la tine).

**Cum trece spre vânzare fără să pară reclamă:**
- Produsul (clubul) **nu apare** în corp. Tot videoul e valoare gratuită.
- Vânzarea e **prelungirea formatului**: „restul episoadelor nu vor fi pe YouTube" (chip „9 serii" tăiat).
- Oferta e un singur card negru-galben, ~40 s, cu termen explicit (până pe 29.11) și link în descriere.

## 2f. Tonul vocii și felul de a explica

- Conversațional, auto-ironic, la persoana I, cu pauze scurte. Cuvinte de stradă din când în când (nu le preluăm).
- Explică prin **contraste** (chat = instrucțiune / Code = execută), **analogii** simple și **liste numerotate**.
- Cifre peste tot, rostite rotund.
- Se adresează unui singur om („tu"), anticipându-i obiecțiile.
- Își asumă rolul de începător, nu de guru.

## 2g. Cele 5 lucruri care fac videoul să funcționeze

1. **Hook din viață reală + întrebare deschisă**, cu b-roll (copil, vase, tastatură), fără să zică ce vinde.
2. **Statut amenințat, în cifre**, arătate pe ecran pe măsură ce le spune.
3. **Onestitate calculată** (3 clarificări numerotate, „abilitatea ta e 60%"): dezarmează scepticismul înainte de ofertă.
4. **Diferența explicată într-o frază** („chat-ul îți dă instrucțiune, Code face treaba") și ilustrată cu un mock-up animat, nu cu jargon.
5. **Vânzarea ca prelungire a poveștii**: ofertă scurtă, la final, legată de raritatea formatului, cu termen.

## 2h. Limbajul vizual (nou, din cadre)

- **Decor schimbat la fiecare 5–10 minute**: canapea cu copilul, poster pe perete alb, masa din bucătărie, plimbare cu căruciorul, masă cu invitata, selfie în aer liber. Scopul e re-hook vizual, ca spectatorul să nu simtă monotonia unui talking head de 45 de minute.
- **Grafică unitară:** fundal pastel în degrade, carduri albe în stil de fereastră de aplicație, **accent galben ca evidențiator** pe cuvântul-cheie, bare animate, cifre mari.
- **Chip-uri galbene numerotate** („Clarificare 1 din 3") ca mecanism de re-hook.
- **Prop fizic** (posterul) ca punct vizual de ancorare a unui segment lung.
- **Cercul feței în colț (PiP)** în timpul înregistrărilor de ecran, ca omul să nu dispară.
- **Lower-third** cu nume/rol pentru invitată.
- Brandul lor e negru-galben (pagina web, cardul de ofertă).

---

## 3. Ce păstrăm, ce înlocuim

**Păstrăm** (structura psihologică, ritmul, tonul):
- Hook din situația ei reală + întrebare deschisă. `[DE ÎNTREBAT ELENA: situația ei]`
- Miza în cifre, nu în adjective, arătate pe ecran pe măsură ce le spune.
- Recapitularea problemei la mijloc (re-hook).
- Diferența într-o frază + demo mic, vizibil.
- Blocul de onestitate înaintea ofertei, numerotat („1 din 3").
- Oferta scurtă, la final, cu termen, ca prelungire a poveștii. Fără pitch în corp.
- **Mecanismul decorurilor:** schimbare de loc la fiecare secțiune. Locațiile Elenei (mașină, parcare, parc, mall, living, birou) acoperă exact nevoia.
- Ton de ghid care explică simplu, nu guru.

**Înlocuim:**

| În model | La Nevo |
|---|---|
| Artiom și Nick Saraev ca „amenințare de statut" | Figuri foarte cunoscute, pe tema VOC. Fără elevi, fără oameni reali din viața Elenei, fără nume de participanți/afaceri. |
| Costul echipei în ruble | Costul timpului: ce nu se mai face când montajul ia toată ziua. Cifrele Elenei `[DE ÎNTREBAT ELENA]`. Nu inventăm. |
| Posterul cu 22 de agenți | **Demo real cu Nevo** (idee → script → reel → carusel), apoi segmentul Elenei despre agenți. |
| Mock-up-uri animate pentru produs | La Nevo e mai tare **înregistrarea reală**, pentru că produsul există. Mock-up-uri doar pentru concepte (ex.: „VOC": ce cer oamenii). |
| Claude vs ChatGPT | „Nevo e despre reel-uri interesante, nu frumoase. Pentru oamenii care au ce spune." + limita asertivă. |
| Instalare (VPN, număr) | Nu e cazul. Locul ei: primul pas concret cu Nevo. `[DE ÎNTREBAT ELENA: cum se pornește Nevo]` |
| Oferta Кэш'ю, 2 luni la prețul uneia | Nevo singur 75 € · NeuroCreator 400 € cu Nevo inclus cadou. |
| Negru-galben | **Brandul Nevo** (brand book-ul Elenei), nu al modelului. |

**Figuri candidate pentru VOC** (propuneri de verificat; nu le folosim fără confirmare):
- **Airbnb, fondatorii:** în primii ani au mers la gazde, au văzut pozele slabe, apoi au făcut ei poze profesionale. Poveste documentată, legată de fotografia ta. *[de verificat sursa înainte de filmare]*
- **Jeff Bezos:** obsesia pentru client („scaunul gol") e repovestită des, dar detaliile variază. *[de verificat]*
- **Citatul „calul mai rapid" atribuit lui Henry Ford** e apocrif; nu-l folosim ca fapt.
- **Figuri din România/Moldova:** `[DE ÎNTREBAT ELENA: pe cine recunoaște publicul ei și are o poveste verificabilă despre „a asculta oamenii și a le da ce cer"]`. Nu am găsit un nume ales în Notion.

**Reguli din „Semnătura Elenei" (Notion):**
- Nu copiem alți creatori: luăm doar psihologia, niciodată aspectul.
- Nu inventăm fapte, scene sau trăiri despre Elena.
- Clienții nu se numesc fără acordul lor.
- Campaniile de monetizare pornesc, conform Notion, cu un editorial filmat profesionist în studio. `[DE ÎNTREBAT ELENA: videoul Nevo e acest editorial sau e separat? Locațiile tale înseamnă „fără studio"?]`
- „Creier Digital" nu se anunță public ca „ceva nou". `[DE ÎNTREBAT ELENA: cum numim public crearea de agenți în video?]`

**Aspect vizual:** al Elenei și al brandbook-ului Nevo. Nu am găsit pagina „Nevo Brand book noua identitate" în Notion. `[DE ÎNTREBAT ELENA: link sau fișier]`

## Neconcordanțe între brief și Notion (REZOLVATE pe 25 nov, vezi „Actualizare" la final)

1. **Prețul NeuroCreator:** brieful zice 400 € (Black Friday). Notion (oferta din noiembrie) arată 299 €, în 2 rate; Neuronuț 75 € la Black Friday (confirmat 15 nov). Folosesc 400 € și 75 € din brief. `[DE CONFIRMAT 400 €, termen, rate]`
2. **Dovada „10 participanți":** jurnalul Notion din 11 nov spune 4 participante declarate. Cifra 10 poate fi mai nouă. `[DE CONFIRMAT la data filmării]`
3. **„6 afaceri vorbitoare de română":** nu am găsit-o în paginile citite. Notion notează că acordul afacerilor pentru reelul de dovadă (29 nov) e încă deschis. `[DE CONFIRMAT acordul]`
4. **Nume:** Notion folosește încă „Neuronuț" pe pagini; brieful zice „Nevo". Am folosit „Nevo".
5. **Timpul pe zi:** Notion a stabilit pe 17 nov „o oră pe zi" pentru comunicare. Dacă apare în video, e „o oră".

## Actualizare 25 nov: confirmări de la Elena

- **Nume:** Nevo (fostul Neuronuț). Confirmat.
- **Preț:** NeuroCreator 400 € (cu Nevo inclus), Nevo singur 75 €. Confirmat. Termenul ofertei: încă `[DE ÎNTREBAT ELENA]`.
- **Dovezi:** 10 participanți NeuroCreator care creează zilnic cu Nevo și 6 afaceri vorbitoare de română care l-au integrat. Confirmate. Rămân fără nume.
- **Brand book:** primit (Nevo Brand book noua identitate, noiembrie 2026). Regulile se aplică în `blueprint-video-nevo.md`.
- **Încă deschis:** acordul afacerilor pentru reelul de dovadă publică, cuvântul-cheie al campaniei, numele public al ofertei de agenți.
