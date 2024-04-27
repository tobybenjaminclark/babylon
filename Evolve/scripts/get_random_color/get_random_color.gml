// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function get_random_color()
{
	// Check if the color list has been created and is stored in a global variable
	if (!variable_global_exists("color_list")) {
	    // Create the color list if it does not exist
	    global.color_list = ds_list_create();
	    ds_list_add(global.color_list, c_red);
	    ds_list_add(global.color_list, c_lime);
	    ds_list_add(global.color_list, c_aqua);
	    ds_list_add(global.color_list, c_yellow);
		ds_list_add(global.color_list, c_orange);
		ds_list_add(global.color_list, c_blue);
		ds_list_add(global.color_list, c_fuchsia);
		ds_list_add(global.color_list, c_gray);
		ds_list_add(global.color_list, c_silver);
		ds_list_add(global.color_list, c_maroon);
		ds_list_add(global.color_list, c_olive);
		ds_list_add(global.color_list, c_green);
		ds_list_add(global.color_list, c_purple);
		ds_list_add(global.color_list, c_teal);
		ds_list_add(global.color_list, c_navy);
		ds_list_add(global.color_list, c_black);
		ds_list_add(global.color_list, c_white);
	}

	// Handle the case where all colors have been removed
	if (ds_list_empty(global.color_list)) {
	    return "No more colors available";  // Return this message if no colors are left
	}

	// Select a random index in the list
	var index = irandom_range(0, ds_list_size(global.color_list) - 1);
	var color = ds_list_find_value(global.color_list, index);  // Retrieve the color at the random index
	ds_list_delete(global.color_list, index);  // Remove the color from the list

	return color;  // Return the selected color
}