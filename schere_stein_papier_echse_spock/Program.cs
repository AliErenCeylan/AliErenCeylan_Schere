using System;
using System.Diagnostics.Eventing.Reader;

internal class Program
{
    private static void Main()
    {
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("Benutzernamen Eingeben: ");
        string name = Console.ReadLine();
        Console.WriteLine("Spieler: " + name);
        Console.WriteLine("          ");
        Console.ResetColor();

        while (0 == 0)
        {

            Console.Write("Spielzug Eingeben: ");
            string Spieler = Console.ReadLine();
            Console.WriteLine(name + "'s Spielzug: " +Spieler);

            int[] Moves = new int[]
            {
            1,//Schere
            2,//Stein
            3,//Papier
            4,//Echse
            5,//Spock
            };


            if (Spieler != "Schere" && Spieler != "Stein" && Spieler != "Papier" && Spieler != "Echse" && Spieler != "Spock")
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Ungültige Eingabe");
                Console.ResetColor ();
            }
            else
            {
                Random random = new Random();
                int index = random.Next(Moves.Length);
                int Bot = Moves[index];

                if (Bot == 1)
                {
                    Console.WriteLine("Computer's Zug: Schere");
                }
                else if (Bot == 2)
                {
                    Console.WriteLine("Computer's Zug: Stein");
                }
                else if (Bot == 3)
                {
                    Console.WriteLine("Computer's Zug: Papier");
                }
                else if (Bot == 4)
                {
                    Console.WriteLine("Computer's Zug: Echse");
                }
                else if (Bot == 5)
                {
                    Console.WriteLine("Computer's Zug: Spock");
                }

                Console.ForegroundColor = ConsoleColor.Green;
                if (Spieler == "Schere" && Bot == 3)
                {
                    Console.WriteLine("Schere schneidet Papier. Du hast Gewonnen");
                }
                else if (Spieler == "Papier" && Bot == 2)
                {
                    Console.WriteLine("Papier bedeckt Stein. Du hast Gewonnen");
                }
                else if (Spieler == "Stein" && Bot == 4)
                {
                    Console.WriteLine("Stein zerquetscht Echse. Du hast Gewonnen");
                }
                else if (Spieler == "Echse" && Bot == 5)
                {
                    Console.WriteLine("Echse vergiftet Spock. Du hast Gewonnen");
                }
                else if (Spieler == "Spock" && Bot == 1)
                {
                    Console.WriteLine("Spock zertrümmert Schere. Du hast Gewonnen");
                }
                else if (Spieler == "Schere" && Bot == 4)
                {
                    Console.WriteLine("Schere köpft Echse. Du hast Gewonnen");
                }
                else if (Spieler == "Echse" && Bot == 3)
                {
                    Console.WriteLine("Echse frisst Papier. Du hast Gewonnen");
                }
                else if (Spieler == "Papier" && Bot == 5)
                {
                    Console.WriteLine("Papier widerlegt Spock. Du hast Gewonnen");
                }
                else if (Spieler == "Spock" && Bot == 2)
                {
                    Console.WriteLine("Spock verdampft Stein. Du hast Gewonnen");
                }
                else if (Spieler == "Stein" && Bot == 1)
                {
                    Console.WriteLine("Stein zertrümmert Schere. Du hast Gewonnen");
                }

                Console.ResetColor();
                Console.ForegroundColor = ConsoleColor.Red;

                if (Spieler == "Papier" && Bot == 1)
                {
                    Console.WriteLine("Schere schneidet Papier. Du hast Verloren");
                }
                else if (Spieler == "Stein" && Bot == 3)
                {
                    Console.WriteLine("Papier bedeckt Stein. Du hast Verloren");
                }
                else if (Spieler == "Echse" && Bot == 2)
                {
                    Console.WriteLine("Stein zerquetscht Echse. Du hast Verloren");
                }
                else if (Spieler == "Spock" && Bot == 4)
                {
                    Console.WriteLine("Echse vergiftet Spock. Du hast Verloren");
                }
                else if (Spieler == "Schere" && Bot == 5)
                {
                    Console.WriteLine("Spock zertrümmert Schere. Du hast Verloren");
                }
                else if (Spieler == "Echse" && Bot == 1)
                {
                    Console.WriteLine("Schere köpft Echse. Du hast Verloren");
                }
                else if (Spieler == "Papier" && Bot == 4)
                {
                    Console.WriteLine("Echse frisst Papier. Du hast Verloren");
                }
                else if (Spieler == "Spock" && Bot == 3)
                {
                    Console.WriteLine("Papier widerlegt Spock. Du hast Verloren");
                }
                else if (Spieler == "Stein" && Bot == 5)
                {
                    Console.WriteLine("Spock verdampft Stein. Du hast Verloren");
                }
                else if (Spieler == "Schere" && Bot == 2)
                {
                    Console.WriteLine("Stein zertrümmert Schere. Du hast Verloren");
                }

                Console.ResetColor();
                Console.ForegroundColor = ConsoleColor.Cyan;

                if (Spieler == "Schere" && Bot == 1 || Spieler == "Stein" && Bot == 2 || Spieler == "Papier" && Bot == 3 || Spieler == "Echse" && Bot == 4 || Spieler == "Spock" && Bot == 5)
                {
                    Console.WriteLine("Unentschieden");
                }

                Console.ResetColor();
            }
            Console.WriteLine("             ");
        }
        Console.ReadKey();
    }
}