using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    internal class PencilCase
    {
        private Pencil[] pcase;
        private int maxPencil;
        private int numOfPencils;
        private string color;

        public PencilCase(int maxPencil, string color)
        {

            this.maxPencil = maxPencil;
            this.numOfPencils = 0;
            this.color = color;
            this.pcase = new Pencil[maxPencil];
            for (int i = 0; i < maxPencil; i++)
            {
                this.pcase[i] = null;
            }
        }

        public void setmaxPencil(int maxPencil)
        {
            this.maxPencil = maxPencil;
        }

        public void setnumOfPencils(int numOfPencils)
        {
            this.numOfPencils = numOfPencils;
        }

        public void setcolor(string color)
        {
            this.color = color;
        }

        public int GetmaxPencil()
        {
            return this.maxPencil;
        }

        public int GetnumOfPencils()
        {
            return this.numOfPencils;
        }

        public string Getcolor()
        {
            return this.color;
        }
        public void SetPencilCase(Pencil[] a)
        {
            for (int i = 0; i < a.Length; i++)
            {
                this.pcase[i] = a[i];
                this.numOfPencils++;
            }
        }
        public Pencil[] GetPcase()
        {
            Pencil[] copy = new Pencil[this.pcase.Length];
            for (int i = 0; i < numOfPencils; i++)
            {
                copy[i] = this.pcase[i];
            }
            return copy;
        }
        private int Shortest()
        {
            int smallest = this.pcase[0].Getlength();
            for (int i =1; i < this.numOfPencils; i++)
            {

                if (this.pcase[i].Getlength() < smallest)
                {
                    smallest = this.pcase[i].Getlength();
                }
            }
            return smallest;


        }
        public void Sharpen()
        {
            int shortest_pencil = Shortest();
            for (int i = 0; i < this.numOfPencils; i++)
            {
                if (this.pcase[i].Getcolor() == this.Getcolor() && this.pcase[i].Getsharpened() == false)
                {
                    this.pcase[i].setlength(shortest_pencil);
                    this.pcase[i].setsharpened(true);
                }
            }


        }
    }
}
