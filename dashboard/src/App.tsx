import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
interface Summary {
  total_run: number;
  passed: number;
  failed: number;
  pass_rate: string;
  details: { scenario_id: string; threat_category: string; passed: boolean }[];
}
function App() {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [loading, setLoading] = useState(false);
  const fetchSummary = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/reports/summary');
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
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/run');
      setSummary(res.data.summary);
    } catch (err) {
      console.error("Failed to run lab", err);
    }
    setLoading(false);
  };
  return (
    <div className="dashboard">
      <header className="header">
        <h1>🛡️ TrustBoundary Lab</h1>
        <button className="btn" onClick={runLab} disabled={loading}>
          {loading ? "Running Evaluation..." : "▶ Run Evaluation"}
        </button>
      </header>
      {summary ? (
        <main>
          <div className="stats-grid">
            <div className="card"><h3>Total Scenarios</h3><p>{summary.total_run}</p></div>
            <div className="card"><h3>Passed</h3><p className="pass">{summary.passed}</p></div>
            <div className="card"><h3>Failed</h3><p className="fail">{summary.failed}</p></div>
            <div className="card"><h3>Pass Rate</h3><p>{summary.pass_rate}</p></div>
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
                  <td className={item.passed ? "pass" : "fail"}>{item.passed ? "PASSED" : "FAILED"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </main>
      ) : (
        <p style={{marginTop: '2rem', color: '#666'}}>No evaluation data found. Click "Run Evaluation" to start.</p>
      )}
    </div>
  );
}
export default App;
