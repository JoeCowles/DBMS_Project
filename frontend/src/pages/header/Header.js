import { useNavigate, useLocation } from "react-router-dom";
import "./Header.css";

const Header = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    localStorage.removeItem('user');
    sessionStorage.removeItem('user');
    navigate("/");
  };

  const isActive = (path) => {
    return location.pathname === path ? "active" : "";
  };

  return (
    <div className="header">
      <div className="logo" onClick={() => navigate("/dashboard")}>
        PolicyHub
      </div>

      <div className="nav-links">
        <button
          className={isActive("/dashboard")}
          onClick={() => navigate("/dashboard")}
        >
          Dashboard
        </button>

        <button
          className={isActive("/search")}
          onClick={() => navigate("/search")}
        >
          Search
        </button>

        <button
          className={isActive("/settings")}
          onClick={() => navigate("/settings")}
        >
          Settings
        </button>
      </div>

      <div className="header-actions">
        <button className="logout" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
};

export default Header;