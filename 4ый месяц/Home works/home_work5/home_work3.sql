USE study_database;

SELECT categories.category, YEAR(actions.action_date) AS "year",  
SUM(actions.qty*actions.price) / CAST(actions.qty AS FLOAT) AS "totalSum",
MAX(actions.price) AS "max", MIN(actions.price) AS "min"
FROM actions
INNER JOIN products ON products.id = actions.product_id
INNER JOIN categories ON categories.id = products.category_id
GROUP BY categories.category, YEAR(actions.action_date)
ORDER BY categories.category and YEAR(actions.action_date);