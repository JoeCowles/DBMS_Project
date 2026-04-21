import { useState } from "react";
//import { useNavigate } from "react-router-dom";
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
  
  //const navigate = useNavigate();

  const handleSearch = async (e) => {
    e.preventDefault();
    if (formData.procedureName) {
      try {
        const response = await fetch(`http://localhost:8000/procedure-types/search?name=${encodeURIComponent(formData.procedureName)}`);
        if (response.ok) {
          const data = await response.json();
          alert(`Procedure Type Found!\nID: ${data.id}\nName: ${data.name}\nDescription: ${data.description}`);
        } else {
          alert("Procedure type not found");
        }
      } catch (error) {
        alert("Search failed: " + error.message);
      }
    } else {
      alert("Please enter a procedure name");
    }
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