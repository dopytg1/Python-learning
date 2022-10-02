SELECT YEAR(actions.action_date) as year, month(actions.action_date) as month,
day(actions.action_date) as day,
SUM(actions.qty * actions.price) as `sum` FROM actions
GROUP BY YEAR(actions.action_date) 
UNION distinct
SELECT year(actions.action_date), MONTH(actions.action_date),
day(actions.action_date), 
SUM(actions.qty * actions.price) FROM actions
GROUP BY MONTH(actions.action_date)
UNION distinct
SELECT year(actions.action_date), month(actions.action_date),
DAY(actions.action_date),
SUM(actions.qty * actions.price) FROM actions
GROUP BY DAY(actions.action_date)
order by year, month, day;