
import java.util.*;

class hello
{

public static void main(String args[])
{

System.out.println("Name=janak");
System.out.println("email=janak123@gmail.com");
System.out.println("mobile no=8160959262");

Scanner sc=new Scanner(System.in);
int a,b,c,d,e,t;
float avg;
System.out.println("\nenter the valu for a=");
a=sc.nextInt();
System.out.println("\nenter the valu for b=");
b=sc.nextInt();
System.out.println("\nenter the valu for c=");
c=sc.nextInt();
System.out.println("\nenter the valu for d=");
d=sc.nextInt();
System.out.println("\nenter the valu for e=");
e=sc.nextInt();



t=a+b+c+d+e;
System.out.println("Sum="+(t));

avg=t/5;
System.out.println("avg="+(avg));

if(avg>=70)
{
    System.out.println("Grade=A");
}
else if(avg>=50)
{
    System.out.println("Grade=b");
}
else if(avg>=40)
{
    System.out.println("Grade=c");
}
else if(avg>=39)
{
    System.out.println("Grade=d");
}
else if(avg<33)
{
    System.out.println("Grade=e");
    System.out.println("fail...");
}






}

}