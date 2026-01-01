import googlemaps
import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_js_eval import streamlit_js_eval
key = "AIzaSyBSUrSudF7neYoTA52DTM2mVZnF_x9K5aM"
gmaps = googlemaps.Client(key=key)

coords = streamlit_js_eval(
    js_expressions="""
    new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            pos => resolve({latitude: pos.coords.latitude, longitude: pos.coords.longitude}),
            err => resolve(null)  // return null if denied/error
        );
    })
    """,
    key="get_location"
)
latitude = coords['latitude']
longitude = coords['longitude']
print(f"📍 Latitude: {coords['latitude']}, Longitude: {coords['longitude']}")
st.write(f"📍 Latitude: {coords['latitude']}, Longitude: {coords['longitude']}")
places_result = gmaps.places_nearby(
    location=(latitude ,longitude),
    radius=100,   
    type="hospital"
)
m = folium.Map(location=[latitude , longitude] , zoom_start=200)
folium.Marker([latitude , longitude] , popup= "You are here" ).add_to(m)

st_folium(m, 700 , 500)