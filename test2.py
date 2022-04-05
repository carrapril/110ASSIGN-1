


def test_dict():
    me = {
        "first": "April",
        "last": "Carr",
        "age": 30,
        "hobbies": ["bike riding, running, reading"],
        "address": {
            "street": "Island Ave",
            "city": "Wonderland"
            },
        "another": 12,
        
    }
    print(me["first"] + " " + me["last"])
    print("My age is: " + str(me["age"]))
    print(f"My age is: {me['age']}")
    
    address = me["address"]
    print(type(address))
    print(address["street"])
    
    #add new keys
    me["color"] = "red"
    
    #modify exisiting age
    me["age"] = 31
    
    #check if a key exist in a dict
    if "age" in me:
        print("age exist")




print("------Dictionary Test-------")
test_dict()