from fastapi import FastAPI

users_db = dict()
ticket_db = dict()
product_db = dict()

app = FastAPI()

@app.get("/")
def say_hi():
    return "Hello John Doe"


@app.get("/about/")
def about_us():
    return "Bu biz haqimizdagi oyna."


@app.get("/contact/")
def kontakt():
    return "Biz bilan bog`laning."


@app.get("/work")
def our_work():
    return "Bizning natijalar"


@app.get("/some_page")
def extra_page():
    return "Bu bizning sahifamiz..." \
    "this is our page..."



@app.post("/user/create")
def user_add():
    user_id = 12,
    name = "John Doe",
    age = 22,
    edu = "Islamic Academy"

    new_user = {
        "id" : user_id,
        "name" : name,
        "age " : age,
        "edu" : edu
    }

    users_db[user_id] = new_user
    return new_user



@app.post("/users/ticket")
def user_ticket():
    
    user_id = 21 ,
    user_ticket= "hi hi hi"

    
    new_ticket = {
     'user_id' : user_id,
     'user_ticket' : user_ticket
    }

    ticket_db[user_id] = new_ticket
    return 


@app.post("/products")
def product_create():

    product_id = 1,
    product_name = 'Non',
    product_quant = 4

    new_product = {
        "product_id":product_id,
        "name": product_name,
        "quantity":product_quant
    }

    product_db[product_id] = new_product
    return new_product

@app.delete("/product/delete")
def delete_product(id:int):
    id = product_db.pop(id)
    return "Product muvaffaqqiyatli o`chirildi."


@app.put("user/update")
def update_user(id:int):
    pass


@app.put("product/update")
def update_product(id:int):
    pass


@app.patch("/a")
def patch_a():
    pass