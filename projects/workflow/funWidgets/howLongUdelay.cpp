//author:bGZo
//update:200111
#include<iostream>
#include <windows.h>
using namespace std;
int main() {
    int p[13] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };
    int y, m, d, yy, mm, dd, day = 0;
    SYSTEMTIME st;
    GetLocalTime(&st);
    yy = st.wYear;
    mm = st.wMonth;
    dd = st.wDay;
    char w;
    cout << "输入你的拖延开始的时间(yyyy.mm.dd或yyyy/mm/dd)：\n";
    cin >> y >> w >> m >> w >> d;
    cout << "你是一直拖延到现在吗？（y/n)\n";
    cin.get();
    char pu=cin.get();
    if (pu == 'y') {
        //首先是今年距离年末多少天，然后太能往下算！！！
        if (y % 400 == 0 || (y % 100 && y % 4 == 0))p[2] = 29;
        else p[2] = 28;
        day += p[m] - d;
        for (int i = m + 1; i < 13; i++)day += p[i];
        //我枯了，尼玛
        for (int i = y + 1; i < yy; i++) {
            if (i % 400 == 0 || (i % 100 && i % 4 == 0))day += 366;
            else day += 365;
        }
        if (yy % 400 == 0 || (yy % 100 && yy % 4 == 0))p[2] = 29;
        else p[2] = 28;
        for (int i = 1; i < mm; i++) day += p[i];
        day += dd;
        cout << "经过我一天一天数数计算，你竟然拖延了" << day << "天?!\n"
            "但是我一直相信，如果你将这些时间好好的利用起来，你会和现在大不一样，至少你不会用我，对吗？";
    }
    else {
        cout <<"请你再次输入你的时间（NOW）（形式如上）：" ;
        cin >> yy >> w >> mm >> w >> dd;
        if (y % 400 == 0 || (y % 100 && y % 4 == 0))p[2] = 29;
        else p[2] = 28;
        day += p[m] - d;
        for (int i = m + 1; i < 13; i++)day += p[i];
        //我枯了，尼玛
        for (int i = y + 1; i < yy; i++) {
            if (i % 400 == 0 || (i % 100 && i % 4 == 0))day += 366;
            else day += 365;
        }
        if (yy % 400 == 0 || (yy % 100 && yy % 4 == 0))p[2] = 29;
        else p[2] = 28;
        for (int i = 1; i < mm; i++) day += p[i];
        day += dd;
        cout << "经过我一天一天数数计算，你竟然拖延了" << day << "天?!\n"
            "但是我一直相信，如果你将这些时间好好的利用起来，你会和现在大不一样，至少你不会用我，对吗？";
    }
}

/*
1. 在确定读取y/n后，我居然把如此简单的程序写错了······我已经不想和自己说些什么了，我TM的。<font size=4 color="red">值得注意的是，如果是连续的东西（特别是时间直接的连贯的事物），首先一点确定一个好计算的短点，将之前的先计算完，再整理好计算的部分，所谓掐头去尾就是这个道理</font>

2. 之前还犯过一个错误就是获取不到输入的是y还是n（这里模拟Linux）具体的问题就是永远获取的是空格,写法如下：

   ```c++
   int main() {
       char w;
       cin >> w;
       cout << p << endl;
       if (p == 'y')cout << "1";
       else cout << "0";
   }
   ```

   原因是因为：

   所以应该改为：

   ```c++
   int main() {
       char p=cin.get();
       cout << p << endl;
       if (p == 'y')cout << "1";
       else cout << "0";
   }
   ```

   但是应用于上面的程序的时候不知道为什么读取的时候不会停留，而是直接跳过，我猜测是直接读取的上面的一个换行符所导致的结果，所以中间加了两个`cin.get()；`

3. 第三点，我查阅了一下获取系统时间的方法（应该是调用window的API接口实现的）

   ```c++
   #include<iostream>
   #include<cstdio>
   #include <windows.h>
   using namespace std;
   int main()
   {
       SYSTEMTIME st;
       GetLocalTime(&st);
       printf("%d-%02d-%02d %02d:%02d:%02d", st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond);
       printf("\nAnd it's the %d day of a week.", st.wDayOfWeek);
       system("pause");
       return 0;
   }
   ```

*/