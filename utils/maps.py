import folium
import pandas as pd


def load_data():
    return pd.read_csv("places.csv")


def save_data(df):
    df.to_csv("places.csv")


def create_standard_map():
    center = (13.133932434766733, 16.103938729508073)
    return folium.Map(center, zoom_start=3)


def add_maker(my_map, df):
    for _, place in df.iterrows():
        folium.Marker(
            location=[
                place['latitude'],
                place['longitude']
                ],
            tooltip=place['name'],
            popup=place['name']
        ).add_to(my_map)
    return my_map


def create_map():
    try:
        dados = load_data()
        my_mapa = create_standard_map()
        my_new_mapa = add_maker(my_mapa, dados)
        my_new_mapa.save("templates/my_new_map.html")
    except:
        return False
    return True
