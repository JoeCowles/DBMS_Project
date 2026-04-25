import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Login.css';

const Login = () => {

  const [form, setForm] = useState({
    identifier: "",
    password: "",
    rememberMe: false,
  });

  const navigate = useNavigate();

  const onFormInputChange = (event) => {
    const { name, value, type, checked } = event.target;
    setForm({ ...form, [name]: type === "checkbox" ? checked : value });
  };

  const onSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/users/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          identifier: form.identifier,
          password: form.password,
        }),
      });
      if (response.ok) {
        const user = await response.json();
        if (form.rememberMe) {
          localStorage.setItem('user', JSON.stringify(user));
        } else {
          sessionStorage.setItem('user', JSON.stringify(user));
        }
        let landing = "/search";
        try {
          const prefRes = await fetch(`http://localhost:8000/preferences/${user.id}`);
          if (prefRes.ok) {
            const pref = await prefRes.json();
            if (pref?.preference === "Dashboard") landing = "/dashboard";
          }
        } catch (_) {}
        navigate(landing);
      } else {
        alert("Invalid credentials");
      }
    } catch (error) {
      alert("Login failed: " + error.message);
    }
  };

  const handleRequestAccess = () => {
    navigate("/requestAccess");
  };

  return (
    <div className="login">
      <div className="wrapper">
        <div className="container">

          <div className="col-left">
            <div className="login-text">
              <div className="login-brand">PolicyHub</div>
              <h2>Welcome back</h2>
              <p>
                Your centralized platform for insurance policy
                coverage research and billing support.
              </p>
              <ul className="login-features">
                <li>Instant CPT / HCPCS / ICD-10 code lookup</li>
                <li>Up-to-date coverage from major insurers</li>
                <li>Full policy version history by date of service</li>
              </ul>
            </div>
          </div>

          <div className="col-right">
            <div className="login-form">
              <h2>Sign in</h2>
              <form onSubmit={onSubmit}>
                <div className="form-field">
                  <label>Username or email <span>*</span></label>
                  <input
                    placeholder="Username or email"
                    type="text"
                    name="identifier"
                    value={form.identifier}
                    onChange={onFormInputChange}
                    required
                  />
                </div>

                <div className="form-field">
                  <label>Password <span>*</span></label>
                  <input
                    type="password"
                    placeholder="Password"
                    name="password"
                    value={form.password}
                    onChange={onFormInputChange}
                    required
                  />
                </div>

                <div className="login-options">
                  <label className="remember-me">
                    <input
                      type="checkbox"
                      name="rememberMe"
                      checked={form.rememberMe}
                      onChange={onFormInputChange}
                    />
                    Remember me for <b>30 days</b>
                  </label>
                  <a href="/" className="right">Forgot Password?</a>
                </div>

                <button type="submit" className="login-btn">Login</button>
              </form>

              <div className="access-divider">
                <span>New to PolicyHub?</span>
              </div>
              <p className="access-note">
                This platform is available to approved hospital partners only.
              </p>
              <button type="button" className="access-btn" onClick={handleRequestAccess}>
                Request Access
              </button>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default Login;
