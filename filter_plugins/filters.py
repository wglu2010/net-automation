import datetime
import collections
from netaddr import IPSet

def uppercase_all(arg): 
    return arg.upper() 

def split_newlines(arg, index):
    return arg.split('\n')[index]

def timestamper(arg):
    return str('{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now()))+'_'+arg

def format_uptime(arg):
    return str(datetime.timedelta(seconds=arg))

def get_key(arg, i=0):
    return list(arg.keys())[i]

def get_keys(arg):
    return list(arg.keys())

def balance_graph(graph):
    """ Takes a list of neighbor tuples and returns it 
    reverse-sorted based on neighbor occurences  """
    
    # Counts how many times each neighbor occurs
    count = collections.Counter([x for (x,y) in graph]+[y for (x,y) in graph])

    # Group neighbors based on neighbor occurence count
    neigh_count = {}
    for tup in graph:
        total = count[tup[0]]+count[tup[1]]
        if total in neigh_count:
            neigh_count[total].append(tup)
        else:
            neigh_count[total] = [tup]

    # Within tuples with same neighbor count, reorder tuples so 
    # that the most occuring neighbor is first
    reordered = []
    for key in neigh_count:
        value = neigh_count[key]
        count = collections.Counter([x for (x,y) in value]+[y for (x,y) in value])
        for tup in value:
            if count[tup[1]] > count[tup[0]]:
                reordered.append((tup[1],tup[0],key))
            else:
                reordered.append(tup+(key,))

    # Reverse sort neighbor tuples based on neighbor count
    reordered.sort(key=lambda item: item[2], reverse=True)

    # Return list of neighbor tuples without neighbor count
    return [(x,y) for (x,y,z) in reordered]

def subtract_subnet(original_subnet, remove_subnets):
    """Subtract a list of subnets from original subnet and return leftover
    subnet(s) in a list"""
    original = IPSet([original_subnet])
    for subnet in remove_subnets:
        original.remove(subnet)
    
    return [str(subnet) for subnet in original.iter_cidrs()]

def is_in_tuplist(tuplist, value):
    """Checks if value is present in a list of tuples"""
    return len([tup for tup in tuplist if value in tup]) > 0

def nodes_not_in_fabric(nodes, provider_fabric, customer_fabric):
    """Returns nodes that are not defined in the fabric"""
    fabric = provider_fabric + customer_fabric

    # Unpacks the fabric and node dictionaries, keeping only the names
    nodes = [n['name'] for n in nodes]
    fabric = [node for f in fabric for node in [f['right'],f['left']]]
    
    # Returns the list of fabric names subtracted from the list of all nodes
    return list(set(nodes) - set(fabric))

def unique_list(arg):
    '''Returns a list containing only unique elements, order is not preserved!'''
    return list(set(arg))

class FilterModule(object): 
    def filters(self): 
        return {
        'uppercase_all': uppercase_all,
        'split_newlines': split_newlines,
        'timestamper': timestamper,
        'format_uptime': format_uptime,
        'get_keys': get_keys,
        'balance_graph':balance_graph,
        'get_key': get_key,
        'subtract_subnet': subtract_subnet,
        'is_in_tuplist': is_in_tuplist,
        'nodes_not_in_fabric': nodes_not_in_fabric,
        } 

