import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
     <Navbar sticky="top" bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#cardMain">SightSense</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#card1">Features</Nav.Link>
            <Nav.Link href="#card2">Why</Nav.Link>
            <Nav.Link href="#card3">How</Nav.Link>
            <Nav.Link href="#card4">Demo</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
