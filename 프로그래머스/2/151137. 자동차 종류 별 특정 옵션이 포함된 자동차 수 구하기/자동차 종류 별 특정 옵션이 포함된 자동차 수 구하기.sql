-- 코드를 입력하세요
SELECT
    CAR_TYPE,
    COUNT(CAR_ID) CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS Like '%가죽시트%' 
    OR OPTIONS Like '%통풍시트%' 
    OR OPTIONS Like '%열선시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;