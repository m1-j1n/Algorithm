-- 코드를 입력하세요
SELECT
    FP.PRODUCT_ID,
    FP.PRODUCT_NAME,
    SUM(FO.AMOUNT) * FP.PRICE AS TOTAL_SALES
FROM FOOD_ORDER FO
JOIN FOOD_PRODUCT FP
on FO.PRODUCT_ID = FP.PRODUCT_ID
WHERE YEAR(FO.PRODUCE_DATE) = 2022 and MONTH(FO.PRODUCE_DATE) = 5
GROUP BY FP.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FP.PRODUCT_ID;