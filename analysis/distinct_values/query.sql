SELECT
    t.Status,
    COUNT(*) AS num_distinct_values,
    SUM(t.num_values) AS num_values
FROM (
    SELECT
        Status,
        Appointment_ID,
        COUNT(*) AS num_values
    FROM Appointment
    GROUP BY Status, Appointment_ID
) AS t
GROUP BY t.Status
ORDER BY t.Status
