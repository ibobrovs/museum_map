import folium
import pandas as pd
from folium.plugins import MarkerCluster

# Data loading
df = pd.read_csv("map_data.csv")

# Map ceneter (based on average coordinates)
lat_center = df["lat"].mean()
lon_center = df["long"].mean()

# Map initialization
m = folium.Map(location=[lat_center, lon_center], zoom_start=7)

# Clastering markers
marker_cluster = MarkerCluster().add_to(m)

# Icons
icon_map = {
    "cemetery": ("cross-sign", "black"),
    "monument": ("info-sign", "blue"),
    "fortification": ("tower", "green"),
}

# Marker creation
for idx, row in df.iterrows():
    icon_name, color = icon_map.get(row['type'], ("question-sign", "gray"))
    popup_html = f"""
    <b>{row['vieta']}</b><br>
    <i>{row['place']}</i><br><br>
    {row['apraksts']}<hr>{row['overview']}<br><br>
    <a href="{row['gmaps_url']}" target="_blank">📍 Open in Google Maps</a>
    """
    icon = folium.Icon(icon=icon_name, color=color, prefix='glyphicon')
    marker = folium.Marker(
        location=[row["lat"], row["long"]],
        popup=folium.Popup(popup_html, max_width=300),
        icon=icon
    )
    marker.add_to(marker_cluster)

# Saves
m.save("interactive_museum_map.html")
