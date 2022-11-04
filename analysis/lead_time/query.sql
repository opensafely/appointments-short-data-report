SELECT
    lead_time_in_days,
    COUNT(lead_time_in_days) AS frequency
FROM (
    -- If `BookedDate <= StartDate`, then `StartDate - BookedDate >= 0`.
    SELECT DATEDIFF(
        DAY,
        CAST(BookedDate AS DATE), -- earlier
        CAST(StartDate AS DATE) -- later
    ) AS lead_time_in_days
    FROM Appointment
) AS t
GROUP BY lead_time_in_days
ORDER BY lead_time_in_days
