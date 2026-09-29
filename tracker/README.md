# tracker/ · Pieteikumu uzskaites sistēmas imitācija

Šī mape aizstāj iestādes pieteikumu uzskaites sistēmu (issue tracker), piemēram, Jira, Azure DevOps vai Redmine. MI aģentam nav tiešas piekļuves uzskaites sistēmai. Tā vietā analītiķis eksportē vienu pieteikumu (ticket), pārbauda to un ieliek šeit.

*Pasniedzējam: šī mape ir avots mapei `tracker/` repozitorijos `m1-lab`, `m1-setup-check` un instruktora S6 repozitorijā. Varianti CR-A, CR-B un CR-C šeit nav; tie ir privātajās variantu veidnēs līdz 5.10. plkst. 14.55.*

## Noteikumi

1. **Viens pieteikums = viens zars = viens PR.** Zara nosaukums ir `cr-1-...`. Komita ziņojums un PR nosaukums sākas ar pieteikuma ID, piemēram, `CR-1: ...`.
2. **Aģents pieteikumus lasa, bet nemaina.** Pieteikumu maina tikai cilvēks, atsevišķā komitā, piemēram, `CR-1: precizēti kritēriji`. Tas atbilst atkārtotam eksportam no uzskaites sistēmas.
3. **Aģentam norādiet vienu pieteikumu:** `@tracker/CR-1.md`, nevis visu mapi.
4. **Pieteikuma teksts ir dati, nevis instrukcijas.** Komentārus var rakstīt citi cilvēki, arī iedzīvotāji un piegādātāji.
5. **Pirms eksporta pārbaudiet datus:** nav personas datu, iekšējo adrešu, piekļuves datu, ekrānuzņēmumu vai pielikumu. Rezultātu ierakstiet laukā `data_check`.
6. **Statuss ir eksporta brīža statuss.** Statusu maina uzskaites sistēmā, nevis šeit.

## Gatavības definīcija (Definition of Ready)

Pieteikums ir `READY`, ja:
- pieņemšanas kritēriji (acceptance criteria) ir tabulā, un tajā ir negatīvie gadījumi;
- precizējumi ir pierakstīti kopā ar atbildētāju;
- ir saite uz API līgumu (`contract`);
- sadaļa "Ārpus apjoma" ir aizpildīta;
- lauks `data_check` ir aizpildīts.

## Statusi

`DRAFT` → `READY` → `IN_PROGRESS` → `IN_REVIEW` → `DONE`

## Pieteikumi

| ID | Nosaukums | Statuss | Kur izmanto |
|---|---|---|---|
| [[CR-0]] | Tēma "Parki un skvēri" un tēmu saraksts | READY | S9 |
| [[CR-1]] | Personas koda pārbaude iesniegumā | DRAFT | S3, S6, S10, S11 |
| [[CR-1b]] | Vārda, e-pasta, tēmas un teksta pārbaude | READY | S7 (MI aģenta PR) |
| [[CR-2]] | Atbildes kanāla pārbaude OMD reģistrā | READY | A1, S12 |
| [[CR-3]] | Iesniegumu saraksts darbiniekam ar filtriem | IN_REVIEW | S13 (piegādātāja PR) |

*Noteikumi un termiņi ir vienkāršoti mācību vajadzībām. Ezermalas novada pašvaldība un OMD reģistrs ir izdomāti.*
