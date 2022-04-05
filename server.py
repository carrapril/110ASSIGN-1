import json
from unicodedata import category
from unittest import result
from flask import Flask, abort, request
from mock_data import catalog


app = Flask("Server")


@app.route("/")
def home():
    return "hello from flask"


@app.route("/me")
def about_me():
    return "April Carr"

#####################################    API Endpoints ALWAYS Return JSONS ######################################################

@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json() # return data (payload) from the request
    
    # set a unique _id on product
    product["_id"] = 2
    catalog.append(product)  # save it to database
     
    
    return json.dumps(product)




#### get /api/catalog/count

@app.route("/api/catalog/count", methods=["get"])
def products():
    count= (f"There are: {len(catalog)}") 
    
    return json.dumps(count)

#get /api/catalog/total sum of all product prices

@app.route("/api/catalog/total", methods=["get"])
def total_price():
    
    total = 0
    
    for product in catalog:
        total += product["price"]
    
    return json.dumps(total) 

#get /api/product/id

@app.route("/api/product/<id>")
def get_by_id(id):
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)
        
    return abort(404, "No Product with that ID")


@app.route("/api/products/cheapest", methods=["get"])
def cheapest_product():
    
    products = catalog[0]

    for prices in catalog:
        if prices["price"] < products["price"]:
            products = prices
            
    return json.dumps(products)    

#get /api/categories

@app.route("/api/categories", methods=["get"])
def categories():
    uniquecategory = []
    for prod in catalog:
        category = prod["category"]
        if not category in uniquecategory:
            uniquecategory.append(category)
            
    return json.dumps(uniquecategory)        

#
# ticket 2345
#create an endpoint that allow the client to get all the products for a specified category

@app.route("/api/catalog/<category>")
def prods_by_category(category):
    result = []
    for product in catalog:
        if product["category"] == category:
            result.append(product)
            
    return json.dumps(result)

@app.get("/api/someNumbers")
def some_numbers():
    #return a list with numbers from 1 to 50 as json
    numbers = []
    
    for num in range(1,51):
        numbers.append(num)
        
    return json.dumps(numbers)


#####################################
######################coupon code endpoints###############
####################################################

allCoupons = []

#create the get/api/couponCode
#return all coupons as json list

@app.route("/api/couponCode", methods=["GET"])
def get_coupons():
    return json.dumps(allCoupons)

#create the post 
# get the coupon from the request
# assign the _id
# and add it all coupons
# return the coupon as json
#@app.post("/api/couponCode")

@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
    coupon = request.get_json()
    coupon["_id"] = 42
    
    allCoupons.append(coupon)
    
    return json.dumps(coupon)



app.run(debug=True)