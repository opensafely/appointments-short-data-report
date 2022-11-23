SELECT
    t1.Organisation_ID,
    t1.booked_date,
    COUNT(*) AS num_distinct_values,
    SUM(t1.num_values) AS num_values
FROM (
    SELECT
        t0.Organisation_ID,
        t0.Appointment_ID,
        t0.booked_date,
        COUNT(*) AS num_values
    FROM (
        -- GROUP BY is processed before SELECT, so we can't SELECT booked_date
        -- and GROUP BY it in the same query. So, we SELECT booked_date in an
        -- inner query and GROUP BY it in an outer query.
        SELECT
            Organisation_ID,
            Appointment_ID,
            DATEFROMPARTS(YEAR(BookedDate), MONTH(BookedDate), 1) AS booked_date
        FROM Appointment
    ) AS t0
    GROUP BY t0.Organisation_ID, t0.Appointment_ID, t0.booked_date
) AS t1
GROUP BY t1.Organisation_ID, t1.booked_date
ORDER BY t1.Organisation_ID, t1.booked_date
