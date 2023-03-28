from django.test import TestCase

from channels.models import Channel
from content.models import Content

from channels.ratings import ratings

class NormalRatingsTest(TestCase):

	def setUp(self):
		cont1 = Content(file='req1.txt', rating='2.0')
		cont1.save()
		cont2 = Content(file='req2.txt', rating='8.0')
		cont2.save()
		cont3 = Content(file='req3.txt', rating='5.0')
		cont3.save()
		cont4 = Content(file='req4.txt', rating='6.0')
		cont4.save()

		c1 = Channel(name='Entertainment')
		c1.save()
		c2 = Channel(name='Movies', parent=c1)
		c2.save()
		c3 = Channel(name='TV_shows', parent=c1)
		c3.save()
		c4 = Channel(name='Movies1', parent=c2)
		c4.save()
		c4.content.add(cont1)
		c4.save()
		c5 = Channel(name='Movies2', parent=c2)
		c5.save()
		c5.content.add(cont2)
		c5.save()
		c6 = Channel(name='Show1', parent=c3)
		c6.save()
		c7 = Channel(name='S1E1', parent=c6)
		c7.save()
		c7.content.add(cont3)
		c7.content.add(cont4)
		c7.save()
		
	def test_ratings(self):

		mocked_data = {'Entertainment': 5.2, 'TV_shows': 5.5, 'Show1': 5.5, 'S1E1': 5.5,'Movies': 5.0, 'Movies1': 2.0, 'Movies2': 8.0}

		rat_results = ratings.calculate_ratings()

		self.assertDictEqual(mocked_data, rat_results)

class OnlyRootRatingsTest(TestCase):

	def setUp(self):
		cont1 = Content(file='req1.txt', rating='2.0')
		cont1.save()

		c1 = Channel(name='Entertainment')
		c1.save()
		c1.content.add(cont1)
		c1.save()

		
	def test_ratings(self):

		mocked_data = {'Entertainment': 2.0}

		rat_results = ratings.calculate_ratings()

		self.assertDictEqual(mocked_data, rat_results)

		