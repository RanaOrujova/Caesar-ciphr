def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():  # Böyük hərflər üçün
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():  # Kiçik hərflər üçün
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # Digər simvollar (rəqəmlər, boşluqlar və s.)
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Şifrələməni geri çevirmək üçün mənfi sürüşdürmə

# Nümunə istifadə
original_text = "Hello, World!"
shift_amount = 3

encrypted = caesar_encrypt(original_text, shift_amount)
decrypted = caesar_decrypt(encrypted, shift_amount)

print("Orijinal mətn:", original_text)
print("Şifrələnmiş mətn:", encrypted)
print("Şifrə açılmış mətn:", decrypted)
