#!/usr/bin/env python3
from pathlib import Path

# Delete short 1.041
short = Path('/workspace/civil-bootcamp/MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/Transportation_Urban_Systems/01_1.041_Transportation_Systems.md')
if short.exists():
    short.unlink()
    print('DELETED short 1.041')
else:
    print('Not found (may already be deleted)')

# Verify long version
long = Path('/workspace/civil-bootcamp/MIT_CEE_Core/Track_3_Energy_Transportation_Societal_Systems/Energy_Systems/01_1.041_Transportation_Systems.md')
print('Long 1.041:', long.exists())
