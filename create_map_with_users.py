# File: create_map.py
import folium
import analyse_json
from geopy.geocoders import ArcGIS
import html
from geopy.exc import GeocoderTimedOut

def get_coordinates(adress):
    """
    (str) -> (list)
    This function finds lattitude and longitude of given address using
    geocoder.
    Precondition: the address must be appropriate, so it can be found on map.
    >>>get_coordinates('Mountain View, CA')
    [37.3860517, -122.0838511]
    >>>get_coordinates('Russell Winkelaar's flat, Toronto, Ontario, Canada)
    None
    >>>get_coordinates(Lviv, Ukraine)
    [49.839683, 24.029717]
    """
    try:
        geolocator = ArcGIS()
        # Get location in appropriate form.
        location = geolocator.geocode(adress)
        # Get coordinates of address.
        if location:
            coordinates = (location.latitude, location.longitude)
            # Return coordinatess as [longitude and lattitude] list.
            return coordinates
    except GeocoderTimedOut:
        # TIME Error
        return get_coordinates(adress)
    else:
        return ''


def collect_info(acct, num_of_users):
    """
    (str, int) -> (dict)
    This function processes information about user's friends, formates it in
    appropriate way (so that it it can be represented in html page properly)
    and returnes a dict, made of coordinates-keys and info-values.
    """
    # Get json file as dict, using analyse_json module.
    diction = analyse_json.get_dict_from_json(acct, num_of_users)
    # Create list of screen_names, formated properly for html.
    scr_name = [html.escape(analyse_json.get_val(diction, 'screen_name'),
                quote=True) for _ in range(num_of_users)]
    # Create list of friend's addresses.
    address = [html.escape(analyse_json.get_val(diction, 'location'),
               quote=True) for _ in range(num_of_users)]
    # Create list of coordinates, got by address, using ArcGIS geocoder.
    loc = [get_coordinates(adr) for adr in address]
    # Zip (merge) created lists into one info_list, which keeps tuples of \
    # all needed info about friend.
    info_list = list(zip(loc, scr_name, address))
    # Create dict with keys = coordinates and vaues = information.
    map_dict = dict()
    for info in info_list:
        loc_key = info[0]
        pop_info = info[1] + '--' + info[2]
        if loc_key in map_dict:
            map_dict[loc_key] += '<br>' + pop_info
        else:
            map_dict[loc_key] = pop_info
    return(map_dict)


def create_map(map_dict):
    # Build a simple map.
    tw_map = folium.Map(location=[49.839683, 24.029717],
                       tiles='openstreetmap',
                       zoom_start=10)
    friends_markers = folium.FeatureGroup().add_to(tw_map)

    for user in map_dict:
        folium.Marker(user,
                      popup=map_dict[user],
                      icon=folium.Icon(icon='user',
                      color='blue')).add_to(friends_markers)

    tw_map.add_child(friends_markers)
    # Save created map as .html file.
    tw_map.save("templates/twitter_friends_map.html")

def main():
    """
    This function cotrols execution of other functions of this module,
    calling them with certain arguments.
    """
    # Account name.
    acct = input("User-name: ")
    # Number of friends
    num_of_users = int(input("number: "))
    map_dict = collect_info(acct, num_of_users)
    print(map_dict)
    create_map(map_dict)


if __name__ == "__main__":
    main()
