from redis import Redis

cache_endpoint = 'xxxx.xxx.....cache.amazonaws.com'
service_port = 6379

redis = Redis(host=cache_endpoint, port=service_port)

def key_value_get_set(){
    key = "sportsman"
    value = "Pele"

    # Store the key-value pair
    redis.set(key, value)

    # Retrieve the value for key='sportsman'
    player_name = redis.get(key)
}  


def key_value_set_ttl(){

    # Store the key-value pair with TTL
    redis.set(key, value, ttl)

    # Retrieve the TTL value -- how many more seconds this data will live 
    ttl_value = redis.ttl(key)

    # Reset the TTL value to 90 seconds from now 
    redis.expire(key, 90)
}

def dict_get_set(){
    # Put all key-value pairs to a dictionary at first
    dict_data = {'sportsman':'Pele', 'sportswoman': 'Mia Hamm', 'robot':'R2D2'}
    # Store the dictionary in cache
    redis.mset(dict_data) 

    # Retrieve the dictionary with the usual get() 
    sportsman_listed = redis.get('sportsman')  
}

def list_data_type_get_set(){
    # our data-type is 'list' 
    african_countries = ['Nigeria', 'Egypt', 'Rwanda', 'Morocco', 'Egypt']
    # Assign it to a key, use sadd() to convert it to a set and then store 
    redis.sadd('african_list', *african_countries) 

    # Retrieve the full list using lrange() with start=0 and end=-1   
    african_countries_list = redis.lrange('african_list', 0, -1)

    # Retrieve a speicifc range of values from the list    
    african_countries_list = redis.lrange('african_list', 2, 3)
}

def set_data_type_get_set(){
    # our data-type is 'list' 
    african_countries = ['Nigeria', 'Egypt', 'Rwanda', 'Morocco', 'Egypt']
    # Assign it a key, use sadd() to convert it to a set and then store 
    redis.sadd('african_set', *african_countries) 

    # Retrieve the set using smembers() function  
    african_countries_list = redis.smembers('african_set')
}

def cache_remove_retriove_many_keys(){ 
    redis.keys()

    redis.keys("afri*")

    redis.keys("*rica")

    redis.keys("*afri*")

    redis.exists("Africa")

    redis.delete("african")
}

try:
    cache_is_working = redis.ping()    
    print('I am Redis. Try me. I can remember things, only for a short time though :)')

except Exception as e:
    print('EXCEPTION: host could not be accessed ---> ', repr(e))


