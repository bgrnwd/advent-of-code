use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file_path = &args[1];

    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path).unwrap();

    let arr: Vec<&str> = contents.split("\n\n").collect();

    let mut max = 0;
    let mut elves: [i32; 3] = [0, 0, 0];
    for elf in arr {
        let calories: Vec<String> = elf
            .split("\n")
            .map(|x| x.to_string().parse().unwrap())
            .collect();
        let mut sum = 0;
        for cal in calories {
            sum += cal.parse::<i32>().unwrap();
        }
        if sum > max {
            max = sum;
        }
        let min = elves.iter().min().unwrap();
        if sum > *min {
            elves[elves.iter().position(|&x| x == *min).unwrap()] = sum;
        }
    }
    println!("Max: {}", max);
    println!(
        "Sum of 3 top elves: {} - {:?}",
        elves.iter().sum::<i32>(),
        elves
    );
}
