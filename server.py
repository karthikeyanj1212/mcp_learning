from fastmcp import FastMCP
import os
import json

# Get port from environment (Railway sets this)
PORT = int(os.environ.get("PORT", 8000))
HOST = "0.0.0.0"  # Important: bind to all interfaces

mcp = FastMCP(name="Cloud MCP Server")

# ============ YOUR TOOLS ============

@mcp.tool()
def get_employee(employee_id: str) -> str:
    """Get employee information by ID."""
    employees = {
        "101": {"name": "Alice", "role": "Developer", "salary": 95000},
        "102": {"name": "Bob", "role": "Designer", "salary": 85000},
        "103": {"name": "Carol", "role": "Manager", "salary": 110000},
    }
    emp = employees.get(employee_id, {"error": "Employee not found"})
    return json.dumps(emp)

@mcp.tool()
def list_employees() -> str:
    """List all employees."""
    employees = [
        {"id": "101", "name": "Alice", "role": "Developer"},
        {"id": "102", "name": "Bob", "role": "Designer"},
        {"id": "103", "name": "Carol", "role": "Manager"},
    ]
    return json.dumps(employees)

@mcp.tool()
def calculate_bonus(salary: float, rating: float) -> str:
    """Calculate bonus based on salary and performance rating (1-5)."""
    bonus_pct = rating * 5  # 5% to 25%
    bonus = salary * (bonus_pct / 100)
    return json.dumps({
        "salary": salary,
        "rating": rating,
        "bonus_percentage": f"{bonus_pct}%",
        "bonus_amount": bonus
    })

# ============ HEALTH CHECK ============

@mcp.tool()
def health_check() -> str:
    """Check if server is running."""
    return json.dumps({"status": "healthy", "server": "Cloud MCP"})

# ============ RUN SERVER ============

if __name__ == "__main__":
    print(f"🚀 Starting MCP Server on {HOST}:{PORT}")
    mcp.run(transport="sse", host=HOST, port=PORT)
