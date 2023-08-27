def vowel_filter(function):
  def wrapper():
    result = function()
    vowels = ['a','e', 'o', 'i', 'u ', 'y']
    return [letter for letter in result if letter in vowels]

  return wrapper