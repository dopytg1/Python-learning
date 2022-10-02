-- 1)

select products.product, actions.amount from actions
inner join products on products.id = actions.id_product
where actions.operation = "coming" and year(actions.action_date) = 2020
and actions.id_storage = 1
group by products.product;

-- 2)

select products.product, actions.amount from actions
inner join products on products.id = actions.id_product
where actions.operation = "leaving" and year(actions.action_date) = 2020
and actions.id_storage = 2
group by products.product;

-- 3)

select category.category, actions.amount from actions
inner join products on products.id = actions.id_product
inner join category on category.id = products.id_category
where actions.operation = "coming" and year(actions.action_date) = 2020
and actions.id_storage = 1
group by products.product;

-- 4)

select brand.brand, actions.amount from actions
inner join products on products.id = actions.id_product
inner join brand on brand.id = products.id_brand
where actions.operation = "coming" and year(actions.action_date) = 2020
and actions.id_storage = 1
group by products.product;

-- 5)

select products.product, sum(amount) from actions
inner join products on products.id = actions.id_product
where actions.id_storage = 2 
and year(actions.action_date) = 2020
and actions.amount > 0
group by products.product;

-- 6)

select products.product, sum(actions.amount) from actions
inner join products on products.id = actions.id_product
where actions.id_counterparties = 1
and year(actions.action_date) = 2019
group by products.product;

-- 7)

select products.product, sum(actions.amount) from actions
inner join products on products.id = actions.id_product
where actions.id_counterparties = 1
and year(actions.action_date) = 2019
and actions.id_storage = 1
and actions.amount > 0
group by products.product;

-- 8)

select products.product, sum(actions.amount) from actions
inner join products on products.id = actions.id_product
where actions.id_counterparties = 2
and year(actions.action_date) = 2020
and actions.id_storage = 1
and actions.amount < 0
group by products.product;

-- 9)

select counterparties.contractor, sum(actions.amount) from actions 
inner join counterparties on counterparties.id = actions.id_counterparties
where actions.id_product = 2 and actions.amount > 0 
and year(actions.action_date) = 2019;


-- 10)

select counterparties.contractor, sum(actions.amount) from actions 
inner join counterparties on counterparties.id = actions.id_counterparties
where actions.id_product = 2 and actions.amount < 0 
and year(actions.action_date) = 2020;

-- 11)

select products.product, sum(actions.amount) from actions
inner join products on products.id = actions.id_product
inner join counterparties on counterparties.id = actions.id_counterparties
where counterparties.id_storage is not null
and actions.id_storage = 4
and year(actions.action_date) = 2020
group by products.product;

-- 12)

select products.product, sum(actions.amount) from actions
inner join products on products.id = actions.id_product
inner join counterparties on counterparties.id = actions.id_counterparties
where counterparties.id_storage is not null
and counterparties.id_storage = 2
and year(actions.action_date) = 2020
group by products.product;
