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
                    <div class="container h-100 bg-white shadow rounded"> 
                      <div class="embed-responsive embed-responsive-16by9">
                        <iframe width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0927d59e-54ed-47a6-a49b-2f86af043148&groupId=4001c553-d51b-4145-82b4-b02d62bc38ba&autoAuth=true&ctid=3ff6cfa4-e715-48db-b8e1-0867b9f9fba3&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWF1c3RyYWxpYS1zb3V0aGVhc3QtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D" frameborder="0" allowFullScreen="true"></iframe>
                      </div>
                    </div> 
                  </div>
                  <div class="col-6">
                    <div class="container h-100 bg-white shadow rounded"> 
                      <div class="embed-responsive embed-responsive-16by9">
                        <iframe width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=b2c7f30f-3343-47fe-a959-efe773743d0d&groupId=4001c553-d51b-4145-82b4-b02d62bc38ba&autoAuth=true&ctid=3ff6cfa4-e715-48db-b8e1-0867b9f9fba3&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWF1c3RyYWxpYS1zb3V0aGVhc3QtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D" frameborder="0" allowFullScreen="true"></iframe>                      </div>
                    </div>  
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