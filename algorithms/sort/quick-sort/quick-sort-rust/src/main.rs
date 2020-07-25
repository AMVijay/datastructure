mod quicksort;

fn main() {
    let mut test_array_1 = [15, 13, 9, 8, 7, 2, 3];

    quicksort::quick_sort(&mut test_array_1);

    println!("Final Result");
    for i in 0..test_array_1.len() {
        print!("{} ", test_array_1[i]);
    }

    let mut test_array_2 = [15, 13, 5, 9, 7, 2];

    quicksort::quick_sort(&mut test_array_2);

    println!("Final Result");
    for i in 0..test_array_2.len() {
        print!("{} ", test_array_2[i]);
    }
}
