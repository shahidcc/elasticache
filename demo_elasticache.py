from redis import Redis
import os

cache_endpoint = os.environ["CACHE_ENDPOINT"]
service_port = 6379

#redis = Redis(host=cache_endpoint, port=service_port)      # returns bytes, not strings
redis = Redis(host=cache_endpoint, port=service_port, decode_responses=True)  # returns strings

def key_value_get_set():
    key = "sportsman"
    value = "Pele"

    # Store the key-value pair
    redis.set(key, value)
    print("WRITE: key = ", key)

    # Retrieve the value for key='sportsman'
    player_name = redis.get(key)
    print("READ: player_name = ", str(player_name), "\n")

def key_value_set_ttl():
    key = "sportsman"
    value = "Pele"
    ttl = 120

    # Store the key-value pair with TTL
    redis.set(key, value, ttl)
    print("WRITE: key = ", key, " -- TTL = ", ttl)
    # Retrieve the TTL value -- how many more seconds this data will live 

    # Reset the TTL value to 90 seconds from now 
    redis.expire(key, 90)

    ttl_value = redis.ttl(key)
    print("READ: new TTL = ", ttl_value, "\n")


def dict_get_set():
    # Put all key-value pairs to a dictionary at first
    dict_data = {'sportsman':'Pele', 'sportswoman': 'Mia Hamm', 'sportsrobot':'R2D2'}
    # Store the dictionary in cache
    redis.mset(dict_data) 
    print("WRITE: Dictionary data = ", str(dict_data) )
    
    # Retrieve the dictionary with the usual get() 
    sportsman_listed = redis.get('sportsman')  
    print("READ: sportsman = ", sportsman_listed, "\n")

def list_data_type_get_set():
    # our data-type is 'list' 
    african_countries = ['Nigeria', 'Egypt', 'Rwanda', 'Morocco', 'Egypt']
    # Assign it to a key, use sadd() to convert it to a set and then store 
    redis.lpush('african_country_list', *african_countries) 
    print("WRITE: List data = ", str(african_countries) )

    # Retrieve the full list using lrange() with start=0 and end=-1   
    list_of_african_countries = redis.lrange('african_country_list', 0, -1)
    print("READ: full list = ", list_of_african_countries )
    
    # Retrieve a speicifc range of values from the list    
    list_of_african_countries = redis.lrange('african_country_list', 2, 3)
    print("READ: partial list = ", list_of_african_countries, "\n" )

def set_data_type_get_set():
    # our data-type is 'list' 
    african_countries = ['Nigeria', 'Egypt', 'Rwanda', 'Morocco', 'Egypt']
    # Assign it a key, use sadd() to convert it to a set and then store 
    redis.sadd('african_set', *african_countries) 
    print("WRITE: List data type= ", african_countries)    

    # Retrieve the set using smembers() function  
    set_of_african_countries = redis.smembers('african_set')
    print("READ: Set data type= ", set_of_african_countries, "\n" )    

def cache_list_remove_keys():
    # list all keys in the cache   
    redis.keys()

    # list the keys that match a pattern  
    redis.keys("afri*")

    redis.keys("*rica")
    
    redis.keys("*afri*")
 
    # check if a key exists 
    redis.exists("sportsman")

    # delete a key 
    key_to_delete = "sportsman" 
    redis.delete(key_to_delete)
    print("DELETED: key = ", key_to_delete)   
    
    # delete keys that match the pattern "africa*" and "sports*"
    keys_to_delete = redis.keys("africa*")
    redis.delete(*keys_to_delete)
    print("DELETED: keys = ", keys_to_delete)   

    keys_to_delete = redis.keys("sports*")
    redis.delete(*keys_to_delete)
    print("DELETED: keys = ", str(keys_to_delete), "\n")   

try:
    cache_is_working = redis.ping()    
    print('\nI am Redis. Try me. I can remember things, only for a short time though :)\n')
    
    key_value_get_set()
    key_value_set_ttl()
    dict_get_set()
    list_data_type_get_set()
    set_data_type_get_set()
    cache_list_remove_keys()
    
except Exception as e:
    print('EXCEPTION: host could not be accessed ---> ', repr(e))
