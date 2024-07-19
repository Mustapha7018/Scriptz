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
    Date,
    Enum,
    ForeignKey
)

# Database configuration
DATABASE_URL = 'sqlite:///:memory:'

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
    SHORT_LET = "Short Let"

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
    CONDO = "Condo"
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
    publish_status = Column(Enum(PublishStatus), default=PublishStatus.UNPUBLISH)
    property_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    market_status = Column(Enum(MarketStatus), nullable=False)
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
    "Modern Condo near University",
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
    "Modern condo located near the university, perfect for students and faculty members.",
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

images = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
    "https://example.com/image4.jpg",
    "https://example.com/image5.jpg",
    "https://example.com/image6.jpg",
    "https://example.com/image7.jpg",
    "https://example.com/image8.jpg",
    "https://example.com/image9.jpg",
    "https://example.com/image10.jpg"
]

residential_subtypes = list(ResidentialSubtype)
commercial_subtypes = list(CommercialSubtype)

# Generate sample listings
def generate_sample_listings(num_listings):
    fake = Faker()
    listings = []
    
    for i in range(num_listings):
        property_type = random.choice(list(PropertyType))
        title = titles[i % len(titles)]
        description = descriptions[i % len(descriptions)]
        street_name, house_number, zip_code, city, country, digital_address = addresses[i % len(addresses)]
        media = images[i % len(images)]

        if property_type == PropertyType.RESIDENTIAL:
            subtype = random.choice(residential_subtypes)
        else:
            subtype = random.choice(commercial_subtypes)

        listing = Listing(
            property_id=fake.uuid4(),
            title=title,
            description=description,
            market_status=random.choice(list(MarketStatus)),
            category=random.choice(list(Category)),
            type=property_type,
            subtype=subtype.value,
            currency=random.choice(list(Currency)),
            price=round(random.uniform(10000, 1000000), 2),
            price_frequency=random.choice(["Per Month", "Per Year", "Per Day"]),
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
            bedrooms=random.randint(1, 5) if property_type == PropertyType.RESIDENTIAL else None,
            bathrooms=random.randint(1, 3) if property_type == PropertyType.RESIDENTIAL else None,
            kitchen=random.randint(1, 2) if property_type == PropertyType.RESIDENTIAL else None,
            furnished_status=random.choice(list(FurnishedStatus)) if property_type == PropertyType.RESIDENTIAL else None,
            total_floors=random.randint(1, 10) if property_type == PropertyType.COMMERCIAL else None,
            floor_number=random.randint(1, 10) if property_type == PropertyType.COMMERCIAL else None,
            parking_spaces=random.randint(0, 20) if property_type == PropertyType.COMMERCIAL else None,
            num_floors_building=random.randint(1, 20) if subtype == ResidentialSubtype.APARTMENT else None,
            floor_number_unit=random.randint(1, 20) if subtype == ResidentialSubtype.APARTMENT else None,
            student_friendly=fake.boolean(),
            num_stories=random.randint(1, 3) if subtype == ResidentialSubtype.HOUSE else None,
            garage_spaces=random.randint(1, 3) if subtype == ResidentialSubtype.HOUSE else None,
            room_type="Single" if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            hostel_type="Dormitory" if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            location_type="On-Campus" if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            shared_facilities=fake.boolean() if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            meal_plan_available=fake.boolean() if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            study_areas_available=fake.boolean() if subtype == ResidentialSubtype.STUDENTS_HOSTEL else None,
            star_rating=random.randint(1, 5) if subtype == ResidentialSubtype.HOTEL else None,
            restaurant_on_site=fake.boolean() if subtype == ResidentialSubtype.HOTEL else None,
            office_description=fake.text() if subtype == CommercialSubtype.OFFICE_SPACE else None,
            meeting_rooms_available=fake.boolean() if subtype == CommercialSubtype.OFFICE_SPACE else None,
            reception_area=fake.boolean() if subtype == CommercialSubtype.OFFICE_SPACE else None,
            display_window=fake.boolean() if subtype == CommercialSubtype.SHOP else None,
            storage_room=fake.boolean() if subtype == CommercialSubtype.SHOP else None,
            ceiling_height=round(random.uniform(3, 10), 2) if subtype == CommercialSubtype.WAREHOUSE else None,
            loading_docks=fake.boolean() if subtype == CommercialSubtype.WAREHOUSE else None,
            office_space_included=fake.boolean() if subtype == CommercialSubtype.WAREHOUSE else None,
            goods_suitable="Electronics,Furniture,Clothing" if subtype == CommercialSubtype.WAREHOUSE else None,
            max_capacity=random.randint(50, 500) if subtype == CommercialSubtype.EVENT_SPACE else None,
            event_types_suitable="Conference,Wedding,Party" if subtype == CommercialSubtype.EVENT_SPACE else None,
            catering_facilities=fake.boolean() if subtype == CommercialSubtype.EVENT_SPACE else None,
            av_equipment_available=fake.boolean() if subtype == CommercialSubtype.EVENT_SPACE else None,
            negotiable=fake.boolean()
        )
        
        listings.append(listing)
    return listings

# Create the database and tables
Base.metadata.create_all(engine)

# Generate and add listings to the session
listings = generate_sample_listings(1)
session.add_all(listings)
session.commit()

# Query and print the listings to verify
for listing in session.query(Listing).all():
    print(f"ID: {listing.id}, Title: {listing.title}, Description: {listing.description}, Address: {listing.street_name}, {listing.city}")
