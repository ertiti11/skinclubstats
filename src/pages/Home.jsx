
import CaseComponent from "../components/CaseComponent";
import React, { useState, useEffect} from "react";
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

  
  return (
    <div>
    {cases.map((caseData) => (
      <React.Fragment key={caseData.name}>
        {console.log(caseData)}        
      </React.Fragment>
    ))}
  </div>
  );
  
};



{/* <CaseComponent 
          ev={caseData.ev}
          image={caseData.image}
          irb={caseData.irb}
          price={caseData.price}
          profit_chance={caseData.profit_chance}
          profit_chanceX1dot5={caseData.profit_chanceX1dot5}
          profit_chanceX2={caseData.profit_chanceX2}
          profit_chanceX3={caseData.profit_chanceX3}
          profit_chanceX10={caseData.profit_chanceX10}
          real_price={caseData.real_price}
        /> */}