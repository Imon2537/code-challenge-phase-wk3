from band import Band
from venue import Venue
from concert import Concert

# Create instances based on inserted data
band1 = Band(1)  
band2 = Band(2)  
venue1 = Venue(1)  
venue2 = Venue(2)  

concert1 = Concert(1)   
concert2 = Concert(2)  

# Output data for each band
print("Band 1 Concerts:", band1.concerts())
print("Band 1 Venues:", band1.venues())
print("Band 2 Concerts:", band2.concerts())
print("Band 2 Venues:", band2.venues())

# Output data for each venue
print("Venue 1 Concerts:", venue1.concerts())
print("Venue 1 Bands:", venue1.bands())
print("Venue 2 Concerts:", venue2.concerts())
print("Venue 2 Bands:", venue2.bands())

# Output data for each concert
print("Concert 1 Band:", concert1.band())
print("Concert 1 Venue:", concert1.venue())
print("Concert 2 Band:", concert2.band())
print("Concert 2 Venue:", concert2.venue())
