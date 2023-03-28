import logging

from typing import Dict
from django.db.models import Avg

from channels.models import Channel

def calculate_ratings() -> Dict[str, float]:
	root = Channel.get_roots()[0]
	scores = get_children_rec(root, {})
	return scores


def get_children_rec(channel: Channel, scores: Dict[str, float]) -> Dict[str, float]:

	avg = channel.content.all().aggregate(avg_contents=Avg('rating'))
	channel_score = 0

	if not avg['avg_contents']:
		children = channel.get_children()
		for child in children:
			channel_score += get_children_rec(child, scores)[child.name]
		scores[channel.name] = round(channel_score/len(children), 1)
		return scores
	else:
		scores[channel.name] = float(avg['avg_contents'])
		return scores
