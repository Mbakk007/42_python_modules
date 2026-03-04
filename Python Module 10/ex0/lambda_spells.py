from typing import List, Dict
# lambda is used to create short, one-line functions.


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        raise ValueError("Mage list cannot be empty")
    try:
        max_power = max(mages, key=lambda x: x['power'])['power']
        min_power = min(mages, key=lambda x: x['power'])['power']
        avg_power = round(sum(mage['power'] for mage in mages) / len(mages), 2)
    except Exception as e:
        print(f"{e}")
    return {'max_power': max_power,
            'min_power': min_power,
            'avg_power': avg_power}


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Support'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'Offense'},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) comes before "
          f"{sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")
    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
