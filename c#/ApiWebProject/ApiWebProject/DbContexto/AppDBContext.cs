
using ApiWebProject.Models;
using Microsoft.EntityFrameworkCore;

namespace ApiWebProject.DbContexto
{
    public class AppDBContext : DbContext
    {
        public AppDBContext(DbContextOptions<AppDBContext> options) : base(options)
        {

        }
        public DbSet<Cliente> Clientes { get; set; }
    }
}
