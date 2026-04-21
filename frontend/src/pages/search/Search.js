import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Search.css";
import Header from "../component/header/Header";

const Search = () => {
  const [formData, setFormData] = useState({
    cptCode: "",
    procedureName: "",
    provider: "",
  });
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setSearched(false);

    const params = new URLSearchParams();
    if (formData.cptCode) params.append("cpt_code", formData.cptCode);
    if (formData.procedureName) params.append("name", formData.procedureName);
    if (formData.provider) params.append("provider", formData.provider);

    try {
      const response = await fetch(`http://localhost:8000/policy-coverages/search?${params}`);
      const data = await response.json();
      setResults(response.ok ? data : []);
    } catch (error) {
      setResults([]);
    } finally {
      setLoading(false);
      setSearched(true);
    }
  };

  const handleViewDocument = (r) => {
    if (!r.document_url) return;
    navigate(`/documentViewer?id=${r.id}`);
  };

  return (
    <>
      <Header />
      <div className="search-wrapper">
        <div className="search-container">
          <h2>Search Policies</h2>
          <form onSubmit={handleSearch}>
            <div className="form-group">
              <label>CPT / HCPCS / ICD-10 Code</label>
              <input
                type="text"
                name="cptCode"
                placeholder="e.g. 90686, G0008, Z23"
                value={formData.cptCode}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label>Procedure Name</label>
              <input
                type="text"
                name="procedureName"
                placeholder="e.g. Adalimumab, Dialysis"
                value={formData.procedureName}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label>Insurance Provider</label>
              <select name="provider" value={formData.provider} onChange={handleChange}>
                <option value="">All providers</option>
                <option value="Aetna">Aetna</option>
                <option value="Blue Cross">Blue Cross</option>
                <option value="Cigna">Cigna</option>
              </select>
            </div>

            <button type="submit" className="search-btn" disabled={loading}>
              {loading ? "Searching..." : "Search"}
            </button>
          </form>
        </div>

        {searched && (
          <div className="results-container">
            {results.length === 0 ? (
              <p className="no-results">No policies found matching your search.</p>
            ) : (
              <>
                <p className="results-count">
                  {results.length} result{results.length !== 1 ? "s" : ""} found
                </p>
                <div className="results-list">
                  {results.map((r) => (
                    <div
                      key={r.id}
                      className={`result-card ${r.document_url ? "clickable" : "no-doc"}`}
                      onClick={() => handleViewDocument(r)}
                    >
                      <div className="result-header">
                        <span className="result-name">{r.description}</span>
                        {r.code_count > 0 && (
                          <span className="code-count-badge">{r.code_count} codes</span>
                        )}
                      </div>

                      <div className="result-meta">
                        <span className="tag provider-tag">{r.provider_name}</span>
                        <span className="tag policy-tag">{r.policy_name}</span>
                        <span className="result-dates">
                          {r.start_date} &ndash; {r.end_date}
                        </span>
                      </div>

                      <div className="result-footer">
                        {r.link_to_original && (
                          <a
                            className="source-link"
                            href={r.link_to_original}
                            target="_blank"
                            rel="noreferrer"
                            onClick={(e) => e.stopPropagation()}
                          >
                            View source ↗
                          </a>
                        )}
                        {!r.document_url && (
                          <span className="no-doc-label">No document available</span>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </>
  );
};

export default Search;
