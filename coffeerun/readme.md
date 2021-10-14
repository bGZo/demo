# Coffee Run

This is the demo of the book named <<Front-End Web Development: The Big Nerd Ranch Guide>>(I read its zh-cn translational version), it matters me a lot, even though I've learned the Web Development.

```shell
# get the listener
browser-sync start --server -- file "stylesheets/*.css, scripts/*.js, *.html" 

# Some function(part)
App.DataStore();
window.App.DataStore();
var dsOne = new App.DataStore();
var dsTwo = new App.DataStore();
dsOne.data['email']='james@bond.com';
dsOne.data['order']='black coffee';
dsTwo.data['email']='money@bond.com';
dsTwo.data['order']='chai tea';
dsOne.data
{email: "james@bond.com", order: "black coffee"}
dsTwo.data
{email: "money@bond.com", order: "chai tea"}
var myTruck=new App.Truck('007',new App.DataStore());
myTruck.createOrder({emailAddress: 'dr@no.com', coffee: 'decaf'});
myTruck.db
myTruck.printOrders();
```
<!-- 
数据交互 -> 原型函数(属性)

分层处理模块, 每一个模块都是基于上一个模块搭建的 -->
