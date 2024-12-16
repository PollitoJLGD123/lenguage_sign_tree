using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;
using System.IO;

namespace ModernApp.MVVM.View
{
    /// <summary>
    /// Interaction logic for HomeView.xaml
    /// </summary>
    public partial class HomeView : UserControl
    {
        private Process cmdProcess;
        public HomeView()
        {
            InitializeComponent();
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            try
            {
                string pythonScriptPath = @"E:\UNT\Ciclo 06\Sistemas Inteligentes\Proyect_Sklearn";
                string pythonScriptName = "llamada_python.py";

                // Crear un archivo batch temporal
                string batchFilePath = Path.Combine(Path.GetTempPath(), "RunPythonScript.bat");
                using (StreamWriter sw = new StreamWriter(batchFilePath))
                {
                    sw.WriteLine("@echo off");
                    sw.WriteLine($"cd /d \"{pythonScriptPath}\"");
                    sw.WriteLine($"python \"{pythonScriptName}\"");
                    sw.WriteLine("pause");
                }

                // Iniciar el proceso cmd para ejecutar el archivo batch
                cmdProcess = new Process
                {
                    StartInfo = new ProcessStartInfo("cmd.exe", $"/c \"{batchFilePath}\"")
                    {
                        UseShellExecute = true,
                        CreateNoWindow = false
                    }
                };

                cmdProcess.Start();

                MessageBox.Show("Aplicación Python iniciada en una nueva ventana de comando.");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error al iniciar la aplicación Python: {ex.Message}");
            }
        }
    }
}
