import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")

info_list1 = [
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Modern Warehouse in Accra",
        "description": "A spacious warehouse in the industrial area of Accra, suitable for various types of goods.",
        "propertyType": 7,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 2000,
        "availableStartDate": "2024-09-01T00:00:00.000Z",
        "availableEndDate": "2025-08-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 30000,
        "negotiable": True,
        "streetName": "Industrial Road",
        "houseNumber": "WH200",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA200",
        "longitude": -0.1924,
        "latitude": 5.6308,
        "amenities": [
            "Loading Dock",
            "Parking Space",
            "24/7 Security",
            "CCTV Surveillance",
            "Backup Power Supply",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_397432_2024_07_25_21_08_27.png",
        ],
        "warehouse": {
            "totalFloors": 1,
            "floorNumber": 0,
            "parkingSpace": True,
            "ceilingHeight": 15,
            "loadingDockAvailable": True,
            "officeSpaceAvailable": True,
            "suitableGoods": [0, 4],
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Spacious Office in Accra",
        "description": "A spacious office space in the heart of Accra, suitable for various types of businesses.",
        "propertyType": 6,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 500,
        "availableStartDate": "2024-09-01T00:00:00.000Z",
        "availableEndDate": "2025-08-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 5000,
        "negotiable": True,
        "streetName": "Business Avenue",
        "houseNumber": "BA500",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA500",
        "longitude": -0.1924,
        "latitude": 5.6308,
        "amenities": [
            "Parking Space",
            "24/7 Security",
            "CCTV Surveillance",
            "Backup Power Supply",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_753878_2024_07_25_21_14_41.png",
        ],
        "office": {
            "totalFloors": 1,
            "floorNumber": 0,
            "parkingSpace": True,
            "officeSpaceAvailable": True,
            "suitableBusinesses": [0, 1, 2, 3],
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "University of Ghana Student Hostel",
        "description": "A student-friendly hostel located on the University of Ghana campus with modern amenities.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 300,
        "availableStartDate": "2024-08-01T00:00:00.000Z",
        "availableEndDate": "2025-07-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 5,
        "price": 5000,
        "negotiable": True,
        "streetName": "Legon Hill",
        "houseNumber": "UG101",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA123",
        "longitude": -0.1935,
        "latitude": 5.6508,
        "amenities": [
            "WiFi",
            "Study Area",
            "Laundry Facility",
            "24/7 Security",
            "Common Room",
            "Sports Facilities",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_865631_2024_07_25_21_08_18.png",
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 100,
            "numberOfBathrooms": 50,
            "numberOfWashrooms": 50,
            "numberOfKitchens": 5,
            "roomTypes": [0, 1],
            "studentHostelType": 2,
            "studentHostelLocation": 0,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Accra City Student Hostel",
        "description": "A modern student hostel located off-campus in Accra, providing a comfortable and secure living environment.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 250,
        "availableStartDate": "2024-09-01T00:00:00.000Z",
        "availableEndDate": "2025-08-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 5,
        "price": 4500,
        "negotiable": False,
        "streetName": "Independence Avenue",
        "houseNumber": "AC123",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA124",
        "longitude": -0.1821,
        "latitude": 5.6037,
        "amenities": [
            "WiFi",
            "Gym",
            "Laundry Facility",
            "24/7 Security",
            "Common Room",
            "Study Area",
            "Parking Space",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_997524_2024_07_25_21_08_20.png",
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 80,
            "numberOfBathrooms": 40,
            "numberOfWashrooms": 40,
            "numberOfKitchens": 4,
            "roomTypes": [1, 2],
            "studentHostelType": 0,
            "studentHostelLocation": 1,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Legon Gardens Student Hostel",
        "description": "A spacious and well-equipped student hostel near the University of Ghana, offering a variety of amenities for a comfortable stay.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 350,
        "availableStartDate": "2024-10-01T00:00:00.000Z",
        "availableEndDate": "2025-09-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 5,
        "price": 5200,
        "negotiable": True,
        "streetName": "University Avenue",
        "houseNumber": "LG202",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA125",
        "longitude": -0.2000,
        "latitude": 5.6550,
        "amenities": [
            "WiFi",
            "Gym",
            "Laundry Facility",
            "24/7 Security",
            "Common Room",
            "Study Area",
            "Parking Space",
            "Cafeteria",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_988819_2024_07_25_21_08_21.png",
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 120,
            "numberOfBathrooms": 60,
            "numberOfWashrooms": 60,
            "numberOfKitchens": 6,
            "roomTypes": [0, 3],
            "studentHostelType": 1,
            "studentHostelLocation": 1,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Prime Student Residency",
        "description": "An upscale student hostel located close to the University of Ghana, offering premium amenities and a secure living environment.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 400,
        "availableStartDate": "2024-11-01T00:00:00.000Z",
        "availableEndDate": "2025-10-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 5,
        "price": 6000,
        "negotiable": True,
        "streetName": "Prime Avenue",
        "houseNumber": "PR101",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA126",
        "longitude": -0.2100,
        "latitude": 5.6600,
        "amenities": [
            "WiFi",
            "Gym",
            "Laundry Facility",
            "24/7 Security",
            "Common Room",
            "Study Area",
            "Swimming Pool",
            "Parking Space",
            "Cafeteria",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_021903_2024_07_25_21_08_24.png",
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 150,
            "numberOfBathrooms": 75,
            "numberOfWashrooms": 75,
            "numberOfKitchens": 10,
            "roomTypes": [1, 4],
            "studentHostelType": 2,
            "studentHostelLocation": 1,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Elegant Family House in East Legon",
        "description": "A beautiful and spacious family house located in the serene neighborhood of East Legon, Accra.",
        "propertyType": 0,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 500,
        "availableStartDate": "2024-09-15T00:00:00.000Z",
        "availableEndDate": "2025-09-15T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 350000,
        "negotiable": True,
        "streetName": "Palm Street",
        "houseNumber": "EL200",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA127",
        "longitude": -0.1807,
        "latitude": 5.6397,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Garage",
            "Garden",
            "Swimming Pool",
            "Security System",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_273799_2024_07_25_21_08_14.png",
        ],
        "house": {
            "furnishedStatus": True,
            "numberOfBedrooms": 5,
            "numberOfBathrooms": 4,
            "numberOfWashrooms": 4,
            "numberOfKitchens": 1,
            "numberOfStories": 2,
            "garageSpace": 2,
            "studentFriendly": False,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Cozy Family House in Kumasi",
        "description": "A cozy and modern family house located in the peaceful neighborhood of Ahodwo, Kumasi.",
        "propertyType": 0,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 400,
        "availableStartDate": "2024-10-01T00:00:00.000Z",
        "availableEndDate": "2025-09-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 280000,
        "negotiable": True,
        "streetName": "Garden Road",
        "houseNumber": "AH345",
        "city": "Kumasi",
        "country": "Ghana",
        "zipCode": "KU456",
        "longitude": -1.6212,
        "latitude": 6.6920,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Garage",
            "Garden",
            "Security System",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_243132_2024_07_25_21_08_15.png",
        ],
        "house": {
            "furnishedStatus": True,
            "numberOfBedrooms": 4,
            "numberOfBathrooms": 3,
            "numberOfWashrooms": 3,
            "numberOfKitchens": 1,
            "numberOfStories": 1,
            "garageSpace": 1,
            "studentFriendly": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Modern Office Space in Takoradi",
        "description": "A contemporary office space located in the bustling business district of Takoradi, ideal for startups and established businesses.",
        "propertyType": 5,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 800,
        "availableStartDate": "2024-11-01T00:00:00.000Z",
        "availableEndDate": "2025-10-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 500000,
        "negotiable": True,
        "streetName": "Harbor Road",
        "houseNumber": "TK789",
        "city": "Takoradi",
        "country": "Ghana",
        "zipCode": "TK789",
        "longitude": -1.7554,
        "latitude": 4.8848,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Reception Area",
            "Meeting Rooms",
            "Security System",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_092489_2024_07_25_21_14_44.png",
        ],
        "officeSpace": {
            "totalFloors": 5,
            "floorNumber": 3,
            "parkingSpace": True,
            "officeSpaceType": 0,
            "meetingRoomsAvailable": True,
            "receptionAreaAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Serenity Guest House in Cape Coast",
        "description": "A charming guest house located in the scenic town of Cape Coast, offering a relaxing and comfortable stay for visitors.",
        "propertyType": 4,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 600,
        "availableStartDate": "2024-12-01T00:00:00.000Z",
        "availableEndDate": "2025-11-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 150,
        "negotiable": True,
        "streetName": "Beach Road",
        "houseNumber": "CC101",
        "city": "Cape Coast",
        "country": "Ghana",
        "zipCode": "CC123",
        "longitude": -1.2464,
        "latitude": 5.1053,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Restaurant On Site",
            "24/7 Security",
            "Parking Space",
            "Swimming Pool",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_830082_2024_07_25_21_18_58.png",
        ],
        "guestHouse": {
            "furnishedStatus": True,
            "numberOfBedrooms": 20,
            "numberOfBathrooms": 20,
            "numberOfWashrooms": 20,
            "numberOfKitchens": 1,
            "starRating": 4,
            "restaurantOnSite": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Grand Event Space in Tamale",
        "description": "A spacious and elegant event space in Tamale, perfect for weddings, conferences, and other large gatherings.",
        "propertyType": 8,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 1000,
        "availableStartDate": "2024-11-15T00:00:00.000Z",
        "availableEndDate": "2025-11-14T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 2000,
        "negotiable": True,
        "streetName": "Independence Street",
        "houseNumber": "TM567",
        "city": "Tamale",
        "country": "Ghana",
        "zipCode": "TM123",
        "longitude": -0.8393,
        "latitude": 9.4008,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Catering Service Available",
            "Audio Visual Equipment Available",
            "Restrooms",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_687182_2024_07_25_21_16_59.png",
        ],
        "eventSpace": {
            "totalFloors": 2,
            "floorNumber": 1,
            "parkingSpace": True,
            "maximumCapacity": 500,
            "cateringServiceAvailable": True,
            "audioVisualEquipmentsAvailable": True,
            "suitableEvents": [0, 4, 6],
        },
    },
]

info_list2 = [
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Modern Student Hostel in Downtown",
        "description": "A spacious and well-furnished student hostel located in the heart of the city. Close to major universities and public transport.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 1500,
        "availableStartDate": "2024-09-01T00:00:00Z",
        "availableEndDate": "2025-05-31T23:59:59Z",
        "paymentCurrency": 1,
        "paymentFrequency": 2,
        "price": 500,
        "negotiable": True,
        "streetName": "University Avenue",
        "houseNumber": "25",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "00233",
        "longitude": -0.1869644,
        "latitude": 5.6037168,
        "amenities": ["Wi-Fi", "Study Area", "Gym"],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_346239_2024_07_25_22_33_25.png"
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 50,
            "numberOfBathrooms": 25,
            "numberOfWashrooms": 20,
            "numberOfKitchens": 5,
            "roomTypes": [0, 1, 2],
            "studentHostelType": 2,
            "studentHostelLocation": 1,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Cozy Off-Campus Student Hostel",
        "description": "Affordable and secure student hostel located off campus with easy access to classrooms and library.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 1000,
        "availableStartDate": "2024-08-15T00:00:00Z",
        "availableEndDate": "2025-06-30T23:59:59Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 300,
        "negotiable": False,
        "streetName": "Campus Road",
        "houseNumber": "10",
        "city": "Kumasi",
        "country": "Ghana",
        "zipCode": "00234",
        "longitude": -1.623362,
        "latitude": 6.674552,
        "amenities": ["Wi-Fi", "Study Area", "Cafeteria"],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_698657_2024_07_25_22_33_31.png"
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 40,
            "numberOfBathrooms": 20,
            "numberOfWashrooms": 15,
            "numberOfKitchens": 3,
            "roomTypes": [1, 2, 3],
            "studentHostelType": 1,
            "studentHostelLocation": 0,
            "sharedFacilities": True,
            "mealPlanAvailable": True,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Affordable Student Hostel Near University",
        "description": "Spacious student hostel with modern amenities, located within walking distance to the university campus.",
        "propertyType": 2,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 1200,
        "availableStartDate": "2024-09-01T00:00:00Z",
        "availableEndDate": "2025-07-01T23:59:59Z",
        "paymentCurrency": 1,
        "paymentFrequency": 2,
        "price": 400,
        "negotiable": True,
        "streetName": "Academic Drive",
        "houseNumber": "45",
        "city": "Tamale",
        "country": "Ghana",
        "zipCode": "00235",
        "longitude": -0.851775,
        "latitude": 9.406014,
        "amenities": ["Wi-Fi", "Study Area", "Security"],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_695598_2024_07_25_22_33_48.png"
        ],
        "studentHostel": {
            "furnishedStatus": True,
            "numberOfBedrooms": 30,
            "numberOfBathrooms": 15,
            "numberOfWashrooms": 10,
            "numberOfKitchens": 2,
            "roomTypes": [0, 1, 2],
            "studentHostelType": 2,
            "studentHostelLocation": 1,
            "sharedFacilities": True,
            "mealPlanAvailable": False,
            "studyAreaAvailable": True,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": False,
        },
    },
]

info_list3 = [
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Green Views Residential Project",
        "description": "A modern and eco-friendly residential apartment located in the heart of Accra, offering luxurious living spaces with green amenities.",
        "propertyType": 1,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 200,
        "availableStartDate": "2024-09-01T00:00:00.000Z",
        "availableEndDate": "2025-08-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 250000,
        "negotiable": True,
        "streetName": "Green Avenue",
        "houseNumber": "GV102",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA128",
        "longitude": -0.1860,
        "latitude": 5.6038,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Swimming Pool",
            "Gym",
            "Parking Space",
            "24/7 Security",
            "Garden",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_007456_2024_07_26_11_21_18.png",
        ],
        "apartment": {
            "furnishedStatus": True,
            "numberOfBedrooms": 3,
            "numberOfBathrooms": 2,
            "numberOfWashrooms": 2,
            "numberOfKitchens": 1,
            "numberOfFloorsInBuilding": 10,
            "floorNumberOfUnit": 5,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
            "studentFriendly": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Luxurious Villa in Sunyani",
        "description": "A luxurious and spacious villa located in the tranquil suburbs of Sunyani, offering a perfect blend of comfort and elegance.",
        "propertyType": 0,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 600,
        "availableStartDate": "2024-10-01T00:00:00.000Z",
        "availableEndDate": "2025-09-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 400000,
        "negotiable": True,
        "streetName": "Sunyani Road",
        "houseNumber": "SN500",
        "city": "Sunyani",
        "country": "Ghana",
        "zipCode": "SN123",
        "longitude": -2.3300,
        "latitude": 7.3400,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Garage",
            "Garden",
            "Swimming Pool",
            "Security System",
            "Gym",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_845720_2024_07_26_11_21_35.png"
        ],
        "house": {
            "furnishedStatus": True,
            "numberOfBedrooms": 6,
            "numberOfBathrooms": 5,
            "numberOfWashrooms": 5,
            "numberOfKitchens": 1,
            "numberOfStories": 2,
            "garageSpace": 3,
            "studentFriendly": False,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Signature Apartment in Accra",
        "description": "An exclusive and contemporary apartment located in the prime area of Accra, featuring state-of-the-art amenities and a breathtaking view of the city.",
        "propertyType": 1,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 250,
        "availableStartDate": "2024-09-01T00:00:00.000Z",
        "availableEndDate": "2025-08-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 300000,
        "negotiable": True,
        "streetName": "Independence Avenue",
        "houseNumber": "SA101",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA001",
        "longitude": -0.1945,
        "latitude": 5.6038,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Swimming Pool",
            "Gym",
            "Parking Space",
            "24/7 Security",
            "Garden",
            "Conference Room",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_919354_2024_07_26_11_21_21.png",
        ],
        "apartment": {
            "furnishedStatus": True,
            "numberOfBedrooms": 4,
            "numberOfBathrooms": 3,
            "numberOfWashrooms": 3,
            "numberOfKitchens": 1,
            "numberOfFloorsInBuilding": 15,
            "floorNumberOfUnit": 8,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
            "studentFriendly": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Prime Office Space in Kumasi",
        "description": "A modern and well-equipped office space located in the central business district of Kumasi, ideal for growing businesses.",
        "propertyType": 5,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 700,
        "availableStartDate": "2024-10-01T00:00:00.000Z",
        "availableEndDate": "2025-09-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 450000,
        "negotiable": True,
        "streetName": "Business Street",
        "houseNumber": "KU200",
        "city": "Kumasi",
        "country": "Ghana",
        "zipCode": "KU789",
        "longitude": -1.6167,
        "latitude": 6.6666,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Reception Area",
            "Meeting Rooms",
            "Security System",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_053570_2024_07_26_11_21_25.png",
        ],
        "officeSpace": {
            "totalFloors": 6,
            "floorNumber": 2,
            "parkingSpace": True,
            "officeSpaceType": 0,
            "meetingRoomsAvailable": True,
            "receptionAreaAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Executive Office Space in Tema",
        "description": "A premium office space located in the industrial hub of Tema, offering top-notch facilities for corporate businesses.",
        "propertyType": 5,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 900,
        "availableStartDate": "2024-11-01T00:00:00.000Z",
        "availableEndDate": "2025-10-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 600000,
        "negotiable": True,
        "streetName": "Industrial Avenue",
        "houseNumber": "TE300",
        "city": "Tema",
        "country": "Ghana",
        "zipCode": "TE456",
        "longitude": -0.0166,
        "latitude": 5.6697,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Reception Area",
            "Meeting Rooms",
            "Security System",
            "Cafeteria",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_340648_2024_07_26_11_21_27.png"
        ],
        "officeSpace": {
            "totalFloors": 10,
            "floorNumber": 5,
            "parkingSpace": True,
            "officeSpaceType": 0,
            "meetingRoomsAvailable": True,
            "receptionAreaAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Downtown Office Space in Accra",
        "description": "A highly accessible and well-designed office space located in the heart of Accra's business district, perfect for dynamic businesses.",
        "propertyType": 5,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 850,
        "availableStartDate": "2024-12-01T00:00:00.000Z",
        "availableEndDate": "2025-11-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 3,
        "price": 550000,
        "negotiable": True,
        "streetName": "Business Avenue",
        "houseNumber": "AC400",
        "city": "Accra",
        "country": "Ghana",
        "zipCode": "GA129",
        "longitude": -0.2030,
        "latitude": 5.6000,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Reception Area",
            "Meeting Rooms",
            "Security System",
            "Cafeteria",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_877341_2024_07_26_11_21_38.png"
        ],
        "officeSpace": {
            "totalFloors": 12,
            "floorNumber": 6,
            "parkingSpace": True,
            "officeSpaceType": 0,
            "meetingRoomsAvailable": True,
            "receptionAreaAvailable": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Modern Apartment in Tema",
        "description": "A luxurious and modern apartment located in the vibrant city of Tema, offering a comfortable and convenient lifestyle.",
        "propertyType": 1,
        "listingType": 1,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 180,
        "availableStartDate": "2024-10-01T00:00:00.000Z",
        "availableEndDate": "2025-09-30T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 270000,
        "negotiable": True,
        "streetName": "Residential Lane",
        "houseNumber": "TM500",
        "city": "Tema",
        "country": "Ghana",
        "zipCode": "TE123",
        "longitude": -0.0200,
        "latitude": 5.6700,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Swimming Pool",
            "Gym",
            "Parking Space",
            "24/7 Security",
            "Garden",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_396905_2024_07_26_11_21_40.png"
        ],
        "apartment": {
            "furnishedStatus": True,
            "numberOfBedrooms": 3,
            "numberOfBathrooms": 2,
            "numberOfWashrooms": 2,
            "numberOfKitchens": 1,
            "numberOfFloorsInBuilding": 10,
            "floorNumberOfUnit": 4,
            "laundryFacilityAvailable": True,
            "cleaningServiceAvailable": True,
            "studentFriendly": True,
        },
    },
    {
        "listerId": "f7dbc673-4cd9-477b-a809-0739846dd5fb",
        "title": "Elegant Event Space in Kumasi",
        "description": "A spacious and elegant event space located in Kumasi, ideal for weddings, conferences, and other large gatherings.",
        "propertyType": 8,
        "listingType": 0,
        "propertyPublishStatus": 1,
        "propertyMarketStatus": 1,
        "propertySize": 1200,
        "availableStartDate": "2024-11-01T00:00:00.000Z",
        "availableEndDate": "2025-10-31T23:59:59.000Z",
        "paymentCurrency": 0,
        "paymentFrequency": 2,
        "price": 3000,
        "negotiable": True,
        "streetName": "Event Plaza",
        "houseNumber": "KU123",
        "city": "Kumasi",
        "country": "Ghana",
        "zipCode": "KU234",
        "longitude": -1.6155,
        "latitude": 6.6800,
        "amenities": [
            "WiFi",
            "Air Conditioning",
            "Parking Space",
            "Catering Service Available",
            "Audio Visual Equipment Available",
            "Restrooms",
        ],
        "pictures": [
            "https://storage.googleapis.com/terra-storage/property_images/file_847027_2024_07_26_11_21_41.png"
        ],
        "eventSpace": {
            "totalFloors": 2,
            "floorNumber": 1,
            "parkingSpace": True,
            "maximumCapacity": 700,
            "cateringServiceAvailable": True,
            "audioVisualEquipmentsAvailable": True,
            "suitableEvents": [0, 4, 5],
        },
    },
]


for info in info_list3:
    response = requests.post(api_url, json=info)
    print(response.content)
