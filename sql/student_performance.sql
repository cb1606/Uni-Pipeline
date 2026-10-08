-- Student Performance Transformation
-- Purpose: Classify students based on their Database Systems mark

SELECT
    student_id,
    name,
    qualification,
    year,
    module,
    mark,
    CASE
        WHEN mark >= 70 THEN 'Distinction'
        WHEN mark >= 50 THEN 'Pass'
        ELSE 'Fail'
    END AS performance
FROM students;
