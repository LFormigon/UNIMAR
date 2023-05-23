//Ex1
//TextReader reader = new StreamReader(@"C:\Users\Aula\Desktop\navarro\ex2\nomes_telefones.txt");

//String linha = reader.ReadLine();

//while (linha != null)
//{
//    if (linha != null)
//    {
//        int comecoNum = linha.IndexOf(")") + 2;
//        string num = linha.Substring(comecoNum);
//        string[] caractEspec = linha.Split('(', ')');
//        string valor = caractEspec[1].Trim();
//        Console.WriteLine("{0} {1}", valor, num);
//    }

//    linha = reader.ReadLine();
//}





//Ex2
//TextReader reader = new StreamReader(@"C:\Users\Aula\Desktop\navarro\ex2\nomes_telefones.txt");

//String linha = reader.ReadLine();

//while (linha != null)
//{

//    if (linha != null)
//    {
//        string nome = linha.Substring(0, linha.IndexOf("(")).Trim().ToUpper();

//        if (nome.Length > 12)
//        {
//            Console.WriteLine(nome);
//        }
//    }

//    linha = reader.ReadLine();


//}





//Ex3
//TextReader reader = new StreamReader(@"C:\Users\Aula\Desktop\navarro\ex2\datas.txt");

//String linha = reader.ReadLine();

//while (linha != null)
//{

//    if (linha != null)
//    {
//        string data = linha.Substring(6, 4);

//        Console.WriteLine(data);
//    }

//    linha = reader.ReadLine();
//}





//Ex4
//TextReader reader = new StreamReader(@"C:\Users\Aula\Desktop\navarro\ex2\marcas_carros.txt");

//String linha = reader.ReadLine();

//while (linha != null)
//{
//    if (linha != null)
//    {
//        string marca = linha.Substring(0, linha.IndexOf("@"));

//        Console.WriteLine(marca);
//    }

//    linha = reader.ReadLine();
//}





//Ex5
TextReader reader = new StreamReader(@"C:\Users\Aula\Desktop\navarro\ex2\produtos_estoque.txt");

String linha = reader.ReadLine();
int qtd = 0;
double valorTotal = 0.0;

while (linha != null)
{
    if (linha != null)
    {
        qtd += Convert.ToInt32(linha.Substring(linha.IndexOf('|') + 1));

        valorTotal += Convert.ToInt32(linha.Substring(linha.IndexOf('|') + 1)) * Convert.ToDouble(linha.Substring(linha.IndexOf('$') + 1, 5));
    }

    linha = reader.ReadLine();
}

Console.WriteLine("Quantidade Total: " + qtd + "\nPreço total: $" + string.Format("{0:#.00}", valorTotal / 100));
