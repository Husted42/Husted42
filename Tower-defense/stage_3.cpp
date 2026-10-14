// Sort enemies by distance to exit (ascending)
auto insertion_sort_enemy_range(auto arr) {
    for (int i = 1; i < arr.size(); i++) {
        auto key = arr[i]; // Enemy to insert
        int j = i - 1;     // Previous enemy

        // Shift enemies with greater distance to the right
        while (j >= 0 && arr[j].distance_to_exit > key.distance_to_exit) {
            arr[j + 1] = arr[j]; // Shift right
            j--;                // Move left
        }

        arr[j + 1] = key; // Insert at correct position
    }
    return arr; // Return sorted list
}


auto sorted_list = insertion_sort_enemy_range(me.enemies_in_range);

// Shoot enemies in sorted order
for (auto e : sorted_list) {
	printf(e.distance_to_exit);
    me.shoot(e);
}