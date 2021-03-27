namespace WindowsFormRealEstate
{
    partial class Form_RealEstate
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
            this.components = new System.ComponentModel.Container();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.blockDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.sellingDateDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.adresssDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.cityDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.typeestateDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.roomsDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.floornumDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.surfaceDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.sellingpriceDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.pricechangeDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.purchaseBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.realEstateDataSet = new WindowsFormRealEstate.RealEstateDataSet();
            this.fillByToolStrip = new System.Windows.Forms.ToolStrip();
            this.fillByToolStripButton = new System.Windows.Forms.ToolStripButton();
            this.purchaseTableAdapter = new WindowsFormRealEstate.RealEstateDataSetTableAdapters.purchaseTableAdapter();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.label_city = new System.Windows.Forms.Label();
            this.label_Street = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.purchaseBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.realEstateDataSet)).BeginInit();
            this.fillByToolStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToOrderColumns = true;
            this.dataGridView1.AutoGenerateColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.blockDataGridViewTextBoxColumn,
            this.sellingDateDataGridViewTextBoxColumn,
            this.adresssDataGridViewTextBoxColumn,
            this.cityDataGridViewTextBoxColumn,
            this.typeestateDataGridViewTextBoxColumn,
            this.roomsDataGridViewTextBoxColumn,
            this.floornumDataGridViewTextBoxColumn,
            this.surfaceDataGridViewTextBoxColumn,
            this.sellingpriceDataGridViewTextBoxColumn,
            this.pricechangeDataGridViewTextBoxColumn});
            this.dataGridView1.DataSource = this.purchaseBindingSource;
            this.dataGridView1.Location = new System.Drawing.Point(29, 79);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(1046, 472);
            this.dataGridView1.TabIndex = 0;
            // 
            // blockDataGridViewTextBoxColumn
            // 
            this.blockDataGridViewTextBoxColumn.DataPropertyName = "block";
            this.blockDataGridViewTextBoxColumn.HeaderText = "block";
            this.blockDataGridViewTextBoxColumn.Name = "blockDataGridViewTextBoxColumn";
            // 
            // sellingDateDataGridViewTextBoxColumn
            // 
            this.sellingDateDataGridViewTextBoxColumn.DataPropertyName = "selling_Date";
            this.sellingDateDataGridViewTextBoxColumn.HeaderText = "selling_Date";
            this.sellingDateDataGridViewTextBoxColumn.Name = "sellingDateDataGridViewTextBoxColumn";
            // 
            // adresssDataGridViewTextBoxColumn
            // 
            this.adresssDataGridViewTextBoxColumn.DataPropertyName = "adresss";
            this.adresssDataGridViewTextBoxColumn.HeaderText = "adresss";
            this.adresssDataGridViewTextBoxColumn.Name = "adresssDataGridViewTextBoxColumn";
            // 
            // cityDataGridViewTextBoxColumn
            // 
            this.cityDataGridViewTextBoxColumn.DataPropertyName = "city";
            this.cityDataGridViewTextBoxColumn.HeaderText = "city";
            this.cityDataGridViewTextBoxColumn.Name = "cityDataGridViewTextBoxColumn";
            // 
            // typeestateDataGridViewTextBoxColumn
            // 
            this.typeestateDataGridViewTextBoxColumn.DataPropertyName = "type_estate";
            this.typeestateDataGridViewTextBoxColumn.HeaderText = "type_estate";
            this.typeestateDataGridViewTextBoxColumn.Name = "typeestateDataGridViewTextBoxColumn";
            // 
            // roomsDataGridViewTextBoxColumn
            // 
            this.roomsDataGridViewTextBoxColumn.DataPropertyName = "rooms";
            this.roomsDataGridViewTextBoxColumn.HeaderText = "rooms";
            this.roomsDataGridViewTextBoxColumn.Name = "roomsDataGridViewTextBoxColumn";
            // 
            // floornumDataGridViewTextBoxColumn
            // 
            this.floornumDataGridViewTextBoxColumn.DataPropertyName = "floor_num";
            this.floornumDataGridViewTextBoxColumn.HeaderText = "floor_num";
            this.floornumDataGridViewTextBoxColumn.Name = "floornumDataGridViewTextBoxColumn";
            // 
            // surfaceDataGridViewTextBoxColumn
            // 
            this.surfaceDataGridViewTextBoxColumn.DataPropertyName = "surface";
            this.surfaceDataGridViewTextBoxColumn.HeaderText = "surface";
            this.surfaceDataGridViewTextBoxColumn.Name = "surfaceDataGridViewTextBoxColumn";
            // 
            // sellingpriceDataGridViewTextBoxColumn
            // 
            this.sellingpriceDataGridViewTextBoxColumn.DataPropertyName = "selling_price";
            this.sellingpriceDataGridViewTextBoxColumn.HeaderText = "selling_price";
            this.sellingpriceDataGridViewTextBoxColumn.Name = "sellingpriceDataGridViewTextBoxColumn";
            // 
            // pricechangeDataGridViewTextBoxColumn
            // 
            this.pricechangeDataGridViewTextBoxColumn.DataPropertyName = "price_change";
            this.pricechangeDataGridViewTextBoxColumn.HeaderText = "price_change";
            this.pricechangeDataGridViewTextBoxColumn.Name = "pricechangeDataGridViewTextBoxColumn";
            // 
            // purchaseBindingSource
            // 
            this.purchaseBindingSource.DataMember = "purchase";
            this.purchaseBindingSource.DataSource = this.realEstateDataSet;
            // 
            // realEstateDataSet
            // 
            this.realEstateDataSet.DataSetName = "RealEstateDataSet";
            this.realEstateDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // fillByToolStrip
            // 
            this.fillByToolStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fillByToolStripButton});
            this.fillByToolStrip.Location = new System.Drawing.Point(0, 0);
            this.fillByToolStrip.Name = "fillByToolStrip";
            this.fillByToolStrip.Size = new System.Drawing.Size(1104, 25);
            this.fillByToolStrip.TabIndex = 1;
            this.fillByToolStrip.Text = "fillByToolStrip";
            // 
            // fillByToolStripButton
            // 
            this.fillByToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.fillByToolStripButton.Name = "fillByToolStripButton";
            this.fillByToolStripButton.Size = new System.Drawing.Size(39, 22);
            this.fillByToolStripButton.Text = "FillBy";
            this.fillByToolStripButton.Click += new System.EventHandler(this.fillByToolStripButton_Click);
            // 
            // purchaseTableAdapter
            // 
            this.purchaseTableAdapter.ClearBeforeFill = true;
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(72, 28);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(134, 21);
            this.comboBox1.TabIndex = 2;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Location = new System.Drawing.Point(293, 28);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(134, 21);
            this.comboBox2.TabIndex = 3;
            // 
            // label_city
            // 
            this.label_city.AutoSize = true;
            this.label_city.Location = new System.Drawing.Point(42, 36);
            this.label_city.Name = "label_city";
            this.label_city.Size = new System.Drawing.Size(24, 13);
            this.label_city.TabIndex = 4;
            this.label_city.Text = "City";
            // 
            // label_Street
            // 
            this.label_Street.AutoSize = true;
            this.label_Street.Location = new System.Drawing.Point(243, 36);
            this.label_Street.Name = "label_Street";
            this.label_Street.Size = new System.Drawing.Size(35, 13);
            this.label_Street.TabIndex = 5;
            this.label_Street.Text = "Street";
            // 
            // Form_RealEstate
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1104, 563);
            this.Controls.Add(this.label_Street);
            this.Controls.Add(this.label_city);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.fillByToolStrip);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form_RealEstate";
            this.Text = "RealEstate";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.purchaseBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.realEstateDataSet)).EndInit();
            this.fillByToolStrip.ResumeLayout(false);
            this.fillByToolStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private RealEstateDataSet realEstateDataSet;
        private System.Windows.Forms.BindingSource purchaseBindingSource;
        private RealEstateDataSetTableAdapters.purchaseTableAdapter purchaseTableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn blockDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn sellingDateDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn adresssDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn cityDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn typeestateDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn roomsDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn floornumDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn surfaceDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn sellingpriceDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn pricechangeDataGridViewTextBoxColumn;
        private System.Windows.Forms.ToolStrip fillByToolStrip;
        private System.Windows.Forms.ToolStripButton fillByToolStripButton;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.Label label_city;
        private System.Windows.Forms.Label label_Street;
    }
}

