from fastapi import FastAPI

users_db = dict()



app = FastAPI()

@app.get("/very first page")
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



@app.post("/user")
def user_add():
    user_id = user_id,
    name = name,
    age = age,
    edu = edu

    new_user = {
        "id" : id,
        "name" : name,
        "age " : age,
        "edu" : edu
    }

    users_db[user_id] = new_user
    return new_user




    return 