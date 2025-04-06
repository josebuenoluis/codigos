using ApiWebProject.Models;
using ApiWebProject.DbContexto;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;

namespace ApiWebProject.Controllers
{
    [ApiController]
    [Route("clientes")]
    public class ClienteController : ControllerBase
    {
        private readonly AppDBContext _context;

        public ClienteController(AppDBContext context)
        {
            _context = context;
        }   

        [HttpGet]
        [Route("listar")]
        public IActionResult listarClientes()
        {
            List<Cliente> clientes = new List<Cliente>()
            {
                new Cliente { nombre = "Juan", apellido = "Perez", edad = 30 },
                new Cliente { nombre = "Maria", apellido = "Gomez", edad = 25 },
                new Cliente { nombre = "Carlos", apellido = "Lopez", edad = 40 }
            };

            return Ok(clientes);
        }
        [HttpGet]
        [Route("listardb")]
        public IActionResult listarClientesDB()
        {
            var bd = _context.Clientes.ToList();
            return Ok(bd);
        }
    }
}
