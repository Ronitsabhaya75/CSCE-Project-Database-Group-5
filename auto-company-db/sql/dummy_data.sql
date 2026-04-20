-- CLEAR EXISTING DATA (If re-running)
TRUNCATE TABLE Vehicle_Part, Plant_Model, Plant_Part, Model_Part, Dealer_Brand, Customer_Inquiry, Sale, Inventory, Vehicle, Part, Model, Brand, Options, Plant, Supplier, Customer, Dealer, Company RESTART IDENTITY CASCADE;

-- 1. INDEPENDENT ENTITIES
INSERT INTO Company (name, hq_address) VALUES 
('Apex Motor Group', '100 Apex Way, Detroit, MI'),
('Nova Dynamics', '500 Innovation Blvd, Austin, TX');

INSERT INTO Dealer (name, address, city, state, phone) VALUES 
('Fort Worth Auto Hub', '123 Texas Trail', 'Fort Worth', 'TX', '817-555-0199'),
('Dallas Elite Motors', '888 Commerce St', 'Dallas', 'TX', '214-555-0288'),
('Sunset Drives', '404 Ocean Ave', 'Los Angeles', 'CA', '310-555-0377');

INSERT INTO Customer (first_name, last_name, address, phone, gender, annual_income) VALUES 
('Alice', 'Johnson', '789 Pine Ln, Fort Worth, TX', '817-555-9911', 'F', 85000.00),
('Bob', 'Smith', '456 Oak Dr, Dallas, TX', '214-555-8822', 'M', 110000.00),
('Charlie', 'Davis', '123 Maple Blvd, LA, CA', '310-555-7733', 'M', 75000.00);

-- Note: Inserting Getrag so your DBA query has something to find!
INSERT INTO Supplier (name, address, contact_phone) VALUES 
('Getrag Transmissions', '1 Autobahn, Munich, Germany', '+49-123-456'),
('Bosch Electronics', '5 Tech Park, Berlin, Germany', '+49-987-654'),
('Apex Internal Parts', '200 Apex Way, Detroit, MI', '313-555-0000');

INSERT INTO Plant (supplier_id, name, address, city, state, plant_type) VALUES 
(1, 'Getrag Munich Facility', '1 Autobahn', 'Munich', 'Bavaria', 'parts-manufacturing'),
(2, 'Bosch ECU Plant', '5 Tech Park', 'Berlin', 'Berlin', 'parts-manufacturing'),
(NULL, 'Apex Assembly Line A', '300 Apex Way', 'Detroit', 'MI', 'final-assembly');

INSERT INTO Options (engine_type, transmission_type, color) VALUES 
('5.0L V8', '6-Speed Manual', 'Cherry Red'),
('2.0L Turbo 4-Cyl', '8-Speed Automatic', 'Midnight Blue'),
('Electric Motor', '1-Speed Direct Drive', 'Pearl White');

-- 2. DEPENDENT ENTITIES
INSERT INTO Brand (company_id, brand_name, country_of_origin) VALUES 
(1, 'Velocity', 'USA'),
(2, 'EcoDrive', 'USA');

-- Note: Added 'Convertible' to test the Marketing Team's Seasonal Query
INSERT INTO Model (brand_id, model_name, body_style, year) VALUES 
(1, 'V-Roadster', 'Convertible', 2024),
(1, 'V-Cruiser', 'Sedan', 2024),
(2, 'Volt-Hatch', 'Hatchback', 2023);

INSERT INTO Part (supplier_id, part_name, part_type) VALUES 
(1, 'Getrag 6MT-82', 'Transmission'),
(2, 'Bosch Engine Control Unit', 'Electronics'),
(3, 'V8 Block', 'Engine');

INSERT INTO Vehicle (vin, model_id, options_id, manufacture_date, status) VALUES 
('VIN11111111111111', 1, 1, '2023-05-10', 'sold'),
('VIN22222222222222', 1, 1, '2024-01-15', 'available'),
('VIN33333333333333', 2, 2, '2023-08-20', 'sold'),
('VIN44444444444444', 3, 3, '2023-11-05', 'available');

-- 3. TRANSACTIONAL ENTITIES
INSERT INTO Inventory (dealer_id, vin, date_received, date_sold, price) VALUES 
(1, 'VIN11111111111111', '2023-05-15', '2023-06-01', 55000.00),
(1, 'VIN22222222222222', '2024-02-01', NULL, 56000.00),
(2, 'VIN33333333333333', '2023-09-01', '2023-09-10', 35000.00),
(3, 'VIN44444444444444', '2023-11-10', NULL, 42000.00);

-- These sales power the 3-Year Trend OLAP query
INSERT INTO Sale (vin, dealer_id, customer_id, sale_date, sale_price) VALUES 
('VIN11111111111111', 1, 1, '2023-06-01', 54500.00),
('VIN33333333333333', 2, 2, '2023-09-10', 34000.00);

-- Unfulfilled inquiries for the Marketing query
INSERT INTO Customer_Inquiry (customer_id, dealer_id, model_id, inquiry_date, notes, status) VALUES 
(3, 1, 1, '2024-04-10', 'Wants a red convertible before summer, checking inventory.', 'Unfulfilled'),
(1, 2, 3, '2024-04-12', 'Curious about EV tax credits for the Volt-Hatch.', 'In Progress');

-- 4. JUNCTION TABLES
INSERT INTO Dealer_Brand (dealer_id, brand_id) VALUES (1, 1), (2, 1), (3, 2);
INSERT INTO Model_Part (model_id, part_id) VALUES (1, 1), (1, 3), (2, 2), (3, 2);
INSERT INTO Plant_Part (plant_id, part_id) VALUES (1, 1), (2, 2), (3, 3);
INSERT INTO Plant_Model (plant_id, model_id) VALUES (3, 1), (3, 2), (3, 3);

-- Linking the defective Getrag Transmission to specific VINs for the DBA defect query!
INSERT INTO Vehicle_Part (vin, part_id, plant_id, manufacture_date) VALUES 
('VIN11111111111111', 1, 1, '2023-05-01'),
('VIN22222222222222', 1, 1, '2024-01-05'),
('VIN33333333333333', 2, 2, '2023-08-10'),
('VIN44444444444444', 2, 2, '2023-10-25');