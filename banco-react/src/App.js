import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import TopBar from "./ui/TopBar";
import Home from "./ui/Home";

import ListaClientes from "./Clientes/ListaClientes";
import CrearCliente from "./Clientes/CrearCliente";
import EliminarCliente from "./Clientes/EliminarCliente";
import ActualizarCliente from "./Clientes/ActualizarCliente";

function App() {
  return (
    <Router>
      <div>
        <TopBar/>
        <Routes>

          <Route path="/clientes" element={<ListaClientes/>} />
          <Route path="/clientes/agregar" element={<CrearCliente/>} />
          <Route path="/clientes/eliminar/:id" element={<EliminarCliente/>} />
          <Route path="/clientes/actualizar/:id" element={<ActualizarCliente/>} />

          <Route path="/" element={<Home/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;