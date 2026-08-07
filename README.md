# ACPIA — Agentic Child Protection Investigation Assistant

**Hackathon MVP · Phase 1 — Project Scaffold**

ACPIA is an agentic AI assistant designed to help investigators analyze digital communications in child protection cases. This repository contains a proof-of-concept (POC) built for a hackathon — it is **not** a production application.

---

## Overview

Investigators reviewing chat exports face large volumes of unstructured text, scattered entities, and subtle patterns that are easy to miss manually. ACPIA aims to automate key analysis steps through a pipeline of specialized AI agents.

| Agent | Purpose |
|---|---|
| **Text Agent** | Parse and normalize raw chat exports |
| **Entity Agent** | Extract people, locations, dates, and contact details |
| **Correlation Agent** | Link related messages, contacts, and behavioral patterns |
| **Timeline Agent** | Reconstruct a chronological event sequence |
| **Summary Agent** | Produce an investigator-ready narrative summary |

---

## Project Structure

```
acpia-poc/
│
├── frontend/                  # UI layer (Phase 2+)
│
├── backend/
│   ├── agents/
│   │   ├── text_agent.py        # Chat parsing & normalization
│   │   ├── entity_agent.py      # Named entity extraction
│   │   ├── correlation_agent.py # Cross-message pattern linking
│   │   ├── timeline_agent.py    # Chronological reconstruction
│   │   └── summary_agent.py     # Investigative summary generation
│   ├── app.py                 # Backend entry point
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variable template
│
├── sample_data/
│   └── sample_chat.txt        # Synthetic WhatsApp chat for testing
│
└── README.md
```

---

## Sample Data

`sample_data/sample_chat.txt` contains a **synthetic, fictional** WhatsApp-style chat export. It is included solely for development and demo purposes and does not represent real individuals or events.

The sample includes:
- Multiple participants with distinct communication styles
- Timestamps in standard WhatsApp export format
- Patterns relevant to investigation workflows (e.g., secrecy requests, off-platform contact suggestions, meeting arrangements)

---

## Getting Started

> **Phase 1 status:** Scaffold only. No functionality is implemented yet.

### Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend, future phases)

### Backend Setup (future phases)

```bash
cd backend
cp .env.example .env
# Edit .env with your API keys
pip install -r requirements.txt
python app.py
```

---

## Development Roadmap

| Phase | Scope | Status |
|---|---|---|
| **Phase 1** | Project scaffold, sample data, documentation | ✅ Current |
| Phase 2 | Agent implementations & backend API | Planned |
| Phase 3 | Frontend UI & end-to-end pipeline | Planned |
| Phase 4 | Demo polish & presentation | Planned |

---

## Important Notice

This project is a **hackathon proof-of-concept**. It must not be used for real investigations without proper legal review, data handling policies, and human oversight. All sample data is entirely fictional.

---

## License

See [LICENSE](LICENSE) for details.
