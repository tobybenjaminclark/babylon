/// @description Insert description here
// You can write your code in this editor

// WASD controller in GameMaker Studio 2

// Define movement speed
movement_speed = 10;

// Check for input and move the player accordingly
if (keyboard_check(ord("W"))) {
    y -= movement_speed; // Move up when W is pressed
}

if (keyboard_check(ord("S"))) {
    y += movement_speed; // Move down when S is pressed
}

if (keyboard_check(ord("A"))) {
    x -= movement_speed; // Move left when A is pressed
}

if (keyboard_check(ord("D"))) {
    x += movement_speed; // Move right when D is pressed
}


/// obj_camera Step Event

//this is cahnges the zoom based on scolling but you can set it how ever you like
zoom_level = clamp(zoom_level + (((mouse_wheel_down() - mouse_wheel_up())) * 0.1), 0.5, 2);

//Get current size
var view_w = camera_get_view_width(view_camera[0]);
var view_h = camera_get_view_height(view_camera[0]);

//Set the rate of interpolation
var rate = 0.2;

//Get new sizes by interpolating current and target zoomed size
var new_w = lerp(view_w, zoom_level * default_zoom_width, rate);
var new_h = lerp(view_h, zoom_level * default_zoom_height, rate);

//Apply the new size
camera_set_view_size(view_camera[0], new_w, new_h);

var vpos_x = camera_get_view_x(view_camera[0]);
var vpos_y = camera_get_view_y(view_camera[0]);

//change coordinates of camera so zoom is centered
var new_x = lerp(vpos_x,vpos_x+(view_w - zoom_level * default_zoom_width)/2, rate);
var new_y = lerp(vpos_y,vpos_y+(view_h - zoom_level * default_zoom_height)/2, rate);





