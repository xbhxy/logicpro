#QUESTION13

SELECT
    s.student_name,
    s.city,
    c.course_name,
    r.subject,
    r.marks
FROM students s
INNER JOIN courses c
    ON s.course_id = c.course_id
LEFT JOIN results r
    ON s.student_id = r.student_id;


#QUESTION14

SELECT
    c.course_name,
    COUNT(DISTINCT s.student_id) AS total_students,
    AVG(r.marks) AS average_marks
FROM courses c
INNER JOIN students s
    ON c.course_id = s.course_id
INNER JOIN results r
    ON s.student_id = r.student_id
GROUP BY c.course_id, c.course_name
HAVING AVG(r.marks) > 70;


#QUESTION15

WITH StudentAvg AS (
    SELECT
        s.student_id,
        s.student_name,
        s.course_id,
        AVG(r.marks) AS average_marks
    FROM students s
    JOIN results r
        ON s.student_id = r.student_id
    GROUP BY
        s.student_id,
        s.student_name,
        s.course_id
)
SELECT
    student_name,
    average_marks,
    RANK() OVER (
        PARTITION BY course_id
        ORDER BY average_marks DESC
    ) AS student_rank
FROM StudentAvg;