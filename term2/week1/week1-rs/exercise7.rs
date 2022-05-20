use std::io;

fn main() {

    let mut width = String::new();
    println!("Enter the width: ");
    io::stdin()
        .read_line(&mut width)
        .expect("Failed to read, get good");
    let width = width.trim().parse::<i32>().unwrap();

    println!();

    for i in (0..(width+1)).rev() {
        for x in (1..(i+1)).rev() {
            print!("{}", x)
        }
        println!();
    }

}