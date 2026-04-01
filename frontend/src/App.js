import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/login/Login"; 
import DocumentViewer from "./pages/documentViewer/DocumentViewer"; 
import Search from "./pages/search/Search"; 
import RequestAccess from "./pages/requestAccess/RequestAccess";
import Landing from "./pages/landing/Landing";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/requestAccess" element={<RequestAccess />} />  
        <Route path="/search" element={<Search />} />
        <Route path="/documentViewer" element={<DocumentViewer />} />
      </Routes>
    </Router>
  );
}

export default App;
