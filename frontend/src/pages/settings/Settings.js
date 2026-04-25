import { useEffect, useState } from "react";
import "./Settings.css";
import Header from "../header/Header";
import { getCurrentUser } from "../../utils/CurrentUser";

const LANDING_OPTIONS = ["Search", "Dashboard"];

const Settings = () => {
  const initialUser = getCurrentUser();
  const [form, setForm] = useState({
    username: initialUser?.username ?? "",
    email: initialUser?.email ?? "",
    password: "",
  });
  const [preference, setPreference] = useState("Search");
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (!initialUser?.id) return;
    fetch(`http://localhost:8000/preferences/${initialUser.id}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (data?.preference) setPreference(data.preference);
      })
      .catch(() => {});
  }, [initialUser?.id]);

  const handleFormChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleProfileSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);
    try {
      const res = await fetch(
        `http://localhost:8000/users/${encodeURIComponent(initialUser.username)}`,
        {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: form.username,
            email: form.email,
            password: form.password,
          }),
        }
      );
      if (!res.ok) throw new Error("Failed to update profile");
      const updated = await res.json();
      const storage = localStorage.getItem("user") ? localStorage : sessionStorage;
      storage.setItem("user", JSON.stringify(updated));
      setStatus({ type: "success", msg: "Profile updated." });
    } catch (err) {
      setStatus({ type: "error", msg: err.message });
    }
  };

  const handlePreferenceSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);
    try {
      const res = await fetch("http://localhost:8000/preferences", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: initialUser.id, preference }),
      });
      if (!res.ok) throw new Error("Failed to update preference");
      setStatus({ type: "success", msg: "Preference saved." });
    } catch (err) {
      setStatus({ type: "error", msg: err.message });
    }
  };

  return (
    <>
      <Header />
      <div className="settings-wrapper">
        <div className="settings-section">
          <h2>Account</h2>
          <form onSubmit={handleProfileSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input
                type="text"
                name="username"
                value={form.username}
                onChange={handleFormChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                name="email"
                value={form.email}
                disabled
              />
            </div>

            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                name="password"
                value={form.password}
                onChange={handleFormChange}
                placeholder="New password"
                required
              />
            </div>

            <button type="submit" className="save-btn">Save Profile</button>
          </form>
        </div>

        <div className="settings-section">
          <h2>Preferences</h2>
          <form onSubmit={handlePreferenceSubmit}>
            <div className="form-group">
              <label>Landing page after login</label>
              <select
                value={preference}
                onChange={(e) => setPreference(e.target.value)}
              >
                {LANDING_OPTIONS.map((opt) => (
                  <option key={opt} value={opt}>{opt}</option>
                ))}
              </select>
            </div>

            <button type="submit" className="save-btn">Save Preference</button>
          </form>
        </div>

        {status && (
          <p className={`status-msg ${status.type}`}>{status.msg}</p>
        )}
      </div>
    </>
  );
};

export default Settings;
