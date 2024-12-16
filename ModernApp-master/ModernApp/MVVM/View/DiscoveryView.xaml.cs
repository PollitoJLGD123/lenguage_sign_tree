using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ModernApp.MVVM.View
{
    /// <summary>
    /// Interaction logic for DiscoveryView.xaml
    /// </summary>
    public partial class DiscoveryView : UserControl
    {
        public DiscoveryView()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                // Configurar el proceso
                ProcessStartInfo startInfo = new ProcessStartInfo
                {
                    FileName = @"c:\Users\USUARIO\AppData\Local\Programs\Python\python312\python.exe",
                    Arguments = "\"D:\\SISTEMAS\\CICLO VI\\Sistemas Inteligentes\\Semana 15\\lenguage_sign_tree\\testing.py\"",
                    RedirectStandardOutput = true, // Capturar la salida del script
                    RedirectStandardError = true, // Capturar errores del script
                    UseShellExecute = false, // No usar shell
                    CreateNoWindow = true // No crear ventana visible
                };

                // Ejecutar el proceso
                using (Process process = Process.Start(startInfo))
                {
                    // Leer la salida del script
                    string output = process.StandardOutput.ReadToEnd();
                    string errors = process.StandardError.ReadToEnd();

                    process.WaitForExit(); // Esperar a que termine el script

                    // Mostrar resultados en consola o UI
                    if (!string.IsNullOrEmpty(output))
                    {
                        MessageBox.Show("Output:\n" + output, "Resultado");
                    }

                    if (!string.IsNullOrEmpty(errors))
                    {
                        MessageBox.Show("Errors:\n" + errors, "Errores");
                    }
                }
            }
            catch (Exception ex)
            {
                // Manejo de errores
                MessageBox.Show("Error al ejecutar el script:\n" + ex.Message, "Error");
            }
        }
    }
}
