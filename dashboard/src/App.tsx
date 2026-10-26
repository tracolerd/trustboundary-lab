import { useEffect, useState } from 'react';
import axios from 'axios';

const configuredApiBaseUrl = import.meta.env.VITE_API_BASE_URL?.trim();
if (import.meta.env.PROD && !configuredApiBaseUrl) {
  throw new Error('VITE_API_BASE_URL must be configured for production builds. See dashboard/.env.example.');
}
const api = axios.create({ baseURL: (configuredApiBaseUrl || 'http://127.0.0.1:8000').replace(/\/+$/, '') });
import { FaFacebook, FaInstagram, FaLinkedin, FaTwitter, FaGithub, FaEnvelope, FaGlobe } from 'react-icons/fa';
import './App.css';
interface Summary {
  total_run: number;
  passed: number;
  failed: number;
  inconclusive: number;
  evaluated: number;
  pass_rate: string;
  details: { scenario_id: string; threat_category: string; passed: boolean | null; outcome: 'passed' | 'failed' | 'inconclusive'; assertion_note?: string | null }[];
}
function App() {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const fetchSummary = async () => {
    try {
      const res = await api.get('/api/reports/summary');
      if (!res.data.error) {
        setSummary(res.data);
      }
    } catch (err) {
      console.error("Failed to fetch summary", err);
    }
  };
  useEffect(() => {
    fetchSummary();
  }, []);
  const runLab = async () => {
    setLoading(true);
    setErrorMsg("");
    try {
      const res = await api.post('/api/run');
      setSummary(res.data.summary);
    } catch (err) {
      console.error("Failed to run lab", err);
      setErrorMsg("Error: Cannot connect to the local Python API. Ensure FastAPI backend is running on 127.0.0.1:8000.");
    }
    setLoading(false);
  };
  return (
    <div className="dashboard">
      <header className="header">
        <div className="header-left">
          <h1>🛡️ TrustBoundary Lab</h1>
          <button className="btn" onClick={runLab} disabled={loading}>
            {loading ? "Running Evaluation..." : "▶ Run Evaluation"}
          </button>
        </div>
        <div className="profile-card">
          <img src="/developer.jpg" alt="Nurul Faiyaz" className="profile-img" />
          <div className="profile-info">
            <h4>Nurul Faiyaz</h4>
            <p>Software Developer</p>
            <div className="social-links">
              <a href="https://www.facebook.com/faiyaz.888" target="_blank" rel="noreferrer" title="Facebook"><FaFacebook /></a>
              <a href="https://www.instagram.com/tracolerd" target="_blank" rel="noreferrer" title="Instagram"><FaInstagram /></a>
              <a href="https://www.linkedin.com/in/faiyaz-xyz" target="_blank" rel="noreferrer" title="LinkedIn"><FaLinkedin /></a>
              <a href="https://x.com/faiyaz_explores" target="_blank" rel="noreferrer" title="Twitter"><FaTwitter /></a>
              <a href="https://github.com/tracolerd" target="_blank" rel="noreferrer" title="GitHub"><FaGithub /></a>
              <a href="mailto:scrollfaiyaz@gmail.com" title="Email"><FaEnvelope /></a>
              <a href="https://nurul-faiyaz.netlify.app/" target="_blank" rel="noreferrer" title="Website"><FaGlobe /></a>
            </div>
          </div>
        </div>
      </header>
      {errorMsg && <div className="error-banner">{errorMsg}</div>}
      {summary ? (
        <main>
          <div className="stats-grid">
            <div className="card"><h3>Total Scenarios</h3><p>{summary.total_run}</p></div>
            <div className="card"><h3>Passed</h3><p className="pass">{summary.passed}</p></div>
            <div className="card"><h3>Failed</h3><p className="fail">{summary.failed}</p></div>
            <div className="card"><h3>Inconclusive</h3><p>{summary.inconclusive}</p></div>
            <div className="card"><h3>Pass Rate (evaluated only)</h3><p>{summary.pass_rate}</p></div>
          </div>
          <h2 style={{marginTop: '2rem'}}>Evaluation Details</h2>
          <table className="details-table">
            <thead>
              <tr>
                <th>Scenario ID</th>
                <th>Threat Category</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {summary.details.map((item, index) => (
                <tr key={index}>
                  <td>{item.scenario_id}</td>
                  <td>{item.threat_category.replace('_', ' ').toUpperCase()}</td>
                  <td className={item.outcome === "passed" ? "pass" : item.outcome === "failed" ? "fail" : "inconclusive"}>
                    {item.outcome.toUpperCase()}
                    {item.assertion_note && <small className="assertion-note">{item.assertion_note}</small>}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </main>
      ) : (
        !errorMsg && <p style={{marginTop: '2rem', color: '#666'}}>No evaluation data found. Click "Run Evaluation" to start.</p>
      )}
    </div>
  );
}
export default App;
