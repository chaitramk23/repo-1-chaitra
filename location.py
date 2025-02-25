import geocoder

# Get current location based on IP
location = geocoder.ip('me')

# Print location details
print("Your current location:")
print(f"City: {location.city}")
print(f"State: {location.state}")
print(f"Country: {location.country}")
print(f"Latitude: {location.lat}, Longitude: {location.lng}")

