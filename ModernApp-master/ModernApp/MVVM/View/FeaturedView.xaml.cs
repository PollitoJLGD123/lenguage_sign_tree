using System;
using System.Collections.Generic;
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
    /// Interaction logic for FeaturedView.xaml
    /// </summary>
    public partial class FeaturedView : UserControl
    {
        public FeaturedView()
        {
            InitializeComponent();
            btnConsultar.Click += Button_Click;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

            string palabra = txtPalabra.Text.ToLower();

            var imagePaths = new List<BitmapImage>();

            string imagenCompletaPath = @"E:\UNT\Ciclo 06\Sistemas Inteligentes\Proyect_Sklearn\ModernApp-master\ModernApp\Signs";

            foreach (char letra in palabra)
            {
                // Construir la ruta a la imagen
                string path = System.IO.Path.Combine(imagenCompletaPath, $"{letra}.jpg");

                if (System.IO.File.Exists(path))
                {
                    var image = new BitmapImage();
                    image.BeginInit();
                    image.UriSource = new Uri(path, UriKind.Absolute);  // Usar UriKind.Absolute para rutas absolutas
                    image.CacheOption = BitmapCacheOption.OnLoad;
                    image.EndInit();

                    imagePaths.Add(image); // Agregar la imagen a la lista
                }
                else
                {
                    MessageBox.Show($"No se encontro la ruta {letra}");
                }
            }

            imagesControl.ItemsSource = imagePaths;

        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
    }
}
