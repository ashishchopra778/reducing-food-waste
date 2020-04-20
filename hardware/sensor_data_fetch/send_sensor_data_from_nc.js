const dns = require('dns')
const net = require('net');
const HOST = '127.0.0.1';
const PORT = 2000;


var connectionString = "HostName=xxxxxxxxxx;DeviceId=xxxxxxx;SharedAccessKey=xxxxxxxxxxxx";
 
// use factory function from AMQP-specific package
var clientFromConnectionString = require('azure-iot-device-amqp').clientFromConnectionString;
 
// AMQP-specific factory function returns Client object from core package
var client = clientFromConnectionString(connectionString);
 
// use Message object from core package
var Message = require('azure-iot-device').Message;

var socket_client = new net.Socket();

socket_client.connect(PORT, HOST, function() {
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
});

socket_client.on('data', function(data) {
  console.log('Received data : ' + data.toString());
  
  try {
    json_data = JSON.parse(data.toString());
    console.log(json_data)

    payload = { deviceId: 'IBS_TH1_nc_satellite', temperature: json_data.payload[0], humidity: json_data.payload[1] }
    console.log("Connected to internet - sending data to cloud via satellite ...");
    var msg = new Message(JSON.stringify(payload));
    client.sendEvent(msg, function (err) {
    if (err) {
      console.log(err.toString());
    } else {
      console.log('Message sent' + msg.getData());
    };
    });
  } catch(err) {
    console.log(err.toString());
  }

});

socket_client.on('close', function() {
  console.log('Connection closed');
});