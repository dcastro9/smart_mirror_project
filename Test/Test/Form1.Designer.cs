namespace Test
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.datelabel = new System.Windows.Forms.Label();
            this.timelabel = new System.Windows.Forms.Label();
            this.templabel = new System.Windows.Forms.Label();
            this.conditionlabel = new System.Windows.Forms.Label();
            this.locationlabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // datelabel
            // 
            this.datelabel.AutoSize = true;
            this.datelabel.Font = new System.Drawing.Font("Georgia", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.datelabel.Location = new System.Drawing.Point(12, 9);
            this.datelabel.Name = "datelabel";
            this.datelabel.Size = new System.Drawing.Size(32, 14);
            this.datelabel.TabIndex = 1;
            this.datelabel.Text = "date";
            // 
            // timelabel
            // 
            this.timelabel.AutoSize = true;
            this.timelabel.Font = new System.Drawing.Font("Georgia", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.timelabel.Location = new System.Drawing.Point(12, 23);
            this.timelabel.Name = "timelabel";
            this.timelabel.Size = new System.Drawing.Size(40, 18);
            this.timelabel.TabIndex = 3;
            this.timelabel.Text = "time";
            // 
            // templabel
            // 
            this.templabel.AutoSize = true;
            this.templabel.Font = new System.Drawing.Font("Georgia", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.templabel.Location = new System.Drawing.Point(19, 69);
            this.templabel.Name = "templabel";
            this.templabel.Size = new System.Drawing.Size(45, 18);
            this.templabel.TabIndex = 4;
            this.templabel.Text = "temp";
            // 
            // conditionlabel
            // 
            this.conditionlabel.AutoSize = true;
            this.conditionlabel.Font = new System.Drawing.Font("Georgia", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.conditionlabel.Location = new System.Drawing.Point(12, 87);
            this.conditionlabel.Name = "conditionlabel";
            this.conditionlabel.Size = new System.Drawing.Size(61, 14);
            this.conditionlabel.TabIndex = 5;
            this.conditionlabel.Text = "condition";
            // 
            // locationlabel
            // 
            this.locationlabel.AutoSize = true;
            this.locationlabel.Font = new System.Drawing.Font("Georgia", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.locationlabel.Location = new System.Drawing.Point(12, 58);
            this.locationlabel.Name = "locationlabel";
            this.locationlabel.Size = new System.Drawing.Size(53, 14);
            this.locationlabel.TabIndex = 6;
            this.locationlabel.Text = "location";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(436, 160);
            this.Controls.Add(this.locationlabel);
            this.Controls.Add(this.conditionlabel);
            this.Controls.Add(this.templabel);
            this.Controls.Add(this.timelabel);
            this.Controls.Add(this.datelabel);
            this.Name = "Form1";
            this.Text = "Mirror Interface";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label datelabel;
        private System.Windows.Forms.Label timelabel;
        private System.Windows.Forms.Label templabel;
        private System.Windows.Forms.Label conditionlabel;
        private System.Windows.Forms.Label locationlabel;






    }
}

