package cc.bgzo.cms.config;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/* File Name: MybatisPlusConfig
 * Author: bGZo
 * Created Time: 7/23/2022 17:01
 * License: MIT
 * Description:
 */
@Configuration
@MapperScan(basePackages = {"cc.bgzo.cms.back.mapper"})
public class MybatisPlusConfig {
    /*
     * 分页插件，自动识别数据库类型
     * 多租户，请参考官网【插件扩展】
     */
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
}
