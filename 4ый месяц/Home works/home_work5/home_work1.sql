USE study_database;

SELECT brands.brand, SUM(qty*actions.price) AS "totalSum" FROM actions
INNER JOIN products ON products.id = actions.product_id
INNER JOIN brands ON brands.id = products.brand_id
GROUP BY brands.brand;
