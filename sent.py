
import random

random.seed()

def e(arg):
    if callable(arg):
        return arg()
    else:
        return arg

def choose(*args):
    def f():
        return e(random.choice(args))
    return f

def lit(s):
    def f():
        return s
    return f

def j(*args):
    def f():
        r = []
        for a in args:
            r.append(e(a))
        return "".join(r)
    return f

def opt(*vals):
    return choose(j(*vals), "")


MASS_NOUN = choose("water", "butter", "cheese", "mustard", "salad")
COUNT_NOUN = choose("cheese", "baby", "car", "computer", "salad", "door", "house")
PROPER_NOUN = choose("Martin", "Adriana")
PROPER_POSESSIVE = j(PROPER_NOUN, "'s")

PLURAL_DETERMINER = choose("some", "the", PROPER_POSESSIVE)
SINGULAR_DETERMINER = choose("some", "the", PROPER_POSESSIVE)

TRANSITIVE_VERB = choose("ate", "saw", "threw", "dropped", "loves", "kissed", "married")
INTRANSITIVE_VERB = choose("slept", "arose", "stank", "yelped")

PARTICIPAL = choose("limping", "falling")

ADVERB = choose("sluggishly", "quickly", "immediately", "enthusiastically", "stubbornly", "willingly", "unwillingly")
ADJECTIVE = choose("huge", "tiny", "wonderful", "magnificent", PARTICIPAL)
CONJUNCTION = choose("but", "and")

PREPOSITION = choose("across", "over", "around", "into", "onto", "through")

NP = choose(
    j(PLURAL_DETERMINER, opt(" ", ADJECTIVE), " ", choose(MASS_NOUN)),
    j(SINGULAR_DETERMINER, opt(" ", ADJECTIVE), " ", choose(COUNT_NOUN)),
    PROPER_NOUN,
)

VP = j(choose(
    INTRANSITIVE_VERB,
    j(TRANSITIVE_VERB, " ", NP),
), opt(" ", ADVERB), opt(" ", PREPOSITION, " ", NP))

S = j(NP, " ", VP)

MAIN = choose(
    j(S, "."),
    j(S, ", ", CONJUNCTION, " ", S, "."),
)

for i in xrange(1, 20):
    result = MAIN()
    print result

