---
id: CR-3
type: change-request
title: "Iesniegumu saraksts darbiniekam ar filtriem"
status: IN_REVIEW
priority: medium
reporter: "Reģistrācijas nodaļa (izdomāts)"
owner: "@vendor-team"
contract: "docs/openapi.yaml · GET /submissions?status=&topic="
depends_on: [CR-0]
exported: "2026-10-05 · Ezermalas pieteikumu sistēma (simulācija)"
data_check: "Nav personas datu, iekšējo adrešu vai pielikumu"
---

# CR-3 · Iesniegumu saraksts darbiniekam ar filtriem

> Noteikumi vienkāršoti mācību vajadzībām. Izmaiņu izstrādāja piegādātājs, un tā ir pārskatīšanā.

## Apraksts (description)

Darbiniekam vajag iesniegumu sarakstu, ko var filtrēt pēc statusa un tēmas. Šobrīd darbinieks meklē iesniegumus pa vienam pēc ID.

## Pieņemšanas kritēriji (acceptance criteria)

| # | Ievade | Sagaidāmais rezultāts |
|---|---|---|
| 1 | `GET /submissions?status=RECEIVED` | 200, tikai `RECEIVED` iesniegumi |
| 2 | `GET /submissions?topic=ROADS` | 200, tikai tēma `ROADS` |
| 3 | Abi filtri kopā | 200, abi nosacījumi izpildās vienlaikus |
| 4 | `GET /submissions?status=DONE` (nezināms statuss) | 400 `VALIDATION_ERROR`, lauks `status` |
| 5 | Jebkurš saraksts | Katram ierakstam: `id`, `status`, `topic`, `receivedAt`, `dueDate`, `replyChannel` |

## Precizējumi (clarifications)

| Jautājums | Atbilde | Kas atbildēja, kad |
|---|---|---|
| Vai sarakstā rādīt `fullName` un `body`? | **Atvērts.** Jālemj datu aizsardzības speciālistam. | — |

## Ārpus apjoma (out of scope)

- Autentifikācija un lomas. **Prototipā to nav. Ražošanas vidē tās ir obligātas.**
- Lapošana (pagination)

## Komentāri (comments)

- 2026-10-02 · Piegādātājs: "Izstrādāts un notestēts. Lūdzu, apstipriniet PR."
