class Palindrome():

    def isPalindrome(self):
        self.resp = ''.join(reversed(word))

        if (word == self.resp):
            print("Yes")
            return True
        else:
            print("No")
            return False


word = input("Enter your word\n>>>")

ans = Palindrome()

ans.isPalindrome()