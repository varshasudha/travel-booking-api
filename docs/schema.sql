-- SQL schema for Travel Booking API

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    date DATE NOT NULL,
    seats_available INT NOT NULL,
    price NUMERIC NOT NULL
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    flight_id INT REFERENCES flights(id),
    user_id INT NOT NULL,
    status TEXT DEFAULT 'CONFIRMED',
    created_at TIMESTAMP DEFAULT now()
);