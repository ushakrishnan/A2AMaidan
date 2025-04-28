
## Time
server
.venv\Scripts\activate
cd Time\server
python tell_time_server.py
`
 * Serving Flask app 'tell_time_server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [28/Apr/2025 18:43:31] "GET /.well-known/agent.json HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2025 18:43:31] "POST /tasks/send HTTP/1.1" 200 -
`

client
.venv\Scripts\activate
cd Time/client
python time_client.py
`
Connected to: TellTimeAgent – Tells the current time when asked.
Agent says: The current time is: 2025-04-28 18:43:31
`

## Echo
server
.venv\Scripts\activate
cd Echo\server
python echo_agent.py

`
 Running on all addresses (0.0.0.0)
 Running on http://127.0.0.1:5001
 Running on http://100.70.234.58:5001
Press CTRL+C to quit
127.0.0.1 - - [28/Apr/2025 18:26:26] "GET /.well-known/agent.json HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2025 18:27:25] "GET /.well-known/agent.json/.well-known/agent.json HTTP/1.1" 404 -
127.0.0.1 - - [28/Apr/2025 18:27:38] "GET /.well-known/agent.json HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2025 18:30:04] "GET /.well-known/agent.json HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2025 18:30:04] "POST /tasks/send HTTP/1.1" 200 -
`

client
.venv\Scripts\activate
cd Time/client
python client_agent.py

`Discovered Agent: EchoAgent
Agent Description: A simple agent that echoes back user messages.
Agent URL: http://localhost:5001
Agent's reply: Hello! You said: 'Hello, Agent!'
`
