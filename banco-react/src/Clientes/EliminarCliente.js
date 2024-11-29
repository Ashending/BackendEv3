import React, {useState, useEffect} from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";


function EliminarCliente(){
    const [cliente, setCliente] = useState([]);
    const [error, setError] = useState("");
    const navigate = useNavigate();
    let {id} = useParams();

    const cargarDatosClientes = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/api/cliente/${id}`)
            setCliente (response.data[0]);
        } catch (error) {
            console.log(error)
        }
    };

    useEffect(() => {
        cargarDatosClientes();
    },[cargarDatosClientes]);

    const onSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.delete(`http://localhost:8000/api/cliente/${id}`);
            navigate("/clientes")
        } catch (error) {
            console.log(error)
            if (error.response) {
                setError("Se ha producido un error:" || error.response.statusText);
            }
        }
    }

    return(
        <div className="container">
            <h1>Eliminar Cliente</h1>
            <hr></hr>
            {error && (
                <div className="alert alert-danger" role="alert">
                    {error}
                </div>
            )}
            <div className="card">
                <div className="card-header">Confirme la eliminación del cliente</div>
                <div className="card-body">
                    <h1>¿Desea eliminar a este cliente?</h1>
                    <h2>{cliente && cliente.nombres} {cliente.id_cliente}</h2>
                    <button type="submir" className="btn btn-primary" onClick={onSubmit}>Eliminar cliente</button>
                </div>
            </div>
        </div>
    )
}
export default EliminarCliente;