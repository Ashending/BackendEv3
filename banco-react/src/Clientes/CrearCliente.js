import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function CrearClientes() {
    const [id_cliente, setIdCliente] = useState("");
    const [edad, setEdad] = useState("");
    const [genero, setGenero] = useState("");
    const [saldo, setSaldo] = useState("");
    const [estado_actividad, setEstadoActividad] = useState("");
    const [nivel_satisfaccion, setNivelSatisfaccion] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const volverAtras = () => {
        navigate(-1);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:8000/api/cliente', {
                id_cliente,
                edad,
                genero,
                saldo,
                estado_actividad,
                nivel_satisfaccion
            });
            navigate("/clientes");
        } catch (error) {
            console.error(error);
            if (error.response) {
                setError("Se ha producido un error:" || error.response.statusText);
            }
        }
    };

    return (
        <div className="container">
            <h1>Agregar Cliente</h1>
            <hr></hr>
            {error && (
                <div className="alert alert-danger" role="alert">
                    {error}
                </div>
            )}
            <div className="card">
                <div className="card-header">Complete los datos del nuevo cliente</div>
                <div className="card-body">
                    <form onSubmit={onSubmit}>
                        <div className="form-group">
                            <label>Id Cliente</label>
                            <input type="number" className="form-control" value={id_cliente} onChange={(e) => setIdCliente(e.target.value)} />
                            <label>Edad</label>
                            <input type="number" className="form-control" value={edad} onChange={(e) => setEdad(e.target.value)} />
                            <label>Genero</label>
                            <input type="text" className="form-control" value={genero} onChange={(e) => setGenero(e.target.value)} />
                            <label>Saldo</label>
                            <input type="text" className="form-control" value={saldo} onChange={(e) => setSaldo(e.target.value)} />
                            <label>Estado actividad</label>
                            <input type="email" className="form-control" value={estado_actividad} onChange={(e) => setEstadoActividad(e.target.value)} />
                            <label>Nivel de satisfaccion</label>
                            <input type="number" className="form-control" value={nivel_satisfaccion} onChange={(e) => setNivelSatisfaccion(e.target.value)} />
                            <button type="submit" className="btn btn-primary">Crear Cliente</button>
                            <button type="button" className="btn btn-secondary" onClick={volverAtras}>Cancelar</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default CrearClientes;
