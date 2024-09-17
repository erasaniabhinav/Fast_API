# application programming interface — a software intermediary that allows two applications to talk to each other. 
# APIs are an accessible way to extract and share data
#models talk to datbase and controllers control the logic also views build the webapp 
#everything stays in one growing large codebase
#duplication can be eliminated in api and routes will interact by making calls
#del route, update, log in , logout call and make calls to API
#if api is in place we can connect anything to it, by interacting back n forth 
#python api is called FAST-API


#importing fastapi
from fastapi import FastAPI
from models import List_class

#instantiating fastapi class in variable app
#FastAPI() is a call to the constructor method of the FastAPI class. 
#This constructor method is responsible for creating new instances of the FastAPI class.
app = FastAPI()

list_new = []

#path decorator says that whatever method below is in charge of handling request going to "/""
@app.get("/")
def read_root():
    return {"Hello": "this is using"}

#get all list_new
@app.get("/list_new")
def get_list_new():
    return {"list_new":list_new}

#we use pydantic to validate (leads to clean data and defined)
#When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
@app.post("/list_new")
def create_list_new(i:List_class):
    list_new.append(i)
    return {"list_new":"new item has been added"}

#get_single_list_new
@app.get("/list_new/{y}")
def get_list_new(y:int):
    for i in list_new:
        if i.id == y:
            return {"item": i}

    return {"message":"no id found"}

#update list_new
@app.put("/list_new/{k}")
def update_list_new(k:int,m:List_class):
    for i in list_new:
        if i.id == k:
            i.id = k
            i.item = m.item
            return {"list_new":"new item has been updated"}
            return{"list_new": list_new}

 
    return {"list_new":"id not found "}



#delete list_new
@app.delete("/list_new/{z}")
def delete_list_new(z:int):
    for i in list_new:
        if i.id == z:
            list_new.remove(i)
            return{"message":"item has been deleted"}
            

    return {"message":"no id found"}