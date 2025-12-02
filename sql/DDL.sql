CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE HealthInfo (
    member_id UNIQUE REFERENCES Members(member_id),
    heart_rate_bpm INTEGER,
    current_weight_lb INTEGER
);

CREATE TABLE FitnessGoals (
    member_id UNIQUE REFERENCES Members(member_id),
    target_weight_lb INTEGER
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE AvailableTimeslots (
    trainer_id INTEGER REFERENCES Trainers(trainer_id),
    time_slot_hour TIME
);

CREATE TABLE Rooms (
    room_number SERIAL PRIMARY KEY
);

CREATE TYPE EVENT_TYPE_ENUM AS ENUM ('Personal Session', 'Group Class');

CREATE TABLE FitnessEvents (
    event_id SERIAL PRIMARY KEY,
    event_type EVENT_TYPE_ENUM NOT NULL,
    room_number INTEGER REFERENCES Rooms(room_number),
    trainer_id INTEGER REFERENCES Trainers(trainer_id),
    time_slot_hour TIME
);

CREATE TABLE EventBookings (
    booking_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES FitnessEvents(event_id),
    member_id INTEGER REFERENCES Members(member_id)
);

CREATE TABLE AdministrativeStaff (
    admin_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
