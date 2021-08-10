-- join連接alter

-- 取得所有部門經理的名子
SELECT `employee`.`emp_id`,`employee`.`name`,`branch`.`manager_id`
FROM `employee`
LEFT JOIN `branch`
on `employee`.`emp_id`=`branch`.`manager_id`;