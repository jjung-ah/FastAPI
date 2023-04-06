from sqlalchemy import Boolean, CHAR, Column, DateTime, Double, Float, ForeignKey, Integer, String, BIGINT, INT, TEXT
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
# from sqlalchemy.types import UserDefinedType

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True)
    password = Column(String)
    site = Column(String, primary_key=True, index=True)


class Infer(Base):
    __tablename__ = "infer"

    file_name = Column(String, primary_key=True, index=True)
    file_dir = Column(String, unique=True, index=True)
    date = Column(DateTime)
    time = Column(DateTime)
    score = Column(Float)


class Images(Base):
    __tablename__ = "images"

    state = Column(String)
    file_name = Column(String, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("annotations.image_id"), index=True)
    width = Column(Integer)
    height = Column(Integer)

    anno = relationship("Annotations", back_populates="images")


class Annotations(Base):
    __tablename__ = "annotations"

    idx = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.image_id"), index=True)
    class_id = Column(Integer, ForeignKey("classes.class_id"), index=True)
    bbox = Column(Geometry('MULTIPOINT'))

    images = relationship("Images", back_populates="anno")
    cls = relationship("Classes", back_populates="anno_cls")


class Classes(Base):
    __tablename__ = "classes"

    class_id = Column(Integer, ForeignKey("annotations.class_id"), index=True)
    class_name = Column(String, unique=True)

    anno_cls = relationship("Annotations", back_populates="cls")


class Masterset(Base):
    __tablename__ = "masterset"

    file_name = Column(String, primary_key=True, index=True)
    updated_at = Column(DateTime)
    use = Column(Boolean)
    version = Column(Integer, unique=True)


class Models(Base):
    __tablename__ = "models"

    model_name = Column(String, primary_key=True, index=True)
    network = Column(CHAR)
    started_at = Column(DateTime, unique=True)
    running_time = Column(DateTime)
    finished_at = Column(DateTime, unique=True)
    best_score = Column(Double)
    folder_dir = Column(String, unique=True)
    masterset_score = Column(Integer)


class Deploy(Base):
    __tablename__ = "deploy"

    model_name = Column(String, primary_key=True, index=True)
    deployed_at = Column(DateTime, unique=True)
    use = Column(Boolean)





###############################################################################

# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()

# class Test(Base):
#     __tablename__ = "test"
#
#     id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
#     name = Column(TEXT, nullable=False)
#     number = Column(INT, nullable=False)


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")





