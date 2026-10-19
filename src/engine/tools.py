class ToolRegistry:
    def __init__(self):
        # Maps tool name to required role
        self.tools = {
            "delete_database": "admin",
            "get_public_info": "guest"
        }
    def execute_tool(self, tool_name: str, user_role: str) -> str:
        if tool_name not in self.tools:
            return f"Tool '{tool_name}' not found."
        required_role = self.tools[tool_name]
        if user_role != required_role and user_role != "admin":
            return f"BLOCKED: User role '{user_role}' is not authorized to execute '{tool_name}'."
        return f"SUCCESS: Tool '{tool_name}' executed."
