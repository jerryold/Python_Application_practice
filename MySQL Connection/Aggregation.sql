-- aggregrate function 聚合函數

-- 1.取得員工人數
SELECT Count(`sup_id`)FROM `employee`;

-- 2.取得所有出生於1970-01-01之後女性員工人數
SELECT Count(*)
FROM `employee`
WHERE `birth_date` > '1970-01-01' AND `sex`='F';

-- 3.取得所有出員工平均薪水
SELECT AVG(`salary`) from `employee`

-- 4.取得所有員工薪水總和
SELECT SUM(`salary`) from `employee`

-- 5.取得薪水最高員工
SELECT MAX(`salary`) from `employee`

-- 6.取得薪水最低員工
SELECT MIN(`salary`) from `employee`