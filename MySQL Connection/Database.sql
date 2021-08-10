--  練習

-- 1. 取得所有員工資料
SELECT * FROM `employee`;
-- 2. 取得所有客戶資料
SELECT * FROM `client`;
-- 3. 按照薪水低到高取得員工資料
SELECT * FROM `employee`
ORDER BY `sex`;

-- 4.取得薪水前三高的員工
SELECT * FROM `employee`
ORDER BY `salary` DESC
LIMIT 3;

-- 5.取得所有員工名子
SELECT `name` FROM `employee`;

