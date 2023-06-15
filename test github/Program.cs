namespace ConsoleApp4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Pencil p1 = new Pencil("red", 5, false);
            Pencil p2 = new Pencil("yellow", 7, false);
            Pencil p3 = new Pencil("red", 10, false);
            Pencil[] p = { p1, p2, p3 };

            PencilCase x1 = new PencilCase(30, "red");
            x1.SetPencilCase(p);
            x1.Sharpen();
            Console.WriteLine(p1.Getlength());




        }
    }
}