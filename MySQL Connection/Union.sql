 -- union聯集
 
 -- 員工名子 union 客戶名子
 SELECT `name`
 FROM `employee`
 UNION
 SELECT `client_name`
 FROM `client`;
 -- 2.員工id+員工名子 union 客戶id+客戶名子
SELECT `emp_id`,`name`
FROM `employee`
UNION
SELECT `client_id`,`client_name`
FROM `client`;
 
 -- 3.員工薪水 union銷售金額
SELECT `salary`
FROM `employee`
UNION
SELECT `total_sales`
FROM `works_with`;