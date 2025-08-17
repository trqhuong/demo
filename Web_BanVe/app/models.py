from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum, ForeignKey, Time
from enum import Enum as RoleEnum
from enum import Enum as ReviewEnum
from enum import Enum as TicketEnum
from enum import Enum as TypeEnum
from enum import Enum as EventEnum
from app import db, app
from sqlalchemy.orm import relationship
from datetime import datetime

class Role(RoleEnum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"

class ReviewStatus(ReviewEnum):
    PENDING_APPROVAL ="Pending approval"
    APPROVED ="Approved"
    REJECTED="Rejected"

class TicketStatus(TicketEnum):
    Available="Available"
    Confirmed = "Confirmed"
    Completed = "Completed" #khi vé đã đc sử dụng
    Cancelled = "Cancelled"

class TypeTicket(TypeEnum):
    Standard ="Standard"
    VIP="VIP"

class EventType(EventEnum):
    Music="Music"
    StageAndArts="StageAndArts"
    Others="Others"


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

class User(Base):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    role = Column(Enum(Role), default=Role.CUSTOMER)
    organizer = relationship(" Organizer ", backref="user", uselist=False)
    bill = relationship('Bill', backref='user', lazy=True)


class Organizer (Base):
    CompanyName = Column(String(50), nullable=False)
    TaxCode = Column(String(50), nullable=False)
    Status = Column(Enum(ReviewStatus), nullable=False, default=ReviewStatus.PENDING_APPROVAL)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="organizer", uselist=False )
    event =relationship('Event', backref='organizer', lazy=True)



class Ticket(Base):
    Status=Column(Enum(TicketStatus), nullable=False, default=TicketStatus.Available)
    Type =Column(Enum(TypeTicket), nullable=False, default=TypeTicket.Standard)
    Price = Column(Float, nullable=False)
    Quantity = Column(Integer, nullable=False)
    event_id=Column(Integer, ForeignKey("event.id"))
    bill = relationship('Bill', backref='ticket', lazy=True)


class Bill(Base):
    user_id = Column(Integer, ForeignKey("user.id"))
    ticket_id=Column(Integer, ForeignKey("ticket.id"))
    Created_date= Column(DateTime, nullable=False, default=datetime.now())
    Ticket_quantity= Column(Integer, nullable=False)
    Total_price = Column(Float, nullable=False)
    Status = Column(Boolean, nullable=True)

class Event(Base):
    name = Column(String(50), nullable=False)
    Time = Column(Time, nullable=False, default=datetime.now().time)
    Description= Column(String(100), nullable=False)
    Type=Column(Enum(EventType), nullable=False, default=EventType.Others)
    organizer_id= Column(Integer, ForeignKey("organizer.id"))
    ticket=relationship('Ticket', backref='event', lazy=True)
    location_id= Column(Integer, ForeignKey("location.id"))

class Location(Base):
    name= Column(String(100), nullable=False)
    event=relationship('Event', backref='location', lazy=True)

class Artist(Base):
    name = Column(String(50), nullable=False)

class Event_Artist(Base):
    artist_id=Column(Integer, ForeignKey("artist.id"))
    event_id = Column(Integer, ForeignKey("event.id"))

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()