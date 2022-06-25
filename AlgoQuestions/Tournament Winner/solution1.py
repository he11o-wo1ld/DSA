home = 1

def tournamentWinner(competitions, results):
    # Write your code here.
	curr_best_team = ""
	score = {curr_best_team: 0}
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition
		
		winningTeam = homeTeam if result == home else awayTeam
		
		updateScores(winningTeam, 3, score)
		
		if score[winningTeam] > score[curr_best_team]:
			curr_best_team = winningTeam
			
	return curr_best_team

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0
	
	scores[team] += points
