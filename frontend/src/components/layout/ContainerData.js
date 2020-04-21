import React from 'react';

function ContainerData () {
  return (
    <div class="container h-100 mt-5"> 
      <div class="row h-100">
        <div class="col-12">
          <div class="container h-100 bg-white shadow rounded"> 
            <div class="embed-responsive embed-responsive-16by9">
              <iframe width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0927d59e-54ed-47a6-a49b-2f86af043148&groupId=4001c553-d51b-4145-82b4-b02d62bc38ba&autoAuth=true&ctid=3ff6cfa4-e715-48db-b8e1-0867b9f9fba3&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWF1c3RyYWxpYS1zb3V0aGVhc3QtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D" frameborder="0" allowFullScreen="true"></iframe>
            </div>
          </div> 
        </div>
      </div>       
    </div>
  )
}

export default ContainerData;