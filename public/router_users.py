#from sqlalchemy.orm import sessionmaker, declarative_base, Session
#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
#from models.good import Main_User, New_Respons, Tags, User, Base
from config import settings
from sqlalchemy import create_engine, text
# определяем параметры для подключения

#settings.DATABASE_URL = 'sqlite:///./test02.db

#engine = create_engine(settings.POSTGRES_DATABASE_URL)

engine = create_engine(url = settings.POSTGRES_DATABASE_URLS, echo=True)
#SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

with engine.connect() as conn:
    res = conn.info(text("select version()"))
    print(f"res = {res}")
#Base.metadata.create_all(bind=engine)
#SessionLocal = async_session(engine)

#def init_db():
#    Base.metadata.create_all(bind=engine)
#def init_db():
#   async with engine.begin() as conn:
#        await conn.run.sync(Base.metadata.create_all)

#def get_async_session():

     #async with session(engine) as session:
     #    try:
      #     yield session
     #    finally:
     #      session.close()
#
# def get_session():
#     with Session(engine) as session:
#         try:
#           yield session
#         finally:
#           session.close()


# реализация маршрутов для операций c конкретными тегами - конкретизация роутера
# users_router = APIRouter(tags=[Tags.users], prefix='/api/users')
# info_router = APIRouter(tags=[Tags.info])
# def coder_passwd(cod: str):
#     return cod*2
#
# #DB: Session = Depends(get_async_session)
# @users_router.get("/{id}", response_model=Union[New_Respons, Main_User], tags=[Tags.info])
# def get_user_(id: int, DB , response: Response):
#     '''
#     получаем пользователя по id
#     '''
#     user = DB.query(User).filter(User.id == id).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if user == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     # если пользователь найден, отправляем его
#     else:
#         return user
# @users_router.get("/", response_model=Union[list[Main_User], New_Respons], tags=[Tags.users])
# def get_user_db( ):
#     '''
#     получаем все записи таблицы
#     '''
#     users = DB.query(User).all()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if users == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователи не найдены"})
#     return users
# @users_router.post("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users], status_code=status.HTTP_201_CREATED)
# def create_user(item: Annotated[Main_User,
# Body(embed=True, description="Новый пользователь")]):
#     try:
#       user = User(id=item.id, name=item.name, hashed_password=coder_passwd(item.name))
#
#       if user is None:
#           raise HTTPException(status_code=404, detail="Объект не определен")
#       DB.add(user)
#       DB.commit()
#       DB.refresh(user)
#       return user
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Произошла ошибка при добавлении объекта {user}")
#
#
# @users_router.put("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users])
# def edit_user_(item: Annotated[Main_User,
# Body(embed=True, description="Изменяем данные для пользователя по id")]):
#     # получаем пользователя по id
#     user = DB.query(User).filter(User.id == item.id).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if user == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     # если пользователь найден, изменяем его данные и отправляем обратно клиенту
#     user.name = item.name
#     try:
#         DB.commit()
#         DB.refresh(user)  # сохраняем изменения
#     except HTTPException:
#         return JSONResponse(status_code=404, content={"message": ""})
#     return user
#
# @users_router.delete("/{id}", response_class=JSONResponse, tags=[Tags.users])
# def delete_user(id: int):
#     # получаем пользователя по id
#     user = DB.query(User).filter(User.id == id).first()
#
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if user == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     try:
#         DB.delete(user)
#         DB.commit()  # сохраняем изменения
#     except HTTPException:
#         JSONResponse(content={'message' : f'Ошибка'})
#     return JSONResponse(content={'message' : f'Пользователь удалён {id}'})

# @users_router.patch("/{id}", response_model=Union[Main_User, New_Respons], tags=[Tags.users])
# def edit_user(item: Annotated[Main_User,
# Body(embed=True, description="Изменяем данные по id")], DB: Session = Depends(get_async_session)):
#     # получаем пользователя по id
#     try:
#         item_good = find_good(str(item.id)) #нашли элемент по ключу
#         # item_good = good_dict[str(item.id)]
#         if item_good == None:
#             return New_Respons(message="ошибка")
#
#         good_model = Good(**item_good)   #преобразовали элемент из словаря в модель
#
#         update_good_dict = item.dict(exclude_unset=True) #преобразуем объект модели в словарь, но только только те данные,
#         # которые были установлены (отправлены в запросе), без значений по умолчанию (данные для изменения в удобный
#         # формат)
#         good_model_copy = good_model.copy(update=update_good_dict) # обновляем данные  модели на новые
#         good_dict[str(item.id)] = jsonable_encoder(good_model_copy)
#         return good_model_copy
#     except HTTPException:
#         return New_Respons(message = f'Ошибка {response.status_code}')

