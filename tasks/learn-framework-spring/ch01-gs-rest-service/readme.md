## gs-rest-service Notes

- origin url: [Getting Started | Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/#initial )

- In Spring’s approach to building RESTful web services, HTTP requests are handled by a controller.

### traditional MVC controller vs RESTful web service controller

- A key difference between a traditional MVC controller and the RESTful web service controller shown earlier is **the way that the HTTP response body is created**.
  - Rather than relying on a view technology to perform server-side rendering of the greeting data to HTML, this RESTful web service controller populates and returns a `Greeting` object. The object data will be written directly to the HTTP response as JSON.

### Annotation

- `@RestController`
  - marks the class as a controller where every method returns a domain object instead of a view. It is shorthand for including both `@Controller` and `@ResponseBody`.
    - The `Greeting` object must be converted to JSON. Thanks to Spring’s HTTP message converter support, you need not do this conversion manually.
- Because `Jackson 2` is on the classpath, Spring’s `MappingJackson2HttpMessageConverter` is automatically chosen to convert the `Greeting` instance to JSON.
- `@SpringBootApplication` is a convenience annotation that adds all of the following:
    - `@Configuration`: Tags the class as a source of bean definitions for the application context.
    - `@EnableAutoConfiguration`: Tells Spring Boot to start adding beans based on classpath settings, other beans, and various property settings. For example, if `spring-webmvc` is on the classpath, this annotation flags the application as a web application and activates key behaviors, such as setting up a `DispatcherServlet`.
    - `@ComponentScan`: Tells Spring to look for other components, configurations, and services in the `com/example` package, letting it find the controllers.

### 并发 AtomicLong

- [JUC-02- AtomicLong使用入门及源码详解 | Echo Blog](https://houbb.github.io/2019/01/20/juc-02-atomiclong )
  - 可以原子更新的 Long 值。
  - AtomicLong 用于诸如原子递增的序列号之类的应用程序中，并且不能用作 Long 的替代品。
  - 但是，此类确实扩展了Number，以允许通过处理基于数字的类的工具和实用程序进行统一访问。
  - 当我们在进行计数统计的时，通常会使用 AtomicLong 来实现AtomicLong 能保证并发情况下计数的准确性，其内部通过 CAS 来解决并发安全性的问题
    - 跳到实现里面 VM_SUPPORTS_LONG_CAS 是一个静态变量，加载时调用VMSupportsCS8方法
    - VMSupportsCS8判断当前的JVM是否支持无锁的CAS，只调用一次并缓存下来

### Unit Test

- 单元测试 `MockMvc` via: [SpringBoot基础之MockMvc单元测试 - 知乎](https://zhuanlan.zhihu.com/p/61342833 )
  - 拟对象 (mock object) 是以可控的方式模拟真实对象行为的假对象
  - `spring-test` 包提供
  - 实现了对Http请求的模拟
    - 能够直接使用网络的形式，转换到Controller的调用
    - 测试速度快
    - 不依赖网络环境
    - 提供了一套验证的工具

```java
/** 编写测试类
  * via: https://zhuanlan.zhihu.com/p/61342833
  */
//SpringBoot1.4版本之前用的是SpringJUnit4ClassRunner.class
@RunWith(SpringRunner.class)
//SpringBoot1.4版本之前用的是@SpringApplicationConfiguration(classes = Application.class)
@SpringBootTest
//测试环境使用，用来表示测试环境使用的ApplicationContext将是WebApplicationContext类型的
@WebAppConfiguration
public class HelloWorldTest {
    private MockMvc mockMvc;
    @Autowired
    private WebApplicationContext webApplicationContext;
    @Before
    public void setup() {
        // 实例化方式一
        mockMvc = MockMvcBuilders.standaloneSetup(new HelloWorldController()).build();
        // 实例化方式二
//        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
    }


/** 单元测试方法
  */
@Test
public void testHello() throws Exception {
    /*
     * 1、mockMvc.perform执行一个请求。
     * 2、MockMvcRequestBuilders.get("XXX")构造一个请求。
     * 3、ResultActions.param添加请求传值
     * 4、ResultActions.accept(MediaType.TEXT_HTML_VALUE))设置返回类型
     * 5、ResultActions.andExpect添加执行完成后的断言。
     * 6、ResultActions.andDo添加一个结果处理器，表示要对结果做点什么事情
     *   比如此处使用MockMvcResultHandlers.print()输出整个响应结果信息。
     * 7、ResultActions.andReturn表示执行完成后返回相应的结果。
     */
    mockMvc.perform(MockMvcRequestBuilders
            .get("/hello")
            // 设置返回值类型为utf-8，否则默认为ISO-8859-1
            .accept(MediaType.APPLICATION_JSON_UTF8_VALUE)
            .param("name", "Tom"))
            .andExpect(MockMvcResultMatchers.status().isOk())
            .andExpect(MockMvcResultMatchers.content().string("Hello Tom!"))
            .andDo(MockMvcResultHandlers.print());
}
```


- 常用的测试

```java
/* 测试普通控制器 */
mockMvc.perform(get("/user/{id}", 1)) //执行请求  
            .andExpect(model().attributeExists("user")) //验证存储模型数据  
            .andExpect(view().name("user/view")) //验证viewName  
            .andExpect(forwardedUrl("/WEB-INF/jsp/user/view.jsp"))//验证视图渲染时forward到的jsp  
            .andExpect(status().isOk())//验证状态码  
            .andDo(print()); //输出MvcResult到控制台

/* 得到MvcResult自定义验证 */
MvcResult result = mockMvc.perform(get("/user/{id}", 1))//执行请求  
        .andReturn(); //返回MvcResult  
Assert.assertNotNull(result.getModelAndView().getModel().get("user")); //自定义断言

/*验证请求参数绑定到模型数据及Flash属性*/
mockMvc.perform(post("/user").param("name", "zhang")) //执行传递参数的POST请求(也可以post("/user?name=zhang"))  
            .andExpect(handler().handlerType(UserController.class)) //验证执行的控制器类型  
            .andExpect(handler().methodName("create")) //验证执行的控制器方法名  
            .andExpect(model().hasNoErrors()) //验证页面没有错误  
            .andExpect(flash().attributeExists("success")) //验证存在flash属性  
            .andExpect(view().name("redirect:/user")); //验证视图

/* 文件上传 */
byte[] bytes = new byte[] {1, 2};  
mockMvc.perform(fileUpload("/user/{id}/icon", 1L).file("icon", bytes)) //执行文件上传  
        .andExpect(model().attribute("icon", bytes)) //验证属性相等性  
        .andExpect(view().name("success")); //验证视图

/* JSON请求/响应验证 */
String requestBody = "{\"id\":1, \"name\":\"zhang\"}";
mockMvc.perform(post("/user")
        .contentType(MediaType.APPLICATION_JSON).content(requestBody)
        .accept(MediaType.APPLICATION_JSON))                          // 执行请求
        .andExpect(content().contentType(MediaType.APPLICATION_JSON)) // 验证响应contentType(JSON)
        .andExpect(jsonPath("$.id").value(1));
        // NOTE: Json path验证JSON. via: http://goessner.net/articles/JsonPath

String errorBody = "{id:1, name:zhang}";
MvcResult result = mockMvc.perform(post("/user")
        .contentType(MediaType.APPLICATION_JSON).content(errorBody)
        .accept(MediaType.APPLICATION_JSON))                          // 执行请求
        .andExpect(status().isBadRequest())                           // 400错误请求
        .andReturn();
Assert.assertTrue(HttpMessageNotReadableException.class.isAssignableFrom(result.getResolvedException().getClass()));//错误的请求内容体


/*异步测试 Callable*/
MvcResult result = mockMvc.perform(get("/user/async1?id=1&name=zhang")) //执行请求  
        .andExpect(request().asyncStarted())  
        .andExpect(request().asyncResult(CoreMatchers.instanceOf(User.class))) //默认会等10秒超时  
        .andReturn();  
mockMvc.perform(asyncDispatch(result))
        .andExpect(status().isOk())
        .andExpect(content().contentType(MediaType.APPLICATION_JSON))
        .andExpect(jsonPath("$.id").value(1));

/* 全局配置 */
mockMvc = webAppContextSetup(wac)
            .defaultRequest(get("/user/1").requestAttr("default", true))
            //默认请求 如果其是Mergeable类型的，会自动合并的哦 mockMvc.perform中的RequestBuilder
            .alwaysDo(print())  //默认每次执行请求后都做的动作  
            .alwaysExpect(request().attribute("default", true)) //默认每次执行后进行验证的断言  
            .build();
mockMvc.perform(get("/user/1"))
            .andExpect(model().attributeExists("user"));
```


## Jenkins

- [开始使用 Jenkins](https://www.jenkins.io/zh/doc/pipeline/tour/getting-started/ )
  - Jenkins Pipeline（或简称为 "Pipeline"）是一套插件，将持续交付的实现和实施集成到 Jenkins 中
