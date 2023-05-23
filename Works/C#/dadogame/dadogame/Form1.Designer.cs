namespace dadogame

{

    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            button1 = new Button();
            label4 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.BackColor = Color.Transparent;
            label1.Location = new Point(118, 9);
            label1.Name = "label1";
            label1.Size = new Size(95, 19);
            label1.TabIndex = 0;
            label1.Text = "Jogo do Dado";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.BackColor = Color.Transparent;
            label2.Location = new Point(118, 106);
            label2.Name = "label2";
            label2.Size = new Size(89, 19);
            label2.TabIndex = 1;
            label2.Text = "Jogador 1:  0";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.BackColor = Color.Transparent;
            label3.Location = new Point(118, 150);
            label3.Name = "label3";
            label3.Size = new Size(89, 19);
            label3.TabIndex = 2;
            label3.Text = "Jogador 2:  0";
            // 
            // button1
            // 
            button1.Location = new Point(127, 201);
            button1.Name = "button1";
            button1.Size = new Size(80, 26);
            button1.TabIndex = 5;
            button1.Text = "Sortear";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.BackColor = Color.Transparent;
            label4.Font = new Font("Segoe UI", 10F, FontStyle.Regular, GraphicsUnit.Point);
            label4.Location = new Point(118, 55);
            label4.Name = "label4";
            label4.Size = new Size(95, 19);
            label4.TabIndex = 6;
            label4.Text = "Sem vencedor";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = Properties.Resources._8887766_dados_de_fundo_amarelo_vetor;
            ClientSize = new Size(347, 301);
            Controls.Add(label4);
            Controls.Add(button1);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Font = new Font("Segoe UI", 10F, FontStyle.Regular, GraphicsUnit.Point);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Button button1;
        private Label label4;
    }
}