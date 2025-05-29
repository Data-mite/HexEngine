import json
from path import generate_path
from graph import render_path_with_networkx

if __name__ == "__main__":
    path = generate_path(num_tiles=10)
    print(json.dumps(path, indent=2))
    render_path_with_networkx(path)
