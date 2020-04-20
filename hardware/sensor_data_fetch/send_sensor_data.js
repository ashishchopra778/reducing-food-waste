const log4js = require('log4js')
const IBS_TH1 = require('./ibs_th1');
const dns = require('dns')
const net = require('net');
const HOST = '10.42.0.82';
const PORT = 2001;
const DELAY = 10000;			// to send data every 10 seconds
const RECONNECT_DELAY = 10000; // reconnect delay of 10 seconds


var connectionString = "HostName=xxxxxxxxxx;DeviceId=xxxxxxx;SharedAccessKey=xxxxxxxxxxxx";
 
// use factory function from AMQP-specific package
var clientFromConnectionString = require('azure-iot-device-amqp').clientFromConnectionString;
 
// AMQP-specific factory function returns Client object from core package
var client = clientFromConnectionString(connectionString);
 
// use Message object from core package
var Message = require('azure-iot-device').Message;

log4js.getLogger('ibs_th1').level = 'trace';

var socket_client = new net.Socket();

const callback = data => {
  console.log(data.address, data.date, data.temperature, data.humidity,
		  data.probeType, data.battery); 
  setTimeout(
	proper_channel_send_data,
	DELAY,
	socket_client, data
  );
};

function connect_socket_client(socket_client){
	socket_client.connect(PORT, HOST, function() {
			  		console.log('CONNECTED TO: ' + HOST + ':' + PORT);
			  	});	
}

function proper_channel_send_data(socket_client, data){
  	dns.resolve('www.google.com', function(dns_err) {
		if (dns_err) {
			try{
			  	console.log("No internet connectivity - sending data via Mesh Network...");

			  	var msg = {
			  		  "objectType": "sendPayload",
			  		  "payloadType": "acknowledged",
			  		  "nodeId": 32,
			  		  "port": 0,
			  		  "payload": [
			  			  Math.round(data.temperature),
			  			  Math.round(data.humidity)
			  		  ]
			  	}
  				connect_socket_client(socket_client);
			  	socket_client.write(JSON.stringify(msg), function (err) {
			  	  if (err) {
			  		console.log(err.toString());
			  	  } else {
			  		console.log('Message sent : ' + JSON.stringify(msg));
			  	  };
			  	});

			} catch(other_err){
				console.log('other error !')
				console.log(other_err.toString());
			}

		} else {
		  console.log("Connected to internet - sending data to cloud directly...");
		  payload = { deviceId: 'IBS_TH1_direct', temperature: data.temperature, humidity: data.humidity }
		  var msg = new Message(JSON.stringify(payload));
		  client.sendEvent(msg, function (err) {
			if (err) {
			  console.log(err.toString());
			} else {
			  console.log('Message sent' + msg.getData());
			};
		  });
		}
  	});	
}


socket_client.on('data', function(data) {
	try{
		console.log('Received data : ' + data.toString());
	} catch(err){
		console.log(err.toString());
	}
});

socket_client.on('close', function() {
  console.log('Connection closed, reconnecting ...');
  try{
  	socket_client.connect(PORT, HOST, function() {
		console.log('CONNECTED TO: ' + HOST + ':' + PORT);
  	});
  } catch(err) {
  	console.log(err.toString());
  	console.log('Reconnecting after ' + RECONNECT_DELAY + ' milliseconds ...')
  	try {
  		setTimeout(
  			connect_socket_client,
  			RECONNECT_DELAY,
  			socket_client
  		);
  	} catch (second_err) {
  		console.log('Unable to re-establish connection');
  		console.log(second_err.toString());
  	}
  }
});

socket_client.on('error', function() {
	console.log('....');
});


const device = new IBS_TH1();
device.subscribeRealtimeData(callback);
console.log('Subscribed');

setTimeout(() => {
  device.unsubscribeRealtimeData();
  console.log('Unsubscribed');
  process.exit();
}, 1000000);
