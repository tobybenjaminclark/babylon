// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function generate_environment()
{
	DPIscaling();
	randomize();
	height_map = generateSimplexNoise2D((room_width div 32) + 1, 10, 256);

	for (var x1 = 0; x1 < (room_width div 32); x1++)
	{
		for(var y1 = 0; y1 < (room_height div 32); y1++)
		{
			var random_number = irandom_range(0, 356);
			if(height_map[x1][y1] > 185)
			{
				if random_number < (height_map[x1][y1])
				{	
					generate_bush(x1 * 32, y1 * 32);
				}
			}
			else if(height_map[x1][y1] > 120)
			{
				if random_number < (height_map[x1][y1])
				{
					generate_grass(x1 * 32, y1 * 32);
				}
			}
		}
	}
}