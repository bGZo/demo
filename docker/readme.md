本项目完全参考教程 [A Docker Tutorial for Beginners](https://docker-curriculum.com/#introduction). 首先是陆内基本操作, 先来一套镜像替换组合拳. 如下<sup>[1](#j1)</sup>:

```shell
$ sudo apt-get remove docker docker-engine 
$ docker-ce docker.io #卸载旧版本docker
$ sudo apt-get remove --auto-remove docker #清空旧版docker占用的内存
$ sudo apt-get update  

$ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common #安装环境
$ curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add - #阿里云的docker GPG密钥
$ sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" #阿里镜像源
$ sudo apt-get update
$ apt-cache madison docker-ce #查看多版本

$ sudo apt-get install -y docker-ce #安装最新版
$ sudo apt-get install -y docker-ce=5:19.03.6~3-0~ubuntu-bionic #安装5:19.03.6~3-0~ubuntu-bionic版

$ sudo service docker restart
$ sudo systemctl restart docker #重启Docker

$ sudo docker version # Docker 版本
```

登录阿里云, 在 `控制台->容器镜像服务->镜像加速器` [里面](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)找到对应的加速器地址.

```shell
$ cd /etc/docker | sudo mkdir -p /etc/docker
$ sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://xxxxxxxx.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
# more details see: https://docs.docker.com/engine/install
```
替换成功后, 运行`sudo docker run hello-world`, 检验是否成功.


![](https://z3.ax1x.com/2021/06/28/RNt0kn.png)

<div id="j1">[1]. https://www.cnblogs.com/chengmf/p/13122013.html</div>
<div id="j2">[2]. https://github.com/prakhar1989/docker-curriculum</div>
