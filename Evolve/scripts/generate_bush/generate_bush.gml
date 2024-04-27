// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information

/* Gets the sprite for a specific bush */
function get_bush_sprite(_bush_id)
{
	switch (_bush_id)
	{
	    case BUSH_HARD:			return spr_bush_hard;
	    case BUSH_HARD_SMALL:	return spr_bush_hard_small;
	    case BUSH_SOFT:			return spr_bush_soft;
	    case BUSH_SOFT_SMALL:	return spr_bush_soft_small;
	    case BUSH_RED:			return spr_bush_red;
	    case BUSH_PINK:			return spr_bush_pink;
	    case BUSH_ORANGE:		return spr_bush_orange;
	    case CACTUS_BIG:		return spr_cactus_big;
	    case CACTUS_SMALL:		return spr_cactus;
		case FERN_HARD:			return spr_fern_hard;
		case FERN_HARD_SMALL:	return spr_fern_hard_small;
		case FERN_SOFT:			return spr_fern_soft;
		case FERN_SOFT_SMALL:	return spr_fern_soft_small;
	    default:				return noone;
	}
}

/* Generates a bush at a specified x/y position */
function generate_bush(_x_pos, _y_pos)
{
	var bush_id = irandom_range(1, 9);
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_bush);
	inst.sprite_index = get_bush_sprite(bush_id);
	inst.o_id = bush_id;
}

/* Generates grass at a specified x/y position */
function generate_grass(_x_pos, _y_pos)
{
	var bush_id = irandom_range(10, 13);
	var inst = instance_create_layer(_x_pos, _y_pos, "Instances", o_bush);
	inst.sprite_index = get_bush_sprite(bush_id);
	inst.o_id = bush_id;
}