def wordcount(readtxt):
    dict={}
    readlist=readtxt.split()
    for every_word in readlist:
        if every_word in dict:
            dict[every_word]+=1
        else:
            dict[every_word]=1
    return dict


readtext="""
    this is a test txt!
    can you see this ?
    """
dict1={}
dict1=wordcount(readtext)
print(dict1)