## gs consuming rest Notes


- origin url: [Getting Started | Consuming a RESTful Web Service](https://spring.io/guides/gs/consuming-rest)

```java
@SpringBootApplication
public class ConsumingRestApplication {

	private static final Logger log = LoggerFactory.getLogger(ConsumingRestApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(ConsumingRestApplication.class, args);
	}

	@Bean
	public RestTemplate restTemplate(RestTemplateBuilder builder) {
		return builder.build();
	}

	@Bean
	public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
		return args -> {
			Quote quote = restTemplate.getForObject(
					"https://quoters.apps.pcfone.io/api/random", Quote.class);
			log.info(quote.toString());
		};
	}
}
```

- add a few other things to the ConsumingRestApplication class to get it to show quotations from our RESTful source.
  - A logger, to send output to the log (the console, in this example).
  - A `RestTemplate`, which uses the Jackson JSON processing library to process the incoming data.
  - A `CommandLineRunner` that runs the `RestTemplate` (and, consequently, fetches our quotation) on startup.
- `@Bean`: 告诉方法，产生一个Bean对象，然后这个Bean对象交给Spring管理
  - 产生这个Bean对象的方法Spring只会调用一次，随后这个Spring将会将这个Bean对象放在自己的IOC容器中
  - 这些bean都需要在@Configuration注解下进行创建，在一个方法上使用@Bean注解就表明这个方法需要交给Spring进行管理
  - ```java
    @Target({ElementType.METHOD, ElementType.ANNOTATION_TYPE})
    @Retention(RetentionPolicy.RUNTIME)
    @Documented
    public @interface Bean {

        @AliasFor("name")
        String[] value() default {};

        @AliasFor("value")
        String[] name() default {};

        Autowire autowire() default Autowire.NO;

        String initMethod() default "";

        String destroyMethod() default AbstractBeanDefinition.INFER_METHOD;

    }
    ```
- `RestTemplate` makes interacting with most RESTful services a one-line incantation. And it can even bind that data to custom domain types.
  - First, you need to create a domain class to contain the data that you need.(Quote.java)
- `@JsonIgnoreProperties` from the Jackson JSON processing library to indicate that any properties not bound in this type should be ignored. via: [@jsonignore和@JsonIgnoreProperties的区别_筱_智的博客-CSDN博客_@jsonignoreproperties](https://blog.csdn.net/pojpoj/article/details/85292512)
  - In case your variable name and key in JSON doc do not match, you can use `@JsonProperty` annotation to specify the exact key of the JSON document.
  - ```java
    //生成json时将name和age属性过滤
    @JsonIgnoreProperties({“name”},{“age”})
    public class user {
        private String name;
        private int age;
    }

    public class user {
        private String name;
        @JsonIgnore
        private int age;
    }
    ```
