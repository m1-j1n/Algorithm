-- 코드를 입력하세요
SELECT
    i.ANIMAL_ID,
    i.ANIMAL_TYPE,
    i.NAME
FROM ANIMAL_INS i 
JOIN ANIMAL_OUTS o
on i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE like 'Intact%' 
and o.SEX_UPON_OUTCOME not like 'Intact%';