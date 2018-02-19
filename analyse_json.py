import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_dict_from_json(acct, num_of_users):
    """
    (str, int)
    This function gets json file about Twitter friends list from Twitter URL.
    Returned json file contains info about certain amount (given by user) of
    friends of cetain account (with given account-name).
    """
    print('')
    if (len(acct) < 1):
        return ''
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': num_of_users})
    connection = urllib.request.urlopen(url, context=ctx)
    try:
        data = connection.read().decode()
    except JSONDecodeError("Invalid json file.", doc, pos):
        print("Invalid json file. Please, check and try again.")
    js = json.loads(data)
    print(js)
    return js


def extract_info(info_key, json_dict):
    """
    (str, dict) -> (list / int / str)
    This function gets certain information from js_dict, by given key
    (info_key parameter).
    """
    try:
        assert(len(info_key) > 0)
        if info_key in json_dict:
            print(json_dict[info_key])
            return(json_dict[info_key])
        else:
            print("Entered info parameter is not available.")
            return ''
    except AssertionError:
        print("You didn't enter information key.Please try again.")


try:
    acct = input('Enter Twitter Account: ')
    num_of_users = int(input("Enter amount of friends, which You want to get \
information about: "))
    assert (len(acct))
    get_dict_from_json(acct, num_of_users)
except ValueError:
    print("You entered wrong value(s). Please, check the input and try again.")
except AssertionError:
    print()
