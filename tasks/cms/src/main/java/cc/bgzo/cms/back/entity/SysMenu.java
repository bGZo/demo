package cc.bgzo.cms.back.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableLogic;
import lombok.Data;

import java.util.Date;

/* File Name: SysMenu
 * Author: bGZo
 * Created Time: 7/23/2022 15:30
 * License: MIT
 * Description: 系统菜单
 */
@Data
public class SysMenu {
    @TableId(type = IdType.AUTO)
    private Integer id;
    private Integer pid;
    private String  name;
    private String  url;
    private String  perms;      // 角色
    private String  icon;

    private Integer createBy;
    private Date    createDate;
    private Integer updateBy;
    private Date    updateDate;

    @TableLogic
    private String  delFlag;
}
