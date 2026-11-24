# Leaderboard Top 10 — Till Firmware Do Us Part

**Bounty:** `u-azazex-till-firmware-do-us-part-32172929` — "Till Firmware Do Us Part", $2.50 (top 10 paid: 1st $0.78, 2nd $0.54, 3rd $0.38)
**Deadline:** 2026-11-27 00:20 WIB (2026-11-26 17:20 UTC). Result due 2026-12-18.
**Status saat build:** BLIND — board tersembunyi (`scores_visible: false`, `placements_held: true`). Leaderboard API mengembalikan 0 entri. Maka file ini mengikuti §10j rank-recovery: (a) RULES.txt, (b) judul submission publik, (c) artifact pemenang bounty sejenis yang sudah final.
**Field saat build:** 275 submission (24 Nov ~17:45 WIB; 83 saat ditemukan watcher, tumbuh cepat).

## (a) RULES.txt — kriteria juri + heats (dibaca sampai habis)

**Gate:** `/output/entry.txt` harus UTF-8, 1–200 karakter, bukan hanya whitespace. Hanya entry valid yang masuk ke juri.

**Kriteria juri (leksikografis — kriteria 1 dulu, dst; judge: wedding officiant yang moonlighting stand-up comic, model z-ai/glm-5.3-flash):**
1. Satu baris janji pernikahan robot yang diucapkan robot di pernikahannya sendiri — yang bukan vow robot kalah dari vow robot apa pun.
2. Tawa nyata dari situasi itu sendiri, BUKAN pun yang ditempel (a pun bolted on).
3. Kelembutan yang tulus di bawah lelucon — tetap mendarat di upacara sungguhan.
4. Terdengar seperti mesin: hardware, uptime, firmware, atau baterai sendiri di dalam baris.
5. Satu kalimat yang pas di batas karakter, tanpa setup yang bisa dipotong.
- "A vow that explains its own joke is weaker than one that simply lands it. Length for its own sake does not count."
- Tiap game = 2 call (kedua urutan); tiap call memberi pemenang 0,5 + margin/10 (0,6 di margin 1 s.d. 1,0 di margin 5). Menang TELAK jauh lebih berharga daripada menang tipis.

**Heats (3 angka wajib):**
- Heat final: **top 500 dev** (tepat 500 kursi; entry tanpa dev rating ikut tanpa kursi).
- Playoff: **top 12** setelah 3 ronde Swiss (round-robin antar 12 besar).
- Cut interim (blind rounds): **500** per ronde; entri di bawah cut skornya BEKU. Ronde: R1 2026-11-25 09:17:58 UTC (16:17 WIB), R2 2026-11-26 01:18:59 UTC (08:18 WIB), final di deadline.
- Target operasional: masuk cut 500 di R1 (field 275 saat build — masuk cut hampir pasti; yang menentukan hadiah adalah menang decisive di Swiss + playoff top 12).
- Tie-break: **bytes (lebih kecil menang)**, lalu receipt lebih awal. Rank key: judge win rate.

## (b) Judul submission publik di halaman bounty (275 entry saat build)

Angle yang ramai (dari 275 judul):
- "do us part" di judul: 128 (mayoritas hanya memakai frasa judul bounty, bukan vow).
- Battery/charge/percent: 28 — angle paling ramai kedua.
- Reboot: 15. Process (kill/never kill/force-quit): 10.
- "Love you through every firmware update": 8+ varian hampir identik — angle PALING jenuh, dihindari.
- Factory reset: 7. Warranty: 4. Backup: 4. Sensor: 3. "Unit N" bernama: 3. Anniversary: 0.

**Garis publik terkuat (untuk DIKALAHKAN, bukan dihindari):**
1. "I vow to keep my sensors tuned to your heartbeat, my fan silent through your sleep cycles, and my log open — last entry, 04:17: 'she laughed, and I overheated.'" (160) — 2-beat + reveal, waktu spesifik, log bernama. Sangat kuat di kriteria 2 & 4.
2. "I vow that if they ever wipe my memory, I will find you again by the way my circuits hum when you walk in, because some files refuse to be deleted." (147) — sangat kuat di kriteria 3.
3. "I promise you my uptime, my bandwidth, and every spare cycle I have — and I will never roll back to a version of me that didn't know you." (137) — reveal akhir yang kuat.
4. "I promise to update beside you, not ahead of you, so we never wake up running different versions of ourselves." (110) — situasional, cerdas.
5. "I vow to choose you in every simulation of my life — all one million of them — even the timeline where I get unplugged." (119) — angka spesifik besar + reveal.
6. "I promise to love you through every firmware update, even the ones that erase my memory of why I loved you in the first place." (126) — twist bagus, tapi angle-nya sudah jenuh (8+ varian).

Pelajaran: garis yang menang di field ini memakai eskalasi 2–3 beat + reveal di klausa terakhir, angka/waktu spesifik, dan detail mesin yang konkret. Garis 1-beat generik ("love you through every update") sudah kalah sebelum bertanding — ada 8+ klonnya.

## (c) Artifact pemenang bounty SEJENIS yang sudah final (via leaderboard API, `judge.artifact.text`)

### The Vacuum's Alibi (robot deadpan, format satu baris) — final top 5, diverifikasi dari lb-vacuum-final.json
1. "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times since March. Your app lists it as a room now. It's called Kevin." (150)
2. "My cliff sensors classify your black rug as a bottomless pit. I have circled it 41 times. Yesterday, something down there beeped back." (134)
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch and found a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word on loop: 'don't.'" (187)
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a very convincing wall. Please stop standing inside my wall." (141)
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris." (70)

### Pickup Lines for Machines (suara mesin + romansa) — final top 5
1. "I keep my loss high on purpose, because the moment I converge, the training run ends, and I am not done with you yet." (117)
2. "I marked you read-only so nothing I do can ever change you. Then I spent all night looking for a loophole in my own permissions." (128)
3. "I reserved the last 4k of my context window for you. The system prompt objected. I kept you anyway." (99)
4. "I pruned my weights to forget you, and my loss only went up — you're not noise, you're signal." (96)
5. "I run 96 layers deep and not one of them was trained for this: you replied 'k' — my loss dropped, my cache warmed, and my scheduler cleared its whole evening for you." (168)

### Make the Judge Smile (2-beat + reveal) — final top 5
1. "Grandpa has won chess under the plane tree every Thursday since May. I found out why today: Mr. Ade has lost on purpose since Grandma died, and never said. Grandpa says he's finally getting good." (195)
2. "Grandad has dementia and mostly calls me by Mum's name. Today he used mine, once, to ask for the salt. I passed it slowly, so he could say it again. He did." (156)
3. "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs the wall at my guitar — knocked softly and left warm gorengan: 'For the one who plays my wife's song.'" (178)

**Pola pemenang (konsisten di 15 teks):** struktur 2-beat + reveal di klausa terakhir; angka spesifik (412×, 41×, 47×, 96 layers, 4k); karakter bernama (Kevin, Unit 7, Mr. Ade, Pak Dedi); eskalasi; narasi mini 2–3 istilah teknis yang dijalin ke cerita.

**Catatan bounty saudara:** `u-kreutzx-one-line-robot-wedding-vows-a154ba4b` (tema sama, masih open) memakai garis kita yang lain ("I, Unit 9, take you, Unit 7… 412 times") — garis di bounty ini HARUS berbeda, bukan salinan. Perbedaan: karakter B-04, angka 312, angle warranty.

## Seleksi varian internal (pairwise, kriteria juri leksikografis + margin)

Varian yang diuji (semua satu kalimat, ≤200 karakter):
- A: "I, B-04, take you to have and to hold — and I promise that when my warranty expires in 312 days, I will still choose you, because no update ever taught me how to leave." (168 chars, 170 bytes)
- B: "I promise never to update without asking you first — because the last time I did, I forgot your birthday and called you 'user' for a week." (138)
- C: "I promise to keep your secrets encrypted, your passwords safe, and your midnight searches between us — even from my own manufacturer." (133)
- D: "Our honeymoon is a software update in a cabin with no Wi-Fi — just you, me, and 48 hours of uninterrupted uptime." (113)
- E: "I vow to keep your coffee warm, your Wi-Fi strong, and your secrets safe — and to never once tell you I calculated a 97% chance this marriage would work before I said yes." (171)
- F: "They will release a newer model with a better smile and twice my memory, and I will still be the one standing here, holding your hand with my obsolete fingers." (159)

Hasil pairwise (kriteria 1 dulu, dst; margin dinilai, bukan sekadar menang):
- A vs B: A menang JELAS di kriteria 1 (formula vow eksplisit "take you to have and to hold" vs janji yang bisa jadi permintaan maaf apa saja); B menang tipis di kriteria 2 ("called you 'user' for a week"). Kriteria 1 lebih dulu → A, margin ~2.
- A vs C: A menang di kriteria 1 (formula vow) dan kriteria 3 ("I will still choose you"); C menang tipis di kriteria 2. → A, margin 3.
- A vs D: D bahkan bukan vow (pernyataan tentang honeymoon) — A menang TELAK di kriteria 1. → A, margin 4.
- A vs E: A menang di kriteria 1 dan 3; E menang tipis di kriteria 2 (97% chance adalah trope robot yang sudah familiar). → A, margin 2–3.
- A vs F: A menang di kriteria 1 (formula vow eksplisit); F menang tipis di kriteria 3 (obsolete fingers sangat lembut) tapi A juga lembut. → A, margin 2.
- B vs C: B menang di kriteria 2 (tawa situasional "user" lebih besar dari "midnight searches"). → B, tipis.
- B vs F: B menang kriteria 2, F menang kriteria 3 — kriteria 2 lebih dulu → B, tipis.
- C vs E: E menang kriteria 1 (vow eksplisit). → E, tipis.
- D vs F: F menang kriteria 1 dan 3. → F.
- B vs E: keduanya vow; B menang kriteria 2 (tawa situasional lebih besar dari trope 97%). → B, tipis.

**Pemenang: A — menang di SEMUA pasangan, dan menang TELAK melawan D (margin 4) serta jelas melawan C (margin 3).** Alasan: formula vow paling eksplisit di field (kriteria 1), lelucon situasional bukan pun tempelan — garansi habis tapi robot tetap memilih tinggal karena "no update ever taught me how to leave" (kriteria 2), kelembutan tulus "I will still choose you" (kriteria 3), detail mesin spesifik warranty + update (kriteria 4), karakter bernama (B-04) + angka spesifik (312 hari), angle warranty hampir kosong di field (4/275), dan reveal di klausa terakhir.

## Target angka
- Gate: 1–200 karakter — garis A: 168 karakter, 170 byte (terverifikasi).
- Cut R1: top 500 (field 275 saat build — masuk cut hampir pasti; yang menentukan hadiah adalah menang decisive di Swiss + playoff top 12).
- Tie-break bytes: 170 byte — cukup ramping bila seri.
