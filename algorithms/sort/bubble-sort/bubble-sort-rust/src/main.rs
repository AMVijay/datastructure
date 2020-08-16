mod bubblesort;

fn main() {
    let mut input_array : [isize;6] = [5,4,9,2,1,8];
    bubblesort::bubblesort(&mut input_array);

    println!("final Result :: ");
    for i in 0..input_array.len(){
        print!("{} ", input_array[i]);
    }

    let mut test_array_1 = [15, 13, 9, 8, 7, 2, 3];

    bubblesort::bubblesort(&mut test_array_1);

    println!("Final Result");
    for i in 0..test_array_1.len() {
        print!("{} ", test_array_1[i]);
    }

    let mut test_array_2 = [15, 13, 5, 9, 7, 2];

    bubblesort::bubblesort(&mut test_array_2);

    println!("Final Result");
    for i in 0..test_array_2.len() {
        print!("{} ", test_array_2[i]);
    }
}
