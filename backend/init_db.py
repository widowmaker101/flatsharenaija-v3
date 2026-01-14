from app.database import Base, engine
from app.models.user import User  # Import models to register them
from app.models.listing import Listing

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
