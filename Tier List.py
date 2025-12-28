tier_list={"S":["Linear Algebra","MultivariableCalc"],"A":["Intro to Stats", "Further Math models"],
           "B":["Sohcastic Calc"],"C":["SQL","Linear Regression"],"D":["Probability Distributions"]}

def add_to_tier(tier, item):
    if tier in tier_list:
        tier_list[tier].append(item)
        print(f"Added '{item}' to tier {tier}")
    else:
        print("Invalid tier!")

def remove_from_tier(tier, item):
    if tier in tier_list and item in tier_list[tier]:
        tier_list[tier].remove(item)
        print(f"Removed '{item}' from tier {tier}")
    else:
        print(f"Item '{item}' not found in tier {tier}")

def move_between_tiers(item, old_tier, new_tier):
    if old_tier in tier_list and item in tier_list[old_tier]:
        tier_list[old_tier].remove(item)
        tier_list[new_tier].append(item)
        print(f"Moved '{item}' from tier {old_tier} to tier {new_tier}")
    else:
        print(f"Item '{item}' not found in tier {old_tier}")

def print_tier_list():
    print("\nCurrent Tier List:")
    for tier in ["S", "A", "B", "C", "D"]:
        print(f"{tier}: {tier_list[tier]}")
