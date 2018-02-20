import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl
import collections


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_dict_from_json(acct, num_of_users):
    """
    (str, int) -> (dict)
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
    return js


def get_val(diction, key):
    """
    (dict, str) -> (collection / str)
    This function processes a deep search entered key and returnes it's value.

    >>>get_val({'users':[{'asd':{123}, 'info':{'loc': 'YES'}}]}, 'loc')
    YES
    >>>get_val({'users':[{'asd':{123}, 'info':{'loc': 'YES'}}]}, 'locti')

    """
    if type(diction) == dict:
        for el in diction:
            if el == key:
                val = diction[el]
                del diction[el]
                return val
            elif (isinstance(diction[el], collections.Iterable) and
                    type(diction[el]) != str):
                val = get_val(diction[el], key)
                if val:
                    return val
    elif isinstance(diction, collections.Iterable) and type(diction) != str:
        for el in diction:
            if el == key:
                val = el
                diction.remove(el)
                return val
            elif isinstance(el, collections.Iterable) and type(el) != str:
                val = get_val(el, key)
                if val:
                    return val
    return ''


def get_input():
    try:
        # Get user-name of account, whose friends info to get.
        acct = input('Enter Twitter Account: ')
        assert (len(acct) > 0)
        # Get number of friends to get info from.
        num_of_users = int(input("Enter amount of friends, to get \
information about: "))
        # Get key parameter, according to which the search will be done.
        key = (input("Enter key value to search through json file: "))
        return [acct, num_of_users, key]

    except ValueError:
        print("You entered wrong value(s). Please, check the input and \
try again.")
    except AssertionError:
        return ''


def main():
    try:
        while True:
            # Get values from user.
            input_values = get_input()
            # Stop if nothing entered.
            if not input_values:
                break
            # Extract input info.
            acct = input_values[0]
            num_of_users = input_values[1]
            key = input_values[2]
            # Get json as dictionary.
            js_diction = get_dict_from_json(acct, num_of_users)
            # Find seeked value (by key) for given number of users.
            results = set()
            for _ in range(num_of_users):
                res_value = get_val(js_diction, key)
                if res_value:
                    print("{} : {}".format(key, res_value))
                    results.update(res_value)
        return results
    except urllib.error.HTTPError:
        print("HTTP Error. Please try again later.")


if __name__ == "__main__":
    main()
