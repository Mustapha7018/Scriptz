import json
import pandas as pd
from faker import Faker
import random
from enum import Enum as PyEnum
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Enum,
    ForeignKey
)

# Database configuration
DATABASE_URL = 'sqlite:///property_rental.db'

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Enum definitions
class PublishStatus(PyEnum):
    UNPUBLISH = "Unpublish"
    PUBLISH = "Publish"

class MarketStatus(PyEnum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    SOLD = "Sold"

class Category(PyEnum):
    FOR_RENT = "For Rent"
    FOR_SALE = "For Sale"

class Currency(PyEnum):
    GHC = "GHC"
    USD = "USD"

class FurnishedStatus(PyEnum):
    FULLY_FURNISHED = "Fully Furnished"
    PARTIALLY_FURNISHED = "Partially Furnished"
    NOT_FURNISHED = "Not Furnished"

class PropertyType(PyEnum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"

class ResidentialSubtype(PyEnum):
    APARTMENT = "Apartment"
    HOUSE = "House"
    STUDENTS_HOSTEL = "Students' Hostel"
    HOTEL = "Hotel"
    GUEST_HOUSE = "Guest House"

class CommercialSubtype(PyEnum):
    OFFICE_SPACE = "Office Space"
    SHOP = "Shop"
    WAREHOUSE = "Warehouse"
    EVENT_SPACE = "Event Space"

# Define the Listing class
class Listing(Base):
    __tablename__ = 'listings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    publish_status = Column(Enum(PublishStatus), default=PublishStatus.PUBLISH)
    property_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    market_status = Column(Enum(MarketStatus), default=MarketStatus.AVAILABLE)
    category = Column(Enum(Category), nullable=False)
    type = Column(Enum(PropertyType), nullable=False)
    subtype = Column(String, nullable=False)
    currency = Column(Enum(Currency), nullable=False)
    price = Column(Float, nullable=False)
    price_frequency = Column(String, nullable=False)
    street_name = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    digital_address = Column(String, nullable=False)
    map = Column(String, nullable=True)
    property_size = Column(Float, nullable=False)
    media = Column(String, nullable=True) 
    additional_amenities = Column(String, nullable=True)  
    contact_first_name = Column(String, nullable=False)
    contact_last_name = Column(String, nullable=False)
    contact_phone = Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    # Residential-specific fields
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    kitchen = Column(Integer, nullable=True)
    furnished_status = Column(Enum(FurnishedStatus), nullable=True)
    # Commercial-specific fields
    total_floors = Column(Integer, nullable=True)
    floor_number = Column(Integer, nullable=True)
    parking_spaces = Column(Integer, nullable=True)
    # Apartment-specific fields
    num_floors_building = Column(Integer, nullable=True)
    floor_number_unit = Column(Integer, nullable=True)
    student_friendly = Column(Boolean, nullable=True)
    # House-specific fields
    num_stories = Column(Integer, nullable=True)
    garage_spaces = Column(Integer, nullable=True)
    # Hostel-specific fields
    room_type = Column(String, nullable=True)
    hostel_type = Column(String, nullable=True)
    location_type = Column(String, nullable=True)
    shared_facilities = Column(Boolean, nullable=True)
    meal_plan_available = Column(Boolean, nullable=True)
    study_areas_available = Column(Boolean, nullable=True)
    # Hotel-specific fields
    star_rating = Column(Integer, nullable=True)
    restaurant_on_site = Column(Boolean, nullable=True)
    # Guest House-specific fields
    star_rating_gh = Column(Integer, nullable=True)
    restaurant_on_site_gh = Column(Boolean, nullable=True)
    # Office Space-specific fields
    office_description = Column(String, nullable=True)
    meeting_rooms_available = Column(Boolean, nullable=True)
    reception_area = Column(Boolean, nullable=True)
    # Shop-specific fields
    display_window = Column(Boolean, nullable=True)
    storage_room = Column(Boolean, nullable=True)
    # Warehouse-specific fields
    ceiling_height = Column(Float, nullable=True)
    loading_docks = Column(Boolean, nullable=True)
    office_space_included = Column(Boolean, nullable=True)
    goods_suitable = Column(String, nullable=True)  
    # Event Space-specific fields
    max_capacity = Column(Integer, nullable=True)
    event_types_suitable = Column(String, nullable=True)  
    catering_facilities = Column(Boolean, nullable=True)
    av_equipment_available = Column(Boolean, nullable=True)
    # Pricing structure
    negotiable = Column(Boolean, nullable=True)

# Sample data
titles = [
    "Luxury Apartment in Downtown",
    "Cozy Family House with Garden",
    "Spacious Office Space in Business District",
    "Modern accommodation near University",
    "Charming Guest House by the Beach",
    "Elegant Hotel in City Center",
    "Affordable Hostel for Students",
    "Large Warehouse in Industrial Area",
    "Versatile Event Space for Rent",
    "Retail Shop in Popular Mall"
]

descriptions = [
    "This luxury apartment offers stunning views of the downtown skyline and features top-of-the-line amenities.",
    "A cozy family house with a beautiful garden, perfect for children and pets.",
    "Spacious office space located in the heart of the business district, ideal for startups and established companies.",
    "Modern accommodation located near the university, perfect for students and faculty members.",
    "Charming guest house situated by the beach, offering a relaxing atmosphere and stunning ocean views.",
    "Elegant hotel in the city center with a variety of rooms and suites, ideal for business and leisure travelers.",
    "Affordable hostel for students, offering shared rooms and communal facilities.",
    "Large warehouse located in the industrial area, suitable for storage and distribution.",
    "Versatile event space for rent, ideal for weddings, conferences, and other special occasions.",
    "Retail shop located in a popular mall, perfect for a variety of businesses."
]

addresses = [
    ("Main Street", "123", "12345", "Accra", "Ghana", "GA-123-4567"),
    ("Garden Road", "456", "67890", "Kumasi", "Ghana", "KU-234-5678"),
    ("Business Avenue", "789", "11223", "Takoradi", "Ghana", "TA-345-6789"),
    ("University Blvd", "101", "44556", "Tamale", "Ghana", "TM-456-7890"),
    ("Beach Drive", "202", "77889", "Cape Coast", "Ghana", "CC-567-8901"),
    ("City Center Road", "303", "99001", "Sunyani", "Ghana", "SU-678-9012"),
    ("Student Lane", "404", "22334", "Ho", "Ghana", "HO-789-0123"),
    ("Industrial Way", "505", "55667", "Bolgatanga", "Ghana", "BO-890-1234"),
    ("Event Plaza", "606", "88990", "Wa", "Ghana", "WA-901-2345"),
    ("Mall Road", "707", "11234", "Koforidua", "Ghana", "KO-012-3456")
]

# images = [
#     "https://example.com/image1.jpg",
#     "https://example.com/image2.jpg",
#     "https://example.com/image3.jpg",
#     "https://example.com/image4.jpg",
#     "https://example.com/image5.jpg",
#     "https://example.com/image6.jpg",
#     "https://example.com/image7.jpg",
#     "https://example.com/image8.jpg",
#     "https://example.com/image9.jpg",
#     "https://example.com/image10.jpg"
# ]

def generate_images():
    return json.dumps({
        "image1": f"local_path/image{random.randint(1, 100)}.jpg",
        "image2": f"local_path/image{random.randint(1, 100)}.jpg",
        "image3": f"local_path/image{random.randint(1, 100)}.jpg",
        "image4": f"local_path/image{random.randint(1, 100)}.jpg",
        "image5": f"local_path/image{random.randint(1, 100)}.jpg"
    })

residential_subtypes = list(ResidentialSubtype)
commercial_subtypes = list(CommercialSubtype)

def get_price_frequency(property_type, subtype):
    if property_type == PropertyType.RESIDENTIAL:
        if subtype == ResidentialSubtype.STUDENTS_HOSTEL.value:
            return random.choice(["Per Semester", "Per Academic Year"])
        elif subtype in [ResidentialSubtype.HOTEL.value, ResidentialSubtype.GUEST_HOUSE.value]:
            return random.choice(["Per Night", "Per Week"])
    return random.choice(["Per Month", "Per Year"])

# Generate sample listings
def generate_sample_listings(num_listings):
    fake = Faker()
    listings = []
    
    for i in range(num_listings):
        property_type = random.choice(list(PropertyType))
        title = titles[i % len(titles)]
        description = descriptions[i % len(descriptions)]
        street_name, house_number, zip_code, city, country, digital_address = addresses[i % len(addresses)]
        media = generate_images()

        if property_type == PropertyType.RESIDENTIAL:
            subtype = random.choice(residential_subtypes)
        else:
            subtype = random.choice(commercial_subtypes)

        # Basic details
        listing = Listing(
            property_id=fake.uuid4(),
            title=title,
            description=description,
            market_status=MarketStatus.AVAILABLE,
            category=random.choice(list(Category)),
            type=property_type,
            subtype=subtype.value,
            currency=random.choice(list(Currency)),
            price=round(random.uniform(10000, 1000000), 2),
            price_frequency=get_price_frequency(property_type, subtype.value),
            street_name=street_name,
            house_number=house_number,
            zip_code=zip_code,
            city=city,
            country=country,
            digital_address=digital_address,
            map=fake.url(),
            property_size=round(random.uniform(50, 500), 2),
            media=media,
            additional_amenities="Wifi,Parking,Security",
            contact_first_name=fake.first_name(),
            contact_last_name=fake.last_name(),
            contact_phone=fake.phone_number(),
            contact_email=fake.email(),
            negotiable=fake.boolean()
        )

        # Conditional fields
        if property_type == PropertyType.RESIDENTIAL:
            listing.bedrooms = random.randint(1, 5)
            listing.bathrooms = random.randint(1, 3)
            listing.kitchen = random.randint(1, 2)
            listing.furnished_status = random.choice(list(FurnishedStatus))
            
            if subtype == ResidentialSubtype.APARTMENT:
                listing.num_floors_building = random.randint(1, 20)
                listing.floor_number_unit = random.randint(1, 20)
                listing.student_friendly = fake.boolean()
            
            elif subtype == ResidentialSubtype.HOUSE:
                listing.num_stories = random.randint(1, 3)
                listing.garage_spaces = random.randint(1, 3)
                listing.student_friendly = fake.boolean()
            
            elif subtype == ResidentialSubtype.STUDENTS_HOSTEL:
                listing.room_type = random.choice(["Single room", "Double/shared room", "Triple room", "Quad room", "5+ person room(Dormitory)"])
                listing.hostel_type = random.choice(["Male only", "Female only", "Co-ed"])
                listing.location_type = random.choice(["On campus", "Off campus"])
                listing.shared_facilities = fake.boolean()
                listing.meal_plan_available = fake.boolean()
                listing.study_areas_available = fake.boolean()
                listing.laundry_facility_available = fake.boolean()
                listing.cleaning_service_available = fake.boolean()

            elif subtype == ResidentialSubtype.HOTEL:
                listing.star_rating = random.randint(1, 5)
                listing.restaurant_on_site = fake.boolean()
            
            elif subtype == ResidentialSubtype.GUEST_HOUSE:
                listing.star_rating_gh = random.randint(1, 5)
                listing.restaurant_on_site_gh = fake.boolean()

        elif property_type == PropertyType.COMMERCIAL:
            listing.total_floors = random.randint(1, 10)
            listing.floor_number = random.randint(1, 10)
            listing.parking_spaces = random.randint(0, 20)
            
            if subtype == CommercialSubtype.OFFICE_SPACE:
                listing.office_description = fake.text()
                listing.meeting_rooms_available = fake.boolean()
                listing.reception_area = fake.boolean()
            
            elif subtype == CommercialSubtype.SHOP:
                listing.display_window = fake.boolean()
                listing.storage_room = fake.boolean()
            
            elif subtype == CommercialSubtype.WAREHOUSE:
                listing.ceiling_height = round(random.uniform(3, 10), 2)
                listing.loading_docks = fake.boolean()
                listing.office_space_included = fake.boolean()
                listing.goods_suitable = random.choice(["General Merchandise", "Perishable Goods", "Hazardous Materials", "Electronics/Sensitive Equipment", "Industrial/Construction Materials"])
            
            elif subtype == CommercialSubtype.EVENT_SPACE:
                listing.max_capacity = random.randint(50, 500)
                listing.event_types_suitable = random.choice(["Religious", "Wedding", "Funeral", "Festivals", "Conference", "Concert", "Party"])
                listing.catering_facilities = fake.boolean()
                listing.av_equipment_available = fake.boolean()

        listings.append(listing)
    return listings


# Function to export to Excel
def export_to_excel(listings, filename='listings.xlsx'):
    data = []
    for listing in listings:
        row = {column.name: getattr(listing, column.name) for column in Listing.__table__.columns}
        data.append(row)
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)


# Create the database and tables
Base.metadata.create_all(engine)

# Generate and add listings to the session
listings = generate_sample_listings(20)
session.add_all(listings)
session.commit()

# Export the listings to excel file
export_to_excel(listings)



# Query and print the listings to verify
for listing in session.query(Listing).all():
    print(f"ID: {listing.id}, Title: {listing.title}, Type: {listing.type}, Subtype: {listing.subtype}, Price Frequency: {listing.price_frequency}")
    print(f"Media: {listing.media}")
    print("---")