class Player:

  def play(self):
    print("The player is playingcricket.")


class Batsman(Player):

  def play(self):
    print("The batsman is batting.")


class Bowler(Player):

  def play(self):
    print("The bowler is bowling.")


# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
# Call the Play method for each objects
batsman.play()
bowler.play()
