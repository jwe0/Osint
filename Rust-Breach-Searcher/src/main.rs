use std::io::{self, BufRead, Write};
use std::fs::{self, File};
use std::time::Instant;

fn art() {
    print!(r#"

 ____            _     ____                      _     
|  _ \ _   _ ___| |_  / ___|  ___  __ _ _ __ ___| |__  
| |_) | | | / __| __| \___ \ / _ \/ _` | '__/ __| '_ \ 
|  _ <| |_| \__ \ |_   ___) |  __/ (_| | | | (__| | | |
|_| \_\\__,_|___/\__| |____/ \___|\__,_|_|  \___|_| |_|
    
"#)
}




fn main() {
    art();
    print!("Breach Folder: ");
    io::stdout().flush().unwrap();
    let mut folder = String::new();
    io::stdin().read_line(&mut folder).unwrap();

    print!("Query: ");
    io::stdout().flush().unwrap();
    let mut query = String::new();
    io::stdin().read_line(&mut query).unwrap();

    print!("Output File: ");
    io::stdout().flush().unwrap();
    let mut file = String::new();
    io::stdin().read_line(&mut file).unwrap();

    print!("Output? (y/n): ");
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let files = fs::read_dir(folder.trim()).unwrap();
    let mut dump = File::create(file.trim()).unwrap();

    let start = Instant::now();
    for file_entry in files {
        let file = fs::File::open(file_entry.unwrap().path()).unwrap();
        let reader = io::BufReader::new(file);

        for line in reader.lines() {
            if let Ok(line_content) = line {
                let trimmed_line = line_content.trim();
                if trimmed_line.contains(&query.trim()) {
                    if input.trim() == "y" {
                        println!("{}", trimmed_line);
                    }
                    let dump_line = format!("{}\n", trimmed_line);
                    dump.write(dump_line.as_bytes()).unwrap();
                }
            }
        }
    }
    println!("Time elapsed: {:?}s", start.elapsed().as_secs());
}
