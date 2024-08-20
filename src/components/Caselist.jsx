import {useState, useEffect} from 'react'
import axios from 'axios'
import CaseComponent from './CaseComponent'
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
    }
    , [URL]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    console.log(data)
  return (
    <div>
      <h1>Data</h1>
      <div className="flex flex-wrap w-full">
        <pre
        {data &&
          data.map((item) => {
            return (
              <div className="flex flex-col gap-8 mt-32 w-full" key={item.id}>
                <h1 className=" font-bold text-5xl">{item.name}</h1>
                <div className="flex flex-wrap w-full justify-between">
                  {item.cases.map((cas) => {
                    return (
                      <CaseComponent
                        key={cas.id}
                        file={cas.file}
                        name={cas.name}
                        casePrice={cas.price}
                      />
                    );
                  })}
                </div>
              </div>
            );
          })}
      </div>
    </div>
)
}
