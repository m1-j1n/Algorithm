with employees_grade_2022 as (
    select sum(hg.SCORE) as SCORE, hg.EMP_NO, he.EMP_NAME, he.POSITION, he.EMAIL
    from HR_EMPLOYEES he
    join HR_GRADE hg
    on he.EMP_NO = hg.EMP_NO
    group by emp_no
)

select * from employees_grade_2022
where SCORE in (
    select max(SCORE)
    from employees_grade_2022
)