// Threshold Path Hex Generation - Conceptual Logic

from random import choice, randint, random

# Compass directions for hex navigation
DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
INVERSE_DIRECTION = {
    "N": "S", "NE": "SW", "E": "W", "SE": "NW",
    "S": "N", "SW": "NE", "W": "E", "NW": "SE"
}

# Base structure of a generated hex
def generate_hex(hex_id, from_direction=None, continuity_from=None):
    entry_direction = INVERSE_DIRECTION[from_direction] if from_direction else choice(DIRECTIONS)
    
    # Start with 1 mandatory exit (not entry direction)
    possible_exits = [d for d in DIRECTIONS if d != entry_direction]
    exit_directions = [choice(possible_exits)]
    
    # Roll for additional exits
    chances = [(10, 1), (5, 1), (1, 3)]  # [(chance%, max_attempts)]
    used = set(exit_directions + [entry_direction])
    
    for chance, max_attempts in chances:
        for _ in range(max_attempts):
            if random() * 100 <= chance:
                candidates = [d for d in DIRECTIONS if d not in used]
                if candidates:
                    new_exit = choice(candidates)
                    exit_directions.append(new_exit)
                    used.add(new_exit)

    terrain_form = "Sigil Causeway"  # Placeholder — will pull from table
    mood = "Sacred Anticipation"     # Placeholder — will pull from table

    hex_data = {
        "hex_id": hex_id,
        "entry_direction": entry_direction,
        "exit_directions": exit_directions,
        "terrain_form": terrain_form,
        "mood": mood,
        "continuity_from": continuity_from or [],
        "continuity_roll": randint(1, 9),
        "backtrack_possible": INVERSE_DIRECTION[entry_direction] in exit_directions
    }

    return hex_data

# Display exits in Zork-style description
def describe_exits(current_hex, known_hexes):
    entry_inverse = INVERSE_DIRECTION[current_hex["entry_direction"]]
    descriptions = []

    for dir in current_hex["exit_directions"]:
        label = f"{dir} - "
        if dir == entry_inverse:
            label += "(Back) "

        # Simulate known hex lookup
        connected_id = f"X{dir}"  # Dummy placeholder
        target_hex = known_hexes.get(connected_id)

        if target_hex:
            terrain = target_hex["terrain_form"]
            visited = target_hex.get("visited", False)
            label += terrain + ("" if visited else " [Vague Detail]")
        else:
            label += "Unknown Terrain [Unseen]"

        descriptions.append(label)

    return "\n".join(descriptions)
