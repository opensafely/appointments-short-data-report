SELECT
    MAX(BookedDate) AS max_booked_date,
    MIN(BookedDate) AS min_booked_date,
    MAX(StartDate) AS max_start_date,
    MIN(StartDate) AS min_start_date,
    MAX(ArrivedDate) AS max_arrived_date,
    MIN(ArrivedDate) AS min_arrived_date,
    MAX(EndDate) AS max_end_date,
    MIN(EndDate) AS min_end_date,
    MAX(FinishedDate) AS max_finished_date,
    MIN(FinishedDate) AS min_finished_date,
    MAX(SeenDate) AS max_seen_date,
    MIN(SeenDate) AS min_seen_date
FROM Appointment;
