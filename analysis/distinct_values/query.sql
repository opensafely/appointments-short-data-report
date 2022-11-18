SELECT
    t.Organisation_ID,
    COUNT(*) AS num_distinct_values,
    SUM(t.num_values) AS num_values
FROM (
    SELECT
        Organisation_ID,
        Appointment_ID,
        COUNT(*) AS num_values
    FROM Appointment
    GROUP BY Organisation_ID, Appointment_ID
) AS t
GROUP BY t.Organisation_ID
ORDER BY t.Organisation_ID
