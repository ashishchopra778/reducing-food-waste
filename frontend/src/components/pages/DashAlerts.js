import React from 'react';
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Header from './../layout/Header'
import ContainerData from "./../layout/ContainerData";
import Shipping from "./../layout/Shipping";

function DashAlerts() {
  return (
    <HashRouter>
      <div className="Dash-bg">
      <Header/>
        <div class="container-fluid pt-5 h-100">
          <div class="row h-100 pt-4">
            <div className="header" class="col-2 h-100 shadow-lg pt-5 bg-white border border-dark">
                <h5 style={{color:'#4fa4ff'}}>Alerts</h5>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <td scope="row"><NavLink to="/">In Progress</NavLink></td>
                    </tr>
                  </thead>
                  <thead>
                    <tr>
                      <td scope="row"><NavLink to="/shipping">Past Shipments</NavLink></td>
                    </tr>
                  </thead>
                </table>
            </div>
            <div class="col-10 h-75">
              <Route exact path="/" component={ContainerData}/>
              <Route path="/shipping" component={Shipping}/>
            </div>
          </div>
        </div>
      </div> 
    </HashRouter>
  )
}

export default DashAlerts;