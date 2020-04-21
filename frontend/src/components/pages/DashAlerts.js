import React from 'react';
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Header from './../layout/Header'
import ContainerData from "./../layout/ContainerData";
import Shipping from "./../layout/Shipping";
import MyRecommendations from "./../layout/MyRecommendations"

function DashAlerts() {
  return (
    <HashRouter>
      <div className="Dash-bg">
      <Header/>
        <div class="container-fluid pt-5 h-100">
          <div class="row h-100 pt-4">
            <div className="header" class="col-2 h-100 shadow-lg pt-5 bg-white border border-dark">
              <div class="container h-100">             
                  <table class="table table-hover h-40">
                      <tr>
                        <td scope="row"><NavLink to="/">Dashboard</NavLink></td>
                      </tr>
                      <tr>
                        <td scope="row"><NavLink to="/in-progress">In Progress</NavLink></td>
                      </tr>
                      <tr>
                        <td  scope="row"><NavLink to="/shipping">Past Shipments</NavLink></td>
                      </tr>
                      <tr>
                        <td  scope="row"><NavLink to="/my-recommendations">My Recommendations</NavLink></td>
                      </tr>
                      <tr>
                        <td  scope="row"><NavLink to="/manage-dash">Manage My Dashboard</NavLink></td>
                      </tr>
                </table>
              </div>
            </div>
            <div class="col-10 h-75">
              <Route exact path="/" component={ContainerData}/>
              <Route path="/in-progress" component={Shipping}/>
              <Route path="/my-recommendations" component={MyRecommendations}/>
            </div>
          </div>
        </div>
      </div> 
    </HashRouter>
  )
}

export default DashAlerts;