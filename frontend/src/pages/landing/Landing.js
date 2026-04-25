import { useNavigate } from "react-router-dom";
import "./Landing.css";

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div className="landing">

      <div className="navbar">
        <h2>PolicyHub</h2>
        <div className="nav-actions">
          <button onClick={() => navigate("/login")}>Login</button>
          <button className="primary" onClick={() => navigate("/requestAccess")}>
            Request Access
          </button>
        </div>
      </div>

      <div className="hero">
        <div className="hero-text">
          <h1>Insurance Policy Data, Simplified</h1>
          <p>
            PolicyHub provides a centralized platform for hospital billing teams
            to quickly access accurate, up-to-date insurance policy coverage.
          </p>
          <div className="hero-buttons">
            <button className="primary" onClick={() => navigate("/requestAccess")}>
              Get Access
            </button>
            <button onClick={() => navigate("/login")}>Sign In</button>
          </div>
        </div>
      </div>

      <div className="features">
        <h2>Why PolicyHub?</h2>
        <p className="features-sub">Everything your billing team needs — in one place.</p>

        <div className="feature-grid">
          <div className="feature-card">
            <span className="feature-icon">&#128269;</span>
            <h3>Fast Search</h3>
            <p>Find policy coverage instantly using CPT codes or procedures.</p>
          </div>

          <div className="feature-card">
            <span className="feature-icon">&#128204;</span>
            <h3>Up-to-Date Data</h3>
            <p>Access the latest insurance policy changes without delays.</p>
          </div>

          <div className="feature-card">
            <span className="feature-icon">&#128196;</span>
            <h3>Version History</h3>
            <p>View coverage based on Date of Service with full history.</p>
          </div>

          <div className="feature-card">
            <span className="feature-icon">&#127970;</span>
            <h3>Centralized Platform</h3>
            <p>No more spreadsheets — everything in one reliable system.</p>
          </div>
        </div>
      </div>

      <div className="footer">
        <p>&copy; 2026 PolicyHub. All rights reserved.</p>
      </div>
    </div>
  );
};

export default Landing;
