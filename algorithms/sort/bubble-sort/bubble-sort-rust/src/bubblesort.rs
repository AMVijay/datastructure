pub fn bubblesort(array: &mut [isize]){
    let length_of_array = array.len();
    println!("Lengh of Array {}", length_of_array);

    traverse_and_sort(array,length_of_array);
}

fn traverse_and_sort(array: &mut [isize], end_index: usize){

    let mut swap_happened : bool = false;
    for i in 0..end_index-1{
        if array[i] > array[i+1]{
            let temp: isize = array[i];
            array[i] = array[i+1];
            array[i+1] = temp;
            swap_happened = true;
        }
    }

    if swap_happened {
        traverse_and_sort(array, end_index - 1);
    }

}