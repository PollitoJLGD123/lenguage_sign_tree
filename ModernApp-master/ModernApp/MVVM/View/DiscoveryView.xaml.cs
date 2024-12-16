using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;
using System.IO;

namespace ModernApp.MVVM.View
{
    /// <summary>
    /// Interaction logic for DiscoveryView.xaml
    /// </summary>
    public partial class DiscoveryView : UserControl
    {

        private Process cmdProcess;

        public DiscoveryView()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string pythonScriptPath = @"E:\UNT\Ciclo 06\Sistemas Inteligentes\Proyect_Sklearn";
                string pythonScriptName = "testing.py";

                // Crear un archivo batch temporal
                string batchFilePath = Path.Combine(Path.GetTempPath(), "RunPythonScript.bat");
                using (StreamWriter sw = new StreamWriter(batchFilePath))
                {
                    sw.WriteLine("@echo off");
                    sw.WriteLine($"cd /d \"{pythonScriptPath}\"");
                    sw.WriteLine($"python \"{pythonScriptName}\"");
                    sw.WriteLine("pause");
                }

                // Configurar el proceso cmd para ejecutar el archivo batch
                cmdProcess = new Process
                {
                    StartInfo = new ProcessStartInfo("cmd.exe", $"/c \"{batchFilePath}\"")
                    {
                        UseShellExecute = false, // Necesario para EnableRaisingEvents
                        CreateNoWindow = false
                    }
                };

                // Habilitar eventos y suscribirse al evento Exited
                cmdProcess.EnableRaisingEvents = true;
                cmdProcess.Exited += CmdProcess_Exited;

                // Iniciar el proceso
                cmdProcess.Start();

                MessageBox.Show("Aplicación Python iniciada en una nueva ventana de comando.");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error al iniciar la aplicación Python: {ex.Message}");
            }
        }

        private void CmdProcess_Exited(object sender, EventArgs e)
        {
            // Asegurarse de actualizar la UI en el hilo principal
            Dispatcher.Invoke(() =>
            {
                MessageBox.Show("La aplicación Python ha finalizado.");
            });

            // Opcional: Eliminar el archivo batch temporal si ya no es necesario
            try
            {
                string batchFilePath = Path.Combine(Path.GetTempPath(), "RunPythonScript.bat");
                if (File.Exists(batchFilePath))
                {
                    File.Delete(batchFilePath);
                }
            }
            catch
            {
                // Manejar excepciones si es necesario
            }
        }
    }
}
