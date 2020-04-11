import React from 'react';

import Header from './../layout/Header'

function DashAlerts() {
  return (
    <div className="Dash-bg">
      <Header/>
      <div class="container-fluid pt-5 h-100">
        <div class="container-fluid pt-3 h-100">
        <div class="row h-100">
          <div class="col-2 border border-light h-100">
            <div class="element">NAV</div>
          </div>
          <div class="col-10">
            <div class="container h-75 mt-5">
            <div class="row h-50">
              <div class="col-12">
                <div class="row h-100">
                  <div class="col-6"> 
                    <div class="container border border-light h-100"> Element</div> 
                  </div>
                  <div class="col-6">
                    <div class="container border border-light h-100"> Element</div>  
                  </div>
                </div>
              </div>
            </div>
            <div class="row h-50 mt-4">
              <div class="col-12">
                <div class="row h-100">
                  <div class="col-6"> 
                      <div class="container border border-light h-100"> Element</div> 
                  </div>
                  <div class="col-6">
                    <div class="container border border-light h-100"> Element</div>  
                  </div>
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