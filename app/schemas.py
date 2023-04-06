import datetime
from pydantic import BaseModel

'''
    TODO: necessary to checking
'''

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    site: str

    class Config:
        orm_mode = True


class InferBase(BaseModel):
    file_dir: str

class InferCreate(InferBase):
    pass

class Infer(InferBase):
    file_name: str
    date: datetime
    time: datetime
    score: float


class ImagesBase(BaseModel):
    pass

class ImagesCreate(ImagesBase):
    pass

class Images(ImagesBase):
    state: str
    file_name: str
    image_id: int
    width: int
    height: int

    class Config:
        orm_mode = True


class AnnotationsBase(BaseModel):
    pass

class AnnotationsCreate(AnnotationsBase):
    pass

class Annotations(AnnotationsBase):
    idx: int
    image_id: int
    class_id: int
    # bbox: multipoint  # TODO: how to import multipoint
    images: int
    cls: int

    class Config:
        orm_mode = True


class ClassesBase(BaseModel):
    pass

class ClassesCreate(ClassesBase):
    pass

class Classes(ClassesBase):
    pass


class MastersetBase(BaseModel):
    pass

class MastersetCreate(MastersetBase):
    pass

class Masterset(MastersetBase):
    pass



class ModelsBase(BaseModel):
    pass

class ModelsCreate(ModelsBase):
    pass

class Models(ModelsBase):
    pass



class DeployBase(BaseModel):
    pass

class DeployCreate(DeployBase):
    pass

class Deploy(DeployBase):
    pass


###############################################################################

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
# class ItemCreate(ItemBase):
#     pass
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
# class UserBase(BaseModel):
#     email: str
#
# class UserCreate(UserBase):
#     password: str
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True

