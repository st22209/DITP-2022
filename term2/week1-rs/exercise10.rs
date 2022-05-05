fn main() {

    let mut i = 0;

    while i < 10 {
        let res = fib(i);
        println!("{}", res);
        i = i + 1;
    }
}

pub fn fib(n: i32) -> i32 {
    if n <= 1 {
        return n;
    }
    return fib(n-1) + fib(n-2);
}