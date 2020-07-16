mod mergesort;

fn main() {
    let mut array: [isize;6] = [15,13,5,9,7,2];
    mergesort::mergesort(&mut array);

    println!("Final Result");
    for i in 0..array.len(){
        print!("{} ", array[i]);
    }

}
