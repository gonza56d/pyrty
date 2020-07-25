"""Database initial population purposes."""

# Python
import csv
# import pdb

# Django
from django.core.management import call_command

# Pyrty
from comments.models import Comment
from forums.models import Forum
from posts.models import Post
from profiles.models import Profile
from subforums.models import Subforum
from users.models import User


class DBInjector:
	"""Populate the database at the first run."""

	def __init__(self):
		"""Check if database is already populated, if not, run injections."""

		call_command('migrate')

		# pdb.set_trace()

		if self.is_first_run():
			self.inject_users()
			self.inject_forums()
			self.inject_subforums()
			self.inject_posts()
			self.inject_comments()

	def is_first_run(self):
		return not User.objects.filter(username='gonza56d').exists()

	def inject_users(self):
		with open('utils/dbinjector/users.csv', newline='') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				User.objects.create_user(username=row[0], email=row[1], password=row[2])
				user = User.objects.get(username=row[0])
				profile = Profile()
				profile.user = user
				profile.save()

	def inject_forums(self):
		with open('utils/dbinjector/forums.csv', newline='') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				forum = Forum()
				forum.name = row[0]
				forum.save()

	def inject_subforums(self):
		with open('utils/dbinjector/subforums.csv', newline='') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				subforum = Subforum()
				subforum.forum = Forum.objects.get(name=row[0])
				subforum.name = row[1]
				subforum.save()

	def inject_posts(self):
		with open('utils/dbinjector/posts.csv', newline='') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				post = Post()
				post.user = User.objects.get(username=row[0])
				post.subforum = Subforum.objects.get(name=row[1])
				post.title = row[2]
				post.content = row[3]
				post.save()

	def inject_comments(self):
		with open('utils/dbinjector/comments.csv', newline='') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				comment = Comment()
				comment.user = User.objects.get(username=row[0])
				comment.post = Post.objects.get(title=row[1])
				comment.content = row[2]
				comment.save()
