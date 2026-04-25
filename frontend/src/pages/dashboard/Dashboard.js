import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";
import Header from "../header/Header";
import { getCurrentUser } from "../../utils/CurrentUser";

const Dashboard = () => {
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);
  const [user] = useState(getCurrentUser());
  const navigate = useNavigate();

  useEffect(() => {
    if (!user?.id) {
      setLoading(false);
      return;
    }
    fetch(`http://localhost:8000/favorites?user_id=${user.id}`)
      .then((r) => (r.ok ? r.json() : []))
      .then((data) => {
        setFavorites(data);
        setLoading(false);
      })
      .catch(() => {
        setFavorites([]);
        setLoading(false);
      });
  }, [user]);

  const handleUnfavorite = async (coverageId, e) => {
    e.stopPropagation();
    try {
      const res = await fetch(
        `http://localhost:8000/favorites/${user.id}/${coverageId}`,
        { method: "DELETE" }
      );
      if (res.ok) {
        setFavorites((prev) => prev.filter((f) => f.id !== coverageId));
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleViewDocument = (r) => {
    if (!r.document_url) return;
    navigate(`/documentViewer?id=${r.id}`);
  };

  return (
    <>
      <Header />
      <div className="dashboard-wrapper">
        <div className="dashboard-header">
          <h2>My Favorites</h2>
          <p className="dashboard-subtitle">
            {user?.id
              ? `Quick access to policies you've saved.`
              : `Sign in to see your saved policies.`}
          </p>
        </div>

        {!user?.id ? (
          <div className="empty-state">
            <p>You need to be signed in to view favorites.</p>
            <button className="empty-action" onClick={() => navigate("/login")}>
              Go to Login
            </button>
          </div>
        ) : loading ? (
          <p className="loading-text">Loading...</p>
        ) : favorites.length === 0 ? (
          <div className="empty-state">
            <p>You haven't favorited any policies yet.</p>
            <button className="empty-action" onClick={() => navigate("/search")}>
              Search Policies
            </button>
          </div>
        ) : (
          <>
            <p className="results-count">
              {favorites.length} saved polic{favorites.length !== 1 ? "ies" : "y"}
            </p>
            <div className="results-list">
              {favorites.map((r) => (
                <div
                  key={r.id}
                  className={`result-card ${r.document_url ? "clickable" : "no-doc"}`}
                  onClick={() => handleViewDocument(r)}
                >
                  <div className="result-header">
                    <span className="result-name">{r.description}</span>
                    <button
                      className="unfavorite-btn"
                      title="Remove from favorites"
                      onClick={(e) => handleUnfavorite(r.id, e)}
                    >
                      &#9733;
                    </button>
                  </div>

                  <div className="result-meta">
                    <span className="tag provider-tag">{r.provider_name}</span>
                    <span className="tag policy-tag">{r.policy_name}</span>
                    {r.code_count > 0 && (
                      <span className="code-count-badge">{r.code_count} codes</span>
                    )}
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
    </>
  );
};

export default Dashboard;
