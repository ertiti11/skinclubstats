
import CaseComponent from "../components/CaseComponent";
import { useState, useEffect} from "react";
export default function Home() {
  // Usa el custom hook con la URL deseada
    const URL = "http://127.0.0.1:5000/api/main"

  const [cases, setData] = useState([]);

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(URL);
        const data = await response.json();
        setData(data);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [URL]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  console.log(typeof(cases))

  return (
    <div>
      {cases.map((caseData) => (
        console.log(caseData)
      ))}
    </div>
  );
  
};

