# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
) AS ranked_salaries 
WHERE rnk = 2;