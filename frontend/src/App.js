import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import "./App.css";
import About from "./components/pages/About";
import Login from './components/pages/Login';
import DashAlerts from './components/pages/DashAlerts';

// import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/about" component={About} />
        <Route path="/dash-alerts" component={DashAlerts} />
        <Route path="/" component={Login} />
      </Switch>
    </Router>
  );
}

export default App;

