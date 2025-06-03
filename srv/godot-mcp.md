### [Godot MCP](https://github.com/Coding-Solo/godot-mcp)

````{tab} From source
```sh
git clone --depth=1 https://github.com/Coding-Solo/godot-mcp
cd godot-mcp
npm install
npm run build
```
````

#### Setting in VScode/VScodium

- Extension → Cline → Manage MCP Servers → Settings → Configure MCP Servers
	```json
	{
	  "mcpServers": {
	    "godot": {
	      "command": "node",
	      "args": ["/path/to/godot-mcp/build/index.js"],
	      "env": {
	        "DEBUG": "true" // Optional: Enable detailed logging
	      },
	      "disabled": false,
	      "autoApprove": [
	        "launch_editor",
	        "run_project",
	        "get_debug_output",
	        "stop_project",
	        "get_godot_version",
	        "list_projects",
	        "get_project_info",
	        "create_scene",
	        "add_node",
	        "load_sprite",
	        "export_mesh_library",
	        "save_scene",
	        "get_uid",
	        "update_project_uids"
	      ]
	    }
	  }
	}
	```