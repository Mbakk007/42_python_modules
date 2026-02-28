from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        # Decide winner:
        if card1.power > card2.power:
            winner = card1
            loser = card2
        elif card2.power > card1.power:
            winner = card2
            loser = card1
        else:
            if card1.rating >= card2.rating:
                winner = card1
                loser = card2
            else:
                winner = card2
                loser = card1

        winner._apply_match_result(True)
        loser._apply_match_result(False)

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        # sort by rating
        leaderboard = []
        for card_id in self.cards:
            leaderboard.append(self.cards[card_id])

        i = 0
        while i < len(leaderboard):
            j = i + 1
            while j < len(leaderboard):
                if leaderboard[j].rating > leaderboard[i].rating:
                    temp = leaderboard[i]
                    leaderboard[i] = leaderboard[j]
                    leaderboard[j] = temp
                j += 1
            i += 1

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_rating = 0

        for card_id in self.cards:
            total_rating += self.cards[card_id].rating

        if total_cards == 0:
            avg_rating = 0
        else:
            avg_rating = int(total_rating / total_cards)

        status = "active"
        if total_cards == 0:
            status = "inactive"

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": status
        }
