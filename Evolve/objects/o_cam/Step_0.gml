/// @description Insert description here
// You can write your code in this editor

// WASD controller in GameMaker Studio 2

//Check if middle button was clicked
//get current camera position of x and y
var cx = camera_get_view_x(view_camera[0]);
var cy = camera_get_view_y(view_camera[0]);
//speed you want to control the camera
var spd = 4;
//control inputs that move left right up and down
var hori = (keyboard_check(ord("D"))-keyboard_check(ord("A"))) * spd;
var vert = (keyboard_check(ord("S"))-keyboard_check(ord("W"))) * spd;
//set/move the camera

var nx = cx+hori;
var ny = cy+vert;

nx = clamp(nx, 0, room_width - camera_get_view_width(view_camera[0]));
ny = clamp(ny, 0, room_height - camera_get_view_height(view_camera[0]));
camera_set_view_pos(view_camera[0],nx,ny);


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






