select suppliers.supplier as supplier, null as year,null as category, (actions.price*actions.qty) as total from actions
inner join suppliers on suppliers.id = actions.supplier_id
group by suppliers.supplier
union distinct
select suppliers.supplier, year(actions.action_date), null, (actions.price*actions.qty) from actions
inner join suppliers on suppliers.id = actions.supplier_id
group by suppliers.supplier, year(actions.action_date)
union distinct
select suppliers.supplier, year(actions.action_date), categories.category,
(actions.price*actions.qty) from actions
inner join suppliers on suppliers.id = actions.supplier_id
inner join products on products.id = actions.product_id
inner join categories on categories.id = products.category_id
group by suppliers.supplier, year(actions.action_date), categories.category
order by supplier, year, category
