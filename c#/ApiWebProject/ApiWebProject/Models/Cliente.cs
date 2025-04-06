using System.ComponentModel.DataAnnotations;

namespace ApiWebProject.Models
{
    public class Cliente
    {

        [Key]

        public int Id { get; set; }
        public string nombre { get; set; }

        public string apellido { get; set; }    
        public int edad { get; set; }
    }
}
