import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
//import { UserContext } from "../UserContext";
import './Login.css';

const Login = () => {

  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  /*
  const navigate = useNavigate();
  const location = useLocation();

  const { user, fetchUser, emailPasswordLogin } = useContext(UserContext);

  const onFormInputChange = (event) => {
    const { name, value } = event.target;
    setForm({ ...form, [name]: value });
  };

  const redirectNow = () => {
    const redirectTo = location.search.replace("?redirectTo=", "");
    
    setTimeout(() => {
      navigate(redirectTo ? redirectTo : "/dashboard");
    }, 1000); 
  }

  const loadUser = async () => {
    if (!user) {
      const fetchedUser = await fetchUser();
      if (fetchedUser) {
        redirectNow();
      }
    }
  }

  useEffect(() => {
    loadUser(); // eslint-disable-next-line 
  }, []);

  const onSubmit = async (event) => {
    event.preventDefault();
    try {
      const user = await emailPasswordLogin(form.email, form.password);
      if (user) {
        redirectNow();
      }
    } catch (error) {
      if (error.statusCode === 401) {
        alert("Invalid username/password. Try again!");
      } else {
        alert(error);
      }
    }
  };
*/
const navigate = useNavigate();

const handleLogin = () => {
  navigate("/search");
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
              <form>
                <p className="pt-3">
                  <label>Username or email address<span>*</span></label>
                  <input placeholder="Username or Email"
                    label="Email"
                    type="email"
                    name="email"
                    value={form.email}
                    //onChange={onFormInputChange}
                    required />
                </p>
                <p className="pt-3">
                  <label>Password<span>*</span></label>
                  <input type="password" placeholder="Password"
                    label="Password"
                    name="password"
                    value={form.password}
                    //onChange={onFormInputChange}
                    required />
                </p>

                <div className="pt-1">
                  <button type="button mt-3" 
                          onClick={handleLogin}
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
                  <button type="button mt-3" 
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