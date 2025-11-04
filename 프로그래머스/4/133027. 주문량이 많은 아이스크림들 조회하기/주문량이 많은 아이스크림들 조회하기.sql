with sum_of_jan2jul as (
    select g.FLAVOR, SUM(g.TOTAL_ORDER) as TOTAL_ORDER
    from 
    (select * from FIRST_HALF 
    union all 
    select * from JULY) as g
    group by FLAVOR
)

select FLAVOR
from sum_of_jan2jul
order by TOTAL_ORDER desc limit 3;
