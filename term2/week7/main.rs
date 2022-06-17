// put into cargo init project with rand dependency to work

use rand::Rng;
use std::io;

fn main() {
    let mut rng = rand::thread_rng();

    let mut rps = String::new();
    let cpu_choice: u8 = rng.gen_range(1..3);

    println!("Rock Paper Scissors!");
    println!("Enter rock/paper/scissors: ");

    io::stdin().read_line(&mut rps).unwrap();
    let mut rps = rps.to_lowercase();
    let len = rps.len();
    rps.truncate(len - 1);

    let mut computer_choice = String::new();

    if cpu_choice == 1 {
        computer_choice.push_str("rock");
    } else if cpu_choice == 2 {
        computer_choice.push_str("paper");
    } else if cpu_choice == 3 {
        computer_choice.push_str("scissors");
    }

    println!(
        "\nYour Choice: {}\nComputer Choice: {}",
        rps, computer_choice
    );

    if rps == "rock" {
        if computer_choice == "rock" {
            println!("It's a tie!")
        } else if computer_choice == "scissors" {
            println!("You win!")
        } else if computer_choice == "paper" {
            println!("You lose!")
        }
    } else if rps == "paper" {
        if computer_choice == "paper" {
            println!("It's a tie!")
        } else if computer_choice == "rock" {
            println!("You win!")
        } else if computer_choice == "scissors" {
            println!("You lose!")
        }
    } else if rps == "scissors" {
        if computer_choice == "scissors" {
            println!("It's a tie!")
        } else if computer_choice == "paper" {
            println!("You win!")
        } else if computer_choice == "rock" {
            println!("You lose!")
        }
    } else {
        println!("Invalid input!");
    }
}
