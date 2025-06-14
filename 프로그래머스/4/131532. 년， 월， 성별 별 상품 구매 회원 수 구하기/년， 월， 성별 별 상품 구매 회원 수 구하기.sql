-- 코드를 입력하세요
SELECT
    YEAR(os.SALES_DATE) YEAR,
    MONTH(os.SALES_DATE) MONTH,
    ui.GENDER GENDER,
    COUNT(DISTINCT os.USER_ID) USERS
FROM ONLINE_SALE os LEFT JOIN USER_INFO ui
on os.USER_ID = ui.USER_ID
WHERE ui.GENDER is not null
GROUP BY YEAR(os.SALES_DATE), MONTH(os.SALES_DATE), ui.GENDER
ORDER BY YEAR, MONTH, GENDER;