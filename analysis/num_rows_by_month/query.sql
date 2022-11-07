SELECT
    column_name,
    date,
    COUNT(Appointment_ID) AS num_rows
FROM (
    SELECT
        Appointment_ID,
        'BookedDate' AS column_name,
        DATEFROMPARTS(YEAR(BookedDate), MONTH(BookedDate), 1) AS date -- noqa:L016,L029
    FROM Appointment
    UNION ALL
    SELECT
        Appointment_ID,
        'StartDate' AS column_name,
        DATEFROMPARTS(YEAR(StartDate), MONTH(StartDate), 1) AS date -- noqa:L029
    FROM Appointment
) AS t
GROUP BY
    column_name,
    date
ORDER BY
    column_name,
    date
