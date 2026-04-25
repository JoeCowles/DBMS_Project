import { Navigate } from "react-router-dom";
import { getCurrentUser } from "./CurrentUser";

const ProtectedRoute = ({ children }) => {
  const user = getCurrentUser();
  if (!user?.id) {
    return <Navigate to="/login" replace />;
  }
  return children;
};

export default ProtectedRoute;
