use std::io;

fn main() {

    let mut number = String::new();
    println!("Enter a number: ");
    io::stdin()
        .read_line(&mut number)
        .expect("Failed to read, get good");
    let number = number.trim().parse::<i32>().unwrap();

    println!("\n");
    
    for i in 1..number+1 {
        println!("{}", i)
    }
}