# Astromy

import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
dist_au_units = jupiter.sun_distance
dist_km = dist_au_units * 149597870.691
print(dist_km)
