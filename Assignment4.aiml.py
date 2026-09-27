import mysql.connector
class Employee
    {
        private String name;
        private int age;
        private double basicSalary;
        public static void main(String args[])throws IOException
        public Employee(String name, int age, double basicSalary) 
        {
            this.name = name;
            this.age = age;
            this.basicSalary = basicSalary;
        }
        public String getName() 
        {
            return name; 
        }
        public void setName(String name)
        {
            this.name = name;
        }
        public int getAge() 
        {
        return age;
        }
        public void setAge(int age) 
        {
            this.age = age;
        }
        public double getBasicSalary() 
        {
            return basicSalary;
        }
        public void setBasicSalary(double basicSalary) 
        {
            this.basicSalary = basicSalary;
        }
        public void displayDetails() 
        {
            System.out.println("Name: " + name);
            System.out.println("Age: " + age);
            System.out.println("Basic Salary: " +basicSalary);
        }
}
public class Main 
{
    public static void main(String[] args)
    {
        Employee emp1 = new
        Employee("Nupur", 28, 35000);
        emp1.displayDetails();
        emp1.setAge(29);
        emp1.setBasicSalary(40000);
        System.out.println("\nAfter updating details:");
        System.out.println("\nAfter deleting age details:");
        emp1.displayDetails();
        public static void main(String[] args) throws Exception 
        {
            int choice;
            System.out.println("1. Insert");
            System.out.println("2. Display");
            System.out.println("3. Update");
            System.out.println("4. Delete");
            System.out.println("5. Exit");
        }
    }