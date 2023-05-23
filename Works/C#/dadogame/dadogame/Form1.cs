namespace dadogame
{
    public partial class Form1 : Form

    {
        public Form1()
        {
            InitializeComponent();
        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
        int point_jogador1 = 0;
        int point_jogador2 = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = "Jogador 1: " + 0;
            label3.Text = "Jogador 2: " + 0;
            label4.Text = "Sem Vencedor";
            for (int i = 0; i <= 2; i++)
            {
                Random randNum = new Random();

                int vezJog1 = randNum.Next(1, 7);
                int vezJog2 = randNum.Next(1, 7);

                if (vezJog1 > vezJog2)
                {
                    point_jogador1++;
                    label2.Text = "Jogador 1: " + point_jogador1;
                }
                else if (vezJog2 > vezJog1)
                {
                    point_jogador2++;
                    label3.Text = "Jogador 2: " + point_jogador2;
                }

                if (i == 2)
                {
                    if (point_jogador1 > point_jogador2)
                    {
                        label4.Text = "Jogador 1 venceu!!";

                        point_jogador1 = 0;
                        point_jogador2 = 0;
                        break;
                    }
                    else if (point_jogador2 > point_jogador1)
                    {
                        label4.Text = "Jogador 2 venceu!!";

                        point_jogador1 = 0;
                        point_jogador2 = 0;
                        break;
                    }
                    else if (i == 2)
                    {
                        label4.Text = "Empate!!";

                        point_jogador1 = 0;
                        point_jogador2 = 0;
                        break;

                    }
                }
            }
        }
    }
}