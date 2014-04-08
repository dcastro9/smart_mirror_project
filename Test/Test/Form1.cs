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
using System.Xml;
using System.Web;

namespace Test
{
    public partial class Form1 : Form
    {

        //Variables for Weather
        String Temperature;
        String Condition;

        public Form1()
        {
            InitializeComponent();
        }

        //Displays the date and time in labels
        private void displayTimeDate()
        {
            label1.Text = DateTime.Now.ToLongDateString();
            label2.Text = DateTime.Now.ToShortTimeString();
        }

        //Accesses Yahoo Weather to load the Temperature and Condition
        private void GetWeather()
        {
            String query = String.Format("http://weather.yahooapis.com/forecastrss?w=2357024");
            XmlDocument wData = new XmlDocument();
            wData.Load(query);

            XmlNamespaceManager manager = new XmlNamespaceManager(wData.NameTable);
            manager.AddNamespace("yweather", "http://xml.weather.yahoo.com/ns/rss/1.0");

            XmlNode channel = wData.SelectSingleNode("rss").SelectSingleNode("channel");
            XmlNodeList nodes = wData.SelectNodes("/rss/channel/item/yweather:forecast", manager);

            Temperature = channel.SelectSingleNode("item").SelectSingleNode("yweather:condition", manager).Attributes["temp"].Value;
            Condition = channel.SelectSingleNode("item").SelectSingleNode("yweather:condition", manager).Attributes["text"].Value;

            label3.Text = Temperature+"°F";
            label4.Text = Condition;
        }


        //I wasn't sure how to get functions to run on startup, so I simply have a 'Start' button
        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            displayTimeDate();
            GetWeather();
        }

    }
}
