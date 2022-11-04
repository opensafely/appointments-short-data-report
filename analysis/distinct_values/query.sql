SELECT
    (SELECT COUNT(*) FROM (
        SELECT DISTINCT Appointment_ID, Patient_ID FROM Appointment) AS t -- noqa:L016,L036
    ) AS num_distinct_values,
    (SELECT COUNT(*) FROM (
        SELECT Appointment_ID FROM Appointment) AS t
    ) AS num_values
