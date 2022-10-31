SELECT
    column_name,
    year,
    month,
    COUNT(Appointment_ID) AS num_rows
FROM (
    SELECT
        Appointment_ID,
        'BookedDate' AS column_name,
        YEAR(BookedDate) AS year,
        MONTH(BookedDate) AS month
    FROM Appointment
    UNION ALL
    SELECT
        Appointment_ID,
        'StartDate' AS column_name,
        YEAR(StartDate) AS year,
        MONTH(StartDate) AS month
    FROM Appointment
) AS t
GROUP BY
    column_name,
    year,
    month
ORDER BY
    column_name,
    year,
    month
