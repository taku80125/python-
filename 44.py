grades =['a','b','c','d','e','f','g']

def filter_a(grade):
    return grade != 'a'
         

takuma = list(filter(filter_a,grades))
print(takuma)