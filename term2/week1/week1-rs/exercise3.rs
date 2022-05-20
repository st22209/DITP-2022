use std::io;

fn main() {

    let mut start = String::new();
    println!("Enter the start number: ");
    io::stdin()
        .read_line(&mut start)
        .expect("Failed to read, get good");
    let start = start.trim().parse::<i32>().unwrap();

    let mut stop = String::new();
    println!("Enter the stop number: ");
    io::stdin()
        .read_line(&mut stop)
        .expect("Failed to read, get good");
    let stop = stop.trim().parse::<i32>().unwrap();

    let mut increment = String::new();
    println!("Enter the increment amount: ");
    io::stdin()
        .read_line(&mut increment)
        .expect("Failed to read, get good");
    let increment = increment.trim().parse::<usize>().unwrap();

    println!("\n");
    
    for i in (start..stop).step_by(increment) {
        println!("{}", i)
    }
    println!("{}", stop);
}