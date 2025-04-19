WITH cte AS(
SELECT *,DATE_ADD(recordDate,INTERVAL -1 DAY) AS yesterday,LAG(recordDate) OVER(ORDER BY recordDate) AS prevday,LAG(temperature) OVER(ORDER BY recordDate) AS prev_temp FROM Weather)

select id from cte where yesterday=prevday and temperature>prev_temp