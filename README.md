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

### 1. Backend Setup (Required for both CLI and Web)
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google Cloud API key:
    ```env
    GOOGLE_API_KEY=your_key_here
    ```

### 2. Running the System
You can run the system in two modes: **CLI** (Terminal) or **Web** (Browser).

#### Option A: CLI Mode (Interactive Terminal)
Run the main script from the root directory:
```bash
python main.py
```

#### Option B: Web Mode (Dashboard)
You need to run both the Backend API and the Frontend (in separate terminals).

**Terminal 1: Backend API**
```bash
uvicorn src.api.main:app --reload
```
*The API will start at http://127.0.0.1:8000*

**Terminal 2: Frontend**
```bash
cd web
npm install  # Only needed once
npm run dev
```
*The Dashboard will be available at http://localhost:5173*

## 🎮 How to Demo
See [Demo Storyboard](demo%20storyboard.md) for a step-by-step guide to showcasing the project.
