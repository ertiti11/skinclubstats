import useFetchData from "./api/cases";
import { numofcases } from "./utils/numCases";
import CaseComponent from "./components/CaseComponent";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
export default function App() {
 
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}>
          
        </Route>
      </Routes>
    </BrowserRouter>
    
  );
};

