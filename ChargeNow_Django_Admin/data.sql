-- ===================================
-- Database: ChargeNow
-- ===================================
CREATE DATABASE IF NOT EXISTS ChargeNow;
USE ChargeNow;

-- ======================
-- Table: User
-- ======================
CREATE TABLE IF NOT EXISTS User (
    user_id INT(10) AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(30) NOT NULL,
    user_email VARCHAR(30) NOT NULL UNIQUE,
    user_password VARCHAR(15) NOT NULL,
    user_phone BIGINT(15) NOT NULL,
    user_address VARCHAR(100) NOT NULL,
    role ENUM('user','admin') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO User (user_name, user_email, user_password, user_phone, user_address, role) VALUES
('Prem Vadnere','prem@example.com','prem123',9876543210,'Nagpur, India','admin'),
('Rahul Sharma','rahul@example.com','rahul123',9123456780,'Mumbai, India','user'),
('Anjali Deshmukh','anjali@example.com','anjali123',9012345678,'Pune, India','user'),
('Rohit Verma','rohit@example.com','rohit123',9876501234,'Nagpur, India','user'),
('Priya Singh','priya@example.com','priya123',9123409876,'Mumbai, India','user'),
('Karan Patel','karan@example.com','karan123',9012345670,'Pune, India','user'),
('Sneha Jain','sneha@example.com','sneha123',9876512345,'Nagpur, India','user'),
('Amit Kumar','amit@example.com','amit123',9123456789,'Mumbai, India','user'),
('Nisha Sharma','nisha@example.com','nisha123',9012345671,'Pune, India','user'),
('Vikram Desai','vikram@example.com','vikram123',9876543201,'Nagpur, India','user');

-- ======================
-- Table: VanOperator
-- ======================
CREATE TABLE IF NOT EXISTS VanOperator (
    operator_id INT(10) AUTO_INCREMENT PRIMARY KEY,
    operator_name VARCHAR(30) NOT NULL,
    operator_email VARCHAR(30) NOT NULL UNIQUE,
    operator_password VARCHAR(15) NOT NULL,
    operator_phone BIGINT(15) NOT NULL,
    operator_license_doc VARCHAR(100) NOT NULL,
    operator_status ENUM('online','offline') DEFAULT 'offline',
    van_id INT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO VanOperator (operator_name, operator_email, operator_password, operator_phone, operator_license_doc, operator_status, van_id) VALUES
('Suresh Patil','suresh@example.com','suresh123',9123456701,'license1.pdf','offline', NULL),
('Ramesh Joshi','ramesh@example.com','ramesh123',9123456702,'license2.pdf','online', NULL),
('Ajay Kumar','ajay@example.com','ajay123',9123456703,'license3.pdf','online', NULL),
('Sunil Mehta','sunil@example.com','sunil123',9123456704,'license4.pdf','offline', NULL),
('Rajesh Sharma','rajesh@example.com','rajesh123',9123456705,'license5.pdf','online', NULL),
('Anil Verma','anil@example.com','anil123',9123456706,'license6.pdf','offline', NULL),
('Deepak Jain','deepak@example.com','deepak123',9123456707,'license7.pdf','online', NULL),
('Manish Kumar','manish@example.com','manish123',9123456708,'license8.pdf','offline', NULL),
('Nitin Patel','nitin@example.com','nitin123',9123456709,'license9.pdf','online', NULL),
('Sanjay Desai','sanjay@example.com','sanjay123',9123456710,'license10.pdf','online', NULL);

-- ======================
-- Table: UserVehicle
-- ======================
CREATE TABLE IF NOT EXISTS UserVehicle (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    vehicle_company VARCHAR(30) NOT NULL,
    vehicle_name VARCHAR(30) NOT NULL,
    vehicle_model VARCHAR(30) NOT NULL,
    vehicle_number VARCHAR(20) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

INSERT INTO UserVehicle (user_id, vehicle_company, vehicle_name, vehicle_model, vehicle_number) VALUES
(2,'Tesla','Model S','2025','MH12AB1234'),
(3,'Tata','Nexon EV','2024','MH14XY5678'),
(4,'MG','ZS EV','2024','MH15CD9876'),
(5,'Hyundai','Kona EV','2023','MH16EF6543'),
(6,'Mahindra','eVerito','2025','MH17GH3210'),
(7,'Kia','EV6','2025','MH18IJ7654'),
(8,'Jaguar','I-Pace','2024','MH19KL4321'),
(9,'BMW','i3','2023','MH20MN8765'),
(10,'Audi','e-tron','2024','MH21OP1230'),
(2,'Mercedes','EQC','2025','MH22QR0987');

-- ======================
-- Table: ChargingVan
-- ======================
CREATE TABLE IF NOT EXISTS ChargingVan (
    van_id INT AUTO_INCREMENT PRIMARY KEY,
    van_number VARCHAR(15) NOT NULL UNIQUE,
    operator_id INT DEFAULT NULL,
    battery_capacity VARCHAR(3) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (operator_id) REFERENCES VanOperator(operator_id)
);

INSERT INTO ChargingVan (van_number, operator_id, battery_capacity) VALUES
('MH14CV5678',2,'50'),
('MH18DV9012',3,'60'),
('MH19EV3456',4,'55'),
('MH20FV7890',5,'70'),
('MH21GV1234',6,'65'),
('MH22HV5678',7,'60'),
('MH23IV9012',8,'55'),
('MH24JV3456',9,'70'),
('MH25KV7890',10,'65'),
('MH26LV1234',2,'60');

-- ======================
-- Table: Request
-- ======================
CREATE TABLE IF NOT EXISTS request (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    operator_id INT DEFAULT NULL,
    vehicle_id INT NOT NULL,
    user_location VARCHAR(255) NOT NULL,
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_time TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (operator_id) REFERENCES vanOperator(operator_id),
    FOREIGN KEY (vehicle_id) REFERENCES uservehicle(vehicle_id)
);

INSERT INTO Request (user_id, operator_id, vehicle_id, user_location) VALUES
(2,2,1,'Nagpur Main Road'),
(3,3,2,'Pune City Center'),
(4,4,3,'Mumbai Airport'),
(5,5,4,'Nagpur Station'),
(6,6,5,'Pune Market'),
(7,7,6,'Mumbai Bandra'),
(8,8,7,'Nagpur City Center'),
(9,9,8,'Pune Highway'),
(10,10,9,'Mumbai Main Road'),
(2,2,10,'Nagpur IT Park');

-- ======================
-- Table: Booking
-- ======================
CREATE TABLE IF NOT EXISTS booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    operator_id INT NOT NULL,
    booking_status ENUM('pending','accepted','rejected','inprogress','completed','canceled') DEFAULT 'pending',
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    FOREIGN KEY (operator_id) REFERENCES vanoperator(operator_id)
);

INSERT INTO Booking (request_id, operator_id, booking_status, start_time, end_time) VALUES
(1,2,'inprogress','2026-01-01 10:00:00','2026-01-01 11:00:00'),
(2,3,'pending','2026-01-01 11:00:00','2026-01-01 12:00:00'),
(3,4,'accepted','2026-01-01 12:00:00','2026-01-01 13:00:00'),
(4,5,'completed','2026-01-01 13:00:00','2026-01-01 14:00:00'),
(5,6,'canceled','2026-01-01 14:00:00','2026-01-01 15:00:00'),
(6,7,'inprogress','2026-01-01 15:00:00','2026-01-01 16:00:00'),
(7,8,'pending','2026-01-01 16:00:00','2026-01-01 17:00:00'),
(8,9,'accepted','2026-01-01 17:00:00','2026-01-01 18:00:00'),
(9,10,'completed','2026-01-01 18:00:00','2026-01-01 19:00:00'),
(10,2,'inprogress','2026-01-01 19:00:00','2026-01-01 20:00:00');

-- ======================
-- Table: Payment
-- ======================
CREATE TABLE IF NOT EXISTS Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    user_id INT NOT NULL,
    operator_id INT NOT NULL,
    amount FLOAT(10) NOT NULL,
    p_method ENUM('upi','card','wallet') NOT NULL,
    p_status ENUM('success','failed','pending') DEFAULT 'pending',
    payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES Request(request_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (operator_id) REFERENCES vanOperator(operator_id)
);

INSERT INTO Payment (request_id, user_id, operator_id, amount, p_method, p_status) VALUES
(1,2,2,500,'upi','success'),
(2,3,3,600,'card','pending'),
(3,4,4,550,'wallet','success'),
(4,5,5,700,'upi','success'),
(5,6,6,650,'card','failed'),
(6,7,7,600,'wallet','success'),
(7,8,8,550,'upi','pending'),
(8,9,9,700,'card','success'),
(9,10,10,650,'wallet','success'),
(10,2,2,600,'upi','success');

-- ======================
-- Table: Feedback
-- ======================
CREATE TABLE IF NOT EXISTS Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    operator_id INT NOT NULL,
    rating INT CHECK(rating BETWEEN 1 AND 5),
    comments VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (operator_id) REFERENCES VanOperator(operator_id)
);

INSERT INTO Feedback (user_id, operator_id, rating, comments) VALUES
(2,2,5,'Excellent service!'),
(3,3,4,'Good experience.'),
(4,4,5,'Very satisfied!'),
(5,5,3,'Average service.'),
(6,6,4,'Good job!'),
(7,7,5,'Perfect service.'),
(8,8,4,'Nice experience.'),
(9,9,5,'Highly recommend!'),
(10,10,3,'Could be better.'),
(2,2,5,'Will use again!');
