
export default function CaseComponent({file, name, price}) {
  
  return (
    <div>
        <img style={{width: "300px"}} src={`http://localhost:5000/${file.path}`} alt="" />
        <h2>{name}</h2>
        <p>{price/100}$</p>
    </div>
  )
}
