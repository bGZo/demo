package JdkDynamicProxy;

import java.lang.reflect.Proxy;
import java.util.HashMap;
import java.util.Map;

/* File Name: DynamicProxyTest
 * Author: bGZo
 * Created Time: 10/26/2022 11:00
 * License: MIT
 * Description:
 */
public class DynamicProxyTest {
    public static void main(String[] args) {
        Map mapProxyInstance = (Map) Proxy.newProxyInstance(
                DynamicProxyTest.class.getClassLoader(),
                new Class[] { Map.class },
                new TimingDynamicInvocationHandler(new HashMap<>()));

        mapProxyInstance.put("hello", "world");
        mapProxyInstance.get("hello");
    }
//        proxyInstance.put("hello", "world");
////        System.out.println( proxyInstance.get("hello") );
}
