fn main() {
    for i in 18..23 {
        println!("{}", i)
    }
    println!("\n\n");
    for i in (0..15).step_by(2) {
        println!("{}", i);
    }
    println!("\n\n");
    for i in (-10..31).rev().step_by(5){
        println!("{}", i);
    }
}