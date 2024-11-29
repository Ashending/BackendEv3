import React ,{useEffect, useState} from "react";
import axios from "axios"
import { Link } from "react-router-dom";


function ListaClientes(){
    const [clientes, setClientes] = useState([]);
    useEffect(() => {
        const fetchClientes = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/clientes/?_size=500');
                setClientes(response.data);
            } catch (error) {
                console.log(error);
            }
        }; 
        fetchClientes(); 
    },[]);

    return(
        <div className="container">
            <h1>Lista de Clientes</h1>
            <hr></hr>
            <div className="mb-3">
                <a href="/clientes/agregar" className="btn btn-primary">Agregar Cliente</a>
            </div>
            <div className="card">
                <div className="card-header">Lista de Clientes</div>
                <div className="card-body">
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Id Cliente</th>
                                <th>Edad</th>
                                <th>Genero</th>
                                <th>Saldo</th>
                                <th>Estado Actividad</th>
                                <th>Nivel de satisfacción</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            {clientes.map((cliente) => (
                                <tr key={cliente.id_cliente}>
                                    <td>{cliente.id_cliente}</td>
                                    <td>{cliente.edad}</td>
                                    <td>{cliente.genero}</td>
                                    <td>{cliente.saldo}</td>
                                    <td>{cliente.estado_actividad}</td>
                                    <td>{cliente.nivel_satisfaccion}</td>
                                    <td> <Link to={`/clientes/eliminar/${cliente.id_cliente}`} className="btn btn-danger">Eliminar</Link></td> 
                                    <td> <Link to={`/clientes/actualizar/${cliente.id_cliente}`} className="btn btn-warning">Actualizar</Link></td>
                                </tr>
                            ) ) }
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}
export default ListaClientes;