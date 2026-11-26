# Verificări web pentru videoul lung al Elenei Andronache (IA, Claude, Nevo)

Data verificării: 26 noiembrie 2026. Scală de încredere: confirmat / parțial / neverificat.
Note de metodă: o parte din site-uri nu s-au putut deschide din sesiune (blocate de rețea): aljazeera.com, axios.com, decrypt.co, airbnb.com, blog.adobe.com, epidemicsound.com. Pentru ele, informația vine din rezumatul căutării web, nu din citirea paginii, și e marcată „parțial" când contează. Paginile oficiale Anthropic (platform.claude.com, claude.com/pricing, code.claude.com, support.claude.com) s-au citit direct.

---

## A. Explicații simple (public larg)

| Afirmație (formulare simplă) | Sursă | Dată | Încredere |
|---|---|---|---|
| Un model de limbaj e antrenat pe cantități uriașe de text și învață tipare: ce cuvânt (sau fragment de cuvânt) urmează, de obicei, după cele de dinainte. Din asta iese un răspuns, bucată cu bucată. | Descrierea e consensul domeniului; legătura „antrenat pe un corpus mare" vs. „context" apare în documentația Anthropic: [Understanding the context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | acces 26.11.2026 (pagină nedatată) | confirmat (nu e pagină care să definească „next token" în cuvinte simple; formularea e a noastră, deliberat simplificată) |
| Modelul poate „greși cu încredere" pentru că procesul de antrenare și testele îl răsplătesc dacă ghicește, nu dacă spune „nu știu". Faptele rare, care nu se pot deduce din tipare (ex. o dată de naștere), sunt cele mai predispuse la greșeli. | OpenAI / Kalai, Nachum, Vempala, Zhang, „Why Language Models Hallucinate" — [openai.com](https://openai.com/index/why-language-models-hallucinate/) și [arXiv 2509.04664](https://arxiv.org/pdf/2509.04664) | septembrie 2025 | confirmat |
| „Contextul" e memoria de lucru a modelului: tot textul pe care îl poate vedea acum, în conversație, plus ce scrie el. E diferit de ce a învățat la antrenare. | Anthropic, [Understanding the context window](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) | acces 26.11.2026 | confirmat |
| Un asistent „știe" despre tine doar ce i-ai dat în context (mesaje, fișiere, instrucțiuni) sau ce îi dă o funcție de memorie/conectori. Mai mult context nu înseamnă automat mai bine: la contexte foarte lungi, precizia poate scădea. | aceeași pagină Anthropic (fenomenul numit „context rot"); planul Free/Pro include „Memory" și conectori: [claude.com/pricing](https://claude.com/pricing) | acces 26.11.2026 | confirmat |
| Chat vs. agent: într-un chat tu întrebi, el răspunde. Un agent primește un scop, alege singur pașii, folosește unelte (fișiere, comenzi, internet) și face sarcina. | Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents): „workflows" rulează pe un drum fix scris de om, „agents" decid singuri procesul. Descrierea Claude Code: „citește codul, editează fișiere, rulează comenzi" — [code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview) | decembrie 2024 (articolul); docs acces 26.11.2026 | confirmat (textul articolului l-am văzut doar în rezumat; doc. Claude Code citit direct) |
| „Agent" în IA = un sistem în care modelul decide singur ce pași face și ce unelte folosește pentru a atinge un scop. | idem | idem | confirmat |

---

## B. Claude (Anthropic)

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Claude e o familie de modele de IA făcute de Anthropic. | [Models overview](https://platform.claude.com/docs/en/models/overview) | acces 26.11.2026 | confirmat |
| Modelele actuale (cele mai noi) sunt 4: Claude Fable 5.2, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5. Familiile se numesc Fable, Opus, Sonnet, Haiku (Haiku = cel mai rapid; Sonnet = viteză + inteligență; Opus = lucru lung, programare, muncă de cunoaștere; Fable = raționament greu și sarcini lungi de agent). | idem | acces 26.11.2026 | confirmat |
| Există și o familie „Mythos" (ex. Mythos 5.2), cu acces limitat, doar pentru organizații verificate. Nu se menționează ca disponibilă publicului. | idem | acces 26.11.2026 | confirmat |
| Pe Claude.ai, planurile sunt: Free ($0), Pro ($17/lună plătit anual, $200 odată, sau $20 lunar), Max ($100/lună), Ultra ($200/lună), Team și Enterprise. | [claude.com/pricing](https://claude.com/pricing) | acces 26.11.2026 | confirmat (în USD) |
| Prețul Pro în euro: pagina nu arată EUR, doar USD. | idem | acces 26.11.2026 | NEVERIFICAT, nu se afirmă în euro. Se poate spune „aproximativ 20 de dolari pe lună" |
| Pro include Claude Code, Opus, Projects, Claude în Chrome. Free nu include Claude Code (Sonnet și Haiku doar). | idem | acces 26.11.2026 | confirmat |
| Tab-ul „Code" din aplicația desktop: după instalare, te autentifici și dai click pe „Code". Aplicația include Claude Code, nu trebuie instalat separat; e nevoie de abonament plătit. | [Claude Code overview](https://code.claude.com/docs/en/overview) | acces 26.11.2026 | confirmat |
| Claude Code = unealtă de programare agentică: citește codul, editează fișiere, rulează comenzi. Merge în terminal, extensii pentru VS Code și JetBrains, aplicația desktop și browser (claude.ai/code, inclusiv din aplicația mobilă iOS/Android). | idem | acces 26.11.2026 | confirmat |
| Aplicația desktop: macOS, Windows (x64 și ARM64), Linux (beta, Ubuntu/Debian). Pe mobil: iOS (pagina de download listează App Store; ghidul Remote Control leagă și aplicația Android). | [claude.com/download](https://claude.com/download) (claude.ai/download redirecționează aici) + [Remote Control docs](https://code.claude.com/docs/en/remote-control) | acces 26.11.2026 | confirmat |
| Remote Control: o sesiune Claude Code rulează pe calculatorul tău, iar de pe telefon (aplicația Claude iOS/Android) sau din claude.ai/code o vezi și o conduci. Fișierele și uneltele rămân pe calculator; calculatorul trebuie să fie pornit și procesul activ. Pornire: `claude remote-control` sau `/remote-control` (și în tab-ul Code din desktop). Se poate scana un cod QR. | [Remote Control docs](https://code.claude.com/docs/en/remote-control) | acces 26.11.2026 | confirmat |
| Remote Control merge cu planurile Pro, Max, Ultra, Team, Enterprise (nu cu chei API). La Team/Enterprise trebuie activat de un administrator. | idem | acces 26.11.2026 | confirmat (în 2026 apăreau rapoarte vechi că Pro nu avea acces; documentația actuală include Pro) |
| Claude e disponibil în România și Republica Moldova (ambele apar pe lista țărilor suportate). | [Where can I access Claude? (support.claude.com)](https://support.claude.com/en/articles/8461763-supported-countries) | pagina: 16 martie 2026 | confirmat |
| Limite de utilizare (planuri plătite): o limită de sesiune care se resetează la 5 ore și limite săptămânale. Folosirea din claude.ai, Claude Code și Desktop se adună în aceeași limită. Depinde de lungimea conversației, de model și de efort. Anthropic poate ajusta limitele. | [How do usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) | pagină fără dată (marcată „actualizată acum 3 săptămâni") | confirmat |
| Numărul exact de mesaje pe Pro: pagina nu îl dă. | idem | idem | NEVERIFICAT, nu se afirmă un număr |
| Instalare: descarcă aplicația de pe claude.ai/download (redirecționează la claude.com/download), te autentifici, apeși „Code". | [claude.com/download](https://claude.com/download), [overview](https://code.claude.com/docs/en/overview) | acces 26.11.2026 | confirmat |

---

## C. ChatGPT și Codex (o frază neutră)

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| ChatGPT e asistentul conversațional de IA făcut de OpenAI. | [OpenAI](https://openai.com/codex) (context general) | — | confirmat |
| Codex e agentul de programare al OpenAI: lansat în mai 2025 ca agent în cloud în ChatGPT, acum are aplicație desktop (macOS, Windows din 4 martie 2026), CLI, extensie pentru editor și, din 16 aprilie 2026, poate opera alte aplicații pe calculator. | [TechCrunch, 16 mai 2025](https://www.techcrunch.com/2025/05/16/openai-launches-codex-an-ai-coding-agent-in-chatgpt); [OpenAI Help: Codex with your ChatGPT plan](https://help.openai.com/articles/11369540); [OpenAI, Codex for almost everything](https://openai.com/blog/codex-for-almost-everything) | 2025–2026 | confirmat (din rezumatul căutării) |
| Formulare neutră pentru video: „ChatGPT e asistentul OpenAI; Codex e agentul lor care scrie și rulează cod, echivalentul pentru programare al lui Claude Code." | — | — | formulare propusă |

---

## D. Anthropic și bursa

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Anthropic a avut IPO pe Nasdaq, cu tickerul ANT. Ofertă: 980 de milioane de acțiuni la $83, adică aproximativ 81,3 miliarde de dolari. Tranzacționarea a început joi, 19 noiembrie 2026. | [Al Jazeera](https://aljazeera.com/economy/2026/11/19/anthropic-raises-81-3bn-in-biggest-ipo-of-all-time); [CTV](https://www.ctvnews.ca/business/article/anthropic-clinches-biggest-ipo-ever-with-us81-billion-offering/); [Axios](https://axios.com/2026/11/19/anthropic-ipo-claude-crush); [Decrypt](https://decrypt.co/383623/anthropic-tops-spacex-initial-ipo-81-billion-deal-where-the-money-went); [NPR/KUOW, 18 noiembrie](https://www.kuow.org/npr-news/2026-11-18/anthropic-ipo-raises-record-81-3-billion-on-strong-ai-demand) | 18–19 nov. 2026 | confirmat (mai multe surse independente; paginile nu s-au putut deschide, cifrele vin din rezumate de căutare, concordante) |
| Deci „81 de miliarde de dolari" spusă de Elena pe 19 noiembrie e corectă ca ordin de mărime (81,3 mld). | idem | idem | confirmat |
| Atenție 1: nu toți banii merg la companie. Decrypt: aproximativ 79,4 mld $ sunt acțiuni noi (înainte de comisioane); restul vine din acțiuni vândute de acționari existenți. | [Decrypt](https://decrypt.co/383623/anthropic-tops-spacex-initial-ipo-81-billion-deal-where-the-money-went) | 19 nov. 2026 | parțial (o singură sursă pentru defalcare) |
| Atenție 2: „cel mai mare IPO din istorie" e raportat de multe surse (depășește oferta inițială SpaceX din iunie, 75 mld $), dar Decrypt notează că SpaceX a ajuns la 86,25 mld $ cu acțiunile suplimentare. Deci formularea „record" e disputată. | idem + [Al Jazeera](https://aljazeera.com/economy/2026/11/19/anthropic-raises-81-3bn-in-biggest-ipo-of-all-time) | 19 nov. 2026 | parțial. Nu se afirmă „cel mai mare din istorie" |
| Evaluarea: aproximativ 1,5 trilioane $ la prețul ofertei; după prima zi, surse diferite dau cifre diferite (1,75 – 2,1 trilioane $). | surse mixte (Devdiscourse, BusinessDay, Turkiye Today) | 19 nov. 2026 | parțial. Nu se afirmă o evaluare exactă |
| Prima zi: deschidere $111,50, închidere $97,17 (+17,1% față de $83). Un titlu Forbes Australia spune „$145", dar textul lor dă $97,17, deci titlul e probabil greșit. | [TechRepublic](https://www.techrepublic.com/article/news-anthropic-ipo-nasdaq-trading-debut/), [Forbes AU](https://www.forbes.com.au/news/innovation/anthropic-ipo-live-shares-close-first-day-up-more-than-17-percent/) | 19 nov. 2026 | parțial. Nu e nevoie în video |
| Plasament privat separat de 26 mld $, total ~107,3 mld $. | [Al Jazeera](https://aljazeera.com/economy/2026/11/19/anthropic-raises-81-3bn-in-biggest-ipo-of-all-time), [Decrypt](https://decrypt.co/383623/anthropic-tops-spacex-initial-ipo-81-billion-deal-where-the-money-went) | 19 nov. 2026 | parțial |

---

## E. Povești VOC (a asculta oamenii și a le da ce cer)

### E1. Airbnb, pozele profesionale

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Fondatorii Airbnb au mers în New York, au văzut că anunțurile aveau poze slabe și au făcut ei înșiși poze mai bune, cu un aparat închiriat. Sfatul de a face lucruri care nu se scalează (să fie lângă gazde) vine de la Paul Graham (Y Combinator). | Paul Graham, [Do Things That Don't Scale](https://paulgraham.com/ds.htm); Joe Gebbia în [Y Combinator](https://www.ycombinator.com/blog/scaling-product-airbnb) și [First Round Review](https://review.firstround.com/How-design-thinking-transformed-Airbnb-from-failing-startup-to-billion-dollar-business) | iulie 2013 (eseul) | confirmat în esență (am văzut rezumate, nu textele integrale) |
| Gebbia a povestit că au analizat în jur de 40 de anunțuri din New York și pozele erau punctul slab. | First Round Review (din rezumat) | — | parțial |
| „Veniturile / rezervările au dublat după poze": apare doar în surse secundare (bloguri, un furnizor de fotografie, Quartr). Nu am găsit sursă primară. Cifra „200 $ pe săptămână" nu apare în niciuna din sursele găsite. | [Quartr](https://quartr.com/insights/edge/airbnb-the-hospitality-giant-without-property), [Snappr](https://www.snappr.com/enterprise-blog/photography-that-launched-an-empire-how-airbnb-transformed-their-business-with-professional-photography) | — | NEVERIFICAT, nu se afirmă „au dublat" ca fapt. Se poate spune „povestea spune că rezervările au crescut vizibil" |
| Date oficiale actuale: anunțurile care au folosit fotografia profesională Airbnb au avut în medie +19% rezervări net în următoarele 365 de zile, față de cele fără (14.700+ anunțuri, 2024–2025; Airbnb avertizează că nu e garantat). | [Airbnb Pro Photo Program](https://www.airbnb.com/professional_photography) | 2024–2025 | parțial (sursa primară, dar citată din rezumat; e cifră a firmei, nu a unui studiu independent) |
| „Airbnb a spus «hai să ascultăm gazdele»": nu e povestea. Povestea documentată e că ei au observat (date + conversație cu gazde) și au acționat direct. Nu se spune că gazdele „au cerut" poze profesionale. | — | — | NU se atribuie „au cerut gazdele" |

### E2. Alte două exemple internationale

**Domino's (SUA), „Pizza Turnaround", 2009–2010**

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Domino's a primit feedback foarte dur despre gustul pizzei, a reformulat rețeta și a făcut o campanie în care angajați citeau recenzii negative. | [Inc.](https://www.inc.com/jeff-haden/10-years-ago-cardboard-pizza-almost-killed-dominos-then-dominos-did-something-brilliant.html); [HeraldNet/AP](https://www.heraldnet.com/business/dominos-ad-campaign-admits-its-old-pizza-was-pretty-bad); [Cornell Alumni](https://alumni.cornell.edu/cornellians/weiner-dominos) | dec. 2009 – ian. 2010 | confirmat |
| Vânzările comparabile din SUA au crescut cu 14,3% în trimestrul 1 din 2010 (comunicatul de rezultate al companiei). | [RetailWire](https://retailwire.com/discussion/honesty-and-new-recipe-pays-off-for-dominos/), [Entrepreneur](https://www.entrepreneur.com/article/218649) | 6 mai 2010 | parțial (cifra vine din rezumat; de verificat în comunicatul oficial înainte de a o rosti) |
| Surse diferă asupra datei lansării campaniei (decembrie 2009 vs. ianuarie 2010) și asupra câștigului la bursă. | idem | — | Nu se spune data exactă și nu se spun cifre de bursă |

**LEGO Ideas**

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Pe platforma LEGO Ideas fanii propun seturi; o idee care strânge 10.000 de susținători intră în evaluare (de trei ori pe an) la un comitet LEGO. Decizia finală e a LEGO; multe idei cu 10.000 de voturi au fost respinse. | [LEGO, ce se întâmplă după 10.000 de susținători](https://www.lego.com/en-be/service/help-topics/article/what-happens-to-my-product-idea-after-i-reach-10-000-supporters); [Wikipedia](https://www.wikipedia.org/wiki/Lego_Ideas) | pagini LEGO, acces 26.11.2026 | confirmat |
| „LEGO produce tot ce votează fanii": fals. Nu se spune. | idem | — | NU se afirmă |

### E3. Două exemple din România / Republica Moldova

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| România: nu am găsit un caz documentat solid în care o firmă a schimbat un produs după ce a ascultat clienții. Candidați găsiți (BOON detergent, DRIPLY, Carpathian Jerky) sunt interviuri de promovare, cu declarații generale „feedback-ul clienților e prețios". Freshful: cifre despre clienți, fără schimbare concretă legată de feedback. | [BOON, Revista Biz](https://www.revistabiz.ro/secretele-strategiei-boon-detergentul-100-romanesc-testat-in-germania-pret-accesibil-calitate-si-comunitate-loiala-de-clienti/); [DRIPLY, Zile și Nopți](https://zilesinopti.ro/2026/09/16/driply-brand-romanesc-povesti-de-succes/); [Freshful, retail-fmcg.ro](https://www.retail-fmcg.ro/e-commerce-2/freshful-implineste-5-ani.html) | 2022–2026 | NEVERIFICAT, nu se afirmă niciun caz românesc. Doar DRIPLY (zeci de discuții cu clienți înainte de lansare, conform articolului) merită citit integral dacă Elena vrea un exemplu |
| Republica Moldova: nu am găsit o poveste documentată. Apare doar că maib ține întâlniri directe cu clienții (brunchuri, sesiuni), fără un produs concret lansat din ele. | [Wall-Street.ro, CX Moldova](https://www.wall-street.ro/articol/management/cx-urca-in-topul-prioritatilor-in-regiune.html) | — | NEVERIFICAT, nu se afirmă |
| Recomandare: pentru exemplele locale, cel mai sigur e unul din propriul parcurs al Elenei/NeuroLab (poveste trăită, nu de verificat pe web), sau un interviu direct cu o firmă locală. | — | — | — |

---

## F. IA și creatorii de conținut (cifre solide)

| Afirmație | Sursă | Dată | Încredere |
|---|---|---|---|
| Adobe (sondaj Creators' Toolkit, 16.000+ creatori din 8 țări): 87% dintre creatorii care folosesc IA spun că i-a ajutat să-și crească afacerea sau audiența; 75% spun că IA e integrată sau esențială în munca lor. | [eWeek](https://eweek.com/news/adobe-creator-ai-report-trust-control-neuron/); [9to5Mac, 16 iun. 2026](https://9to5mac.com/2026/06/16/adobe-survey-ai-is-helping-creators-grow-but-not-without-tradeoffs/); [YourStory](https://yourstory.com/ai-story/ai-for-creators-adobe-2026-report) | iunie 2026 | parțial (sondaj făcut de un vânzător de unelte creative, autoraportat; sursele diferă ca perioadă de culegere) |
| Adobe, sondaj SUA (2.000+ creatori): 78% dintre cei care folosesc IA spun că accelerează creșterea. | [Adobe blog, 9 nov. 2026](https://blog.adobe.com/en/publish/2026/11/09/from-big-ideas-bigger-opportunities-creators-say-creative-ai-accelerating-growth) (doar titlul, pagina blocată) | 9 nov. 2026 | parțial. Nu se amestecă cu cifra de 87% |
| Epidemic Sound (3.000 creatori, Marea Britanie și SUA): 94% folosesc deja unelte de IA; 89% simt presiune să le adopte ca să rămână competitivi. | [Epidemic Sound, Future Creator Economy Report 2026](https://epidemicsound.com/data-trends/sound-of-creativity-reports/future-creator-economy-report-2026) | 2026 | parțial (rezumat de căutare; raport al unei companii cu interes comercial) |
| CreatorIQ + Influencers.club: 72% dintre creatori folosesc IA pentru idei, scris sau editare. | [MarketingProfs](https://www.marketingprofs.com/charts/2026/54489/the-creator-landscape-in-2026-content-monetization-and-ai-trends) (via rezumat) | 2026 | parțial |
| Concluzie sigură: sondajele din 2026 concordă că IA e folosită de marea majoritate a creatorilor (între ~70% și ~95%, în funcție de definiție și de eșantion). Cifrele nu sunt comparabile între ele. | idem | 2026 | confirmat ca direcție, parțial ca număr exact |
| Nu am găsit studii independente, evaluate de experți, care să măsoare timpul economisit sau veniturile câștigate de creatori datorită IA. | — | — | NEVERIFICAT, nu se afirmă „economisești X ore" |

---

## Ce se poate spune în video, în vorbirea Elenei

1. „Un model de limbaj a citit cantități uriașe de text și a învățat tipare. Când îi scrii, el continuă textul într-un mod care se potrivește cu tiparele acelea."
2. „De aceea poate greși cu încredere: pentru el, să ghicească e mai bine decât să spună «nu știu». Cu cât un fapt e mai rar, cu atât crește riscul."
3. „Contextul e memoria lui de lucru: tot ce vede acum, în conversație. Ce nu i-ai dat, nu știe despre tine."
4. „Într-un chat, tu întrebi și el răspunde. Un agent primește un scop, își alege pașii, folosește unelte și execută sarcina."
5. „Claude e IA făcută de Anthropic. Familiile se numesc Fable, Opus, Sonnet și Haiku."
6. „Abonamentul Pro costă aproximativ 20 de dolari pe lună și include Claude Code." (Dacă plătești anual, 17 dolari pe lună.)
7. „În aplicația Claude de pe calculator ai un tab numit Code. Acolo lucrează Claude ca agent."
8. „Cu Remote Control, o sesiune care rulează pe calculatorul meu o pot conduce de pe telefon. Calculatorul trebuie să rămână pornit."
9. „Claude e disponibil în România și în Republica Moldova."
10. „Limitele de utilizare se resetează la 5 ore și există și o limită pe săptămână. Nu există un număr fix de mesaje promis."
11. „ChatGPT e asistentul făcut de OpenAI. Codex e agentul lor pentru cod."
12. „Pe 19 noiembrie, Anthropic a intrat pe bursă, la Nasdaq, și a strâns aproximativ 81 de miliarde de dolari în IPO." (Cifra e solidă; nu se adaugă „cel mai mare din istorie".)
13. „Airbnb: fondatorii au văzut că pozele anunțurilor din New York erau slabe, au mers acolo și le-au făcut ei înșiși. Airbnb spune azi că anunțurile cu fotografie profesională au în medie cu 19% mai multe rezervări." (Cifra e a Airbnb, nu a unui studiu independent.)
14. „Domino's a luat în serios critici dure despre gustul pizzei, și-a schimbat rețeta și a spus public asta. Au crescut vânzările."
15. „La LEGO Ideas, fanii propun seturi; la 10.000 de susținători, ideea e evaluată de LEGO, iar LEGO decide."
16. „Sondajele din 2026 arată că majoritatea creatorilor folosesc deja IA. Cifrele diferă de la un studiu la altul, de la aproximativ 70% la peste 90%."

## Ce NU se spune

- Prețul Pro „în euro" (pagina oficială arată doar dolari).
- „Cel mai mare IPO din istorie" (disputat: SpaceX a ajuns la 86,25 mld $ cu acțiunile suplimentare), o evaluare exactă a Anthropic sau prețul acțiunii după prima zi.
- „Anthropic a primit 81 de miliarde" ca sumă către companie: o parte merge la acționarii existenți.
- Un număr de mesaje pe Pro (nu e publicat), sau „nelimitat".
- „Airbnb și-a dublat veniturile după poze" sau „de la 200 la 400 de dolari pe săptămână" (nu am sursă primară). Nici „gazdele au cerut poze".
- „Domino's a crescut cu X% la bursă" sau data exactă a campaniei.
- „LEGO produce ce votează fanii."
- Orice exemplu românesc sau moldovenesc „documentat": nu am găsit unul solid.
- „IA te face să economisești X ore" sau „creatorii câștigă X% mai mult" (fără studii independente). Nu se amestecă cifrele Adobe (87%, 78%) între ele, și nu se prezintă ca fapt științific; sunt sondaje ale firmelor.
- Că Remote Control e „doar pentru Max" (documentația actuală include Pro).
- Modelele „Mythos" ca disponibile publicului.
