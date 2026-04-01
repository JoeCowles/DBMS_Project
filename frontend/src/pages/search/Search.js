import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Search.css";

import Header from "../component/header/Header";
const Search = () => {
  const [formData, setFormData] = useState({
    cptCode: "",
    procedureName: "",
    category: "",
    provider: "",
    dateOfService: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };
  
    const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    console.log("Search Data:", formData);
    navigate("/documentViewer");
  };

  return (
    <>
      <Header/>
      
    <div className="search-wrapper">
      <div className="search-container">
        <h2>Search Policies</h2>

        <form onSubmit={handleSearch}>
          <div className="form-group">
            <label>CPT Code</label>
            <input
              type="text"
              name="cptCode"
              placeholder="Enter CPT code"
              value={formData.cptCode}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Procedure Name</label>
            <input
              type="text"
              name="procedureName"
              placeholder="Enter procedure name"
              value={formData.procedureName}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Category</label>
            <select
              name="category"
              value={formData.category}
              onChange={handleChange}
            >
              <option value="">Select category</option>
              <option value="surgery">Surgery</option>
              <option value="diagnostic">Diagnostic</option>
              <option value="therapy">Therapy</option>
            </select>
          </div>

          <div className="form-group">
            <label>Insurance Provider</label>
            <select
              name="provider"
              value={formData.provider}
              onChange={handleChange}
            >
              <option value="">Select provider</option>
              <option value="aetna">Aetna</option>
              <option value="bluecross">Blue Cross</option>
              <option value="cigna">Cigna</option>
            </select>
          </div>

          <div className="form-group">
            <label>Date of Service</label>
            <input
              type="date"
              name="dateOfService"
              value={formData.dateOfService}
              onChange={handleChange}
            />
          </div>

          <button type="submit" className="search-btn" onClick={handleSearch}>
            Search
          </button>
        </form>
      </div>
    </div>
    </>
  );
};

export default Search;