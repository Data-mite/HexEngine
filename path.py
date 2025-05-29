import random

# Directional deltas for octagonal grid
delta = {
    'N': (0, 1), 'NE': (1, 1), 'E': (1, 0), 'SE': (1, -1),
    'S': (0, -1), 'SW': (-1, -1), 'W': (-1, 0), 'NW': (-1, 1)
}
directions = list(delta.keys())

def generate_path(start_coord=(0, 0), num_tiles=10, seed=None):
    """
    Generates a forking path on an octagonal grid.

    Each tile will have one guaranteed exit and up to three additional exits
    depending on branch roll results. Only valid, unvisited coordinates
    are used to prevent overlap and ensure structural fidelity.

    Args:
        start_coord (tuple): Starting coordinate (default: (0, 0))
        num_tiles (int): Total number of nodes to generate
        seed (int, optional): Seed for random generator to ensure reproducibility

    Returns:
        list: List of node dictionaries with:
              - id: unique string identifier
              - entry: direction from which node was entered
              - exits: list of directions this node forks into
              - coord: (x, y) coordinate on grid
              - branch_rolls: list of roll values used to determine forks
    """
    if seed is not None:
        random.seed(seed)  # Ensure reproducible randomness if seed is given

    path = []          # Final list of completed node dictionaries
    queue = []         # Queue for nodes pending processing
    visited = set()    # Tracks fully processed coordinates
    seen_coords = set()# Prevents duplicate node creation
    id_counter = 0     # Incrementing ID for each node

    def next_id():
        nonlocal id_counter
        id_str = f"{id_counter:03}"
        id_counter += 1
        return id_str

    # Initialize path with starting node
    queue.append({
        "id": next_id(),
        "coord": start_coord,
        "entry": "START"
    })

    while queue and len(path) < num_tiles:
        node = queue.pop(0)
        nid = node["id"]
        coord = node["coord"]
        entry = node["entry"]

        if coord in visited:
            continue
        visited.add(coord)

        exits = []
        branch_rolls = []

        all_directions = directions[:]
        random.shuffle(all_directions)  # Randomize direction order per node
        tried_directions = set()

        # Always allow one guaranteed branch
        for d in all_directions:
            dx, dy = delta[d]
            new_coord = (coord[0] + dx, coord[1] + dy)
            if new_coord not in seen_coords and new_coord not in visited:
                seen_coords.add(new_coord)
                new_id = next_id()
                queue.append({
                    "id": new_id,
                    "coord": new_coord,
                    "entry": {v: k for k, v in delta.items()}[(-dx, -dy)]  # Reverse entry
                })
                exits.append(d)
                tried_directions.add(d)
                break  # Only one primary branch

        # Optional forks based on roll thresholds
        for threshold in [0.10, 0.05, 0.02]:
            roll = random.random()
            branch_rolls.append(roll)
            if roll < threshold:
                for d in all_directions:
                    if d in tried_directions:
                        continue
                    dx, dy = delta[d]
                    new_coord = (coord[0] + dx, coord[1] + dy)
                    if new_coord not in seen_coords and new_coord not in visited:
                        seen_coords.add(new_coord)
                        new_id = next_id()
                        queue.append({
                            "id": new_id,
                            "coord": new_coord,
                            "entry": {v: k for k, v in delta.items()}[(-dx, -dy)]
                        })
                        exits.append(d)
                        tried_directions.add(d)
                        break  # One exit per successful roll

        path.append({
            "id": nid,
            "entry": entry,
            "exits": exits,
            "coord": coord,
            "branch_rolls": branch_rolls  # Store roll data for transparency
        })

    return path
