using System.ComponentModel.DataAnnotations;

namespace EnviroCheck
{
    public class Record
    {
        [Required]
        public int Id { get; set; }

        [Required]
        public double Temp { get; set; }

        public double? Humidity { get; set; }

        [Required]
        public DateTime Timestamp { get; set; }
    }
}
