import random
from enum import Enum

class Color(Enum):
    """Enum for player colors"""
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"

class Token:
    """Represents a token in the game"""
    def __init__(self, player_id, token_id, color):
        self.player_id = player_id
        self.token_id = token_id
        self.color = color
        self.position = -1  # -1 means in home, 0-51 is board position, 52+ is home stretch
        self.is_home = True
    
    def __repr__(self):
        return f"{self.color.value[0]}{self.token_id}"

class Player:
    """Represents a player in the game"""
    def __init__(self, player_id, color):
        self.player_id = player_id
        self.color = color
        self.tokens = [Token(player_id, i, color) for i in range(1, 5)]
        self.position = player_id * 13  # Starting position on board
        self.pieces_home = 4
        self.pieces_finished = 0
    
    def __repr__(self):
        return f"Player {self.player_id} ({self.color.value})"

class Board:
    """Represents the Ludo board"""
    def __init__(self):
        self.board = [[] for _ in range(52)]
    
    def place_token(self, token, position):
        """Place a token at a specific position"""
        if 0 <= position < 52:
            if token not in self.board[position]:
                self.board[position].append(token)
    
    def remove_token(self, token, position):
        """Remove a token from a position"""
        if 0 <= position < 52 and token in self.board[position]:
            self.board[position].remove(token)
    
    def get_tokens_at_position(self, position):
        """Get all tokens at a specific position"""
        if 0 <= position < 52:
            return self.board[position]
        return []
    
    def display(self):
        """Display the board state"""
        print("\n" + "="*60)
        print("LUDO BOARD")
        print("="*60)
        for pos in range(52):
            if self.board[pos]:
                tokens = ", ".join(str(token) for token in self.board[pos])
                print(f"Position {pos:2d}: {tokens}")
        print("="*60 + "\n")

class LudoGame:
    """Main Ludo game class"""
    def __init__(self, num_players):
        if not (2 <= num_players <= 4):
            raise ValueError("Ludo requires 2-4 players")
        
        self.num_players = num_players
        self.colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
        self.players = [Player(i, self.colors[i]) for i in range(num_players)]
        self.board = Board()
        self.current_player = 0
        self.game_over = False
        self.winner = None
    
    def roll_dice(self):
        """Roll the dice (returns 1-6)"""
        return random.randint(1, 6)
    
    def get_token_by_number(self, token_number):
        """Get token by its number (1-4) for current player"""
        if 1 <= token_number <= 4:
            return self.players[self.current_player].tokens[token_number - 1]
        return None
    
    def move_token(self, token, steps):
        """Move a token by specified steps"""
        player = self.players[self.current_player]
        
        # Token entering the board
        if token.is_home and steps == 6:
            token.position = player.position
            token.is_home = False
            player.pieces_home -= 1
            self.board.place_token(token, token.position)
            print(f"  Token {token.token_id} enters the board at position {token.position}!")
            return True
        elif token.is_home:
            print(f"  Token {token.token_id} needs a 6 to enter the board. Got {steps}.")
            return False
        
        # Move token on board
        old_position = token.position
        token.position = (token.position + steps) % 52
        
        # Check if token reached or passed home
        if token.position < old_position:  # Wrapped around
            token.position = 52 + (token.position - player.position)
            player.pieces_finished += 1
            print(f"  Token {token.token_id} reached HOME! Total pieces home: {player.pieces_finished}/4")
            return True
        
        self.board.remove_token(token, old_position)
        self.board.place_token(token, token.position)
        
        # Check for capturing opponent tokens
        self.capture_tokens(token, token.position)
        
        return True
    
    def capture_tokens(self, token, position):
        """Capture opponent tokens at the same position"""
        opponents_on_position = [t for t in self.board.get_tokens_at_position(position) 
                                 if t.color != token.color]
        
        for opponent_token in opponents_on_position:
            self.board.remove_token(opponent_token, position)
            opponent_token.is_home = True
            opponent_token.position = -1
            opponent_player = self.players[opponent_token.player_id]
            opponent_player.pieces_home += 1
            print(f"  💥 Token {opponent_token} captured and sent back home!")
    
    def player_turn(self):
        """Execute one player's turn"""
        player = self.players[self.current_player]
        print(f"\n{'='*60}")
        print(f"🎲 {player}'s TURN")
        print(f"{'='*60}")
        
        dice_roll = self.roll_dice()
        print(f"  Dice roll: {dice_roll}")
        
        # Display player's tokens and their status
        print(f"\n  Your tokens:")
        for i, token in enumerate(player.tokens, 1):
            status = "HOME" if token.is_home else f"Position {token.position}"
            print(f"    {i}. Token {token.token_id}: {status}")
        
        # Get valid moves
        valid_moves = self.get_valid_moves(dice_roll)
        
        if not valid_moves:
            print("  No valid moves available. Turn ends.")
            return
        
        # Player selects token to move
        while True:
            try:
                choice = int(input(f"  Select token to move (1-4): "))
                token = self.get_token_by_number(choice)
                if token and choice in valid_moves:
                    self.move_token(token, dice_roll)
                    break
                else:
                    print("  Invalid selection. Try again.")
            except ValueError:
                print("  Please enter a valid number.")
        
        # Check for win condition
        if player.pieces_finished == 4:
            self.game_over = True
            self.winner = player
    
    def get_valid_moves(self, dice_roll):
        """Get list of valid token numbers that can move"""
        player = self.players[self.current_player]
        valid = []
        
        for i, token in enumerate(player.tokens, 1):
            if token.is_home and dice_roll == 6:
                valid.append(i)
            elif not token.is_home and token.position < 52:
                valid.append(i)
        
        return valid
    
    def display_standings(self):
        """Display current game standings"""
        print("\n" + "="*60)
        print("STANDINGS")
        print("="*60)
        for player in self.players:
            print(f"{player}: {player.pieces_finished}/4 pieces home, {player.pieces_home} in starting area")
        print("="*60 + "\n")
    
    def play(self):
        """Main game loop"""
        print("\n" + "🎮 "*15)
        print("WELCOME TO LUDO GAME!")
        print("🎮 "*15)
        
        turn_count = 0
        max_turns = 1000  # Prevent infinite loops
        
        while not self.game_over and turn_count < max_turns:
            self.player_turn()
            self.display_standings()
            
            if self.game_over:
                break
            
            self.current_player = (self.current_player + 1) % self.num_players
            turn_count += 1
        
        if self.winner:
            print("\n" + "🏆 "*15)
            print(f"CONGRATULATIONS! {self.winner} WINS THE GAME! 🏆")
            print("🏆 "*15)
        else:
            print("Game ended due to maximum turns reached.")

def main():
    """Main function to start the game"""
    print("\nWelcome to LUDO!")
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    game = LudoGame(num_players)
    game.play()

if __name__ == "__main__":
    main()
