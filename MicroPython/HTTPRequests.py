import network
import json
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('OTE46E47E', '\"23DiakosiA11\\PentE6693EjI\\')

# Make GET request
import urequests
r = urequests.get("http://192.168.1.8:5001/api/movies")

response = urequests.get("http://192.168.1.8:5001/api/movies")

# Decode the bytes object to a string using .decode()
data = response.content.decode('utf-8')

# Parse the JSON string into a Python object
json_data = json.loads(data)

# Print the JSON data in a standard format (MicroPython does not support pretty-printing via json.dumps)
print(json.dumps(json_data))
# Close the response
response.close()


# Posting a movie
movie = {
    "title": "Blade Runner",
    "year": 1982,
    "rating": 4.05
}

json_data = json.dumps(movie)
url = "http://192.168.1.8:5001/api/movies"
response = urequests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
print(response.text)
response.close()