INSERT INTO Members (first_name, last_name, email) VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Jim', 'Beam', 'jim.beam@example.com'),
    ('Adam', 'Locke', 'adam.locke@example.com'),
    ('Brandon', 'Curie', 'bradon.curie@example.com');

INSERT INTO HealthInfo (member_id, heart_rate_bpm, current_weight_lb) VALUES
    (1, 80, 150),
    (2, 74, 130),
    (3, 120, 210),
    (4, 143, 180),
    (5, 90, 105);

INSERT INTO FitnessGoals (member_id, target_weight_lb) VALUES
    (1, 140),
    (2, 115),
    (3, 150),
    (4, 140),
    (5, 125);

INSERT INTO Trainers (first_name, last_name) VALUES
    ('Joseph', 'Harper'),
    ('Jackson', 'Smith'),
    ('Riley', 'Lincoln'),
    ('Ashley', 'Hudson'),
    ('Alex', 'Kennedy');

Insert INTO AvailableTimeslots (trainer_id, time_slot_hour) VALUES
    (1, '09:00'),
    (1, '10:00'),
    (1, '11:00'),
    (1, '12:00'),
    (2, '13:00'),
    (2, '14:00'),
    (2, '15:00'),
    (3, '16:00'),
    (4, '17:00'),
    (5, '08:00');

INSERT INTO Rooms (room_number) VALUES
    (114),
    (115),
    (116),
    (117),
    (214),
    (215),
    (216),
    (217);

INSERT INTO FitnessEvents (event_type, room_number, trainer_id, time_slot_hour) VALUES
    ('Personal Session', 114, 1, '09:00'),
    ('Personal Session', 114, 1, '10:00'),
    ('Personal Session', 115, 2, '14:00'),
    ('Group Class', 114, 3, '16:00'),
    ('Personal Session', 214, 4, '17:00');

INSERT INTO EventBookings (event_id, member_id) VALUES
    (1, 1),
    (2, 2),
    (4, 1),
    (4, 4),
    (4, 5);

INSERT INTO AdministrativeStaff (first_name, last_name) VALUES
    ('Alice', 'Griffin'),
    ('Avery', 'Quinn'),
    ('James', 'Beckett'),
    ('Logan', 'Sawyer'),
    ('Dylan', 'Wallace');
