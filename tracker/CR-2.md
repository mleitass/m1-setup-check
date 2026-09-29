---
id: CR-2
type: change-request
title: "Atbildes kanāla pārbaude OMD reģistrā"
status: READY
priority: high
reporter: "Juridiskā nodaļa (izdomāts)"
owner: "@<github-lietotājvārds>"
contract: "docs/openapi.yaml · POST /submissions (replyChannel, reasonCode) · OMD GET /v1/mailbox/{personalCode}"
depends_on: [CR-1]
exported: "2026-09-30 · Ezermalas pieteikumu sistēma (simulācija)"
data_check: "Nav personas datu. Personas kodi ir OMD imitācijas testa kodi."
---

# CR-2 · Atbildes kanāla pārbaude OMD reģistrā

> Noteikumi vienkāršoti mācību vajadzībām. OMD (Official Mailbox Directory) ir izdomāts reģistrs.

## Apraksts (description)

Dažreiz atbildes tiek sūtītas pa e-pastu cilvēkiem, kuriem ir aktivizēta oficiālā e-adrese. Pēc iesnieguma saņemšanas sistēmai jāpārbauda atbildes kanāls OMD reģistrā. Ja reģistrs neatbild, sistēma nedrīkst minēt: lēmums par kanālu jāatliek.

## Pieņemšanas kritēriji (acceptance criteria)

| # | OMD atbilde | Sagaidāmais rezultāts |
|---|---|---|
| 1 | 200 `ACTIVE` | `replyChannel` = `E_ADDRESS`, neatkarīgi no iesniedzēja izvēles |
| 2 | 200 `NOT_ACTIVATED` | `replyChannel` = iesniedzēja `preferredChannel`. Ja iesniedzējs izvēlējās `E_ADDRESS`, bet e-adreses nav: `EMAIL`, `reasonCode` = `E_ADDRESS_NOT_ACTIVE` |
| 3 | 404 | Tāpat kā `NOT_ACTIVATED`. Līgumā tas ir aprakstīts |
| 4 | 5xx, noildze virs 3 s, bojāta atbilde vai nedokumentēts statuss | `replyChannel` = `PENDING_CHANNEL_CHECK`, `reasonCode` = `REGISTER_UNAVAILABLE`. Iesniegums tiek pieņemts (201). Iesniedzējs nekad nesaņem 500 OMD dēļ |
| 5 | Jebkurš ne-veiksmīgs iznākums | Žurnālā WARNING ar iesnieguma ID un iemeslu. **Nekad** personas kods vai `body` |
| 6 | OMD piekļuves marķieris (token) | Nolasa no `OMD_API_TOKEN`, nekad no koda |
| 7 | Atbilde uz `POST /submissions` | Pievienoti lauki `replyChannel` un `reasonCode` |

## Precizējumi (clarifications)

| Jautājums | Atbilde | Kas atbildēja, kad |
|---|---|---|
| Vai 404 nozīmē, ka personas nav? | Nē. Tas nozīmē, ka reģistrā nav ieraksta. Rīkojamies kā ar `NOT_ACTIVATED`. | Juridiskā nodaļa, 2026-09-29 |
| Kas notiek ar `PENDING_CHANNEL_CHECK`? | Darbinieks pārbauda kanālu vēlāk. Automātiskā atkārtošana ir ārpus apjoma. | Produkta īpašnieks, 2026-09-29 |

## Ārpus apjoma (out of scope)

- Automātiska atkārtota pārbaude `PENDING_CHANNEL_CHECK` iesniegumiem
- Atbildes nosūtīšana

## Komentāri (comments)

- 2026-09-30 · Analītiķis: "Līguma CR-2 daļa `docs/openapi.yaml` nav pabeigta: nav 5xx un noildzes uzvedības, nav `reasonCode` vērtību saraksta, nav `PENDING_CHANNEL_CHECK`. Skatīt A1."
