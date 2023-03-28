from django.core.management.base import BaseCommand

from channels.ratings import ratings

from datetime import datetime

import pandas as pd

class Command(BaseCommand):
	help = 'Generate channel ratings csv'

	def handle(self, *args, **kwargs):
		time = datetime.now().strftime('%Y_%m_%dT%H_%M_%S')
		scores = ratings.calculate_ratings()

		df = pd.DataFrame(scores.items(), columns=['channel_title', 'average_rating'])
		df.sort_values(by=['rating'], ascending=False, inplace=True)
		
		df.to_csv(f'./data/ratings/ratings_{time}.csv', index=False)