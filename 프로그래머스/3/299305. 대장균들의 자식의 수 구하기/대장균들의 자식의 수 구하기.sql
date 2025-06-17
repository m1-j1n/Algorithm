-- 1. child count 정보를 담은 테이블 생성
WITH Child_Count AS (
SELECT 
    PARENT_ID,
    COUNT(*) AS CHILD_COUNT
FROM ECOLI_DATA
GROUP BY PARENT_ID
)

-- 2. 메인쿼리
SELECT 
    ed.ID,
    COALESCE(cc.CHILD_COUNT, 0) AS CHILD_COUNT
FROM ECOLI_DATA ed
LEFT JOIN Child_Count cc
ON ed.ID = cc.PARENT_ID;