{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "799226b4-09ed-48e3-aed1-cab285f05b30",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Örnek bir şifre listesi\n",
    "registered_passwords = [\"12345\", \"admin123\", \"mypassword\", \"securepass\"]\n",
    "\n",
    "def check_password(input_password):\n",
    "    \"\"\"\n",
    "    Kullanıcının girdiği şifreyi kontrol eden fonksiyon.\n",
    "    \"\"\"\n",
    "    if input_password in registered_passwords:\n",
    "        return \"Şifre doğru! Giriş başarılı.\"\n",
    "    else:\n",
    "        return \"Şifre hatalı! Giriş başarısız.\"\n",
    "\n",
    "# Kullanıcıdan şifre al\n",
    "user_input = input(\"Lütfen şifrenizi girin: \")\n",
    "\n",
    "# Şifreyi kontrol et ve sonucu yazdır\n",
    "result = check_password(user_input)\n",
    "print(result)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
