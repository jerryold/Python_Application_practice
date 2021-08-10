-- subquery 子查詢
-- 1.找出研發部門的經理名子
SELECT `name` 
FROM `employee`
WHERE `emp_id`=(
	SELECT `manager_id` 
	FROM `branch`
	WHERE `branch_name`='研發'
);

-- 2.找出對單一客戶銷售金額超過50000的員工名子
SELECT `name` 
FROM `employee`
WHERE `emp_id` IN(
	SELECT `emp_id` 
	FROM `works_with`
	WHERE `total_sales`>50000
    );
