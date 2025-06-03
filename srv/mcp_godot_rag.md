### [A MCP server for Godot RAG](https://github.com/weekitmo/mcp_godot_rag)

````{tab} From source
```sh
git clone --depth=1 https://github.com/weekitmo/mcp_godot_rag
cd mcp_godot_rag
uv venv --python=3.12
.venv\Scripts\activate.bat
uv sync
cp .env.example .env.local
```

```sh
python download_godot_docs.py
uv pip install docutils
python convert_rst2md.py
python chunker.py -i artifacts
python vectorizer.py -i artifacts/chunks/artifacts_chunks_SZ_400_O_20.jsonl
python main.py -d artifacts/vector_stores/chroma_db -c artifacts_chunks_SZ_400_O_20_all-MiniLM-L6-v2
```
````

#### Setting

- Extension → Cline → Manage MCP Servers → Settings → Configure MCP Servers
	```json
	{
	  "mcpServers": {
	    "godot-rag": {
	      "command": "/path/to/mcp_godot_rag/.venv/Scripts/python.exe",
	      "args": [
	        "/path/to/mcp_godot_rag/main.py",
	        "-d",
	        "/path/to/mcp_godot_rag/artifacts/vector_stores/chroma_db",
	        "-c",
	        "artifacts_chunks_SZ_400_O_20_all-MiniLM-L6-v2"
	      ]
	    }
	  }
	}
	```