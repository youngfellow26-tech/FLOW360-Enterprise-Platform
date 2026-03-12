
import React,{useEffect,useState} from "react"

function App(){

const [tenants,setTenants]=useState([])
const [risk,setRisk]=useState(null)
const [esg,setESG]=useState(null)

useEffect(()=>{
 fetch("http://localhost:8000/tenants")
 .then(r=>r.json())
 .then(data=>setTenants(Object.entries(data)))
},[])

function runRisk(){
 fetch("http://localhost:8000/ai/risk/HaulTruck-21")
 .then(r=>r.json())
 .then(setRisk)
}

function loadESG(){
 fetch("http://localhost:8000/esg")
 .then(r=>r.json())
 .then(setESG)
}

return(
<div style={{background:"#0a0f1c",color:"white",minHeight:"100vh",padding:40}}>

<h1>FLOW360 Enterprise Command Center</h1>

<h2>Mining Tenants</h2>
<ul>
{tenants.map(([name,data])=>(
<li key={name}>{name} — Fleet {data.fleet}% | Production {data.production}%</li>
))}
</ul>

<h2>AI Risk Forecast</h2>
<button onClick={runRisk}>Run Risk Forecast</button>
{risk && (
<div>
Asset: {risk.asset}<br/>
Risk Score: {risk.risk_score}<br/>
Status: {risk.status}
</div>
)}

<h2>ESG Intelligence</h2>
<button onClick={loadESG}>Load ESG Metrics</button>
{esg && (
<div>
Carbon Intensity: {esg.carbon_intensity}<br/>
Water Usage: {esg.water_use}<br/>
Safety Score: {esg.safety_score}
</div>
)}

<h2>3D Global Operations Map</h2>
<div style={{height:350,background:"#111",display:"flex",alignItems:"center",justifyContent:"center"}}>
Three.js 3D Mining Operations Map Placeholder
</div>

</div>
)
}

export default App
