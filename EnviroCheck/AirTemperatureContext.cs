using Microsoft.EntityFrameworkCore;

namespace EnviroCheck
{
    public class AirTemperatureContext : DbContext
    {
        public AirTemperatureContext(DbContextOptions<AirTemperatureContext> options)
            : base(options)
        {
        }

        public DbSet<Record> Records { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Record>().ToTable("Records");
        }
    }
}
