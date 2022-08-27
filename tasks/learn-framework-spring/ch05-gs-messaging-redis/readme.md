## gs-messaging-redis Notes




- POJO, Plain Old Java Object, 简单 java 对象, from 2000
  - 那些没有继承任何类, 也没有实现任何接口, 更没有被其它框架侵入的java对象
  - > "POJO是这样的一种“纯粹的”JavaBean，在它里面除了JavaBean规范的方法和属性没有别的东西，即private属性以及对这个属性方法的public的get和set方法。我们会发现这样的JavaBean很“单纯”，它只能装载数据，作为数据存储的载体，而不具有业务逻辑处理的能力"
  - 可认为是一个**中间对象**
    - -> 持久化之后 -> PO
      - 在运行期，由Hibernate中的cglib动态把POJO转换为PO，PO相对于POJO会增加一些用来管理数据库entity状态的属性和方法。PO对于programmer来说完全透明，由于是运行期生成PO，所以可以支持增量编译，增量调试。
    - -> 传输过程中 -> DTO
    - -> 用作表示层 -> VO
- JavaBean, 遵从特定命名约定的POJO, from Java 2
  - 进程内组件
  - 遵循特定写法(一定的编程原则), 实现一些比较常用的简单功能, 并可以很容易的被重用或者是插入其他应用程序中去(反射技术实例化)
    - [public]必须具有一个公共的无参构造函数
      - 因为 Java Bean 是被容器所创建 (如 Tomcat) 的
    - [private] 全属性私有化 + 全属性的暴露 (getter / setter) + 命名规范
    - 可序列化
      - 比如可以实现Serializable 接口，用于实现bean的持久性
        - Java Bean 是不能被跨进程访问的
- Bean
  - 可重复使用的Java组件
    - 组件就是一个由可以自行进行内部管理的一个或几个类所组成、外界不了解其内部信息和运行方式的群体。使用它的对象只能通过接口来操作
- EJB (Enterprise JavaBean) , Entity Bean,
  - 核心代码，分别是
  - 分类
    - 会话 Bean (Session Bean)
      - 实现业务逻辑
      - 可以直接访问数据库, 更多时候, 它会通过 Entity Bean 实现数据访问
      - 这个类一般用单例模式来实现，因为每次连接都需要用到它
    - 实体Bean (Entity Bean)
      - 域模型对象
      - 用于实现O/R映射
      - 负责将数据库中的表记录映射为内存中的Entity对象
        - 创建一个Entity Bean对象相当于新建一条记录
        - 删除一个 Entity Bean会同时从数据库中删除对应记录
        - 修改一个Entity Bean时, 容器会自动将 Entity Bean 的状态和数据库同步
    - 消息驱动Bean (MessageDriven Bean)
  - 总的来说, EJB是一种是很老、很繁琐的技术标准 (规范) 了, 以至于被 Spring 彻底革了命
    - more via: [EJB到底是什么，真的那么神秘吗？](https://blog.csdn.net/jojo52013145/article/details/5783677 )
- PO, persistent object, 持久对象
  - O/R Mapping, Object Relational Mapping (对象关系映射)
  - 将对象与关系数据库绑定，用对象来表示关系数据
  - hibernate
    - 有时也被称为Data对象，对应数据库中的entity，可以简单认为一个PO对应数据库中的一条记录。
    - 在hibernate持久化框架中与insert/delet操作密切相关。
    - PO中不应该包含任何对数据库的操作。
    - PO的属性是跟数据库表的字段一一对应的。
    - PO对象需要实现序列化接口。
  - ,,,
- DTO, Data Transfer Object, 数据传输对象
  - 主要用于远程调用等需要大量传输对象的地方
  - 将PO中的部分属性抽取出来，就形成了DTO
    - 比如我们一张表有100个字段，那么对应的PO就有100个属性。但是我们界面上只要显示10个字段，客户端用WEB service来获取数据，没有必要把整个PO对象传递到客户端，这时我们就可以用只有这10个属性的DTO来传递结果到客户端，这样也不会暴露服务端表结构.到达客户端以后，如果用这个对象来对应界面显示，那此时它的身份就转为VO（View Object）
  - 用在需要跨进程或远程传输时，它不应该包含业务逻辑。
- VO, value object/view object, 值对象 / 表现层 (视图) 对象
  - value object
    - 业务对象，是存活在业务层的，是业务逻辑使用的
  - view object
    - 用一个VO对象对应整个界面的值
- DAO, data access object, 数据访问对象
  - 封装对数据库的访问。通过它可以把POJO持久化为PO，用PO组装出来VO、DTO
    - 封装对DB (数据库) 的访问 (CRUD操作)
    - 接收业务层的数据，把 POJO 持久化为 PO
- BO, business object 业务对象
  - 主要作用是把业务逻辑封装为一个对象
  - 这个对象可以包括一个或多个其它的对象
  - 主要有三种概念
    - 只包含业务对象的属性；
    - 只包含业务方法；
    - 两者都包含。
  - 在实际使用中，认为哪一种概念正确并不重要，关键是实际应用中适合自己项目的需要






  - via: [什么是JavaBean、bean? 什么是POJO、PO、DTO、VO、BO ? 什么是EJB、EntityBean？ - panchanggui - 博客园](https://www.cnblogs.com/panchanggui/p/11610998.html )