"""
We have a bin of robot parts in a factory. Each part goes to a robot with a specific, unique name. Each part will be described by a string, with the name of the robot and the part name separated by an underscore, like "Rocket_arm".

All robots are made of the same types of parts, and we have a string of all of the parts required to form a complete robot. Given a list of available parts, return the collection of robot names for which we can build at least one complete robot.

"""
from collections import defaultdict
def robotParts(allparts, required_parts_1):
    parts_map = defaultdict(set)
    for s in all_parts:
        temp = s.split("_")
        parts_map[temp[0]].add(temp[1])
    print(parts_map)
    res = []
    required_parts_set = set(required_parts_1.split(","))
    print(required_parts_set)
    for item, parts in parts_map.items():
        print(parts)
        if required_parts_set.issubset(parts):
            res.append(item)

    return res

all_parts = [
"Rocket_claw",
"Rocket_sensors",
"Dustie_case",
"Rust_sensors",
"Bolt_sensors",
"Rocket_case",
"Rust_case",
"Bolt_speaker",
"Rocket_wheels",
"Rocket_speaker",
"Dustie_case",
"Dustie_arms",
"Rust_claw",
"Dustie_case",
"Dustie_speaker",
"Bolt_case",
"Bolt_wheels",
"Rust_legs",
"Bolt_sensors" ]

required_parts_1 = "sensors,case,speaker,wheels"
required_parts_2 = "sensors,case,speaker,wheels,claw"
print(robotParts(all_parts,required_parts_2))
