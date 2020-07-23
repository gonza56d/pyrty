"""Database initial population purposes."""

# Python
import csv
import os
# import pdb
import sys

# Pyrty
from forums.models import Forum
from posts.models import Post
from subforums.models import Subforum
from users.models import User


class DBInjector:
	"""Populate the database at the first run."""

	def __init__(self):
		"""Check if database is already populated, if not, run injections."""

		self.check_migrations()

		if self.is_first_run():
			self.inject_users()
			self.inject_forums()
			self.inject_subforums()
			self.inject_posts()
			self.inject_comments()

	def check_migrations(self):
		os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyrty.settings')
		try:
			from django.core.management import execute_from_command_line
		except ImportError as exc:
			raise ImportError(
				"Couldn't import Django. Are you sure it's installed and "
				"available on your PYTHONPATH environment variable? Did you "
				"forget to activate a virtual environment?"
			) from exc
		execute_from_command_line('migrate')

	def is_first_run(self):
		with open('utils/dbinjector/users.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			return not User.objects.filter(username=list(csv_reader)[0]).exists()

	def inject_users(self):
		with open('utils/dbinjector/users.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				User.objects.create(username=row[0], email=row[1], password=row[2])
				user = User.objects.get(username=row[0])
				profile = Profile()
				profile.user = user
				profile.save()

	def inject_forums(self):
		with open('utils/dbinjector/forums.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				forum = Forum()
				forum.name = row[0]
				forum.save()

	def inject_subforums(self):
		with open('utils/dbinjector/subforums.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				subforum = Subforum()
				subforum.forum = Forum.objects.get(name=row[0])
				subforum.name = row[1]
				subforum.save()

	def inject_posts(self):
		with open('utils/dbinjector/posts.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				post = Post()
				post.user = User.objects.get(username=row[0])
				post.subforum = Subforum.objects.get(name=row[1])
				post.title = row[2]
				post.content = row[3]
				post.save()

	def inject_comments(self):
		with open('utils/dbinjector/comments.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				comment = Comment()
				comment.user = User.objects.get(username=row[0])
				comment.post = Post.objects.get(title=row[1])
				comment.content = row[2]
				comment.save()
