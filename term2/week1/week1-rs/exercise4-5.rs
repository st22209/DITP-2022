fn main() {
    let mut numbers = Vec::new();

    for i in 1..101 {
        numbers.push(i);
    }
    let sum: usize = numbers.iter().sum();
    let average = sum as f32 / numbers.len() as f32;
    println!("Sum: {}\nAverage: {}", sum, average);
}