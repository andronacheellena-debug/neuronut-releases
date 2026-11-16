# Cum iese o versiune nouă de Nevo

## Ordinea (nu se sare niciun pas)
1. **Textul întâi.** Orice schimbare pe care omul o vede în chat (update, licență, mesaje, erori): Claude îi arată Elenei textul exact, înainte de cod. Elena aprobă.
2. **Codul + controlul de mai jos.**
3. **Beta.** Se urcă `neuronut-motor-beta.zip` + `versiune-beta.json`. O primesc doar testerii cu „canal beta” (Elena, Andrei).
4. **Testul real.** Testerii scriu „start” → „da” în Claude Code, pe calculatorul lor (Mac și Windows), cu modelul obișnuit (Sonnet), și trimit poze cu ce a scris Nevo.
5. **„Da” de la Elena** după poze → același zip devine `neuronut-motor.zip` + `versiune.json` (canalul tuturor).

## Controlul la fiecare versiune
- [ ] Nevo nu citește fișiere care nu sunt ale lui (nici fișierele aplicației Claude, nici altceva de pe calculator în afara folderului).
- [ ] Niciun text pentru om nu descrie pași tehnici (scripturi, arhive, rețea, permisiuni) și niciunul nu sună ca și cum omul ar fi apărat de NeuroLab.
- [ ] Nicio comandă de lipit nu cere „fără să mă întrebi”, nu are coduri ascunse, token-uri sau descărcări ciudate.
- [ ] Mesajele de eroare spun ce urmează, nu ce s-a blocat.
- [ ] Testat local: update de la versiunea precedentă, licență (cumpărător / tester / necunoscut), Fundamentul neatins.
- [ ] Testat în Claude Code, nu doar în scripturi.
