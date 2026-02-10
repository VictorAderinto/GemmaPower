import { useState } from 'react'
// import './App.css'
import Dashboard from './components/Dashboard'
import ChatInterface from './components/ChatInterface'

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

function App() {
    const [stats, setStats] = useState(null);
    const [processing, setProcessing] = useState(false);

    const loadCase = async (caseName) => {
        const res = await fetch(`${API_BASE}/load`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ case_name: caseName })
        });
        const data = await res.json();
        setStats(data.stats);
    };

    const sendMessage = async (text) => {
        setProcessing(true);
        try {
            const res = await fetch(`${API_BASE}/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text })
            });
            const data = await res.json();
            if (data.stats) {
                setStats(data.stats);
            }
            return data.response;
        } finally {
            setProcessing(false);
        }
    };

    return (
        <div className="app-container">
            <Dashboard stats={stats} onCaseLoad={loadCase} />
            <ChatInterface onSendMessage={sendMessage} isProcessing={processing} />
        </div>
    )
}

export default App
