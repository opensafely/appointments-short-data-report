SELECT
    t1.Status,
    t1.num_values,
    t2.Description
FROM (
    SELECT
        Status,
        -- WARNING: There are duplicate rows in the Appointment table, so we add
        -- DISTINCT to remove them from this query. When they are removed from the
        -- Appointment table, then we will remove DISTINCT from this query.
        COUNT(DISTINCT Appointment_ID) AS num_values
    FROM Appointment
    WHERE Patient_ID IN (SELECT Patient_ID FROM AllowedPatientsWithTypeOneDissent)
    GROUP BY Status
) AS t1
LEFT OUTER JOIN ( -- noqa: L042
    SELECT -- noqa: L034
        CAST(Code AS INT) AS Code,
        Description
    FROM DataDictionary
    WHERE [Table] = 'Appointment'
) AS t2
ON t1.Status = t2.Code
ORDER BY t1.Status
