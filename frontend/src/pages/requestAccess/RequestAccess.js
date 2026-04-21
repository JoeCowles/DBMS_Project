import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./RequestAccess.css";

const RequestAccess = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    organization: "",
    role: "",
    comment: "",
  });
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (
      !formData.firstName.trim() ||
      !formData.lastName.trim() ||
      !formData.email.trim() ||
      !formData.organization.trim() ||
      !formData.role
    ) {
      setError("Please fill out all required fields.");
      return;
    }

    setSubmitting(true);
    try {
      const response = await fetch("http://localhost:8000/pendingUsers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          firstName: formData.firstName.trim(),
          lastName: formData.lastName.trim(),
          email: formData.email.trim(),
          organization: formData.organization.trim(),
          role: formData.role,
          comment: formData.comment.trim() || null,
        }),
      });

      if (response.ok) {
        alert("Your access request has been submitted. An administrator will review it shortly.");
        setFormData({
          firstName: "",
          lastName: "",
          email: "",
          organization: "",
          role: "",
          comment: "",
        });
        navigate("/login");
      } else if (response.status === 409) {
        setError("A pending request with this email already exists.");
      } else {
        const detail = await response.json().catch(() => ({}));
        setError(detail.detail || "Failed to submit request. Please try again.");
      }
    } catch (err) {
      setError("Request failed: " + err.message);
    } finally {
      setSubmitting(false);
    }
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
            <label>First Name<span>*</span></label>
            <input
              type="text"
              name="firstName"
              placeholder="Enter your first name"
              value={formData.firstName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Last Name<span>*</span></label>
            <input
              type="text"
              name="lastName"
              placeholder="Enter your last name"
              value={formData.lastName}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Work Email<span>*</span></label>
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
            <label>Organization / Hospital<span>*</span></label>
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
            <label>Role<span>*</span></label>
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
              name="comment"
              placeholder="Optional message or justification"
              value={formData.comment}
              onChange={handleChange}
              rows="4"
            />
          </div>

          {error && <p className="error-message">{error}</p>}

          <button
            type="submit"
            className="request-btn"
            disabled={submitting}
          >
            {submitting ? "Submitting..." : "Submit Request"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default RequestAccess;
