// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information

function generate_weightings()
{
	return {
		CONSUME_BUSH_HARD :			random(1),
		CONSUME_BUSH_SOFT :			random(1),
		CONSUME_BUSH_HARD_SMALL :	random(1),
		CONSUME_BUSH_SOFT_SMALL :	random(1),
		CONSUME_BUSH_RED :			random(1),
		CONSUME_BUSH_PINK :			random(1),
		CONSUME_BUSH_ORANGE :		random(1),
		CONSUME_CACTUS_BIG :		random(1),
		CONSUME_CACTUS_SMALL :		random(1),
		CONSUME_FERN_HARD :			random(1),
		CONSUME_FERN_SOFT :			random(1),
		CONSUME_FERN_HARD_SMALL :	random(1),
		CONSUME_FERN_SOFT_SMALL :	random(1)
	}
}

function get_object(_id)
{
    switch(_id)
    {
        case BUSH_HARD:			return "BUSH_HARD";
        case BUSH_HARD_SMALL:	return "BUSH_HARD_SMALL";
        case BUSH_SOFT:			return "BUSH_SOFT";
        case BUSH_SOFT_SMALL:	return "BUSH_SOFT_SMALL";
        case BUSH_RED:			return "BUSH_RED";
        case BUSH_PINK:			return "BUSH_PINK";
        case BUSH_ORANGE:		return "BUSH_ORANGE";
        case CACTUS_BIG:		return "CACTUS_BIG";
        case CACTUS_SMALL:		return "CACTUS_SMALL";
        case FERN_HARD:			return "FERN_HARD";
        case FERN_HARD_SMALL:	return "FERN_HARD_SMALL";
        case FERN_SOFT:			return "FERN_SOFT";
        case FERN_SOFT_SMALL:	return "FERN_SOFT_SMALL";
        default:				return "Unknown Object";
    }
}

function get_action(_struct, _id, _action)
{
	switch(_action)
	{
		case CONSUME: return _struct[$ ("CONSUME_" + get_object(_id))]
	}
}