import { useState, useEffect } from "react";
import axios from "axios";

export default function CaseComponent({ file, name, casePrice }) {
  const URL = `http://localhost:5000/api/cases/${name}`;

  const [skins, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(URL);
        setData(response.data); // Ajustar esto según la estructura de la respuesta
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

  // Inicializar variables
  var profitChance = 0;
  var doubleChance = 0;
  var oneFiveChance = 0;
  var tripeChance = 0;
  var x10Chance = 0;
  var minSkinPrice = Infinity;
  var EV = 0;

  const casePriceNum = Number(casePrice);

  skins.forEach((skin) => {
    const skinPrice = Number(skin.price);
    const skinChance = Number(skin.chance);

    if (isNaN(skinPrice) || isNaN(casePriceNum) || isNaN(skinChance)) {
      console.error(`Valores inválidos detectados: skinPrice=${skin.price}, casePrice=${casePrice}, skinChance=${skin.chance}`);
      return;
    }

    // Actualizar el precio de la skin más barata
    if (skinPrice < minSkinPrice) {
      minSkinPrice = skinPrice;
    }

    // Calcular EV (Valor Esperado)
    EV += (skinPrice * skinChance) / 100;

    if (skinPrice >= casePriceNum) {
      if (skinPrice >= casePriceNum * 2) {
        doubleChance += skinChance;
      }
      if (skinPrice >= casePriceNum * 1.5) {
        oneFiveChance += skinChance;
      }
      if (skinPrice >= casePriceNum * 3) {
        tripeChance += skinChance;
      }
      if (skinPrice >= casePriceNum * 10) {
        x10Chance += skinChance;
      }

      profitChance += skinChance;
    }
  });

  // Calcular realPrice
  var realPrice = casePriceNum - minSkinPrice;

  // Calcular el beneficio esperado de cada tipo
  var expectedProfit = (profitChance / 100) * (realPrice - casePriceNum);
  var expectedOneFiveProfit = (oneFiveChance / 100) * (casePriceNum * 1.5 - casePriceNum);
  var expectedDoubleProfit = (doubleChance / 100) * (casePriceNum * 2 - casePriceNum);
  var expectedTripleProfit = (tripeChance / 100) * (casePriceNum * 3 - casePriceNum);

  // Calcular el ratio beneficio/riesgo usando EV

  // Calcular el índice de riesgo/beneficio (IRB)
  var IRB = (EV * (profitChance + 0.5 * oneFiveChance + 0.75 * doubleChance + tripeChance)) / casePriceNum;

  return (
    <div>
      <img style={{ width: "300px" }} src={`http://localhost:5000/${file.path}`} alt="" />
      <h2>{name.replace("-", " ").replace("_", " ")}</h2>
      <p>Price: {casePrice / 100}$</p>
      <p>Real price: {realPrice / 100}$</p>
      <p>Profit chance: {profitChance}%</p>
      <p>x1.5 chance: {oneFiveChance}%</p>
      <p>x2 chance: {doubleChance}%</p>
      <p>x3 chance: {tripeChance}%</p>
      <p>x10 chance: {x10Chance}%</p>
      <p>Expected Value (EV): {(EV / 100).toFixed(2)}$</p>
      <p>Risk/Benefit Index (IRB): {IRB.toFixed(2)}</p>
    </div>
  );
}
