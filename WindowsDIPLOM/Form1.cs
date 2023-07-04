using OfficeOpenXml;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using System.Data.OleDb;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using Microsoft.Office.Interop.Excel;
using System.IO;
using Spire.Xls;
using Workbook = Spire.Xls.Workbook;
using Worksheet = Spire.Xls.Worksheet;

namespace WindowsDIPLOM
{
    public partial class Form1 : Form
    {
        Double Kp; // Коэффициент резерва
        Double dc; // Средний фактический диаметр скважины
        Double dh; // наружный диаметр обсадной колонны
        Double lcp; // Длина интервала цементирования
        Double q; // расход цемента для приготовления 1м3 тампонажного раствора
        Double d; // внутренний диаметр колоны 
        Double lcs; // высота цементного стакана
        Double Ksj; // коэффициент сжимаемости продавчоной жидкости
        Double lb; // длина столба жидкости в кольцевом пространнстве 
        Double lc; // длина колонны 
        Double Kv; // коэффициент учитывающий потери жидкости
        Double kc; // коэффициент учитывающий потери цемента
        Double Vtp; // Необходимый объём тампонажного раствора
        Double Volume_fluid_dis; // объём продавочной жидкости 
        Double Volume_buffer; // Объём буферной жидкости
        Double pcp; // плотность цементного раствора 
        Double m;
        Double Gt; // Общая масса сухого тампонажного материала 
        Double Vv; // Объём воды необходимый для затворения тампонажного материала
        Double Gp; // Общий расход хичимеческого реагента для приготовления всего объёма тампонажного раствора
        Double n; // Доля химриагента в растворе 

        /// <summary>
        /// /Вторая вкладка
        /// </summary>
        Double pbj; //Плотность буферной жидкости
        Double ppp; // Плотность продавочной жидкости 
        Double hbj; // Высота столба буферной жидкости жидкости
        Double pp;  // плотность бурового раствора
        Double hd; // Глубина уровня цементного раствора за колонной 
        Double H; // глубина скважины по вертикали 
        Double Q; // сумарная производительность цементировочных агрегатов (считается в дальнейшем)
        Double to; // динамическое напряжение сдвига цементного раствора
        Double lkp; // коэффициент гидравлических сопротивлений в кольцевом пространсте 
        Double L; // длина ствола скважины, длина обсадной колонны
        Double ltp; // Коэффициент гидравлических сопротивлений в трубах
        Double DD; // Диаметр долота
        Double a; // коэффициент расширения ствола скважины
        Double Pob; //Величина потерь давления в обвязке устья скважины при цементировании
        /// <summary>
        /// /Вторая вкладка
        /// </summary>
        Double nca;
        Double qca;
        Double Vstop;
        Double qcamin;
        Double Fkp;
        Double Ftp;
        Double Pca_i;
        Double PDYN_i;
        Double TTNO;
        String Messin= "Некоректные данные при вводе, введите значение не используя  букв, при вводе нецелочисленных переменных используйте запятую, а не точку"; // вывод ошибки


        public Form1()
        {
            InitializeComponent();
        }

        string filePath = "путь_к_файлу.xlsx";







        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            //Kp = Convert.ToDouble(textBox1.Text);
            try
            {
                // Получение значения переменной из TextBox
                Kp = Double.Parse(textBox1.Text);
                textBox43.Text = null;
                // Дальнейшая обработка переменной

            }
            catch (FormatException)
            {
                // Обработка исключения при некорректном вводе
                if ((textBox43.Text != null) || (textBox43.Text == "Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
                // MessageBox.Show("Некорректный ввод переменной!");
                //textBox1.Text = null;
            }
            //catch (Exception ex)
            //{
            // Обработка других исключений
            // MessageBox.Show($"Ошибка: {ex.Message}");
            //textBox1.Text = null;
            //}
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            try
            {
                
                dc = Double.Parse(textBox2.Text);
                textBox43.Text = null;
                

            }
            catch (FormatException)
            {          if ((textBox43.Text !=null)||(textBox43.Text== "Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }                    
                                             
            }
            //dc = Convert.ToDouble(textBox2.Text);

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            try
            {
                
                dh = Double.Parse(textBox3.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            //dh = Convert.ToDouble(textBox3.Text);

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                lcp = Double.Parse(textBox4.Text);

                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // lcp = Convert.ToDouble(textBox4.Text);

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                d = Double.Parse(textBox5.Text);

                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // d = Convert.ToDouble(textBox5.Text);

        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                lcs = Double.Parse(textBox6.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // lcs = Convert.ToDouble(textBox6.Text);

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                Ksj = Double.Parse(textBox7.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // Ksj = Convert.ToDouble(textBox7.Text);

        }

        private void textBox8_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                lb = Double.Parse(textBox8.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // lb = Convert.ToDouble(textBox8.Text);

        }

        private void textBox9_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                lc = Double.Parse(textBox9.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            // lc = Convert.ToDouble(textBox9.Text);

        }

        private void textBox10_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Kv = Double.Parse(textBox10.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // Kv = Convert.ToDouble(textBox10.Text);

        }

        private void textBox11_TextChanged(object sender, EventArgs e)
        { }

        private void textBox12_TextChanged(object sender, EventArgs e)
        {
            try
            {
                kc = Double.Parse(textBox12.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }

            }
            //kc = Convert.ToDouble(textBox12.Text);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Vtp = 0.785 * (lcp * Kp * (Math.Pow(dc, 2) - Math.Pow(dh, 2)) + Math.Pow(d, 2) * lcs); // Объём тампонажного раствора
            textBox13.Text = Vtp.ToString();




            Volume_fluid_dis = 0.785 * Ksj * Math.Pow(d, 2) * (lc - lcs); // Объём продавочной жидкости
            textBox14.Text = Volume_fluid_dis.ToString();

            Volume_buffer = 0.785 * (dc - dh) * Kp * lb;// Объём буферной жидкости
            textBox15.Text = Volume_buffer.ToString();

            switch (comboBox1.Text)
            {
                

                case "Облегчённый тампонажный портландцемент для низких и нормальных температур":
                    pcp = 1400;
                    break;

                case "Облегчённый тампонажный портландцемент для нормальных температур и высоких":
                    pcp = 1500;
                    break;

                case "Облегчённый тампонажный цемент для горячих скважин":
                    pcp = 1650;
                    break;
            case "Облегчённый тампонажный цемент повышенной коррозийной стойкости типа ЦТОК":
                    pcp = 1350;
            break;
            case "Облегчённый тампонажный цемент типа ЦТО":
                    pcp = 1900;
            break;
            case "Облегчённый тампонажный цемент типа ЦТО-250":
                    pcp = 1540;
            break;
            case "Облегчённый тампонажный материал типа МТО":
                    pcp = 2200;
            break;
                       
            case "Тампонажный цемент для низкотемпературных скважин типа ЦТН":
                    pcp = 2400;
            break;
            case "Утяжелённый тампонажный цемент типа ШПЦС":
                    pcp = 3000;
            break;
            case "Утяжелённый тампонажный цемент типа УЦГ":
                    pcp = 3100;
            break;
            default:
                    try
                    {
                        pcp = Double.Parse(comboBox1.Text);
                        textBox43.Text = null;
                    }
                    catch (FormatException)
                    {
                        if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                        {
                            textBox43.Text = Messin;
                        }
                    }
                    //pcp = Convert.ToDouble(comboBox1.Text);
                    break;
            }

            q = pcp / (1 + m);
            textBox16.Text = q.ToString();

            Gt = kc * q * Vtp; // Общая масса сухого тампонажного материала 
            textBox18.Text = Gt.ToString();
            Vv = Kv * m * Gt;   // Объём воды для затворения цементного раствора
            textBox19.Text = Vv.ToString();
            Gp = n * Gt; // о
            textBox20.Text = Gp.ToString();
            textBox43.Text = textBox43.Text + "Расчёт параметров произведён";



        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox13_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox14_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox15_TextChanged(object sender, EventArgs e)
        {

        }

        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void textBox16_TextChanged(object sender, EventArgs e)
        {

        }

        private void label16_Click(object sender, EventArgs e)
        {

        }

        private void textBox17_TextChanged(object sender, EventArgs e)
        {
            try
            {
                m = Double.Parse(textBox17.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // m = Convert.ToDouble(textBox17.Text);
        }

        private void textBox20_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox21_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // Получение значения переменной из TextBox
                n = Double.Parse(textBox21.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //n = Convert.ToDouble(textBox21.Text);
        }

        private void label23_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Double PCT;
            PCT = 0.000001 * 9.806 * ((pbj - ppp) * lb + (pp - ppp) * (lcp - lb) + (pcp - ppp) * (H - lcp - lcs));
            // разница гидростатического давления в затрубном пространсте и в колонне обсадных труб при конечном положении уровня цементного
            // цементного раствора в затрубном пространстве 
            Double wkp;
            wkp = 25 * Math.Sqrt(to / pcp); // критическая скорость жидкости в кольцевом пространстве 
            Double Qsum;
            Qsum = 0.785 * (Math.Pow(DD, 2) * a - Math.Pow(dh,2)) * wkp;
            Double PKP;
            PKP = (0.826 * lkp * pcp * lc * Math.Pow(Qsum, 2) * Math.Pow(10, -6)) / (Math.Pow(dc - dh, 3) * Math.Pow(dc + dh, 2));
            Double PTP;
            PTP = 0.826 * ltp * ppp * lc * Math.Pow(Qsum, 2) * Math.Pow(10, -6) / Math.Pow(d, 5);
            // потери давления при турбулетнотом режиме течения жидкости
            Double PDYN;
            PDYN = PTP + PKP + Pob;
            // Суммарные гидравлические потери, возникающие в трубах и затрубном пространстве при закачке  
            // продавочной жидкости  в конце цементирования
            Double PMAX;
            PMAX = PDYN + PCT;//  Максимальное давление в устье скважины
            textBox32.Text = PCT.ToString();
            textBox33.Text = wkp.ToString();
            textBox34.Text = Qsum.ToString();
            textBox35.Text = PKP.ToString();
            textBox36.Text = PTP.ToString();
            textBox37.Text = PDYN.ToString();
            textBox38.Text = PMAX.ToString();



        }

        private void textBox22_TextChanged(object sender, EventArgs e)
        {
            try
            {
                pbj = Double.Parse(textBox22.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //pbj = Convert.ToDouble(textBox22.Text);
        }

        private void textBox23_TextChanged(object sender, EventArgs e)
        {
            try
            {
                ppp = Double.Parse(textBox23.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // ppp = Convert.ToDouble(textBox23.Text);
        }

        private void textBox24_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void textBox25_TextChanged(object sender, EventArgs e)
        {
            try
            {
                pp = Double.Parse(textBox25.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //pp = Convert.ToDouble(textBox25.Text);
        }

        private void textBox26_TextChanged(object sender, EventArgs e)
        {
            try
            {
                //  hd = Double.Parse(textBox26.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //hd = Convert.ToDouble(textBox26.Text);

        }

        private void textBox27_TextChanged(object sender, EventArgs e)
        {
            try
            {
                H = Double.Parse(textBox27.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // H = Convert.ToDouble(textBox27.Text);

        }

        private void textBox28_TextChanged(object sender, EventArgs e)
        {
            try
            {
                to = Double.Parse(textBox28.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //to = Convert.ToDouble(textBox28.Text);

        }

        private void textBox29_TextChanged(object sender, EventArgs e)
        {
            try
            {
                lkp = Double.Parse(textBox29.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // lkp = Convert.ToDouble(textBox29.Text);
        }

        private void textBox30_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // L = Double.Parse(textBox30.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //L = Convert.ToDouble(textBox30.Text);
        }

        private void textBox31_TextChanged(object sender, EventArgs e)
        {
            try
            {
                ltp = Double.Parse(textBox31.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //ltp = Convert.ToDouble(textBox31.Text);
        }

        private void textBox39_TextChanged(object sender, EventArgs e)
        {
            try
            {
                DD = Double.Parse(textBox39.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // DD = Convert.ToDouble(textBox39.Text);
        }

        private void textBox40_TextChanged(object sender, EventArgs e)
        {
            try
            {
                a = Double.Parse(textBox40.Text);
textBox43.Text = null;               
            }
            catch (FormatException)
            {          if ((textBox43.Text !=null)||(textBox43.Text== "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                } 
            }
            //a = Convert.ToDouble(textBox40.Text);
        }

        private void textBox41_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Pob = Double.Parse(textBox41.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //Pob = Convert.ToDouble(textBox41.Text);
        }

        private void textBox43_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox45_TextChanged(object sender, EventArgs e)
        {
            try
            {
                qca = Double.Parse(textBox45.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //qca = Convert.ToDouble(textBox45.Text);
        }
        /// <summary>
        /// 
        /// </summary>

        private void button3_Click(object sender, EventArgs e)
        {
            Double TZ;
            // if (checkBox1.Checked)
            //{ }

            TZ = 1000 * Vtp  / (nca * qca * 60); // Время приготовления и закачки цементного раствора

            Double Tstop;
            Tstop = Vstop * 1000  / (qcamin * 60); // время на посадку пробки
            Double hi_i;
            hi_i = (Fkp * L) / (Ftp + Fkp) + Math.Pow(10, 6) * Fkp * (Pca_i - PDYN_i) / (9.806 * (Ftp + Fkp) * (pcp - pp)) + (L * Ftp - Vtp) / (Ftp + Fkp);
            Double Vpr_i;
            Vpr_i = 0.785 * Math.Pow(d, 2) * hi_i; // Объём продавочной жидкости закаченной на i скорости
            Double tpr_i;
            tpr_i = Vpr_i * 1000 / (nca * qca * 60); // время работы ЦА на i  скорости при продавке цементного раствора
            Double Tpr;
            Tpr = tpr_i + Tstop;// Считается как сумма, общее время продавки цементного расвора в затрудное пространство
            Double TC;
            TC = TZ + Tpr + TTNO; //Общее время цементирования


            textBox53.Text = TZ.ToString();
            textBox54.Text = Tstop.ToString();
            textBox55.Text = hi_i.ToString();
            textBox56.Text = Vpr_i.ToString();
            textBox57.Text = tpr_i.ToString();
            textBox58.Text = Tpr.ToString();
            textBox59.Text = TC.ToString();


        }

        private void label40_Click(object sender, EventArgs e)
        {

        }

        private void textBox44_TextChanged(object sender, EventArgs e)
        {
            try
            {
                nca = Double.Parse(textBox44.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // nca = Convert.ToDouble(textBox44.Text);
        }

        private void textBox46_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Vstop = Double.Parse(textBox46.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // Vstop = Convert.ToDouble(textBox46.Text);
        }

        private void textBox47_TextChanged(object sender, EventArgs e)
        {
            try
            {
                qcamin = Double.Parse(textBox47.Text);
textBox43.Text = null;               
            }
            catch (FormatException)
            {          if ((textBox43.Text !=null)||(textBox43.Text== "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                } 
            }
            // qcamin = Convert.ToDouble(textBox47.Text);
        }

        private void textBox48_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Fkp = Double.Parse(textBox48.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //Fkp = Convert.ToDouble(textBox48.Text);
        }

        private void textBox49_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Ftp = Double.Parse(textBox49.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            // Ftp = Convert.ToDouble(textBox49.Text);
        }

        private void textBox50_TextChanged(object sender, EventArgs e)
        {
            try
            {
                Pca_i = Double.Parse(textBox50.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //Pca_i = Convert.ToDouble(textBox50.Text);
        }

        private void textBox51_TextChanged(object sender, EventArgs e)
        {
            try
            {
                PDYN_i = Double.Parse(textBox51.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //PDYN_i = Convert.ToDouble(textBox51.Text);
        }

        private void textBox52_TextChanged(object sender, EventArgs e)
        {
            try
            {
                TTNO = Double.Parse(textBox52.Text);
                textBox43.Text = null;
            }
            catch (FormatException)
            {
                if ((textBox43.Text != null) || (textBox43.Text == "   Расчёт параметров произведён"))
                {
                    textBox43.Text = Messin;
                }
            }
            //TTNO = Convert.ToDouble(textBox52.Text);         
        }

        private void label60_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
          


        }

        private void button4_Click(object sender, EventArgs e)
        {
           
        }

        private void saveFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }

        private void label61_Click(object sender, EventArgs e)
        {

        }

        private void textBox35_TextChanged(object sender, EventArgs e)
        {

        }

        private void label55_Click(object sender, EventArgs e)
        {

        }

        private void label49_Click(object sender, EventArgs e)
        {

        }

        private void textBox58_TextChanged(object sender, EventArgs e)
        {

        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            textBox43.Text = null;
        }
    }
}





