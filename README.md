## Man in the Middle Attack 
This repo contains code and procedures involved in the course reseach of MitM attack. 

## How to run the server
You can download server.cpp and run it yourself, don't forget to include necessary libraries!
It is a little bit tricky to run the server, **first** find your NSP gateway for your network, and **then** portforward to your device IP and port 23456, **then** find your public IP by running $curl ifconfig.me. **Finally**, start up the server and you can query it using GET / POST method, curl/postman is recommended.
You can also try it with the python server. 
