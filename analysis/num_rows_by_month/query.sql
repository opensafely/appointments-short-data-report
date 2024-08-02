WITH AppointmentWithoutTypeOneDissent
AS (
    SELECT
        Appointment_ID,
        BookedDate,
        StartDate
    FROM Appointment
    WHERE Patient_ID IN (SELECT Patient_ID FROM AllowedPatientsWithTypeOneDissent)
)

SELECT
    column_name,
    date,
    COUNT(Appointment_ID) AS num_rows
FROM (
    -- WARNING: There are duplicate rows in the Appointment table, so we add
    -- DISTINCT to remove them from this query. When they are removed from the
    -- Appointment table, then we will remove DISTINCT from this query.
    SELECT DISTINCT
        Appointment_ID,
        'BookedDate' AS column_name,
        DATEFROMPARTS(YEAR(BookedDate), MONTH(BookedDate), 1) AS date -- noqa:L016,L029
    FROM AppointmentWithoutTypeOneDissent
    UNION ALL
    -- WARNING: There are duplicate rows in the Appointment table, so we add
    -- DISTINCT to remove them from this query. When they are removed from the
    -- Appointment table, then we will remove DISTINCT from this query.
    SELECT DISTINCT
        Appointment_ID,
        'StartDate' AS column_name,
        DATEFROMPARTS(YEAR(StartDate), MONTH(StartDate), 1) AS date -- noqa:L029
    FROM AppointmentWithoutTypeOneDissent
) AS t
GROUP BY
    column_name,
    date
ORDER BY
    column_name,
    date
