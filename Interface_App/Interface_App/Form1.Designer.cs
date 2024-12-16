namespace Interface_App
{
    partial class frmPrincipal
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnOpcion1 = new System.Windows.Forms.Button();
            this.lblTitulo = new System.Windows.Forms.Label();
            this.Salir = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.Cyan;
            this.panel1.Controls.Add(this.button1);
            this.panel1.Controls.Add(this.Salir);
            this.panel1.Controls.Add(this.btnOpcion1);
            this.panel1.Controls.Add(this.lblTitulo);
            this.panel1.Location = new System.Drawing.Point(1, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(921, 535);
            this.panel1.TabIndex = 0;
            // 
            // btnOpcion1
            // 
            this.btnOpcion1.BackColor = System.Drawing.Color.Silver;
            this.btnOpcion1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnOpcion1.Font = new System.Drawing.Font("Cooper Black", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnOpcion1.Location = new System.Drawing.Point(71, 420);
            this.btnOpcion1.Name = "btnOpcion1";
            this.btnOpcion1.Size = new System.Drawing.Size(168, 46);
            this.btnOpcion1.TabIndex = 1;
            this.btnOpcion1.Text = "Camara Señas";
            this.btnOpcion1.UseVisualStyleBackColor = false;
            this.btnOpcion1.Click += new System.EventHandler(this.button1_Click);
            // 
            // lblTitulo
            // 
            this.lblTitulo.AutoSize = true;
            this.lblTitulo.Font = new System.Drawing.Font("Mistral", 28.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTitulo.Location = new System.Drawing.Point(225, 36);
            this.lblTitulo.Name = "lblTitulo";
            this.lblTitulo.Size = new System.Drawing.Size(495, 56);
            this.lblTitulo.TabIndex = 0;
            this.lblTitulo.Text = "Lenguaje de Señas en Python ";
            this.lblTitulo.Click += new System.EventHandler(this.label1_Click);
            // 
            // Salir
            // 
            this.Salir.BackColor = System.Drawing.Color.Silver;
            this.Salir.Cursor = System.Windows.Forms.Cursors.Hand;
            this.Salir.Font = new System.Drawing.Font("Cooper Black", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Salir.Location = new System.Drawing.Point(690, 420);
            this.Salir.Name = "Salir";
            this.Salir.Size = new System.Drawing.Size(180, 46);
            this.Salir.TabIndex = 2;
            this.Salir.Text = "Aprender Señas";
            this.Salir.UseVisualStyleBackColor = false;
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.Silver;
            this.button1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.button1.Font = new System.Drawing.Font("Cooper Black", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(378, 420);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(180, 46);
            this.button1.TabIndex = 3;
            this.button1.Text = "Recomendaciones";
            this.button1.UseVisualStyleBackColor = false;
            // 
            // frmPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(918, 531);
            this.Controls.Add(this.panel1);
            this.Name = "frmPrincipal";
            this.Text = "Frame Principal";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label lblTitulo;
        private System.Windows.Forms.Button btnOpcion1;
        private System.Windows.Forms.Button Salir;
        private System.Windows.Forms.Button button1;
    }
}

