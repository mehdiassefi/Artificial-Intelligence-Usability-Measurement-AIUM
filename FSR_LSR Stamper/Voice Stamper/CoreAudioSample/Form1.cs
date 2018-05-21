using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using CoreAudioApi;
using System.Threading.Tasks;
using System.Diagnostics;

namespace CoreAudioSample
{
    public partial class Form1 : Form
    {
        private MMDevice device;
        int x,count,flag=0,silence, data,resume;
        string fsr, lsr;
        string res = @"c:\Users\Mehdi\Desktop\results.txt";
        Stopwatch stopwatch = new Stopwatch();

        public Form1()
        {
            InitializeComponent();
            silence = 1;
            data = 0;
            resume = 0;
            fsr = "--------------";
            lsr = "--------------";
            MMDeviceEnumerator DevEnum = new MMDeviceEnumerator();
            device = DevEnum.GetDefaultAudioEndpoint(EDataFlow.eRender, ERole.eMultimedia);
            tbMaster.Value = (int)(device.AudioEndpointVolume.MasterVolumeLevelScalar * 100);
            device.AudioEndpointVolume.OnVolumeNotification += new AudioEndpointVolumeNotificationDelegate(AudioEndpointVolume_OnVolumeNotification);
            timer1.Enabled = true;
        }

        void AudioEndpointVolume_OnVolumeNotification(AudioVolumeNotificationData data)
        {
            if (this.InvokeRequired)
            {
                object[] Params = new object[1];
                Params[0] = data;
                this.Invoke(new AudioEndpointVolumeNotificationDelegate(AudioEndpointVolume_OnVolumeNotification), Params);
            }
            else
            {
                tbMaster.Value = (int)(data.MasterVolume * 100);
            }
        }

        private void tbMaster_Scroll(object sender, EventArgs e)
        {
            device.AudioEndpointVolume.MasterVolumeLevelScalar = ((float)tbMaster.Value / 100.0f);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string s;

            string path = @"c:\Users\Mehdi\Desktop\fsrlsr.txt";
            s = DateTimeOffset.Now.ToString("HH:mm:ss:fffff");
            label6.Text = fsr;
            label7.Text = lsr;
            pkMaster.Value = (int)(device.AudioMeterInformation.MasterPeakValue * 100);
            x = (int)(device.AudioMeterInformation.MasterPeakValue * 100);
            //first time
            if (silence == 1 && data == 0 && x > 0 && resume ==0)
            {
                    silence = 0;
                    data = 1;
                    s = DateTimeOffset.Now.ToString("HH:mm:ss:fffff");
                    lsr = fsr = s;

            }

            if (silence == 1 && data == 0 && x > 0 && resume == 1)
            {
                silence = 0;
                data = 1;
                s = DateTimeOffset.Now.ToString("HH:mm:ss:fffff");
                lsr= s;

            }
            //talking!
            if (x > 0 && silence == 0 && data == 1)
            {
                s = DateTimeOffset.Now.ToString("HH:mm:ss:fffff");
                lsr = s;
                resume = 0;
            }
            //stall
            if (x == 0 && silence == 0 && data == 1 && !stopwatch.IsRunning)
            {
                stopwatch.Start();
                silence = 1;
            }
            //resume talking
            if (x > 0 && silence == 1 && data == 1 && stopwatch.IsRunning)
            {
                stopwatch.Reset();
                silence = 0;
                resume = 1;
                s = DateTimeOffset.Now.ToString("HH:mm:ss:fffff");
                lsr = s;

            }
            //stop permanently
            if (x == 0 && silence == 1 && data == 1)
            {
                stopwatch.Stop();
                if (stopwatch.ElapsedMilliseconds > 5000)
                {
                    data = 0;
                    resume = 0;
                    stopwatch.Reset();
                    using (StreamWriter sw = File.AppendText(path))
                    {

                        string st = fsr + "        "  + lsr;
                        sw.WriteLine(st);
                        
                    }
                    using (StreamWriter sw = File.AppendText(res))
                    {

                        string st = "FSR : " + fsr + "    LSR : " + lsr;
                        sw.WriteLine(st);

                    }

                }
                else
                {
                    stopwatch.Start();
                    resume = 1;
                }
            }   

                
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label5.Text = Convert.ToChar(169) + "2014 MSU Networks Lab, All Rights Reserved! ";
        }

        private void pkMaster_Click(object sender, EventArgs e)
        {

        }

        
    }
}