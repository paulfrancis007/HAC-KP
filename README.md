# 🛡️ ACPIA

## Agentic Child Protection Investigation Assistant

> **AI-Powered Multi-Agent Investigation Platform for Digital Evidence Analysis**

---

## 📌 Overview

ACPIA (Agentic Child Protection Investigation Assistant) is a proof-of-concept AI-powered investigation support platform designed to assist authorized agencies in analyzing digital evidence efficiently.

Instead of relying on a single AI model, ACPIA follows a **Multi-Agent Architecture**, where specialized AI agents collaborate to extract entities, correlate evidence, reconstruct timelines, generate knowledge graphs, and produce explainable investigation reports.

The platform is designed to **support investigators—not replace them**—by accelerating evidence analysis while ensuring human oversight.

---

## ✨ Features

- 📄 Text Evidence Analysis
- 👥 Entity Extraction using Gemini AI
- 🕸️ Knowledge Graph Generation
- 📅 Timeline Reconstruction
- ⚠️ Risk Assessment
- 📝 AI Investigation Summary
- 🤖 Multi-Agent Workflow
- 🔍 Explainable Investigation Pipeline

---

# 🏗️ System Architecture

```text
Evidence Upload
       │
       ▼
Text Agent
       │
       ▼
Entity Agent
       │
       ▼
Correlation Agent
       │
       ▼
Knowledge Graph
       │
       ▼
Timeline Agent
       │
       ▼
Summary Agent
       │
       ▼
Investigation Report
```

---

# 🤖 AI Agents

## 📄 Text Agent

- Reads uploaded chat exports
- Normalizes textual evidence
- Prepares evidence for downstream agents

---

## 👥 Entity Agent

Extracts:

- People
- Locations
- Dates
- Phone Numbers
- Email Addresses
- Objects
- Important Events

Powered by **Google Gemini**.

---

## 🔗 Correlation Agent

- Identifies relationships between extracted entities
- Connects people, locations, devices and events
- Generates evidence correlations

---

## 🕸️ Knowledge Graph Agent

Builds an interactive relationship graph showing:

- People
- Locations
- Objects
- Communication Links
- Evidence Relationships

---

## 📅 Timeline Agent

Reconstructs chronological events from digital evidence.

Example:

```
12 Mar 2026
Conversation Started

↓

13 Mar 2026
Photo Request

↓

14 Mar 2026
Meeting Planned

↓

15 Mar 2026
Location Shared
```

---

## 📝 Summary Agent

Generates:

- Investigation Summary
- Risk Indicators
- Key Findings
- Recommended Next Steps

All outputs are intended to support **human investigators**.

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| LLM | Google Gemini |
| Graph Visualization | NetworkX + PyVis |
| AI Design | Multi-Agent Architecture |

---

# 📂 Project Structure

```
ACPIA/

├── backend/
│   ├── agents/
│   │   ├── text_agent.py
│   │   ├── entity_agent.py
│   │   ├── correlation_agent.py
│   │   ├── timeline_agent.py
│   │   └── summary_agent.py
│   │
│   ├── app.py
│   ├── orchestrator.py
│   ├── graph_viz.py
│   ├── config.py
│   └── requirements.txt
│
├── sample_data/
│
├── screenshots/
│
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/HAC-KP.git
```

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

## Configure Environment

Create a file:

```
backend/.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
cd backend

streamlit run app.py
```

---

# 📸 Screenshots

> Add screenshots after the hackathon.

Example:

```
screenshots/

dashboard.png

knowledge_graph.png

timeline.png

summary.png
```

---

# 🎯 Future Scope

- 🖼️ Image Analysis Agent
- 🎥 Video Analysis Agent
- 🎙️ Audio Intelligence Agent
- 📄 OCR Agent
- 📍 Metadata Correlation Agent
- 🧬 Deepfake Detection Agent
- 🌐 OSINT Integration
- 🧠 Explainability Agent
- 📊 Confidence Scoring Agent

---

# ⚖️ Disclaimer

This project is a **Hackathon Proof of Concept** developed for HAC'KP.

The generated insights are intended to **assist investigators** and **must not** be treated as final conclusions.

Human verification and oversight remain essential throughout the investigation process.

---

# 👨‍💻 Author

**Paul Francis**

HAC'KP 2026 Submission

AI • Multi-Agent Systems • Digital Investigation • Knowledge Graphs