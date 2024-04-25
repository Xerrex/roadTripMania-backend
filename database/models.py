import uuid
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from .db_setup import Base


class User(Base):
    """Defines a creator or a passenger of a ride
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    unique_code = Column(String, default=str(uuid.uuid4()), unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    # password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # rides = relationship("Ride", back_populates="creator")


    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # def hash_password(self, password):
    #     """Create password hash
    #     """
    #     self.password_hash = pwd_context.hash(password)


    # def verify_password(self, password):
    #     """Verify password against the password_hash
    #     """
    #     return pwd_context.verify(password, self.password_hash)


# class Ride(Base):
#     """Defines a trip from one place to another
#     using a vehicle
#     """
#     id = Column(Integer, primary_key=True, index=True)
#     unique_code = Column(String, default=str(uuid.uuid4()), unique=True)
#     start_time = Column(DateTime, nullable=False)
#     arrival_time = Column(DateTime, nullable=False)
    
#     user_id = Column(Integer, ForeignKey("users.id"))
#     creator = relationship("User", back_populates="rides")
