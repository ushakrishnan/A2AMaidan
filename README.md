## How to Download and Run the Project

### Step 1: Clone the Repository
1. Open a terminal or command prompt.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/ushakrishnan/A2AMaidan.git
   ```
3. Navigate to the cloned repository:
   ```bash
   cd A2AMaidan
   ```

### Step 2: Set Up the Environment
1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Run the Samples

#### Echo Agent
1. Start the Echo Agent server:
   ```bash
   python Echo/server/echo_agent.py
   ```
   The server will start and listen on `http://127.0.0.1:5001`.

2. Run the Echo Agent client:
   ```bash
   python Echo/client/client_agent.py
   ```
   You should see the agent's response in the terminal.

#### Time Agent
1. Start the Time Agent server:
   ```bash
   python Time/server/tell_time_server.py
   ```
   The server will start and listen on `http://127.0.0.1:5000`.

2. Run the Time Agent client:
   ```bash
   python Time/client/time_client.py
   ```
   You should see the agent's response with the current time in the terminal.


---

## Time
server
.venv\Scripts\activate
cd Time\server
python tell_time_server.py
```
 * Serving Flask app 'tell_time_server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [28/Apr/2025 18:43:31] "GET /.well-known/agent.json HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2025 18:43:31] "POST /tasks/send HTTP/1.1" 200 -
```

client
.venv\Scripts\activate
cd Time/client
python time_client.py
```
Connected to: TellTimeAgent – Tells the current time when asked.
Agent says: The current time is: 2025-04-28 18:43:31
```

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
