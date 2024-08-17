"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""
    
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    
madlibs_stories = {
    "adventure_in_the_place": Story(
        ["adjective", "noun", "verb", "place", "adjective_2"],
        """The {adjective} {noun} decided to {verb} in the {place}. It had a very {adjective_2} time."""
    ),
    "the_animal's_daily_fun": Story(
        ["animal", "verb", "adjective", "noun", "verb_2"],
        """The {animal} loves to {verb} on a {adjective} {noun}. Every day, it {verb_2}s happily."""
    ),
    "the_charming_creature": Story(
        ["place", "adjective", "noun", "verb", "adjective_2"],
        """In the {place}, there was a {adjective} {noun} who liked to {verb}. It always made everyone {adjective_2}."""
    ),
    "a_wishful_journey": Story(
        ["noun", "verb", "adjective", "place"],
        """A {noun} wanted to {verb} in the {place}. It felt very {adjective} afterward."""
    ),
    "dreams_come_true": Story(
        ["verb", "adjective", "noun", "place"],
        """To {verb} in a {adjective} {place} was a dream for the {noun}. It finally came true one day."""
    ),
    "the_ancient_land": Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
}






