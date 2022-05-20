fn main() {
    for i in 25..51 {
        if is_prime(i) == true {
            println!("{}", i)
        }
    }
}

fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    for a in 2..n {
        if n % a == 0 {
            return false;
        }
    }
    return true
}