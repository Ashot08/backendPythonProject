import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from db import create_tables as create_tables
#from public.router_users import init_db

#rom public.router_users import users_router

app = FastAPI()
create_tables()

#DB = databases.Database(settings.POSTGRES_DATABASE_URL)

#app.include_router(users_router)
#@app.on_event("startup")
#def on_startup():
#    open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')
#    init_db()

#@app.on_event("startup")
#async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    #await DB.connect()

#@app.on_event("shutdown")
#def shutdown():
 #   open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: End\n')
#@app.on_event("shutdown")
#async def shutdown():
    #await DB.disconnect()
    #with open("log.txt", mode="a") as log:
        #log.write(f'{datetime.utcnow()}:End\n')


@app.get("/")
def main():
    return FileResponse("files/index.html")

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)