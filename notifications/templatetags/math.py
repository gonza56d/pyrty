"""Custom template tags."""

# Django
from django import template


register = template.Library()


@register.filter(name='add')
def add(value, arg):
	"""Addition"""
	return value + arg


@register.filter(name='substract')
def substract(value, arg):
	"""Substraction"""
	return value - arg
