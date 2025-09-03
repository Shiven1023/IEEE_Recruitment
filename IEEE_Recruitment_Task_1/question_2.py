text = input("Enter a paragraph(max 100 words): ")
words = text.split()
print(words)
# Store palindromes
palindromes = []
for word in words:
  if word.lower() == word.lower()[::-1]:
    palindromes.append(word)
if palindromes:
  print("Palindromes found: "," ".join(palindromes)) 
else:
  print(0)
