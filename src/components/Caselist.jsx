import { useState, useEffect } from 'react';
import axios from 'axios';
import CaseComponent from './CaseComponent';

export default function Caselist() {
  const URL = `http://localhost:5000/api/main`;

  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(URL);
        setData(response.data);
        setLoading(false);
      } catch (error) {
        setError(error);
      }
    };

    fetchData();
  }, [URL]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Data</h1>
      <div className="flex flex-wrap w-full">
        {
        data && data.map((caseData) => (
          console.log(caseData)))

        }
      </div>
    </div>
  );
}
