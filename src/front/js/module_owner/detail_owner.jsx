import React, { useContext, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import { Modal } from "react-bootstrap";
import logo from "../../img/logo-publiex.png";
import { Button, Stack, Container, Col, Row, Image } from "react-bootstrap";
import { FormUpdateOwner } from "../module_owner/form_udpate_owner";

export const DetailOwner = () => {
  const { store, actions } = useContext(Context);
  const params = useParams(); //////////////////////////// get  owner id from the URL
  const id = params.id; ////////////////////////////////// store owner id as a variable

  const dataOwners = store.allOwners; /////////////////////////////Get all owners from store
  const dataOrders = store.allOrders;

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => {
    setShow(true);
    actions.resetDeleteOwnerMessage();
  };

  useEffect(() => {
    /////////////////////////////////////// sends owner id as a parameter to the flux
    actions.getSingleOwner(id);
  }, []);

  const singleOwner = store.singleOwner;

  return (
    <Container className="detail-owner-box py-4">
      <Row>
        <Col className="detail-owner-img">
          <div>
            <Image src={logo} style={{ height: "15vh", width: "20rem" }} />
          </div>
        </Col>
      </Row>

      <Row>
        <Col className="detail-owner-name py-3 ">
          <h3 className="title-blue">{singleOwner.name}</h3>
        </Col>
      </Row>
      <hr className="mt-0"></hr>

      <Row className="detail-info ">
        <Col>
          <Col className="py-1">
            <p>Código: {singleOwner.code}</p>
          </Col>
          <Col className="py-1">
            <p>Compañía: {singleOwner.company}</p>
          </Col>
          <Col className="py-1">
            <p>Email: {singleOwner.email}</p>
          </Col>
          <Col className="py-1">
            <p>Teléfono 1: {singleOwner.phone1}</p>
          </Col>
          <Col className="py-1">
            <p>Teléfono 2: {singleOwner.phone2}</p>
          </Col>
          <Col className="py-1">
            <p>Dirección:{singleOwner.address}</p>
          </Col>
          <Col className="py-1">
            <p>Nota:{singleOwner.comment}</p>
          </Col>
        </Col>
      </Row>
      <hr></hr>

      <Stack direction="horizontal" gap={2} className="mx-auto mt-3 justify-content-center">
        <Link to="/app">
          <button className="btn btn-primary  mx-2">Retornar</button>
        </Link>
        <Button variant="danger" onClick={handleShow}>
          Editar
        </Button>
        <Modal size="lg" show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Editar Owner</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <FormUpdateOwner />
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Cancelar
            </Button>
          </Modal.Footer>
        </Modal>
      </Stack>
    </Container>
  );
};