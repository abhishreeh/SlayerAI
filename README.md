# 🛡️ SlayerAI: The Dark Pattern Slayer & Bureaucracy Navigator
### *Autonomous Personal Consumer Rights Advocate & Regulatory Enforcement Engine*

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-emerald.svg)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/Tests-12%2F12%20Passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)]()

---

## 🎯 The Problem
Modern corporations intentionally weaponize **deceptive user experience (Dark Patterns)** and **bureaucratic friction** to trap consumers and bleed recurring revenue:
* **The Subscription Roach Motel:** Signing up takes 10 seconds online; canceling requires navigating 5 guilt-tripping screens, hidden buttons, or calling during limited business hours.
* **The Stealth Early Termination Fee (ETF):** Annual-Paid-Monthly contracts (exemplified by Adobe) impose shocking 50% remainder cancellation penalties (often $200–$400+) buried in fine print.
* **FinTech & Bank Fee Exploitation:** Banks assess $35 overdraft fees on $3 coffee debits under delayed clearing schedules ("Authorize Positive, Settle Negative").
* **Aviation Stonewalling:** Airlines reject legitimate EU261 / US DOT passenger compensation claims citing bogus "extraordinary technical circumstances."

---

## ⚡ The Solution: SlayerAI (AdvocateOS)
**SlayerAI** is an autonomous multi-scenario AI agent platform that acts as a tireless, legally armed personal consumer rights advocate.

It doesn't just give advice—it **perceives, navigates, and dismantles corporate friction**:
1. **Perception Engine:** Detects and classifies dark patterns (*Roach Motel*, *Confirmshaming*, *Hidden ETF*, *Visual Interference*) directly from UI/DOM elements.
2. **Tactical Exploits:** Automates the famous **Adobe Plan-Swap Loophole** (switching to a month-to-month plan to reset the statutory cancellation window and eliminate the ETF penalty to $0.00).
3. **Statutory Weaponization:** Cites binding regulatory mandates (FTC 16 CFR Part 425 *Click-to-Cancel*, ROSCA 15 U.S.C. § 8403, CFPB Circular 2022-06, and EU 261/2004) to draft legally binding demand packages and negotiate fee reversals.

---

## 🕹️ Interactive Arenas & Scenarios

### 1. Adobe Subscription Slayer & Plan-Swap Loophole
- **Scenario:** Creative Cloud All Apps ($54.99/mo) with 10 months remaining and an aggressive $274.95 early cancellation fee.
- **Visual DOM Simulator:** Interactive recreation of the 4-step Adobe cancellation funnel showing real-time dark pattern badges and visual interference.
- **The Counter-Exploit:** 
  1. The agent detects the $274.95 penalty.
  2. Bypasses the loss-aversion fear copy and mandatory feedback survey.
  3. Executes a contract swap to the Photography Plan ($9.99/mo).
  4. Triggers the statutory 14-day cooling-off reset under consumer law.
  5. Cancels the new plan immediately with **$0.00 Early Termination Fee**!
  6. Generates a formal **FTC Click-to-Cancel Notice** for the user's records.

### 2. FinTech & Banking Fee Disputer
- **Scenario:** $35.00 Overdraft Fee assessed on a minor $4.25 debit purchase.
- **Live Negotiation Chat:** The agent interfaces directly with the bank's customer support representative.
- **Regulatory Counter-Attack:** Rebuffs default denial scripts by citing **CFPB Circular 2022-06** (prohibiting APSN fees under Dodd-Frank UDAAP) and demands proof of electronic affirmative opt-in under **Regulation E (12 CFR § 1005.17)**, securing a full courtesy waiver.

### 3. EU261 & US DOT Flight Compensation Claimer
- **Scenario:** Transatlantic flight delayed 4.5 hours with the airline claiming "operational and technical maintenance issues."
- **Flight Geometry & CJEU Jurisprudence:**
  - Calculates Great-Circle Haversine distance between airports (e.g. JFK -> FRA = 6,206 km -> €600 Tier 3 payout).
  - Automatically debunks the airline's excuse using European Court of Justice precedents (*Wallentin-Hermann C-549/07* and *van der Lans C-257/14*), establishing that mechanical defects are ordinary carrier risks.
  - Generates an official 14-day pre-action demand letter ready for carrier legal submission.

### 4. Custom Objective Advocate
- Users can type any custom corporate hurdle (e.g., *Gym requiring certified snail-mail cancellation*, *Hidden telecom termination fee*).
- The agent classifies the deceptive friction, pairs it with federal/state statutes, and produces a customized dispute battle plan and legal demand.

---

## 🏗️ Project Architecture
```
dark-pattern-slayer/
├── app/
│   ├── main.py                     # FastAPI application & REST endpoints
│   ├── agents/
│   │   ├── base_advocate.py        # Event streaming & timeline ledger
│   │   ├── subscription_slayer.py  # Adobe cancellation & plan-swap exploit
│   │   ├── banking_disputer.py     # Bank fee negotiation & CFPB citations
│   │   └── flight_compensator.py   # EU261 calculator & excuse debunker
│   ├── rules/
│   │   ├── legal_kb.py             # Statutory knowledge base & demand templates
│   │   └── dark_pattern_taxa.py    # Deceptive design taxonomy & regex heuristics
│   ├── simulators/
│   │   ├── adobe_simulator.py      # Faithful multi-step cancellation mockup
│   │   ├── bank_simulator.py       # Live bank representative chat gateway
│   │   └── airline_simulator.py    # Distance geometry & delay excuse engine
│   ├── models/
│   │   └── schemas.py              # Pydantic models for patterns, states, and actions
│   └── templates/
│       └── index.html              # Cyberpunk glassmorphism mission control UI
├── tests/
│   ├── test_advocate.py            # Unit tests for agents and detection engine
│   └── test_api.py                 # REST API integration tests
├── run.py                          # Application startup script
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart Guide

### Prerequisites
- Python 3.10+ (Tested on Python 3.12)
- Dependencies installed via pip

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
python run.py
```
Open your browser to: **`http://127.0.0.1:8000`**

### 3. Run the Test Suite
```bash
python -m unittest discover tests
```

---

## ⚖️ Statutory Consumer Protection Codex
SlayerAI operationalizes the following consumer protection statutes:
* **FTC Negative Option Rule (16 CFR Part 425) & Click-to-Cancel:** Prohibits asymmetric cancellation friction.
* **ROSCA (15 U.S.C. §§ 8401–8405):** Outlaws deceptive recurring negative option billing.
* **California Automatic Renewal Law (ARL § 17600):** Mandates frictionless 1-click online cancellation.
* **CFPB Circular 2022-06 & Dodd-Frank UDAAP (12 U.S.C. § 5536):** Unlawful surprise overdraft fee practices.
* **CFPB Regulation E (12 CFR Part 1005):** Mandatory opt-in protections for debit/ATM overdrafts.
* **EU Regulation (EC) No 261/2004:** Statutory compensation of €250–€600 for flight disruptions >= 3 hours.
* **US DOT 2024 Final Rule (14 CFR Part 260):** Mandatory prompt cash refunds for cancelled/significantly delayed flights.
