# Online Shopping Behavior Analysis
This project analyzes online shopping behavior between men and women using a Flask web application and real-time data streaming with Kafka. The application serves as a live dashboard that visualizes consumer behavior by continuously consuming and processing data.


## Key Features
* Real-Time Data Processing: Utilizes Kafka to consume messages that contain shopping behavior data, distinguishing between male and female shopping patterns.
* WebSocket Integration: Implements Flask-SocketIO to establish real-time communication between the server and client, ensuring instantaneous updates on shopping behavior statistics.
* Data Visualization: Emits processed data to the front end for live display, allowing users to observe trends and insights regarding male and female shopping habits.
* Background Processing: Runs a separate background thread to handle incoming Kafka messages, processing the data and emitting results to connected clients.

## Technologies Used
* Flask: For creating the web application.
* Flask-SocketIO: For real-time bidirectional communication.
* Kafka: For streaming data consumption.
* HTML/CSS: For front-end rendering.
