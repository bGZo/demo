package cc.bgzo.server;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

/* File Name: mythread
 * Author: bGZo
 * Created Time: 8/17/2022 21:37
 * License: MIT
 * Description:
 */


public class Solution extends Thread {


}


//public class Solution extends Thread{
////    public static void main(String[] args) {
////        String a = "hello ";
////        System.out.println(a.concat("world"));
////    }
//
//    private static final char[] numbers = "零壹贰叁肆伍陆柒捌玖".toCharArray();
//    private static final char[] units = "仟佰拾".toCharArray();
//    private static final char[] groups = "圆万亿".toCharArray();
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        double db = sc.nextDouble();
//        System.out.println(Solution.moneyToChinese(new BigDecimal(db)));
//    }
//
//    public static String moneyToChinese(BigDecimal money) {
//        if(money.equals(BigDecimal.ZERO)){
//            return "零圆整";
//        }
//
//        Double max = 1000000000000D;
//        Double min = 0.01D;
//
//        if (money.doubleValue() >= max  || money.doubleValue() < min) {
//            return "大于1万亿或小于1分了";
//        }
//        money = money.setScale(2, RoundingMode.HALF_UP);
//        String numStr = money.toString();
//        int pointPos = numStr.indexOf('.');             // 整数
//        String nInt = null;                             // 小数
//        String nPoint = null;
//        if (pointPos >= 0) {
//            nInt = numStr.substring(0, pointPos);
//            nPoint = numStr.substring(pointPos + 1);
//        } else {
//            nInt = numStr;
//        }
//        StringBuilder sb = new StringBuilder();
//        if(!"0".equals(nInt)){
//            int groupCount = (int) Math.ceil(nInt.length() / 4.0);
//            for (int group = 0; group < groupCount; group++) {
//                boolean zeroFlag = true;
//                boolean noZeroFlag = false;
//                int start = (nInt.length() % 4 == 0 ? 0 : (nInt.length() % 4 - 4)) + 4 * group;
//                for (int i = 0; i < 4; i++) {
//                    if (i + start >= 0) {
//                        int value = nInt.charAt(i + start) - '0';
//                        if (value > 0) {
//                            sb.append(numbers[value]);
//                            if (i < 3) {
//                                sb.append(units[i]);
//                            }
//                            zeroFlag = true;
//                            noZeroFlag = true;
//                        } else if (zeroFlag) {
//                            sb.append('零');
//                            zeroFlag = false;
//                        }
//                    }
//                }
//                if(sb.charAt(sb.length() - 1) == '零'){
//                    sb.deleteCharAt(sb.length() - 1);
//                }
//                if(noZeroFlag || groupCount - group == 1){
//                    sb.append(groups[groupCount - group - 1]);
//                }
//            }
//        }
//        if (nPoint == null || "00".equals(nPoint)) {
//            sb.append('整');
//        }else{
//            int j = nPoint.charAt(0) - '0';
//            int f = nPoint.charAt(1) - '0';
//            if(j > 0){
//                sb.append(numbers[j]).append('角');
//                if(f != 0){
//                    sb.append(numbers[f]).append('分');
//                }
//            }else if("0".equals(nInt)){
//                sb.append(numbers[f]).append('分');
//            }else {
//                sb.append('零').append(numbers[f]).append('分');
//            }
//        }
//        return sb.toString();
//    }
//
//}



//class Solution{
//    private static final char[] data = new char[]{
//            '零', '壹', '贰', '叁', '肆',
//            '伍', '陆', '柒', '捌', '玖'
//    };
//    private static final char[] units = new char[]{
//            '元', '拾', '佰', '仟', '万',
//            '拾', '佰', '仟', '亿'
//    };
//    public static String convert(int money){
//        StringBuffer sbf = new StringBuffer();
//        int unit = 0;
//        while(money != 0){
//            sbf.insert(0, units[unit++]);
//            int numbers = money % 10;
//            sbf.insert(0, data[numbers]);
//            money /= 10;
//        }
//        return sbf.toString();
//    }
//
//
//    public static void main(String []args){
//
//    }
//}