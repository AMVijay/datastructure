pub fn quick_sort(array: &mut [isize]) {
    let start_index = 0;
    let end_index = array.len() - 1;

    divide_and_sort(array, start_index, end_index);
}

fn divide_and_sort(array: &mut [isize], start_index: usize, end_index: usize) {
    if start_index < end_index {
        println!("start Index {}", start_index);
        println!("End Index {}", end_index);
        let pivot_index: usize = partition_and_arrange(array, start_index, end_index);
        // Left side partition and arrange
        if pivot_index > 0 {
            divide_and_sort(array, start_index, pivot_index - 1);
        }
        // Right side partition and arrange
        divide_and_sort(array, pivot_index + 1, end_index);
    }
}

fn partition_and_arrange(array: &mut [isize], start_index: usize, end_index: usize) -> usize {
    let pivot_value = array[end_index];
    println!("Partition value :: {}", pivot_value);
    let mut pivot_index = end_index;
    let mut index = start_index;

    while index <= end_index {
        if array[pivot_index] < array[index] && pivot_index > index {
            println!(
                "pivot comparison {}, {} {}",
                pivot_index, array[pivot_index], array[index]
            );
            let temp = array[index];
            array[index] = array[pivot_index];
            array[pivot_index] = temp;
            pivot_index = index;
            index = index + 1;
        } else if array[pivot_index] > array[index] && pivot_index < index {
            let temp = array[index];
            array[index] = array[pivot_index];
            array[pivot_index] = temp;

            let temp_index = pivot_index;
            pivot_index = index;
            index = temp_index + 1;
        } else {
            index = index + 1;
        }
    }
    println!("pivot index {}", pivot_index);
    // println!("Final Result");
    // for i in 0..array.len(){
    //     print!("{} ", array[i]);
    // }
    return pivot_index;
}
