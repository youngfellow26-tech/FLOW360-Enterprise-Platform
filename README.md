
# FLOW360 Phase 2 – Enterprise Mining Intelligence Platform

Enterprise upgrade featuring:

• Palantir‑style command center UI  
• 3D global mining operations map (Three.js)  
• AI risk forecasting models  
• equipment telemetry streaming (WebSockets)  
• multi‑tenant SaaS authentication (JWT)  
• executive intelligence dashboards  
• supply chain disruption simulator  
• ESG analytics endpoints  

Architecture:

frontend/  → React command center  
backend/   → FastAPI enterprise API  
ai/        → forecasting models  
stream/    → telemetry streaming simulator  

Run locally:

Backend:
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

Frontend:
cd frontend
npm install
npm start
