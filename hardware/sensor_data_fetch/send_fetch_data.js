const log4js = require('log4js')
const IBS_TH1 = require('./ibs_th1');

var connectionString = "HostName=Food-Supply-Chain.azure-devices.net;DeviceId=myRaspberryPi;SharedAccessKey=PZeS9YfawPmtEDzGXbH8CEHz64z8XYqvw2nPFGD7FSY=";
 
// use factory function from AMQP-specific package
var clientFromConnectionString = require('azure-iot-device-amqp').clientFromConnectionString;
 
// AMQP-specific factory function returns Client object from core package
var client = clientFromConnectionString(connectionString);
 
// use Message object from core package
var Message = require('azure-iot-device').Message;

log4js.getLogger('ibs_th1').level = 'trace';

const callback = data => {
  console.log(data.address, data.date, data.temperature, data.humidity,
	      data.probeType, data.battery);
	      var msg = new Message(JSON.stringify({ deviceId: 'IBS_TH1', temperature: data.temperature, humidity: data.humidity })); 

	client.sendEvent(msg, function (err) {
      if (err) {
        console.log(err.toString());
      } else {
        console.log('Message sent' + msg.getData());
      };
          });
};

const device = new IBS_TH1();
device.subscribeRealtimeData(callback);
console.log('Subscribed');

setTimeout(() => {
  device.unsubscribeRealtimeData();
  console.log('Unsubscribed');
  process.exit();
}, 1000000);
