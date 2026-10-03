# Write your MySQL query statement below
SELECT v.customer_id,count(customer_id) as count_no_trans
FROM visits v
left join Transactions t
using (visit_id)
where transaction_id is null
group by customer_id