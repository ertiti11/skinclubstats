
import useFetchData from "../api/cases";
import CaseComponent from "../components/CaseComponent";

export default function Home() {
  // Usa el custom hook con la URL deseada
  const { data, error, loading } = useFetchData(
    "http://127.0.0.1:5000/api/main-sections"
  );

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  var cases = [];
  var caseTypes = [];
  data.map((item) => {
    item.cases.map(() => {
      caseTypes.push(item.title);
      item.cases.map((cas) => {
        cases.push(cas);
      });
    });
  }, []);

  return (
    <div>
      <h1>Data</h1>
      <div className="flex flex-wrap w-full">
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
  );
};

