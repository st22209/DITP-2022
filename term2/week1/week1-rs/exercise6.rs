use std::io;

fn main() {

    let mut width = String::new();
    println!("Enter the width: ");
    io::stdin()
        .read_line(&mut width)
        .expect("Failed to read, get good");
    let width = width.trim().parse::<i32>().unwrap();

    println!("\n");

    for i in 0..width {
        for e in 0..(i+1) {
            print!("{} ", e+1)
        }
        println!();
    }
}