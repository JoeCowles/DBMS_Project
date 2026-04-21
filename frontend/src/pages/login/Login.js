import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Login.css';

const Login = () => {

  const [form, setForm] = useState({
    identifier: "",
    password: ""
  });

  const navigate = useNavigate();

  const onFormInputChange = (event) => {
    const { name, value } = event.target;
    setForm({ ...form, [name]: value });
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
        localStorage.setItem('user', JSON.stringify(user));
        navigate("/search");
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
    <div class="login">
      <div className="wrapper">
        <div className="container">
          <div className="col-left">
            <div className="login-text">
            </div>
          </div>
          <div className="col-right">
            <div className="login-form">
              <h2>Sign-in</h2>
              <form onSubmit={onSubmit}>
                <p className="pt-3">
                  <label>Username or email address<span>*</span></label>
                  <input placeholder="Username or Email"
                    type="text"
                    name="identifier"
                    value={form.identifier}
                    onChange={onFormInputChange}
                    required />
                </p>
                <p className="pt-3">
                  <label>Password<span>*</span></label>
                  <input type="password" placeholder="Password"
                    name="password"
                    value={form.password}
                    onChange={onFormInputChange}
                    required />
                </p>

                <div className="pt-1">
                  <button type="submit" 
                          style={{ fontSize: "15px" }}>
                    Login
                  </button>
                </div>

                <div className="login-options">
                  <a href="/" className="left">Remember me for <b>30 days</b></a>
                  <a href="/" className="right">Forgot Password?</a>
                </div>

              <h2 className="text-white">Don't have access?</h2>
              <p>This platform is available to approved hospital partners only.</p>
              <p>Request access or contact your hospital administrator too get started.</p>
                  
                <div className="pt-1">
                  <button type="button" 
                          onClick={handleRequestAccess}
                          style={{ fontSize: "15px" }}>
                            Request Access
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;