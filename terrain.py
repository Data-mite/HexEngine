import requests
import random
import re

def roll_from_table(table_id):
    try:
        response = requests.get(
            f'https://hexengine-dot-emotionengine.ue.r.appspot.com/getTableEntry?id={table_id}',
            headers={'Authorization': 'Basic chingasa'}
        )
        response.raise_for_status()
        table = response.json()
        narrative = table.get("narrative", "")

        entries = re.findall(r"(\d+(?:–\d+)?):?\s*(.*?)\n", narrative)
        roll = random.randint(1, 20)

        for entry in entries:
            range_str, result = entry
            if '–' in range_str:
                start, end = map(int, range_str.split('–'))
                if start <= roll <= end:
                    return result.strip()
            else:
                if int(range_str) == roll:
                    return result.strip()

        return f"??? (rolled {roll})"
    except Exception as e:
        print(f"Failed to roll from {table_id}: {e}")
        return '???'

def fetch_terrain_for_nodes(path_data):
    """
    For the first node, rolls Biome, then Terrain, then Feature from the HexEngine.
    Other nodes receive default terrain/feature.
    """
    for i, node in enumerate(path_data):
        if i == 0:
            biome = roll_from_table("HG_Biome")
            terrain_table = f"HG_Terrain_{biome.replace(' ', '').replace('+', '')}"
            terrain = roll_from_table(terrain_table)
            feature_table = f"HG_Feature_{biome.replace(' ', '').replace('+', '')}_{terrain.replace(' ', '')}"
            feature = roll_from_table(feature_table)

            node['biome'] = biome
            node['terrain'] = terrain
            node['feature'] = feature
        else:
            node['terrain'] = 'Default Terrain'
            node['feature'] = 'Default Feature'

if __name__ == "__main__":
    from path import generate_path
    path_data = generate_path(num_tiles=10)
    fetch_terrain_for_nodes(path_data)
    for node in path_data:
        print(f"{node['id']}: Biome={node.get('biome', '-')}, Terrain={node['terrain']}, Feature={node['feature']}")
