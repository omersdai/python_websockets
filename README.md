The http.server library sends out a regular HTTP request with HTTP handshakes and then upgrades the connection to a WebSocket connection while websockets library directly establishes a WebSocket connection.

Due to the HTTP nature there is an additional overhead when it comes to the initial connection. After the HTTP request to upgrade the connection to WebSocket communication, the two libraries behave very identically as they are both using websockets to communicate.
So the http.server has higher latency at first but behaves very similarly after the initial connection. They are similar in terms of throughput and scalability because they both use websocket communication.
