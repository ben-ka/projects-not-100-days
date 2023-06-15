using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    internal class Pencil
    {
        private string color;
        private int length;
        private bool sharpened;

        public Pencil(string color, int length, bool sharpened)
        {
            this.color = color;
            this.length = length;
            this.sharpened = sharpened;
        }

        public void setcolor(string color)
        {
            this.color = color;
        }

        public void setlength(int length)
        {
            this.length = length;
        }

        public void setsharpened(bool sharpened)
        {
            this.sharpened = sharpened;
        }

        public string Getcolor()
        {
            return this.color;
        }

        public int Getlength()
        {
            return this.length;
        }

        public bool Getsharpened()
        {
            return this.sharpened;
        }

        public int DoSharp(int x)
        {
            int less_cm = this.length - x;
            this.length -= less_cm;
            return less_cm;

        }

    }
}
