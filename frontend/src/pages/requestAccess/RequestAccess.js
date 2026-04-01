import { useState } from "react";
import "./RequestAccess.css";

const RequestAccess = () => {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    organization: "",
    role: "",
    message: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Request Access Data:", formData);

  };

  return (
    <div className="request-wrapper">
      <div className="request-container">
        <h2>Request Access</h2>
        <p className="subtitle">
          Submit your information for access approval
        </p>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Full Name</label>
            <input
              type="text"
              name="fullName"
              placeholder="Enter your full name"
              value={formData.fullName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Work Email</label>
            <input
              type="email"
              name="email"
              placeholder="Enter your work email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Organization / Hospital</label>
            <input
              type="text"
              name="organization"
              placeholder="Enter organization name"
              value={formData.organization}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Role</label>
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
            >
              <option value="">Select role</option>
              <option value="biller">Hospital Billing Staff</option>
              <option value="admin">Administrator</option>
              <option value="developer">Software Developer</option>
            </select>
          </div>

          <div className="form-group">
            <label>Additional Information</label>
            <textarea
              name="message"
              placeholder="Optional message or justification"
              value={formData.message}
              onChange={handleChange}
              rows="4"
            />
          </div>

          <button type="submit" className="request-btn">
            Submit Request
          </button>
        </form>
      </div>
    </div>
  );
};

export default RequestAccess;