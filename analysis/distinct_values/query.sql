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

        -- WARNING: There are duplicate rows in the Appointment table, so we add
        -- DISTINCT to remove them from this query. When they are removed from the
        -- Appointment table, then we will remove DISTINCT from this query.
        SELECT DISTINCT
            Organisation_ID,
            Appointment_ID,
            DATEFROMPARTS(YEAR(BookedDate), MONTH(BookedDate), 1) AS booked_date
        FROM Appointment
        -- There is an outlier year in BookedDate. The time between the outlier
        -- year and the preceding year is considerable, so the interesting part
        -- of the distribution is compressed. To avoid compressing the
        -- interesting part of the distribution, we exclude years after the
        -- current year from the distribution. We considered several approaches
        -- to exclusion. For more information, see:
        -- https://github.com/opensafely/appointments-short-data-report/pull/38
        WHERE YEAR(BookedDate) <= (SELECT YEAR(GETDATE()))
            AND Patient_ID NOT IN (SELECT Patient_ID FROM PatientsWithTypeOneDissent)
    ) AS t0
    GROUP BY t0.Organisation_ID, t0.Appointment_ID, t0.booked_date
) AS t1
GROUP BY t1.Organisation_ID, t1.booked_date
ORDER BY t1.Organisation_ID, t1.booked_date
