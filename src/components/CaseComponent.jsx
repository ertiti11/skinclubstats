

export default function CaseComponent({ ev, image, irb, price, profit_chance, profit_chanceX1dot5, profit_chanceX2,  profit_chanceX3, profit_chanceX10, real_price, name }) {
  return (
    <div>
      <img style={{ width: "300px" }} src={`http://localhost:5000/${image}`} alt="" />
      <h2>{name}</h2>
      <p>Price: {price / 100}$</p>
      <p>Real price: {real_price / 100}$</p>
      <p>Profit chance: {profit_chance}%</p>
      <p>x1.5 chance: {profit_chanceX1dot5}%</p>
      <p>x2 chance: {profit_chanceX2}%</p>
      <p>x3 chance: {profit_chanceX3}%</p>
      <p>x10 chance: {profit_chanceX10}%</p>
      <p>Expected Value (EV): {(ev / 100).toFixed(2)}$</p>
      <p>Risk/Benefit Index (IRB): {irb}</p>
    </div>
  );
}
