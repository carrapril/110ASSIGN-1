from unicodedata import category
from mock_data import catalog


#count the products whose titles contains the text
def find_prod():
    text = "sunglasses"
    
    # for loop and print the title 
    count = 0
    
    for prod in catalog: 
        title = prod["title"]
        if text.lower() in title.lower():
            
           print(f"The product: {title} ${prod['price']}")  
          
        



def find_category():
    categories = []
    for prod in catalog: 
        category = prod["category"]
        if not category in categories: 
            categories.append(category)
            
            
    print(categories)    
    
    
find_prod()
find_category()
    
        


