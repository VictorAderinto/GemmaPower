# Geo-Spatial Power Grid Agent System

**Powered by Google Gemini 3**

## ⚡ Project Overview
This project demonstrates a next-generation **Agentic Power Grid Management System**. It leverages **Google Gemini 3** to orchestrate a team of specialized AI agents that monitor, analyze, and control different regions of a power grid (IEEE Case 57).

Traditional power grid management is often siloed and reactive. This system introduces a **proactive, decentralized AI architecture** where regional agents collaborate to solve complex grid problems (like overloads or voltage violations) under the supervision of a central Orchestrator.

## 🚀 Key Features
- **Multi-Agent Architecture**: A "Map-Reduce" style agent system where `RegionAgents` analyze local data and an `Orchestrator` synthesizes global decisions.
- **Natural Language Control**: Operators can interact with the grid using natural language (e.g., *"Simulate an outage on Bus 5 and tell me if the grid is stable"*).
- **Real-time Simulation**: Integrated with `pandapower` for accurate power flow calculations.
- **Gemini 3 Integration**: Utilizes the latest Gemini models for high-speed reasoning and structured data processing.

## 🛠️ Architecture
The system consists of:
1.  **Frontend**: A React-based Dashboard for visualization and chat.
2.  **Backend**: A Python/FastAPI server managing the agents.
3.  **Agents**:
    *   **Orchestrator**: The central brain that delegates tasks and aggregates results.
    *   **Region Agents**: Local experts for specific grid clusters.
    *   **Scenario Builder**: A specialized tool for parsing user intent into grid modifications.

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 16+
- Google Cloud API Key (with Gemini access)

### 1. Backend Setup
```bash
cd .
pip install -r requirements.txt
# Create a .env file with your API key
# GOOGLE_API_KEY=your_key_here
uvicorn src.api.main:app --reload
```

### 2. Frontend Setup
```bash
cd web
npm install
npm run dev
```

## 🎮 How to Demo
See [Demo Storyboard](demo%20storyboard.md) for a step-by-step guide to showcasing the project.
