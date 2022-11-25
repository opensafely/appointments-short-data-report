SELECT
    t1.Status,
    t1.num_values,
    t2.Description
FROM (
    SELECT
        Status,
        COUNT(Appointment_ID) AS num_values
    FROM Appointment
    GROUP BY Status
) AS t1
LEFT OUTER JOIN ( -- noqa: L042
    SELECT
        Code,
        Description
    FROM DataDictionary
    WHERE [Table] = 'Appointment'
) AS t2
ON t1.Status = t2.Code
