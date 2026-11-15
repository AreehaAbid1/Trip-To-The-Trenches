# Trip to the Trenches

A deep-sea dive simulator built in Python for the NASA Space Apps Challenge.
Pilot a submarine from the sunlit surface to the deepest trenches and meet
24 real marine creatures across five ocean zones.

## Features
- Descend and surface through five real ocean zones
- Search for creatures by name and learn a fact about each
- A dive log you can sort by depth, danger level or zone
- A final dive report with a rank and badges

## Data structures used
- **Linked list:** keeps the zones in order (descend follows each zone's next link)
- **Stack:** remembers the route (descend pushes a zone, surface pops it)
- **Binary search:** finds a creature by name in a sorted list
- **Selection sort:** orders the dive log (written by hand)

## How to run
Requires Python 3. No extra libraries are needed.

    python TripToTheTrenches_main.py

## Author
Areeha Abid

Final-stage development was assisted by Claude (Anthropic).
