import sys
import json
from client import DifferentialEvolutionOptimizer

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-differential-evolution-vector-optimizer-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "optimize_function",
                    "description": "Optimize multi-dimensional continuous cost function using Differential Evolution",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "dims": {"type": "integer", "default": 2},
                            "max_iter": {"type": "integer", "default": 40},
                            "target_vector": {"type": "array", "items": {"type": "number"}}
                        }
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "optimize_function":
            dims = args.get("dims", 2)
            it = args.get("max_iter", 40)
            target = args.get("target_vector") or [0.5] * dims
            de = DifferentialEvolutionOptimizer()
            cost_fn = lambda p: sum((p[i] - target[i])**2 for i in range(dims))
            data = de.optimize(cost_fn, dims=dims, max_iter=it)
            res = {"content": [{"type": "text", "text": json.dumps(data)}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
