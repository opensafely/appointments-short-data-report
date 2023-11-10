SELECT
    lead_time_in_days,
    COUNT(lead_time_in_days) AS frequency
FROM (
    -- WARNING: There are duplicate rows in the Appointment table, so we add
    -- DISTINCT to remove them from this query. When they are removed from the
    -- Appointment table, then we will remove DISTINCT from this query.
    SELECT DISTINCT
        Appointment_ID,
        -- If `BookedDate <= StartDate`, then `StartDate - BookedDate >= 0`.
        DATEDIFF(
            DAY,
            CAST(BookedDate AS DATE), -- earlier
            CAST(StartDate AS DATE) -- later
        ) AS lead_time_in_days
    FROM Appointment
    WHERE Patient_ID NOT IN (SELECT Patient_ID FROM PatientsWithTypeOneDissent)
) AS t
GROUP BY lead_time_in_days
ORDER BY lead_time_in_days
