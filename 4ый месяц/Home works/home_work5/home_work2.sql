USE study_database;

SELECT suppliers.supplier, SUM(qty*actions.price) AS "totalSum" FROM actions 
INNER JOIN suppliers ON suppliers.id = actions.supplier_id
WHERE YEAR(actions.action_date) = "2020"
GROUP BY suppliers.supplier
UNION
SELECT categories.category, SUM(qty*actions.price) AS "totalSum" FROM actions
INNER JOIN products ON products.id = actions.product_id
INNER JOIN categories ON categories.id = products.category_id
WHERE YEAR(actions.action_date) = "2020"
GROUP BY categories.category;