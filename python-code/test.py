"""
import requests
import osmnx as ox
import folium
import networkx as nx
import streamlit as st
import googlemaps

# ---------- Step 1: Get Current Location ----------
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import osmnx as ox

st.title("🌍 Live User Location")

# Run JavaScript to fetch geolocation
coords = streamlit_js_eval(
    js_expressions=""""""
    new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            pos => resolve({latitude: pos.coords.latitude, longitude: pos.coords.longitude}),
            err => resolve(null)  // return null if denied/error
        );
    })
    """""",
    key="get_location"
)

if coords:
    st.success(f"📍 Latitude: {coords['latitude']}, Longitude: {coords['longitude']}")
else:
    st.warning("Waiting for location… (make sure you allowed it in the browser)")

API_KEY = "AIzaSyBSUrSudF7neYoTA52DTM2mVZnF_x9K5aM"
gmaps = googlemaps.Client(key=API_KEY)
latitude = coords['latitude']
longitude = coords['longitude']
places_result = gmaps.places_nearby(
    location=(latitude, longitude),
    radius=2000, 
    type="hospital"
)
for place in places_result['results']:
    name = place['name']
    address = place.get('vicinity', 'Address not available')
    print(f"{name} - {address}")"""

import requests
import googlemaps
import folium
import polyline   # to decode route points

# ---------- Get Current Location ----------
def get_current_location():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    loc = data['loc'].split(",")
    return float(loc[0]), float(loc[1])

lat, lng = get_current_location()
print("Your Location:", lat, lng)

# ---------- Google Maps API Client ----------
API_KEY =  "AIzaSyBSUrSudF7neYoTA52DTM2mVZnF_x9K5aM"
gmaps = googlemaps.Client(key=API_KEY)

# ---------- Find Nearby Hospitals ----------
places_result = gmaps.places_nearby(
    location=(lat, lng),
    radius=3000,   # 3 km range
    type="hospital"
)

# ---------- Create Map ----------
map_ = folium.Map(location=[lat, lng], zoom_start=14)

# Add your location
folium.Marker(
    [lat, lng],
    popup="You are here",
    icon=folium.Icon(color="blue", icon="user")
).add_to(map_)

# ---------- Add Hospitals + Draw Routes ----------
for place in places_result['results'][:3]:  # limit to 3 hospitals for clarity
    hospital_name = place['name']
    hospital_location = place['geometry']['location']
    h_lat, h_lng = hospital_location['lat'], hospital_location['lng']

    # Distance & Time
    dist_matrix = gmaps.distance_matrix((lat, lng), (h_lat, h_lng), mode="driving")
    distance = dist_matrix["rows"][0]["elements"][0]["distance"]["text"]
    duration = dist_matrix["rows"][0]["elements"][0]["duration"]["text"]

    # Hospital Marker
    folium.Marker(
        [h_lat, h_lng],
        popup=f"{hospital_name}\nDistance: {distance}\nTime: {duration}",
        icon=folium.Icon(color="red", icon="plus-sign")
    ).add_to(map_)

    # ---------- Get Route from Directions API ----------
    directions = gmaps.directions(
        (lat, lng),
        (h_lat, h_lng),
        mode="driving"
    )

    if directions:
        points = polyline.decode(directions[0]['overview_polyline']['points'])
        folium.PolyLine(points, color="green", weight=3, opacity=0.7).add_to(map_)

# ---------- Save & Open Map ----------
map_.save("hospitals_with_routes.html")
print("✅ Map with routes saved as hospitals_with_routes.html")
