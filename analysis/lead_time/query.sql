SELECT
    lead_time_in_days,
    COUNT(lead_time_in_days) AS frequency
FROM (
    SELECT DATEDIFF(
        DAY,
        CAST(StartDate AS DATE),
        CAST(BookedDate AS DATE)
    ) AS lead_time_in_days
    FROM Appointment
) AS t
GROUP BY lead_time_in_days
ORDER BY lead_time_in_days
