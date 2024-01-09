fn main() {
    let n = 2 * 10000000 + 5;
    let mut prime = vec![1; n + 1];
    prime[0] = 0;
    prime[1] = 0;
    for i in 2..=n {
        if prime[i] == 1 {
            let mut j = 2 * i;
            while j <= n {
                prime[j] = 0;
                j += i;
            }
        }
    }

    let mut d = Vec::new();
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let num_tests: i32 = input.trim().parse().unwrap();
    for _ in 0..num_tests {
        input.clear();
        std::io::stdin().read_line(&mut input).unwrap();
        let n: usize = input.trim().parse().unwrap();
        if is_prime(n, &prime) {
            d.push("YES".to_string());
        } else {
            d.push("NO".to_string());
        }
    }
    println!("{}", d.join("\n"));
}

fn is_prime(n: usize, prime: &Vec<i32>) -> bool {
    prime[n] == 1
}

