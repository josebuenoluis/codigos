import { Link } from "react-router-dom";
import novedades from "./novedades";
function Inicio() {
    return (
      <div>
        <h1>Esta es la página de inicio</h1>
        <Link to={novedades}>Haga click para novedades</Link>
      </div>
    );
  }
  
  export default Inicio;