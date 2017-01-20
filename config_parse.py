import sys
import os
import configargparse


def get_args():
	default_config = []

	if '-cf' not in sys.argv and '--config' not in sys.argv:
		default_config = [os.getenv('Earthporn_ShowerThoughts_CONFIG', os.path.join(os.path.dirname(__file__), '../config/config.ini'))]

	parser = configargparse.ArgParser(default_config_files=default_config, auto_env_var_prefix='Earthporn_ShowerThoughts_')

	parser.add_argument("-t", "--text_subreddit", help="display text overlay from top posts in this subreddit")
	parser.add_argument("-i", "--image_subreddit", help="display background image from top post of subreddit")
    	parser.add_argument("-l", "--top_limit",type=int, help="determines how many top submissions to recieve from each subreddit")
	parser.add_argument("-r", "--refresh_rate",type=int, help="determines the refresh rate in seconds for the template to update")

	return vars(parser.parse_args())
