# Remote MCP Server

A Python-based Model Context Protocol (MCP) server built with **FastMCP** that exposes mathematical operations, helper tools, and server metadata.

## Features

### Tools
1. **`add_two_numbers`**: Takes two floating-point numbers `a` and `b`, and returns their sum.
2. **`generate_random_number`**: Generates a random integer between 1 and 100 (inclusive).

### Resources
1. **`info://server_info`**: Contains information/metadata about the running server (name, version, capabilities, status, and supported transports).

---

## Installation

Ensure you have Python 3.13+ and the dependencies installed:

```bash
# Install dependencies using uv (or pip)
uv sync
```

---

## Running the Server

You can run the server in two modes:

### 1. Stdio Mode (Default)
Standard input/output mode is ideal for local integration with MCP clients (like Claude Desktop).

```bash
# Direct run
.venv\Scripts\python main.py

# Or via FastMCP CLI
.venv\Scripts\fastmcp run main.py
```

### 2. SSE Mode (Remote/HTTP Mode)
To host the server as a web service accessible over HTTP via Server-Sent Events (SSE):

```bash
.venv\Scripts\fastmcp run main.py --transport sse --host 0.0.0.0 --port 8000
```
This will start the server binding on `0.0.0.0` at port `8000`.

---

## Verification & Testing

You can use the FastMCP inspect/dev tool to view and test the tools/resources:

```bash
.venv\Scripts\fastmcp dev main.py
```
This spins up a local web inspector where you can interactively invoke `add_two_numbers` and `generate_random_number`, and view the `info://server_info` resource.
