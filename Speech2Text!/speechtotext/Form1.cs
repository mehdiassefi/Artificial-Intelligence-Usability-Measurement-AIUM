using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Speech;
using System.Speech.Recognition;

namespace speechtotext
{
    public partial class Form1 : Form
    {
        SpeechRecognitionEngine recognizer = null;
        OpenFileDialog oFD = null;
        private string FileName = "";
        public Form1()
        {
            InitializeComponent();
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            aboutcs aboutForm = new aboutcs();
            aboutForm.ShowDialog();
        }

        private void ReadBTN_Click(object sender, EventArgs e)
        {
            ReadBTN.Enabled = false;
            ReadFileBTN.Enabled = false;
            recognizer = new SpeechRecognitionEngine();
            if (FileName != "")
            {
                recognizer.SetInputToWaveFile(FileName);
                recognizer.LoadGrammar(new DictationGrammar());
                RecognitionResult Result = recognizer.Recognize();
                //recognizer.RecognizeAsync(RecognizeMode.Multiple);
                StringBuilder Output = new StringBuilder();
                foreach (RecognizedWordUnit Word in Result.Words)
                {
                    Output.Append(Word.Text + " ");
                }
                textBox1.Text = Output.ToString();
            }
            else
            {
                try
                {
                    recognizer.SetInputToDefaultAudioDevice();
                    recognizer.AudioLevel.Equals(100);
                    recognizer.LoadGrammar(new DictationGrammar());
                    RecognitionResult Result = recognizer.Recognize();
                    recognizer.RecognizeAsync(RecognizeMode.Multiple);
                    StringBuilder Output = new StringBuilder();
                    foreach (RecognizedWordUnit Word in Result.Words)
                    {
                        Output.Append(Word.Text + " ");
                    }
                    textBox1.Text = Output.ToString();
                }
                catch
                {
                    MessageBox.Show("Please Connect Microphone", "No Input", MessageBoxButtons.OK);
                }                
            }
        }

        private void ReadFileBTN_Click(object sender, EventArgs e)
        {
            oFD = new OpenFileDialog();
            oFD.Filter = "Audio Wave files (*.wav)|*.wav";
            oFD.Multiselect = false;
            oFD.Title = "Open File For Speech";
            oFD.ShowDialog();
            FileName = oFD.FileName;
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            recognizer.Dispose();
            FileName = "";
            textBox1.Text = "";
            StopBTN.Enabled = false;
            ReadBTN.Enabled = true;
            ReadFileBTN.Enabled = true;
        }
    }
}
