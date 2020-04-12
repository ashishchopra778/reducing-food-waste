import React from 'react';

import Header from './../layout/Header'

function DashAlerts() {
  return (
    <div className="Dash-bg">
      <Header/>
      <div class="container-fluid pt-5 h-100">
        <div class="row h-100 pt-4">
          <div class="col-2 h-100 shadow-lg p-5 bg-white border border-light">
            <div class="container-fluid mt-5">NAV</div>
          </div>
          <div class="col-10">
            <div class="container h-75 mt-5">
            <div class="row h-50">
              <div class="col-12">
                <div class="row h-100">
                  <div class="col-6"> 
                    <div class="container h-100 bg-white shadow p-5 rounded"> Element</div> 
                  </div>
                  <div class="col-6">
                    <div class="container h-100 bg-white shadow p-5 rounded"> Element</div>  
                  </div>
                </div>
              </div>
            </div>
            <div class="row h-50 mt-4">
              <div class="col-12">
                <div class="row h-100">
                  <div class="col-6"> 
                      <div class="container h-100 bg-white shadow p-5 rounded"> Element</div> 
                  </div>
                  <div class="col-6">
                    <div class="container h-100 bg-white shadow p-5 rounded"> Element</div>  
                  </div>
                  </div>
                </div>
            </div>
            </div>
          </div>
        </div>
      </div>
  </div> 
  )
}

export default DashAlerts;