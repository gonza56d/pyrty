"""Handle posts and comments vote logic."""


def handle(positive, instance, user):
    """Handle user vote request.

    Vote can be either positive or negative.
    If a vote of the same type (negative/positive) already exists for this instance
    and user, remove vote and exit function.
    If a vote of the contrary type already exists for this instance and user,
    remove the contrary vote and create the submit type.
    """

    if positive and len(instance.user_positive_vote) > 0:
        # positive vote delete request
        return instance.positive_votes.remove(user)
    elif not positive and len(instance.user_positive_vote) > 0:
        # negative vote create request and instance positive vote
        instance.positive_votes.remove(user)

    if not positive and len(instance.user_negative_vote) > 0:
        # negative vote delete request
        return instance.negative_votes.remove(user)
    elif positive and len(instance.user_negative_vote) > 0:
        # positive vote create request and instance negative vote
        instance.negative_votes.remove(user)

    # create correspondent vote after contrary vote deletion check
    if positive:
        instance.positive_votes.add(user)
    elif not positive:
        instance.negative_votes.add(user)
