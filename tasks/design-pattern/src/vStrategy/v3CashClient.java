package vStrategy;

public class v3CashClient {
    static double total = 0.0d;
    public static void main(String[] args){
//        v3CashSuper csuper = v3CashFactory.createCashAccept(cbxType.Selection.ToString()); //demo
        double totalPrice = 0d;
//        totalPrice = csuper.acceptCash(price *num); //demo
        total += totalPrice;
        System.out.println( totalPrice );
    }
}
