from Stringler import Stringler # type: ignore
import pytest

# Verify valid string size
def test_stringer_empty_string():
    with pytest.raises(ValueError, match="String must have a valid size"):
        Stringler("")

# Verify data
def test_getArr():
    s = Stringler("\tInserting a (random data)!\n")
    s.getArr() == ["inserting", "random", "data"]

# Tokens
def test_getSize():
    s = Stringler("Let's write some unit tests!")
    assert s.getSize() == 4

# Largest
def test_largest():
    s = Stringler("Linux distribution is an operating system")
    assert s.largest() == "distribution"

# Mean
def test_mean():
    s = Stringler("the quick brown fox jumps over the lazy dog")
    assert round(s.mean(), 2) == 4.17

# Std
def test_std():
    s = Stringler("the cat purrs loudly")
    assert round(s.std(), 2) == 1.25

# Skew
def test_skew():
    s = Stringler("This product is more expensive than usual. When will it get cheaper?")
    assert round(s.skew(), 2) == -0.27

# Kurtosis
def test_kurtosis():
    s = Stringler("Do you know what is this? maybe that's an issue.")
    assert round(s.kurtosis(), 2) == 1.50

# Jarque Bera
def test_jarque_bera():
    s = Stringler("Artificial intelligence (AI) refers to the ability of a digital computer"
    "or computer-controlled robot to perform tasks commonly associated with intelligent" \
    "beings.")
    assert round(s.jarqueBera(), 2) == 1.74

# Type to Token Ratio
def test_typeTokenRatio():
    s = Stringler("Let's eat! I need to eat something.")
    assert round(s.typeTokenRatio(), 2) == 0.80

# Polygrams
def test_polygrams():
    s = Stringler("Poly test time! Poly... test... time? Poly time!")
    assert s.polygrams() == {'poly': 3, 'test': 2, 'time': 3}
    assert s.polygrams(2) == {'poly test': 2, 'poly time': 1, 'test time': 2, 'time poly': 2}
    assert s.polygrams(3) == {'poly test time': 2, 'test time poly': 2, 'time poly test': 1, 'time poly time': 1}

# Fashion
def test_fashion():
    s = Stringler("apple banana apple orange banana apple")
    assert s.fashion() == "apple"

# Emotion
def test_emotion():
    s = Stringler("She felt competent as she completed the final task of the day, her confidence shining through. Walking outside," \
    "she was enchanted by the sunset’s vibrant colors. Yet, a small feeling of guilt lingered from the argument with a friend earlier." \
    "Still, she considered herself lucky to have such meaningful relationships. Later, receiving a kind message, she was pleased to know" \
    "things might be okay. But as the night grew quiet, she remained slightly skeptical about what tomorrow might bring.")
    assert s.emotion() == {'adequate': 1, 'anxious': 1, 'attracted': 1, 'happy': 1, 'sad': 1}

# Reaction
def test_reaction():
    s = Stringler("Today was an average day at work, but something unexpected happened. I felt happy when my team congratulated" \
    "me on the project results. Later, my energy was a bit low, but I still felt proud of what we accomplished. On my way home," \
    "I realized how safe I felt in my neighborhood, and as I entered my house, I was surprised with a happy birthday party.")
    assert s.reaction() == {'negative': 1, 'neutral': 2, 'positive': 2}

if __name__ == "__main__":
    pytest.main([__file__, "--verbose"])