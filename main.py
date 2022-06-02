import random


random.seed()


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'You got a card {current}. You score {score} points.')
        else:
            print(f'The croupier got a card {current}. At the croupier score {score} points')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Will you take a card? Yes/No\n')
            if choice == 'Yes':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print("I'm sorry but you lose")
                    break
                elif score == 21 and bot_score == 21:
                    print('Draw')
                elif score == 21 or bot_score > 21:
                    print('Congratulations, you are the winner!')
                    break
            elif choice == 'No':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'You lose, you score {score} points, at the croupier have {bot_score} points.')
                else:
                    print(f'You win, you score {score} points, at the croupier have {bot_score} points.')

                break

    def start(self):
        random.shuffle(self.deck)
        print('The game of Blackjack has Start!')
        print('In blackjack, tens, jacks, queens, and kings are each worth 10 points.\nAce can be worth 1 or 11 points')
        print('----------------------------------')
        self.choice()

        print("See you soon!")


game = BlackJack()
game.start()