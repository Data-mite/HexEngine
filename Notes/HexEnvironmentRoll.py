# Hex Environment Generation via 3d20 Table Cascade

import random

# Compass Biome Table (first d20 roll)
HG_BIOME = {
    1: "Natural", 2: "Natural", 3: "Natural", 4: "Natural", 5: "Natural", 6: "Natural", 7: "Natural",
    8: "Unreal", 9: "Unreal", 10: "Unreal", 11: "Unreal",
    12: "Circle", 13: "Circle", 14: "Circle",
    15: "Chthonic", 16: "Chthonic",
    17: "Astral",
    18: "ScienceFiction", 19: "ScienceFiction",
    20: "OrganicConstruct"
}

# Simplified terrain and feature tables for Natural biome
HG_TERRAIN_NATURAL = {
    1: "Plains", 2: "Forest", 3: "Riverbank", 4: "Wetland", 5: "Desert",
    6: "Tundra", 7: "Prairie", 8: "TemperateForest", 9: "Highlands", 10: "Badlands",
    11: "Shoreline", 12: "Jungle", 13: "WoodlandEdge", 14: "Steppe", 15: "Alpine",
    16: "GlacialMoraine", 17: "CraterField", 18: "VolcanicSlope", 19: "SaltFlat", 20: "PetrifiedForest"
}

# Simulate remote feature table access (mocked)
FEATURE_TABLES = {
    "Natural_Forest": {i: f"Feature-Forest-{i}" for i in range(1, 21)},
    "Natural_Plains": {i: f"Feature-Plains-{i}" for i in range(1, 21)}
    # Extend as needed
}

def roll_d20():
    return random.randint(1, 20)

def roll_environment():
    d20_1 = roll_d20()
    biome_class = HG_BIOME[d20_1]

    # Roll for terrain type
    d20_2 = roll_d20()
    if biome_class == "Natural":
        terrain_type = HG_TERRAIN_NATURAL[d20_2]
    else:
        terrain_type = f"{biome_class}_Unknown"

    # Roll for feature
    d20_3 = roll_d20()
    feature_key = f"{biome_class}_{terrain_type}"
    feature_table = FEATURE_TABLES.get(feature_key, {})
    feature_detail = feature_table.get(d20_3, "Undescribed")

    terrain_form = f"{biome_class} / {terrain_type} / {feature_detail}"
    return terrain_form
