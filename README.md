# iox-mqtt
A simple Python Serial-to-MQTT proxy PaaS application that runs in an IOx container.

---

## Deployment
Using the ioxclient you can run the following commands from this directory to deploy your application: 

### To Package the Application
`ioxclient package .`

*If you have difficulty packaging, review the packaging log and possibly try removing any git objects*

### To Deploy the Appllication 
`ioxclient service install iox_serial_mqtt package.tar.gz`

### To See Information about the Appllication
`ioxclient app info iox_serial_mqtt`

### To Upgrade the Application 
`ioxclient service upgrade iox_serial_mqtt package.tar.gz`

### To Uninstall the Application
`ioxclient service uninstall iox_serial_mqtt`

If you have any problems, you can Activate and Start your application via the IOx Local Manager or Fog Director.

---

## Utilities
You can use the included _write-serial.py_ script to simulate serial traffic.
Refer to [Accessing Serial Interface on IR829 through GOS](https://communities.cisco.com/docs/DOC-63003 "Accessing Serial Interface on IR829 through GOS") for more information on setting up the IOS configuration and wiring details.
