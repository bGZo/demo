#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select firstName, lastName, city, state
from Person p left join Address a
    on p.PersonId=a.PersonId;


# 数据库在通过连接两张或多张表来返回记录时，都会生成一张中间的临时表，
# 然后再将这张临时表返回给用户。 在使用left jion时，on和where条件的区别如下：
    # 1、on条件是在生成临时表时使用的条件，它不管on中的条件是否为真，都会返回左边表中的记录。
    # 2、where条件是在临时表生成好后，再对临时表进行过滤的条件。这时已经没有left join的含义
    # （必须返回左边表的记录）了，条件不为真的就全部过滤掉。
#leetcode submit region end(Prohibit modification and deletion)

# 组合两个表
#表: Person 
#
# 
#+-------------+---------+
#| 列名         | 类型     |
#+-------------+---------+
#| PersonId    | int     |
#| FirstName   | varchar |
#| LastName    | varchar |
#+-------------+---------+
#personId 是该表的主键列。
#该表包含一些人的 ID 和他们的姓和名的信息。
# 
#
# 
#
# 表: Address 
#
# 
#+-------------+---------+
#| 列名         | 类型    |
#+-------------+---------+
#| AddressId   | int     |
#| PersonId    | int     |
#| City        | varchar |
#| State       | varchar |
#+-------------+---------+
#addressId 是该表的主键列。
#该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。
# 
#
# 
#
# 编写一个SQL查询来报告 Person 表中每个人的姓、名、城市和州。如果 personId 的地址不在 Address 表中，则报告为空 null 。 
#
# 以 任意顺序 返回结果表。 
#
# 查询结果格式如下所示。 
#
# 
#
# 示例 1: 
#
# 
#输入: 
#Person表:
#+----------+----------+-----------+
#| personId | lastName | firstName |
#+----------+----------+-----------+
#| 1        | Wang     | Allen     |
#| 2        | Alice    | Bob       |
#+----------+----------+-----------+
#Address表:
#+-----------+----------+---------------+------------+
#| addressId | personId | city          | state      |
#+-----------+----------+---------------+------------+
#| 1         | 2        | New York City | New York   |
#| 2         | 3        | Leetcode      | California |
#+-----------+----------+---------------+------------+
#输出: 
#+-----------+----------+---------------+----------+
#| firstName | lastName | city          | state    |
#+-----------+----------+---------------+----------+
#| Allen     | Wang     | Null          | Null     |
#| Bob       | Alice    | New York City | New York |
#+-----------+----------+---------------+----------+
#解释: 
#地址表中没有 personId = 1 的地址，所以它们的城市和州返回 null。
#addressId = 1 包含了 personId = 2 的地址信息。 
# Related Topics 数据库 👍 1159 👎 0
