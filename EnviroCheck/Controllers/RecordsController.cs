using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace EnviroCheck.Controllers
{
    [Route("/api/[controller]")]
    [ApiController]
    public class RecordsController : ControllerBase
    {
        private readonly AirTemperatureContext _context;

        //private static List<Record> records = new List<Record>();
        private ILogger<RecordsController> _logger;

        public RecordsController(AirTemperatureContext context, ILogger<RecordsController> logger)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Record>> GetById(int id)
        {
            var record = await _context.Records.FindAsync(id);

            if (record is null)
                return NotFound();

            return record;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Record>>> GetAll()
        {
            var records = await _context.Records.ToListAsync();
            return records.Count() > 0 ? records : NotFound();
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Record record)
        {
            var context = new ValidationContext(record);
            var results = new List<ValidationResult>();
            bool isValid = Validator.TryValidateObject(record, context, results, true);

            if (isValid)
            {
                record.Timestamp = DateTime.UtcNow;
                _context.Records.Add(record);
                await _context.SaveChangesAsync();

                return CreatedAtAction(nameof(GetById), new { id = record.Id }, record);
            }

            return BadRequest(results);
        }
    }
}
