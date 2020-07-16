pub fn mergesort(array: &mut [isize]) {
    let size = array.len();

    if size > 2 {
        // Divide and sort the array
        divide_and_sort(array, 0, size - 1);

    }
}

fn divide_and_sort(array: &mut [isize], start_index: usize, end_index: usize) {
    if start_index < end_index {
        let mid_index: usize = (end_index + start_index) / 2;
        // Divide Left Half
        divide_and_sort(array, start_index, mid_index);
        // Divide Right Half
        divide_and_sort(array, mid_index + 1, end_index);
        // Compare and Merge values
        merge(array, start_index, mid_index, end_index);

    }
}

fn merge(array: &mut [isize], start_index: usize, mid_index : usize, end_index: usize) {
    let mut temp_start_index = start_index;
    let mut temp_mid_index = mid_index+1;

    let mut temp_array : Vec<isize> = Vec::new();

    while temp_start_index <= mid_index && temp_mid_index <= end_index {
        if array[temp_start_index] < array[temp_mid_index] {
            temp_array.push(array[temp_start_index]);
            // let temp = array[temp_mid_index];
            // array[temp_mid_index] = array[temp_start_index];
            // array[temp_start_index] = temp;
            temp_start_index = temp_start_index + 1;
        } else {
            temp_array.push(array[temp_mid_index]);
            temp_mid_index = temp_mid_index + 1;
        }
    }

    while temp_start_index <= mid_index {
        temp_array.push(array[temp_start_index]);
        temp_start_index = temp_start_index + 1;
    }

    while temp_mid_index <= end_index {
        temp_array.push(array[temp_mid_index]);
        temp_mid_index = temp_mid_index + 1;
    }

    let mut temp_index = 0;
    let mut array_index = start_index;
    while array_index <= end_index  {
        array[array_index] = temp_array[temp_index];
        temp_index = temp_index + 1;
        array_index = array_index + 1;
    }

}
