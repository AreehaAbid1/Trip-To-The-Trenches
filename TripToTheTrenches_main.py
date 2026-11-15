import os
import time

from zone import Zone
from creatures import Creatures

os.system("")  # makes the colors work in the Windows terminal

# =====================================================================
#  COLORS AND VISUAL HELPERS
# =====================================================================
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# The zones in order from the surface down (used for the depth meter and for sorting by zone)
ZONE_ORDER = ["Epipelagic", "Mesopelagic", "Bathypelagic", "Abyssopelagic", "Hadopelagic"]

# Each zone gets its own color, getting darker/scarier as you go down
ZONE_COLORS = {
    "Epipelagic": "\033[96m",
    "Mesopelagic": "\033[94m",
    "Bathypelagic": "\033[34m",
    "Abyssopelagic": "\033[95m",
    "Hadopelagic": "\033[91m",
}

SUBMARINE = r"""
         ___
    ____/___\____
   /  o   o   o  \_____
  <__________________(@)>
"""


def type_print(text, color="", delay=0.02):
    """Prints text one letter at a time, like a ship's computer typing."""
    print(color, end="")
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print(RESET)


def show_zone(zone):
    """Shows a zone's banner, depth meter and description."""
    color = ZONE_COLORS[zone.name]
    level = ZONE_ORDER.index(zone.name) + 1
    meter = "#" * level + "-" * (5 - level)
    print(color + "=" * 52)
    print(f"  {zone.name.upper()}   ({zone.depth})")
    print(f"  Depth meter: [{meter}]  zone {level} of 5")
    print("=" * 52 + RESET)
    type_print(zone.description, color)


def show_creature(c):
    """Shows all the details of one creature."""
    glow = "Yes" if c.bioluminescent else "No"   # short if/else on one line
    danger_bar = "#" * c.danger_level + "-" * (5 - c.danger_level)
    color = ZONE_COLORS[c.zone]
    print(color + "-" * 52)
    print(f"  {c.name.upper()}")
    print("-" * 52 + RESET)
    print(f"  Zone:           {c.zone}")
    print(f"  Depth:          {c.depth} m")
    print(f"  Danger level:   [{danger_bar}] {c.danger_level} of 5")
    print(f"  Bioluminescent: {glow}")
    type_print("  Fact: " + c.fact, WHITE, 0.01)


# =====================================================================
#  CREATURE DATA  (the 22 creatures, kept in ALPHABETICAL order per zone
#  so that binary search works)
#  Order inside Creatures(): name, zone, depth, danger_level, bioluminescent, fact
# =====================================================================

# ---------- EPIPELAGIC (0-200m) ----------
blue_whale = Creatures("Blue Whale", "Epipelagic", 100, 1, False, "The largest animal known to have ever lived.")
bottlenose_dolphin = Creatures("Bottlenose Dolphin", "Epipelagic", 50, 1, False, "Uses echolocation to find prey.")
clownfish = Creatures("Clownfish", "Epipelagic", 10, 1, False, "Lives among anemone tentacles, protected by its mucus coating.")
great_white_shark = Creatures("Great White Shark", "Epipelagic", 150, 4, False, "An apex predator that keeps replacing lost teeth throughout its life.")
manta_ray = Creatures("Manta Ray", "Epipelagic", 50, 1, False, "Has a wingspan of up to about 7 meters.")

epipelagic_creatures = [blue_whale, bottlenose_dolphin, clownfish, great_white_shark, manta_ray]

# ---------- MESOPELAGIC (200-1000m) ----------
barreleye = Creatures("Barreleye", "Mesopelagic", 700, 1, False, "Has a transparent head and tube-shaped eyes that rotate upward.")
giant_squid = Creatures("Giant Squid", "Mesopelagic", 600, 2, False, "Its eyes are about as big as a dinner plate, among the largest in the animal kingdom.")
hatchetfish = Creatures("Hatchetfish", "Mesopelagic", 400, 1, True, "Lights up its belly to hide its silhouette from predators below.")
lanternfish = Creatures("Lanternfish", "Mesopelagic", 500, 1, True, "One of the most abundant fish on Earth, rising toward the surface each night.")
sperm_whale = Creatures("Sperm Whale", "Mesopelagic", 900, 2, False, "One of the deepest-diving mammals, hunting squid in the dark.")
vampire_squid = Creatures("Vampire Squid", "Mesopelagic", 800, 1, True, "Neither a squid nor a vampire; it escapes by releasing glowing mucus.")

mesopelagic_creatures = [barreleye, giant_squid, hatchetfish, lanternfish, sperm_whale, vampire_squid]

# ---------- BATHYPELAGIC (1000-4000m) ----------
anglerfish = Creatures("Anglerfish", "Bathypelagic", 1500, 3, True, "A glowing lure on its head attracts prey in total darkness.")
cookiecutter_shark = Creatures("Cookiecutter Shark", "Bathypelagic", 1200, 2, True, "Bites cookie-shaped plugs out of larger animals, and even submarine sonar domes.")
fangtooth = Creatures("Fangtooth", "Bathypelagic", 2000, 3, False, "Its teeth are so large it has pockets in its mouth to hold them when it closes.")
gulper_eel = Creatures("Gulper Eel", "Bathypelagic", 2500, 2, True, "Has a huge expandable mouth and a light at the tip of its tail.")
viperfish = Creatures("Viperfish", "Bathypelagic", 1600, 3, True, "Has long fangs and a glowing lure.")

bathypelagic_creatures = [anglerfish, cookiecutter_shark, fangtooth, gulper_eel, viperfish]

# ---------- ABYSSOPELAGIC (4000-6000m) ----------
dumbo_octopus = Creatures("Dumbo Octopus", "Abyssopelagic", 4500, 1, False, "Flaps its ear-like fins to swim; one of the deepest-living octopuses.")
faceless_cusk = Creatures("Faceless Cusk", "Abyssopelagic", 4000, 1, False, "Found at about 4,000m during a 2017 expedition off eastern Australia; its mouth is on its underside.")
sea_pig = Creatures("Sea Pig", "Abyssopelagic", 4800, 1, False, "A sea cucumber that walks on tube feet.")
supergiant_amphipod = Creatures("Supergiant Amphipod", "Abyssopelagic", 5500, 1, False, "A crustacean that can grow to about 34 cm.")

abyssopelagic_creatures = [dumbo_octopus, faceless_cusk, sea_pig, supergiant_amphipod]

# ---------- HADOPELAGIC (6000m+) ----------
challenger_deep_amphipod = Creatures("Challenger Deep Amphipod", "Hadopelagic", 10900, 1, False, "A scavenger found at the deepest known point in the ocean.")
hadal_sea_cucumber = Creatures("Hadal Sea Cucumber", "Hadopelagic", 8000, 1, False, "Sea cucumbers dominate the large animal life in the deepest trenches.")
mariana_snailfish = Creatures("Mariana Snailfish", "Hadopelagic", 7500, 1, False, "Among the deepest fish ever filmed, with a soft, translucent body.")
xenophyophore = Creatures("Xenophyophore", "Hadopelagic", 10600, 1, False, "A single-celled organism large enough to see with the naked eye.")

hadopelagic_creatures = [challenger_deep_amphipod, hadal_sea_cucumber, mariana_snailfish, xenophyophore]

TOTAL_CREATURES = (len(epipelagic_creatures) + len(mesopelagic_creatures) + len(bathypelagic_creatures)
                   + len(abyssopelagic_creatures) + len(hadopelagic_creatures))

# =====================================================================
#  ZONES + LINKED LIST
# =====================================================================
epipelagic = Zone("Epipelagic", "0-200m", "Sunlight zone - bright, familiar", epipelagic_creatures)
mesopelagic = Zone("Mesopelagic", "200-1000m", "Twilight zone - dimming light", mesopelagic_creatures)
bathypelagic = Zone("Bathypelagic", "1000-4000m", "Midnight zone - total darkness", bathypelagic_creatures)
abyssopelagic = Zone("Abyssopelagic", "4000-6000m", "Abyssal zone - crushing pressure", abyssopelagic_creatures)
hadopelagic = Zone("Hadopelagic", "6000m+", "Trenches - the extreme, rare zone", hadopelagic_creatures)

# linked list: each zone points to the next-deeper zone
epipelagic.next = mesopelagic
mesopelagic.next = bathypelagic
bathypelagic.next = abyssopelagic
abyssopelagic.next = hadopelagic
hadopelagic.next = None

# =====================================================================
#  THE TWO LISTS THE GAME KEEPS TRACK OF
# =====================================================================
stack = [epipelagic]   # STACK: where the player has been. The top (last item) is the current zone.
dive_log = []          # DIVE LOG: creatures the player has discovered
deepest_level = 1      # how deep the player has gotten (1 = Epipelagic ... 5 = Hadopelagic)


# =====================================================================
#  ALGORITHMS
# =====================================================================
def binarysearch(creature_list, key):
    """BINARY SEARCH: finds a creature by name in a list sorted alphabetically.
    Returns the creature object, or None if it isn't there."""
    low = 0
    high = len(creature_list) - 1
    while low <= high:
        mid = (low + high) // 2
        midname = creature_list[mid].name.lower()
        if midname < key:
            low = mid + 1          # the name we want is in the right half
        elif midname > key:
            high = mid - 1         # the name we want is in the left half
        else:
            return creature_list[mid]
    return None


def get_value(creature, sort_by):
    """Picks which attribute of a creature we are sorting on."""
    if sort_by == "depth":
        return creature.depth
    elif sort_by == "danger":
        return creature.danger_level
    else:
        return ZONE_ORDER.index(creature.zone)   # sort by zone = surface zones first


def selection_sort(creature_list, sort_by):
    """SELECTION SORT (written by hand, no .sort()): repeatedly finds the smallest
    remaining item and puts it in the next spot. Returns a new sorted list."""
    items = creature_list[:]          # work on a copy so the original dive log keeps its order
    for i in range(len(items)):
        smallest = i
        for j in range(i + 1, len(items)):
            if get_value(items[j], sort_by) < get_value(items[smallest], sort_by):
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]   # swap the two
    return items


# =====================================================================
#  MENUS
# =====================================================================
def creatures_menu():
    """The creature menu. Runs in its own loop until the player chooses 0 (back)."""
    zone = stack[-1]
    color = ZONE_COLORS[zone.name]
    while True:
        print(color + f"\nCreatures of {zone.name} zone:" + RESET)
        for number, creature in enumerate(zone.creatures, start=1):
            print(number, creature.name)
        print("\nCreatures Menu")
        print("0: Back to the main menu")
        print("1: See one creature's full details (search by name)")
        print("2: Show the depth of every creature here")
        print("3: Show the danger level of every creature here")
        more_option = input("Enter option number: ").strip()

        if more_option == "0":
            print("Leaving the creatures menu...")
            break

        elif more_option == "1":
            key = input("Enter name of creature: ").strip().lower()
            result = binarysearch(zone.creatures, key)
            if result == None:
                print("No creature by that name here.")
            else:
                show_creature(result)
                if result not in dive_log:
                    dive_log.append(result)
                    print(GREEN + "** New discovery! Added to your dive log. **" + RESET)
                else:
                    print("(Already in your dive log.)")

        elif more_option == "2":
            for creature in zone.creatures:
                print(f"{creature.name}: {creature.depth} m")

        elif more_option == "3":
            for creature in zone.creatures:
                print(f"{creature.name}: danger level {creature.danger_level} of 5")

        else:
            print("That is not a valid option, try again.")


def show_dive_log():
    """Shows the dive log, sorted however the player chooses."""
    if len(dive_log) == 0:
        print("Your dive log is empty. Search for creatures by name to discover them!")
        return

    print("\nDIVE LOG - sort by:")
    print("1: Depth")
    print("2: Danger level")
    print("3: Zone")
    print("4: Order I discovered them")
    pick = input("Enter option number: ").strip()

    sort_by = None
    if pick == "1":
        sort_by = "depth"
    elif pick == "2":
        sort_by = "danger"
    elif pick == "3":
        sort_by = "zone"
    elif pick != "4":
        print("That is not a valid option.")
        return

    if sort_by == None:
        items = dive_log[:]
    else:
        items = selection_sort(dive_log, sort_by)
        print("1: Low to high")
        print("2: High to low")
        if input("Enter option number: ").strip() == "2":
            items.reverse()

    print("-" * 62)
    for number, c in enumerate(items, start=1):
        print(f"{number:>2}. {c.name:<26} {c.zone:<14} {c.depth:>6}m  danger {c.danger_level}")
    print("-" * 62)
    print(f"Discovered {len(dive_log)} of {TOTAL_CREATURES} creatures.")


def show_report():
    """The ending screen: the dive report."""
    deepest_name = ZONE_ORDER[deepest_level - 1]
    color = ZONE_COLORS[deepest_name]

    # most dangerous creature found (simple search through the dive log)
    scariest = None
    for c in dive_log:
        if scariest == None or c.danger_level > scariest.danger_level:
            scariest = c

    found = len(dive_log)
    if found >= 15:
        rank = "Master of the Deep"
    elif found >= 8:
        rank = "Seasoned Explorer"
    elif found >= 3:
        rank = "Rookie Diver"
    else:
        rank = "Curious Tourist"

    route = []
    for z in stack:
        route.append(z.name)

    print(color + "\n" + "=" * 52)
    print("              D I V E   R E P O R T")
    print("=" * 52 + RESET)
    print(f"  Explorer:            {name}")
    print(f"  Deepest zone:        {deepest_name}")
    print(f"  Final route:         {' > '.join(route)}")
    print(f"  Creatures found:     {found} of {TOTAL_CREATURES}")
    if scariest != None:
        print(f"  Most dangerous find: {scariest.name} (danger {scariest.danger_level})")
    print(f"  Rank:                {rank}")
    if deepest_level == 5:
        print(RED + "  BONUS BADGE:         Trench Conqueror" + RESET)
    print(color + "=" * 52 + RESET)
    type_print(f"Thanks for diving with us, {name}. The ocean keeps its secrets... for now.", CYAN)


# =====================================================================
#  START OF THE GAME
# =====================================================================
print(CYAN + "=" * 52)
print("        T R I P   T O   T H E   T R E N C H E S")
print("=" * 52 + RESET)
print(SUBMARINE)
print(CYAN + "~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^" + RESET)
type_print("What's your name Adventurer?", YELLOW)
name = input()
type_print(f"{name}, do you want to begin your trip to the trenches? (yes/no)", YELLOW)
choice = input().strip().lower()

if choice == "yes" or choice == "y":
    type_print(f"{name}, YOUR DEEP SEA JOURNEY BEGINS!", GREEN)
else:
    print("We are not getting this fun experience then i guess :(")
    exit()

show_zone(stack[-1])

# =====================================================================
#  MAIN MENU LOOP
# =====================================================================
while True:
    print("\n===MAIN MENU===")
    print(f"What do you want to do {name}?")
    print("0: End the expedition (see your dive report)")
    print("1: View Current Zone")
    print("2: Descend To Next Zone")
    print("3: Surface To Previous Zone")
    print("4: View Creatures")
    print("5: View Dive Log")
    option = input("Enter the number: ").strip()

    if option == "0":
        show_report()
        break

    elif option == "1":
        show_zone(stack[-1])

    elif option == "2":
        if stack[-1].next != None:                 # check BEFORE moving
            stack.append(stack[-1].next)           # PUSH the deeper zone onto the stack
            type_print("Descending...", CYAN)
            show_zone(stack[-1])
            if len(stack) > deepest_level:
                deepest_level = len(stack)
            if stack[-1].next == None:
                type_print(f"Woah! {name}, you have reached the bottom of the ocean!", RED)
        else:
            print(f"Woah! {name}, you have already reached the bottom of the ocean.")

    elif option == "3":
        if len(stack) > 1:                         # check BEFORE moving
            stack.pop()                            # POP the current zone off the stack
            type_print("Surfacing...", CYAN)
            show_zone(stack[-1])
        else:
            print("Hey! You are already at the surface champ.")

    elif option == "4":
        creatures_menu()

    elif option == "5":
        show_dive_log()

    else:
        print("That is not a valid option, try again.")