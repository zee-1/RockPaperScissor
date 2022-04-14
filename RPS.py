def RPS_win_loss(User,Bot,inc_scr):
      global Score
      if(User == Bot):
            return "Tie"
      elif(User == "Rock" and Bot == "Scissors"):
            inc_scr()
            return "Win"

      elif(User == "Rock" and Bot == "Paper"):
            return "Loss"
      elif(User == "Paper" and Bot == "Rock"):
            inc_scr()
            return "Win"

      elif(User == "Paper" and Bot == "Scissors"):
            return "Loss"
      elif(User == "Scissors" and Bot == "Paper"):
            inc_scr()
            return "Win"

      elif(User == "Scissors" and Bot == "Rock"):
            return "Loss"

def bot_choice():
      import random
      Bot = random.choice(["Rock","Paper","Scissors"])
      return Bot