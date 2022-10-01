import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/app.scss";
import { Col, Row, Form, Table } from "react-bootstrap";

export const Table_valla = () => {
  const { store, actions } = useContext(Context);
  const [query, setQuery] = useState("");


  //Filter by status
  const dataVallas = store.allVallas.filter((index) => {
    if (query === "") {
      return index;
    } else if (index.ode.toLowerCase().includes(query.toLowerCase())) {
      return index;
    } else if (index.status_id.toLowerCase().includes(query.toLowerCase())) {
      return index;
    }
  });

  return (
    <div>
      <div className="mx-2">
        {/* Filters at the top................................................................... */}

        <Row className="mb-1">
          <Col md={4}>
            <input
              onChange={(e) => setQuery(e.target.value)}
              type="text"
              className="form-control"
              id="inputSearch"
              placeholder="Search"
            ></input>
          </Col>
          <Col md={4}>
            <Form.Group>
              <select
                onChange={(e) => setQuery(e.target.value)}
                id="inputState"
                className="form-control"
              >
                <option defaultValue>Filtrar por estado...</option>
                <option>Arrendada</option>
                <option>Inactiva</option>
                <option>Reservada</option>
                <option>Deshabilitada</option>
              </select>
            </Form.Group>
          </Col>
          <Col md={4}>
            <Form.Group>
              <select id="inputState" className="form-control">
                <option defaultValue>Filtrar por provincia...</option>
                <option>San José</option>
                <option>Alajuela</option>
                <option>Heredia</option>
                <option>Cartago</option>
                <option>Puntarenas</option>
                <option>Guanacaste</option>
                <option>Limón</option>
              </select>
            </Form.Group>
          </Col>
        </Row>

        {/* Table content................................................................... */}

        <Table>
          <thead>
            <tr className="listheader  d-flex">
              <th className="col-1">Código</th>
              <th className="col-2">Nombre</th>
              <th className="col-2">Ruta</th>
              <th className="col-2">Sentido</th>
              <th className="col-1">Horiz/Vert</th>
              <th className="col-1">Tipo</th>
              <th className="col-1">Status</th>
              <th className="col-1">Cliente Id</th>
              <th className="col-1">Propietario Id</th>
            </tr>
          </thead>
          <tbody>
            {dataVallas.map((item, index) => {
              return (
                <tr
                  key={index}
                  // This dinamically changes the background color of the row
                  className={
                    item.status === "Arrendada" ? "arrendada " : "disponible "
                  }
                >
                  <td className="col-1 codeButton">
                    <Link to={"/sitedetail/" + index}>
                      <span>{item.code}</span>
                    </Link>
                  </td>
                  <td className="col-2">{item.name}</td>
                  <td className="col-2">{item.route}</td>
                  <td className="col-2">{item.view}</td>
                  <td className="col-1">{item.layout}</td>
                  <td className="col-1">{item.tipology}</td>
                  <td className="col-1">{item.status}</td>
                  <td className="col-1">{item.client_id}</td>
                  <td className="col-1">{item.owner_id}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      </div>
      <br />

      <Link to="/formValla">
        <button className="btn btn-primary"> + </button>
      </Link>
      {/* <DataGridx /> */}
    </div>
  );
};