def reverse_words(sentence):
  """Reverses the words in a sentence.

  Args:
    sentence: A string.

  Returns:
    A string with the words reversed and the punctuation marks at the end of
    the words.
  """

  words = sentence.split()
  reversed_words = []
  for word in words:
    reversed_word = ""
    for i in reversed(range(len(word))):
      reversed_word += word[i]
    reversed_words.append(reversed_word)

  # Add the punctuation marks at the end of the words.
  for i in range(len(reversed_words)):
    reversed_words[i] += sentence[len("".join(reversed_words[:i]))]

  reversed_sentence = " ".join(reversed_words)
  return reversed_sentence


def main():
  """Takes input and gives output as mentioned in the question."""

  sentence = input("Enter a sentence: ")
  reversed_sentence = reverse_words(sentence)
  print(f"The reversed sentence is: {reversed_sentence}")


if __name__ == "__main__":
  main()
