import React, { useContext, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import { Form, Button } from "react-bootstrap";

export const UserProfile = () => {
  const { store, actions } = useContext(Context);

  const current_user_data = store.current_user_data;

  const [editUser, setEditUser] = useState();
  const handleInputChange = (e) => {
    setEditUser({ ...editUser, [e.target.name]: e.target.value });
  };

  const submitUser = (e) => {
    e.preventDefault();

    actions.updateUser(id, editUser.name, editUser.email, editUser.password);
  };
  const deleteUser = () => {
    actions.deleteUser(current_user_data.id);
  };

  return (
    <Form className="form">
      <Form.Group className="form-group my-2">
        <div className="col-md-10">
          <input
            defaultValue={current_user_data.name}
            className="form-control"
            id="name"
            maxLength="150"
            name="name"
            required=""
            type="text"
            onChange={handleInputChange}
          />
        </div>
      </Form.Group>
      <Form.Group className="form-group my-2">
        <div className="col-md-10">
          <input
            defaultValue={current_user_data.email}
            className="form-control"
            id="name"
            maxLength="150"
            name="name"
            required=""
            type="text"
            onChange={handleInputChange}
          />
        </div>
      </Form.Group>
      <Form.Group className="form-group my-2">
        <div className="col-md-10">
          <input
            defaultValue={current_user_data.password}
            className="form-control"
            id="name"
            maxLength="150"
            name="name"
            required=""
            type="password"
            onChange={handleInputChange}
          />
        </div>
      </Form.Group>

      <Button variant="primary" onClick={submitUser}>
        Actualizar
      </Button>
      <Button variant="danger" className="mx-3" onClick={deleteUser}>
        Eliminar cuenta
      </Button>
    </Form>
  );
};
