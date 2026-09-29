---
id: CR-0
type: change-request
title: "Tēma 'Parki un skvēri' un tēmu saraksts"
status: READY
priority: low
reporter: "Klientu apkalpošanas centrs (izdomāts)"
owner: "@<github-lietotājvārds>"
contract: "docs/openapi.yaml · GET /topics, POST /submissions (topic)"
depends_on: []
exported: "2026-10-05 · Ezermalas pieteikumu sistēma (simulācija)"
data_check: "Nav personas datu, iekšējo adrešu vai pielikumu"
---

# CR-0 · Tēma "Parki un skvēri" un tēmu saraksts

> Noteikumi vienkāršoti mācību vajadzībām.

## Apraksts (description)

Iedzīvotāji bieži raksta par parkiem, bet šādas tēmas nav, tāpēc iesniegumi nonāk tēmā "Cits". Jāpievieno tēma "Parki un skvēri". E-pakalpojumam vajag tēmu sarakstu no API, lai to nevajadzētu uzturēt divās vietās.

## Pieņemšanas kritēriji (acceptance criteria)

| # | Ievade | Sagaidāmais rezultāts |
|---|---|---|
| 1 | `GET /topics` | 200, saraksts: `ROADS` "Ceļi un ielas", `WASTE` "Atkritumi", `PLANNING` "Teritorijas plānošana", `PARKS` "Parki un skvēri", `OTHER` "Cits" |
| 2 | `POST /submissions` ar `topic` = `PARKS` | 201 |
| 3 | `POST /submissions` ar `topic` = `ZOO` | 400 `VALIDATION_ERROR`, lauks `topic` |
| 4 | Esošās tēmas | Kodi un nosaukumi nemainās |

## Precizējumi (clarifications)

| Jautājums | Atbilde | Kas atbildēja, kad |
|---|---|---|
| Vai `OTHER` paliek saraksta beigās? | Jā | Produkta īpašnieks, 2026-10-01 |

## Ārpus apjoma (out of scope)

- Tēmu pārvaldība (pievienošana bez koda izmaiņām)
- Tēmu tulkojumi citās valodās

## Komentāri (comments)

- 2026-09-29 · Klientu apkalpošanas centrs: "Septembrī 40 iesniegumi par parkiem nonāca tēmā 'Cits'."
