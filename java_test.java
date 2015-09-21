import java.util.ArrayList;

class java_test{

 public static void main(String[] args){

    ArrayList<String> a = new ArrayList<String>();
   
    a.add("Zero");
    a.add("First");

    for(int i=0;i<2;i++){
      a.add(" "+i);

     } 

   System.out.println("The total size of ArrayList is:"+a.size());
   
   for(int i=0;i<a.size();i++){
      System.out.println(i+":  "+a.get(i));
   }


}

}
