from band import Band
from venue import Venue
from concert import Concert

# Example of testing methods
band = Band(1)  # Assuming band with id 1 exists
venue = Venue(1)  # Assuming venue with id 1 exists
concert = Concert(1)  # Assuming concert with id 1 exists

print(band.concerts())
print(band.venues())

print(venue.concerts())
print(venue.bands())

print(concert.band())
print(concert.venue())