# Generated-by: Cursor (claude-4-sonnet)
"""
Example MCP Server implementation.

This is a template for creating an MCP (Model Context Protocol) server.
Uncomment and customize based on your MCP server needs.

To enable MCP functionality:
1. Uncomment the MCP dependencies in pyproject.toml
2. Uncomment the MCP script entry point in pyproject.toml
3. Customize this server implementation
4. Run `make mcp-cursor` to configure Cursor integration
"""

# Uncomment these imports when building an MCP server
# import asyncio
# import logging
# from typing import Any, Sequence
#
# from mcp.server import Server
# from mcp.server.models import InitializationOptions
# from mcp.server.stdio import stdio_server
# from mcp.types import (
#     CallToolRequest,
#     CallToolResult,
#     ListToolsRequest,
#     TextContent,
#     Tool,
# )
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# # Create server instance
# server = Server("template-python")
#
#
# @server.list_tools()
# async def handle_list_tools() -> list[Tool]:
#     """List available tools."""
#     return [
#         Tool(
#             name="example_tool",
#             description="An example tool that demonstrates MCP server functionality",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "message": {
#                         "type": "string",
#                         "description": "A message to process"
#                     }
#                 },
#                 "required": ["message"]
#             }
#         )
#     ]
#
#
# @server.call_tool()
# async def handle_call_tool(
#     name: str, arguments: dict[str, Any] | None
# ) -> list[TextContent]:
#     """Handle tool calls."""
#     if name == "example_tool":
#         message = arguments.get("message", "") if arguments else ""
#         result = f"You said: {message}"
#
#         return [
#             TextContent(
#                 type="text",
#                 text=result
#             )
#         ]
#     else:
#         raise ValueError(f"Unknown tool: {name}")
#
#
# async def main() -> None:
#     """Run the MCP server."""
#     logger.info("Starting MCP server...")
#
#     async with stdio_server() as (read_stream, write_stream):
#         await server.run(
#             read_stream,
#             write_stream,
#             InitializationOptions(
#                 server_name="template-python",
#                 server_version="0.1.0",
#                 capabilities=server.get_capabilities(
#                     notification_options=None,
#                     experimental_capabilities=None,
#                 ),
#             ),
#         )
#
#
# if __name__ == "__main__":
#     # Uncomment to run the MCP server
#     # asyncio.run(main())
#     print("MCP server template - uncomment code to enable MCP functionality")


def main() -> None:
    """Placeholder main function for MCP server."""
    print(
        "MCP server template - edit src/template_python/mcp_server.py to implement your MCP server",
    )
    print("See comments in the file for implementation guidance")


if __name__ == "__main__":
    main()
