// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function generate_tribes(_count)
{
	// Parameters
	var num_points = _count; // Number of points or tribes
	var radius = room_width div 3;   // Radius of the circle on which points will be placed

	// Center of the room
	var center_x = room_width / 2;
	var center_y = room_height / 2;

	// Angle between each point (in degrees)
	var angle_step = 360 / num_points;

	// Creating points
	for (var i = 0; i < num_points; i++)
	{
	    // Calculate angle in radians
	    var angle = degtorad(i * angle_step);

	    // Calculate x and y coordinates
	    var _x = center_x + radius * cos(angle);
	    var _y = center_y + radius * sin(angle);
    
	    // Generate Tribe at Position
		generate_tribe(_x, _y)
	}
}