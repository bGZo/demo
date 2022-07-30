package cc.bgzo.cms.utils;

/* File Name: DictUtils
 * Author: bGZo
 * Created Time: 7/24/2022 21:19
 * License: MIT
 * Description: 字典值工具类
 */

import cc.bgzo.cms.back.entity.SysDict;
import cc.bgzo.cms.back.service.ISysDictService;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

/**
 * 在工具类中调用 service(in spring)，查询表中记录
 * NOTE: 少了一个 @Component 无法找到方法
 */
@Component
public class DictUtils {
    @Autowired
    private ISysDictService service;
    private static ISysDictService sysDictService;
    /**
     * 完成对service的注入
     */
    @PostConstruct
    public void init() {
        sysDictService = service;
    }

    /**
     * 根据type和value获取对应的中文label
     * @param type
     * @param value
     * @return
     */
    public String getDictLabel(String type, Integer value) {
        QueryWrapper<SysDict> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("type_code",type);
        queryWrapper.eq("value",value);
        SysDict sysDict = sysDictService.getOne(queryWrapper);
        return sysDict.getLabel();
    }
}

