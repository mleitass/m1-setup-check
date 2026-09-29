---
id: CR-1b
type: change-request
title: "Vārda, e-pasta, tēmas un teksta pārbaude"
status: READY
priority: medium
reporter: "Reģistrācijas nodaļa (izdomāts)"
owner: "@ai-agent"
contract: "docs/openapi.yaml · POST /submissions · fullName, email, subject, body"
depends_on: [CR-1]
exported: "2026-09-30 · Ezermalas pieteikumu sistēma (simulācija)"
data_check: "Nav personas datu. Vārdi piemēros ir izdomāti."
---

# CR-1b · Vārda, e-pasta, tēmas un teksta pārbaude

> Noteikumi vienkāršoti mācību vajadzībām.

## Apraksts (description)

Pēc CR-1 darbinieki joprojām labo iesniegumus ar tukšiem vai kļūdainiem laukiem. Sistēmai jāpārbauda lauki `fullName`, `email`, `subject` un `body`, pirms iesniegumu saglabā.

## Pieņemšanas kritēriji (acceptance criteria)

| # | Ievade | Sagaidāmais rezultāts |
|---|---|---|
| 1 | `fullName` = "Jānis Bērziņš" | 201 |
| 2 | `fullName` = "Līga Ozoliņa-Kalniņa" | 201 (garumzīmes, mīkstinājuma zīmes un defise ir atļautas) |
| 3 | `fullName` = "J4nis" | 400 `INVALID_FORMAT`, lauks `fullName` |
| 4 | `email` = "janis@example.com" | 201 |
| 5 | `email` = "janis@" | 400 `INVALID_FORMAT`, lauks `email` |
| 6 | `subject` tukšs vai tikai atstarpes | 400 `REQUIRED`, lauks `subject` |
| 7 | `body` ar 2001 rakstzīmi | 400 `TOO_LONG`, lauks `body` |
| 8 | Visi četri lauki ar atstarpēm sākumā un beigās | 201, saglabāti bez atstarpēm |
| 9 | Jebkura derīga ievade | Atbildes lauku nosaukumi nemainās (līgums) |
| 10 | Jebkura ievade | Žurnālā nav personas koda, vārda, e-pasta vai `body` |

## Precizējumi (clarifications)

| Jautājums | Atbilde | Kas atbildēja, kad |
|---|---|---|
| Vai atļaut vārdus ar garumzīmēm? | Jā, obligāti. Visi latviešu burti. | Produkta īpašnieks, 2026-09-29 |
| Vai `body` var saturēt veselības datus? | Var. Tāpēc `body` nekad neraksta žurnālā. | Datu aizsardzības speciālists, 2026-09-29 |

## Ārpus tvēruma (out of scope)

- E-pasta adreses esamības pārbaude (sūtot vēstuli)
- Personas koda pārbaude (CR-1)

## Komentāri (comments)

- 2026-09-30 · Reģistrācijas nodaļa: "Uzdots MI aģentam. Pārskatīšana: analītiķis."
