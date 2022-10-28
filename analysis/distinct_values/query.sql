SELECT
    COUNT(DISTINCT Appointment_ID) AS num_distinct_values,
    COUNT(Appointment_ID) AS num_values
FROM
    Appointment;
